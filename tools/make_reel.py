#!/usr/bin/env python3
"""렌더링된 컷 -> 릴스 영상(1080x1920, mp4).

사용법: python3 tools/make_reel.py episodes/001
  episodes/001/out/*.jpg 를 순서대로 이어 episodes/001/out/reel.mp4 를 만든다.
  episode.json 의 "reel" 항목으로 조정:
    "seconds": 3.0 또는 [2.5, 3, 4, ...]  # 컷별 노출 시간
    "bgm": "assets/bgm/calm.mp3"         # 선택. 저장소 루트 기준 경로
    "background": "#fffdf6"              # 세로 화면 여백 색
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FPS = 30
FADE = 0.4


def main(ep_dir: str) -> None:
    ep = Path(ep_dir).resolve()
    meta = json.loads((ep / "episode.json").read_text(encoding="utf-8"))
    reel = meta.get("reel", {})
    imgs = sorted((ep / "out").glob("[0-9]*.jpg"))
    if not imgs:
        sys.exit("먼저 render_panels.py 로 컷을 렌더링하세요.")
    secs = reel.get("seconds", 3.0)
    if not isinstance(secs, list):
        secs = [secs] * len(imgs)
    secs = (secs + [secs[-1]] * len(imgs))[: len(imgs)]
    bg = reel.get("background", "#fffdf6").lstrip("#")

    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for img, s in zip(imgs, secs):
        cmd += ["-loop", "1", "-t", f"{s + FADE:.2f}", "-i", str(img)]
    bgm = reel.get("bgm")
    if bgm:
        cmd += ["-stream_loop", "-1", "-i", str(ROOT / bgm)]

    filters = []
    for i, s in enumerate(secs):
        frames = int((s + FADE) * FPS)
        # 컷을 세로 화면 가운데에 두고 아주 천천히 확대(켄 번스)
        filters.append(
            f"[{i}:v]scale=1080:1350,setsar=1,"
            f"pad=1080:1920:0:285:0x{bg},"
            f"zoompan=z='min(1+0.0006*on,1.06)':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps={FPS},"
            f"trim=duration={s + FADE:.2f},setpts=PTS-STARTPTS[v{i}]"
        )
    last, offset = "v0", 0.0
    for i in range(1, len(secs)):
        offset += secs[i - 1]
        filters.append(f"[{last}][v{i}]xfade=transition=fade:duration={FADE}:offset={offset:.2f}[x{i}]")
        last = f"x{i}"
    total = sum(secs) + FADE
    filters.append(f"[{last}]format=yuv420p[vout]")

    cmd += ["-filter_complex", ";".join(filters), "-map", "[vout]"]
    if bgm:
        a = len(imgs)
        cmd += ["-map", f"{a}:a", "-af", f"afade=t=out:st={total - 1.5:.2f}:d=1.5", "-c:a", "aac", "-b:a", "128k"]
    out = ep / "out" / "reel.mp4"
    cmd += ["-t", f"{total:.2f}", "-r", str(FPS), "-c:v", "libx264", "-preset", "medium",
            "-crf", "20", "-movflags", "+faststart", str(out)]
    subprocess.run(cmd, check=True)
    print(f"릴스 생성: {out.relative_to(ROOT)} ({total:.1f}초)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
