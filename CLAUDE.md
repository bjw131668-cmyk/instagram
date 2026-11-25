# 나물려 툰 (@namullyeo_toon) — 자동 연재 파이프라인

이 저장소는 인스타툰 「나물려의 주식만화」를 **매일 아침 자동으로 제작·업로드**한다.
예약 작업이 매일 07:40(KST)에 새 Claude 세션을 열고 "오늘 회차 진행해줘"라고 지시하면,
아래 **일일 루틴**을 처음부터 끝까지 사람 개입 없이 수행한다.

## 폴더 구조

| 경로 | 내용 |
|---|---|
| `series/*.md` | claude.ai 「나물려 연재」 프로젝트의 기존 MD(캐릭터·대본·피드백 등)를 **그대로 옮겨 둔 것**. 파일 이름·구성은 사용자가 정한 대로 따르고, 새 설정 파일을 만들지 않는다. |
| `episodes/NNN/` | 회차별 산출물: `episode.json`, `panels/*.html`, `out/*.jpg`, `out/reel.mp4`, `published.json` |
| `insights/YYYY-MM-DD.json` | 매일 수집한 인사이트 원본 |
| `assets/toon.css`, `assets/fonts/` | 공통 스타일, 한글 폰트 |
| `tools/` | `render_panels.mjs`(컷 렌더), `make_reel.py`(릴스), `ig.py`(업로드·인사이트) |
| `config.json` | 인스타 계정 ID, Graph API 버전 등 (토큰은 여기 두지 않는다) |

## 일일 루틴

1. **최신화**: `git checkout main && git pull origin main`. `series/*.md`를 모두 읽는다
   (사용자가 밤사이 수정했을 수 있다).
2. **인사이트 수집**: `python3 tools/ig.py insights` → `insights/<오늘>.json`.
   실패하면 오류를 기록하고 계속 진행한다(업로드가 우선).
3. **피드백 반영**: 인사이트를 `series/00 나물려 연재 마스터 프롬프트.md` 7장 방법으로 분석해 `series/나물려 연재 계획.md`의 "성과 기록"에 날짜 섹션으로 추가하고, 배운 점은 대본 DB 맨 위 "제작 규칙 통합본"(근거 표·금지 단어)에 반영한다.
   - 회차별 도달·조회·저장·공유·댓글, 릴스 평균 시청 시간 비교
   - 잘 된 요소 / 안 된 요소 가설, **다음 회차에 적용할 구체적 지시 1~3개**
   - 캐릭터·세계관 설정 자체를 바꾸는 판단은 하지 않는다(그건 사용자 몫). 제안만 적는다.
4. **회차 번호 결정**: `published.json`이 있는 가장 큰 `episodes/NNN` + 1 (없으면 `config.json`의 `last_published_episode` + 1). `나물려 연재 계획.md` 회차표와 맞는지 확인한다.
   같은 번호 폴더가 이미 있고 `published.json`이 없으면 이전 실행이 중간에 실패한 것이므로 그 회차를 이어서 완성한다.
5. **대본**: 대본 DB ①·②의 해당 화를 쓰되, 맨 위 "제작 직전 체크리스트"를 세트별로 점검하고 고친 내용은 대본 DB에 반영한다(마스터 프롬프트 1장). 없으면 기존 MD의 연재 계획·피드백·직전 3화를 참고해 쓰고, 기존 대본 MD의 형식을 따라 저장한다. 컷 수는 캐러셀 기준 **2~10장**(권장 6~8).
6. **컷 제작**: `episodes/NNN/panels/01.html …`을 작성한다.
   - 각 파일은 1080×1350, `<link rel="stylesheet" href="../../../assets/toon.css">` 사용
   - 캐릭터는 `series/`의 캐릭터 MD에 정의된 SVG 형태를 **매 회 동일하게** 재사용(일관성 최우선)
   - 외부 URL(웹폰트, CDN 이미지) 금지 — 저장소 안의 자원만 사용
   - 1번 컷 = 표지(제목·회차), 마지막 컷 = 다음 화 예고 또는 팔로우 유도
7. **렌더 & 검수**: `node tools/render_panels.mjs episodes/NNN` 후 **모든 jpg를 직접 열어 확인**한다.
   글자 잘림·말풍선 겹침·캐릭터 깨짐이 있으면 HTML을 고쳐 다시 렌더한다.
8. **릴스**: `python3 tools/make_reel.py episodes/NNN` (컷별 시간은 대사량에 맞춰 `episode.json`의 `reel.seconds`로 조정).
9. **본문·고정댓글**: `episodes/NNN/episode.json` 작성.
   ```json
   {
     "number": 12, "title": "…",
     "caption": "피드(캐러셀) 본문", "reel_caption": "릴스 본문(비우면 caption 사용)",
     "hashtags": ["#나물려", "#주식만화", "#인스타툰"],
     "pinned_comment": "고정할 댓글",
     "reel": { "seconds": [2.5, 3, 3.5] }
   }
   ```
   주식 종목 추천·매수 권유로 읽힐 표현은 쓰지 않는다. 고정댓글에 "투자 권유 아님" 문구를 포함한다.
10. **푸시**: `git add -A && git commit -m "NNN화 제작" && git push origin main`
    (Graph API가 raw.githubusercontent.com 의 이미지 URL을 읽어가므로 업로드 전에 반드시 push).
11. **업로드**: `python3 tools/ig.py publish episodes/NNN` → 캐러셀 → 릴스 → 각 게시물에 댓글.
    `published.json`에 이미 기록된 항목은 다시 올리지 않으므로 재실행해도 중복 게시되지 않는다.
12. **마무리**: `published.json`을 커밋·푸시하고, 마지막 메시지에 게시물 링크와 피드백 요약을 남긴다.

## 실패 시

- 토큰 만료(`OAuthException`, code 190): 업로드를 멈추고 "인스타 토큰 갱신 필요"라고 보고한다.
- 어떤 단계든 실패하면 그때까지의 산출물을 커밋·푸시해 두고 원인을 요약한다.
  사용자가 `episodes/NNN/out/`의 파일을 받아 직접 올릴 수 있게 한다.
- 고정(pin)은 Graph API가 지원하지 않으므로 댓글만 달린다. 사용자가 앱에서 길게 눌러 고정한다.
