#!/usr/bin/env bash
# 매일 세션 시작 시 1회: 제작 코드(toon/)가 기대하는 환경을 맞춘다.
set -e
REPO="$(cd "$(dirname "$0")/.." && pwd)"
if ! command -v rsvg-convert >/dev/null || ! fc-list | grep -q "NotoSansCJK-Black"; then
  apt-get install -y librsvg2-bin fonts-noto-cjk fonts-noto-cjk-extra >/dev/null 2>&1 \
    || (apt-get update >/dev/null 2>&1 && apt-get install -y librsvg2-bin fonts-noto-cjk fonts-noto-cjk-extra >/dev/null)
fi
# 기존 코드의 경로(/home/claude/toon)를 저장소의 toon/ 으로 연결 — 코드는 수정하지 않는다
mkdir -p /home/claude "$REPO/toon/out"
ln -sfn "$REPO/toon" /home/claude/toon
echo "setup ok: $(rsvg-convert --version | head -1)"
