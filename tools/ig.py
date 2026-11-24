#!/usr/bin/env python3
"""Instagram Graph API 업로드 / 인사이트 수집.

사용법:
  python3 tools/ig.py check                     # 토큰·계정 연결 확인
  python3 tools/ig.py publish episodes/001      # 캐러셀(툰) + 릴스 업로드 + 댓글
  python3 tools/ig.py publish episodes/001 --only carousel|reel
  python3 tools/ig.py insights                  # 업로드된 회차들의 인사이트 -> insights/

설정:
  config.json      : ig_user_id, graph_version, github_raw_base, reel_share_to_feed
  액세스 토큰       : 환경변수 IG_ACCESS_TOKEN, 없으면 클라우드 환경의 네트워크 시크릿
                     (graph.facebook.com 요청에 프록시가 Authorization 헤더를 주입)으로 처리.

이미지는 Graph API가 공개 URL에서 내려받아야 하므로, publish 전에
episodes/<번호>/out/ 이 GitHub에 push 되어 있어야 한다 (raw.githubusercontent.com 사용).
"""
import argparse
import datetime as dt
import json
import os
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
CFG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
VER = CFG.get("graph_version", "v23.0")
GRAPH = f"https://graph.facebook.com/{VER}"
TOKEN = os.environ.get("IG_ACCESS_TOKEN", "proxy-injected")
IG_USER = os.environ.get("IG_USER_ID") or CFG.get("ig_user_id")
KST = dt.timezone(dt.timedelta(hours=9))


def call(method: str, path: str, **params):
    url = path if path.startswith("http") else f"{GRAPH}/{path}"
    r = requests.request(method, url, headers={"Authorization": f"Bearer {TOKEN}"},
                         params=params if method == "GET" else None,
                         data=params if method != "GET" else None, timeout=120)
    try:
        body = r.json()
    except ValueError:
        body = {"raw": r.text[:500]}
    if r.status_code >= 400 or "error" in body:
        raise RuntimeError(f"{method} {path} -> {r.status_code}: {json.dumps(body, ensure_ascii=False)}")
    return body


def wait_ready(container_id: str, timeout: int = 600) -> None:
    t0 = time.time()
    while True:
        st = call("GET", container_id, fields="status_code,status")
        code = st.get("status_code")
        if code == "FINISHED":
            return
        if code in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"컨테이너 {container_id} 처리 실패: {st}")
        if time.time() - t0 > timeout:
            raise RuntimeError(f"컨테이너 {container_id} 처리 시간 초과: {st}")
        time.sleep(5)


def publish_container(container_id: str) -> str:
    wait_ready(container_id)
    media_id = call("POST", f"{IG_USER}/media_publish", creation_id=container_id)["id"]
    return media_id


def comment(media_id: str, text: str) -> str:
    return call("POST", f"{media_id}/comments", message=text)["id"]


def raw_url(ep: Path, name: str) -> str:
    rel = (ep / "out" / name).relative_to(ROOT).as_posix()
    return f"{CFG['github_raw_base'].rstrip('/')}/{rel}"


def full_caption(meta: dict, key: str) -> str:
    cap = meta.get(key) or meta["caption"]
    tags = " ".join(meta.get("hashtags", []))
    return f"{cap}\n\n{tags}".strip()


def publish_carousel(ep: Path, meta: dict) -> dict:
    imgs = sorted((ep / "out").glob("[0-9]*.jpg"))
    if not 2 <= len(imgs) <= 10:
        raise SystemExit(f"캐러셀은 이미지 2~10장이 필요합니다 (현재 {len(imgs)}장)")
    for img in imgs:  # push 됐는지 미리 확인
        u = raw_url(ep, img.name)
        if requests.head(u, timeout=30).status_code != 200:
            raise SystemExit(f"공개 URL에서 이미지를 찾을 수 없습니다. 먼저 git push 하세요: {u}")
    children = [call("POST", f"{IG_USER}/media", image_url=raw_url(ep, i.name), is_carousel_item="true")["id"]
                for i in imgs]
    for c in children:
        wait_ready(c)
    parent = call("POST", f"{IG_USER}/media", media_type="CAROUSEL", children=",".join(children),
                  caption=full_caption(meta, "caption"))["id"]
    media_id = publish_container(parent)
    res = {"media_id": media_id}
    if meta.get("pinned_comment"):
        res["comment_id"] = comment(media_id, meta["pinned_comment"])
    return res


