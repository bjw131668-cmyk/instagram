# 나물려 툰 (@namullyeo_toon) — 자동 연재 파이프라인

이 저장소는 인스타툰 「주식 중독자 나물려」를 **매일 아침 자동으로 제작·업로드**한다.
예약 작업이 매일 아침 새 Claude 세션을 열고 "오늘 회차 진행해줘"라고 지시하면 아래 **일일 루틴**을 수행한다.
너의 역할과 모든 제작 규칙은 `series/00 나물려 연재 마스터 프롬프트.md`를 따른다. 이 파일은 자동화 절차만 정한다.

## 폴더 구조

| 경로 | 내용 |
|---|---|
| `series/*.md` | claude.ai 프로젝트의 원본 MD (마스터 프롬프트, 캐릭터 시트, 연재 계획, 대본 DB ①·②, 예비·후반부 대본 등). 새 설정 파일을 만들지 않는다 |
| `toon/` | 사용자의 기존 제작 코드 그대로 (`make.py`, `lib*.py`, `db.py`, `epN.py`). 구조는 `toon/README_코드구조.md` |
| `episodes/NNN/` | 업로드용 결과물: `out/00~11.jpg`(표지·카드 10장·다음 화 예고), `out/cover.jpg`(릴스 커버), `out/reel.mp4`, `episode.json`(본문·고정 댓글), `published.json`(업로드 기록) |
| `insights/YYYY-MM-DD.json` | 매일 수집한 인사이트 원본 |
| `tools/setup.sh` | rsvg-convert·Noto Sans CJK 설치, `/home/claude/toon` → `toon/` 연결 |
| `tools/collect.py` | `toon/out`의 N화 PNG → `episodes/NNN/out` JPEG |
| `tools/ig.py` | 인스타 업로드·인사이트 |
| `config.json` | 인스타 계정 ID, `last_published_episode`, `reel_mode` 등 (토큰은 두지 않는다) |

## 일일 루틴

1. **준비**: `git checkout main && git pull origin main`, `bash tools/setup.sh`.
   `series/*.md`를 모두 읽는다(사용자가 밤사이 고쳤을 수 있다). 특히 마스터 프롬프트, 캐릭터 시트, 대본 DB 맨 위 "제작 규칙 통합본".
2. **인사이트 수집**: `python3 tools/ig.py insights` → `insights/<오늘>.json`. 실패해도 기록만 하고 계속한다.
3. **피드백 반영**: 마스터 프롬프트 7장 방법으로 분석해
   - `series/나물려 연재 계획.md` "성과 기록"에 `### YYYY-MM-DD N화 ○○ 릴스 기록` 형식으로 수치·해석을 추가
   - 대본 DB ①·② 맨 위 "1. 근거" 표에 한 줄, 새 썸네일 펀치는 금지 단어 목록에 추가
   - 원인은 추정이라고 밝힌다. 캐릭터·세계관·형식 자체를 바꾸는 결정은 하지 않고 제안만 적는다(사용자 몫)
4. **회차 결정**: `published.json`이 있는 가장 큰 `episodes/NNN` + 1, 없으면 `config.json`의 `last_published_episode` + 1.
   `나물려 연재 계획.md` 회차표와 맞는지 확인한다. 같은 번호 폴더에 `published.json`이 없으면 이전 실행이 중간에 멈춘 것이니 이어서 완성한다.
5. **대본 점검**: 대본 DB의 해당 화를 "제작 직전 체크리스트"로 세트별 점검하고, 고친 내용은 대본 DB에 바로 반영한다(`db.py`가 DB에서 읽는다).
6. **장면 코드**: `toon/epN.py`를 만든다. 같은 상대역이 나온 가장 최근 ep 파일을 복사해 배경·소품·표정만 바꾼다
   (상한나 ep12·ep18, 장기보 팀장 ep15·ep17, 박익절 ep13·ep16). 새 조연은 캐릭터 시트 규칙(손가락 5개, 팔뚝→물건→손→소매)으로 새로 그린다.
   캐릭터 외형·나물려(`lib.CHAR`, `lib.NMR_FRONT`)는 절대 바꾸지 않는다.
7. **렌더 & 검수**: `cd /home/claude/toon && python3 epN.py test`로 10번 카드를 먼저 보고, 괜찮으면 `python3 epN.py full`.
   12장을 모두 직접 열어 확인한다: 인물별 손 개수(나물려 정확히 2개), 손가락 5개, 팔-손 연결, 글씨 넘침(`[글씨 넘침]` 출력), 워터마크 가림, 장면이 밝은지.
   문제가 있으면 고쳐 다시 렌더한다.
8. **모으기**: `python3 tools/collect.py N`.
9. **본문·고정 댓글**: `episodes/NNN/episode.json` 작성 — 마스터 프롬프트 5장 템플릿과 대본 DB의 "본문 재료"를 쓴다.
   ```json
   {"number": 19, "title": "재택근무", "file_prefix": "19화_재택근무",
    "caption": "게시물 본문(해시태그 포함)", "reel_caption": "릴스 본문(해시태그 포함)",
    "hashtags": [], "pinned_comment": "대답하기 쉬운 양자택일 질문 + 보낼 대상"}
   ```
10. **푸시**: `git add -A && git commit -m "N화 제작" && git push origin main`
    (Graph API가 raw.githubusercontent.com 의 이미지를 읽어가므로 업로드 전에 반드시 push).
11. **업로드**: `python3 tools/ig.py publish episodes/NNN` → 게시물(캐러셀) → 고정 댓글용 댓글.
    `reel_mode`가 `auto`면 릴스도 올린다. `manual`이면 릴스는 올리지 않는다(사용자가 앱에서 추천 음원 맨 위 곡을 넣어 직접 올림).
    `published.json`에 기록된 항목은 다시 올리지 않으므로 재실행해도 중복 게시되지 않는다.
12. **마무리**: `나물려 연재 계획.md` 회차표 상태와 발행 기록을 갱신하고 `published.json`과 함께 커밋·푸시한다.
    마지막 메시지에 ① 게시물 링크 ② 릴스 파일 링크(수동 모드일 때, `https://raw.githubusercontent.com/bjw131668-cmyk/instagram/main/episodes/NNN/out/reel.mp4`)와 릴스 본문 ③ 피드백 요약 3줄을 남긴다.

## 실패 시

- 토큰 만료(`OAuthException`, code 190): 업로드를 멈추고 "인스타 토큰 갱신 필요"라고 보고한다.
- 어떤 단계든 실패하면 그때까지의 산출물을 커밋·푸시해 두고 원인을 요약해, 사용자가 `episodes/NNN/out/`의 파일로 직접 올릴 수 있게 한다.
- 댓글 고정(pin)은 Graph API가 지원하지 않는다. 댓글만 달리고, 고정은 사용자가 앱에서 한다.
- 인스타 추천 음원은 API로 넣을 수 없다. 그래서 `reel_mode` 기본값이 `manual`이다.
