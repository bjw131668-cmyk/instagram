#!/usr/bin/env python3
"""toon/out 의 N화 결과물을 episodes/NNN/out 으로 모은다 (인스타 API용 JPEG 변환 포함).

사용법: python3 tools/collect.py 18
  00.jpg = 표지, 01~10.jpg = 대사 카드, 11.jpg = 다음 화 예고 (캐러셀 순서 그대로)
  cover.jpg = 릴스 커버, reel.mp4 = 릴스
"""
import shutil, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
n = int(sys.argv[1])
src = ROOT / "toon" / "out"
files = sorted(src.glob(f"{n}화_*"))
if not files:
    sys.exit(f"toon/out 에 {n}화 결과물이 없습니다. 먼저 python3 ep{n}.py full 을 실행하세요.")
dst = ROOT / "episodes" / f"{n:03d}" / "out"
dst.mkdir(parents=True, exist_ok=True)
for f in files:
    name = f.name.split("_", 2)[-1] if f.name.count("_") >= 2 else f.name
    if f.suffix == ".mp4":
        shutil.copy(f, dst / "reel.mp4"); out = "reel.mp4"
    elif "릴스커버" in f.name:
        out = "cover.jpg"; Image.open(f).convert("RGB").save(dst / out, "JPEG", quality=92)
    else:
        idx = f.stem.split("_")[2][:2]  # 00 표지, 01~10, 11 다음화예고
        out = f"{idx}.jpg"; Image.open(f).convert("RGB").save(dst / out, "JPEG", quality=92)
    print(f"{f.name} -> episodes/{n:03d}/out/{out}")