def publish_reel(ep: Path, meta: dict) -> dict:
    video = ep / "out" / "reel.mp4"
    if not video.exists():
        raise SystemExit("reel.mp4 가 없습니다. make_reel.py 를 먼저 실행하세요.")
    common = dict(media_type="REELS", caption=full_caption(meta, "reel_caption"),
                  share_to_feed=str(CFG.get("reel_share_to_feed", True)).lower())
    try:  # 1순위: 파일 직접 업로드 (resumable)
        cid = call("POST", f"{IG_USER}/media", upload_type="resumable", **common)["id"]
        data = video.read_bytes()
        r = requests.post(f"https://rupload.facebook.com/ig-api-upload/{VER}/{cid}", data=data, timeout=600,
                          headers={"Authorization": f"OAuth {TOKEN}", "offset": "0", "file_size": str(len(data))})
        if r.status_code >= 400:
            raise RuntimeError(f"rupload {r.status_code}: {r.text[:300]}")
    except Exception as e:  # 2순위: 공개 URL
        print(f"직접 업로드 실패, video_url 방식으로 재시도: {e}", file=sys.stderr)
        cid = call("POST", f"{IG_USER}/media", video_url=raw_url(ep, "reel.mp4"), **common)["id"]
    media_id = publish_container(cid)
    res = {"media_id": media_id}
    if meta.get("pinned_comment"):
        res["comment_id"] = comment(media_id, meta["pinned_comment"])
    return res


def cmd_publish(ep_dir: str, only: str | None) -> None:
    ep = (ROOT / ep_dir).resolve()
    meta = json.loads((ep / "episode.json").read_text(encoding="utf-8"))
    log_path = ep / "published.json"
    log = json.loads(log_path.read_text()) if log_path.exists() else {}
    for kind, fn in (("carousel", publish_carousel), ("reel", publish_reel)):
        if only and only != kind:
            continue
        if kind in log:
            print(f"{kind}: 이미 업로드됨 ({log[kind]['media_id']}) — 건너뜀")
            continue
        res = fn(ep, meta)
        res["permalink"] = call("GET", res["media_id"], fields="permalink").get("permalink")
        res["published_at"] = dt.datetime.now(KST).isoformat(timespec="seconds")
        log[kind] = res
        log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{kind}: 업로드 완료 {res['permalink']}")


FEED_METRICS = ["reach", "views", "likes", "comments", "shares", "saved", "total_interactions"]
REEL_METRICS = FEED_METRICS + ["ig_reels_avg_watch_time", "ig_reels_video_view_total_time"]


def media_insights(media_id: str, metrics: list[str]) -> dict:
    try:
        rows = call("GET", f"{media_id}/insights", metric=",".join(metrics))["data"]
    except RuntimeError:  # 지원하지 않는 지표가 섞이면 하나씩
        rows = []
        for m in metrics:
            try:
                rows += call("GET", f"{media_id}/insights", metric=m)["data"]
            except RuntimeError:
                pass
    return {r["name"]: r["values"][0]["value"] for r in rows if r.get("values")}


def cmd_insights(days: int) -> None:
    out_dir = ROOT / "insights"
    out_dir.mkdir(exist_ok=True)
    today = dt.datetime.now(KST).date()
    acct = call("GET", IG_USER, fields="username,followers_count,media_count")
    report = {"collected_at": dt.datetime.now(KST).isoformat(timespec="seconds"), "account": acct, "episodes": []}
    for log_path in sorted((ROOT / "episodes").glob("*/published.json")):
        log = json.loads(log_path.read_text())
        meta = json.loads((log_path.parent / "episode.json").read_text(encoding="utf-8"))
        first = min(v["published_at"] for v in log.values())
        if (today - dt.date.fromisoformat(first[:10])).days > days:
            continue
        entry = {"episode": log_path.parent.name, "title": meta.get("title"), "published_at": first}
        for kind, info in log.items():
            m = media_insights(info["media_id"], REEL_METRICS if kind == "reel" else FEED_METRICS)
            entry[kind] = {"permalink": info.get("permalink"), **m}
        report["episodes"].append(entry)
    path = out_dir / f"{today.isoformat()}.json"
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"인사이트 저장: {path.relative_to(ROOT)}")
    print(json.dumps(report, ensure_ascii=False, indent=2))


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    p = sub.add_parser("publish"); p.add_argument("episode"); p.add_argument("--only", choices=["carousel", "reel"])
    i = sub.add_parser("insights"); i.add_argument("--days", type=int, default=7)
    a = ap.parse_args()
    if not IG_USER:
        sys.exit("config.json 에 ig_user_id 를 설정하세요.")
    if a.cmd == "check":
        print(json.dumps(call("GET", IG_USER, fields="id,username,followers_count,media_count"), ensure_ascii=False, indent=2))
    elif a.cmd == "publish":
        cmd_publish(a.episode, a.only)
    else:
        cmd_insights(a.days)


if __name__ == "__main__":
    main()
