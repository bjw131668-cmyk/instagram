#!/usr/bin/env python3
"""주식 중독자의 건강검진 - 한 장 그림 + 대사 10종"""
import subprocess, os, html

W, H = 1080, 1350
OUT = "/home/claude/toon/out"
os.makedirs(OUT, exist_ok=True)
INK = "#1b1b22"

# (의사1, 환자1, 의사2, 환자2)
SCRIPT = [
    ("혈압이 많이\n올랐네요.", "오, 드디어\n오르네요.", "좋아하실 일이\n아닌데요?", "제 건 처음\n올라봐서요.."),
    ("운동은\n하세요?", "매일 합니다.", "어떤 운동\n하시는데요?", "물타기요.\n3년째."),
    ("잠은 잘\n주무세요?", "미국장 끝나면\n바로 잡니다.", "그게 몇\n신데요?", "새벽 6시요.\n서머타임엔 5시."),
    ("체중이 좀\n빠지셨네요.", "계좌도\n빠졌습니다.", "얼마나\n빠졌는데요?", "체중은 3kg,\n계좌는 30%요."),
    ("스트레스는\n언제 받으세요?", "9시부터\n3시 반까지요.", "근무 시간이\n짧으시네요?", "아뇨, 그건\n장 시간이고요.."),
    ("술은 얼마나\n드세요?", "그날 장 보고\n정합니다.", "기분 따라\n드시는군요?", "오르면 축하주,\n내리면 위로주요."),
    ("심장이 갑자기\n빨리 뛰네요?", "방금 알림이\n와서요.", "무슨\n알림인데요?", "제 종목이\n뉴스에 나왔대요.\n안 좋은 쪽으로."),
    ("간 수치가\n너무 높아요.", "고점이라는\n거죠?", "네, 빨리\n낮추셔야 해요.", "제가 사면\n바로 떨어지는데\n살 수 있나요?"),
    ("이 약은 오래\n드셔야 합니다.", "장기 투자네요.\n자신 있습니다.", "꾸준히 하시는\n편인가 봐요?", "네, 5년째\n못 팔고 있어요."),
    ("더 궁금한 거\n있으세요?", "선생님은\n뭐 사셨어요?", "...저도\n같은 종목입니다.", "혈압 같이\n재시죠."),
]


def text_w(s, size):
    w = 0.0
    for ch in s:
        if ch == " ":
            w += 0.30
        elif ch in ".,":
            w += 0.32
        elif ch in "?!%":
            w += 0.62
        elif ch.isdigit() or ch.isascii():
            w += 0.60
        else:
            w += 1.0
    return w * size


FIXED = None

def _draw(cx, cy, rx, ry, tail, lines, size):
    lh = size * 1.22
    y0 = cy - (len(lines) - 1) * lh / 2 + size * 0.36
    bx1, bx2, by, tx, ty = tail
    o = []
    o.append(f'<path d="M{bx1},{by} L{tx},{ty} L{bx2},{by} Z" fill="#fff" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>')
    o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#fff" stroke="{INK}" stroke-width="7"/>')
    o.append(f'<path d="M{bx1+5},{by} L{tx},{ty} L{bx2-5},{by} Z" fill="#fff"/>')
    for i, l in enumerate(lines):
        o.append(f'<text x="{cx}" y="{y0 + i*lh:.1f}" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="{size}" fill="{INK}">{html.escape(l)}</text>')
    return "\n".join(o)

def bubble(cx, cy, rx, ry, tail, text):
    """tail = (base_x1, base_x2, base_y, tip_x, tip_y)"""
    lines = text.split("\n")
    if FIXED:  # 14화부터 글씨 크기 통일: 넘치는 줄은 띄어쓰기에서 자동 줄바꿈(최대 3줄)
        maxw = rx * 1.56
        def wrap(ls, sz):
            out = []
            for l in ls:
                if text_w(l, sz) <= maxw: out.append(l); continue
                cur = ""
                for w in l.split(" "):
                    t = (cur + " " + w).strip()
                    if cur and text_w(t, sz) > maxw: out.append(cur); cur = w
                    else: cur = t
                out.append(cur)
            return out
        size = FIXED
        ls = wrap(lines, size)
        while (len(ls) > 3 or max(text_w(l, size) for l in ls) > maxw) and size > FIXED - 6:
            size -= 2; ls = wrap(lines, size)
        if len(ls) > 3 or max(text_w(l, size) for l in ls) > maxw:
            print("[글씨 넘침]", text.replace("\n", "|"))
        return _draw(cx, cy, rx, ry, tail, ls, size)
    size = 66
    while size > 30:
        widest = max(text_w(l, size) for l in lines)
        total_h = len(lines) * size * 1.22
        if widest <= rx * 1.56 and total_h <= ry * 1.45:
            break
        size -= 2
    lh = size * 1.22
    y0 = cy - (len(lines) - 1) * lh / 2 + size * 0.36
    bx1, bx2, by, tx, ty = tail
    o = []
    o.append(f'<path d="M{bx1},{by} L{tx},{ty} L{bx2},{by} Z" fill="#fff" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>')
    o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#fff" stroke="{INK}" stroke-width="7"/>')
    # 이음매 가리기
    o.append(f'<path d="M{bx1+5},{by} L{tx},{ty} L{bx2-5},{by} Z" fill="#fff"/>')
    for i, l in enumerate(lines):
        o.append(
            f'<text x="{cx}" y="{y0 + i*lh:.1f}" text-anchor="middle" font-family="Noto Sans CJK KR" '
            f'font-weight="900" font-size="{size}" fill="{INK}">{html.escape(l)}</text>'
        )
    return "\n".join(o)


SCENE = f'''
<defs>
  <linearGradient id="wall" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#dfeeea"/><stop offset="1" stop-color="#c9e2dc"/>
  </linearGradient>
  <linearGradient id="desk" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#c99a6b"/><stop offset="1" stop-color="#a97b50"/>
  </linearGradient>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#bfe3f7"/><stop offset="1" stop-color="#eaf6fb"/>
  </linearGradient>
</defs>

<!-- 벽 -->
<rect width="{W}" height="{H}" fill="url(#wall)"/>
<rect y="760" width="{W}" height="14" fill="#b4d2cb"/>
<rect y="774" width="{W}" height="600" fill="#bcd9d2"/>

<!-- 창문 + 블라인드 -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
  <rect x="440" y="300" width="230" height="300" rx="6" fill="url(#sky)"/>
  <g stroke-width="3" stroke="#8fb3c4">
    <line x1="446" y1="340" x2="664" y2="340"/><line x1="446" y1="380" x2="664" y2="380"/>
    <line x1="446" y1="420" x2="664" y2="420"/><line x1="446" y1="460" x2="664" y2="460"/>
    <line x1="446" y1="500" x2="664" y2="500"/><line x1="446" y1="540" x2="664" y2="540"/>
    <line x1="446" y1="580" x2="664" y2="580"/>
  </g>
  <line x1="555" y1="300" x2="555" y2="600" stroke-width="5"/>
</g>

<!-- 시력표 -->
<g transform="translate(40,330)">
  <rect width="120" height="200" rx="6" fill="#fff" stroke="{INK}" stroke-width="5"/>
  <g font-family="Noto Sans CJK KR" font-weight="900" fill="{INK}" text-anchor="middle">
    <text x="60" y="52" font-size="44">E</text>
    <text x="60" y="92" font-size="30">F P</text>
    <text x="60" y="124" font-size="22">T O Z</text>
    <text x="60" y="150" font-size="16">L P E D</text>
    <text x="60" y="172" font-size="11">P E C F D</text>
  </g>
</g>

<!-- 벽 시계: 3시 30분 (장 마감) -->
<g transform="translate(985,390)">
  <circle r="58" fill="#fff" stroke="{INK}" stroke-width="6"/>
  <g stroke="{INK}" stroke-width="4" stroke-linecap="round">
    <line x1="0" y1="-48" x2="0" y2="-40"/><line x1="48" y1="0" x2="40" y2="0"/>
    <line x1="0" y1="48" x2="0" y2="40"/><line x1="-48" y1="0" x2="-40" y2="0"/>
  </g>
  <line x1="0" y1="0" x2="0" y2="40" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <line x1="0" y1="0" x2="26" y2="7" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <circle r="5" fill="#e2483d"/>
</g>

<!-- ===================== 의사 (왼쪽) ===================== -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
  <!-- 몸통: 가운 -->
  <path d="M95,1010 C95,820 150,745 235,725 L365,725 C450,745 505,820 505,1010 Z" fill="#ffffff"/>
  <!-- 안쪽 셔츠 + 넥타이 -->
  <path d="M250,727 L300,820 L350,727 Z" fill="#9fc6e8"/>
  <path d="M288,770 L312,770 L322,860 L300,890 L278,860 Z" fill="#35507a"/>
  <!-- 가운 깃 -->
  <path d="M235,725 L300,900 L250,935 L190,760 Z" fill="#f3f6f8"/>
  <path d="M365,725 L300,900 L350,935 L410,760 Z" fill="#f3f6f8"/>
  <!-- 청진기 -->
  <path d="M215,745 C200,850 250,900 300,905 C350,900 400,850 385,745" fill="none" stroke="#4a5568" stroke-width="9"/>
  <path d="M300,905 L300,950" fill="none" stroke="#4a5568" stroke-width="9"/>
  <circle cx="300" cy="968" r="20" fill="#cfd6de"/>
  <!-- 주머니 펜 -->
  <rect x="408" y="880" width="56" height="60" rx="5" fill="#f3f6f8"/>
  <line x1="424" y1="862" x2="424" y2="900" stroke="#e2483d" stroke-width="8"/>
  <line x1="442" y1="866" x2="442" y2="900" stroke="#2f6fd0" stroke-width="8"/>
  <!-- 목 -->
  <path d="M262,660 L262,735 C285,760 315,760 338,735 L338,660 Z" fill="#f2c9ac"/>
  <!-- 뒷머리 -->
  <path d="M178,545 C165,410 250,360 305,362 C372,360 440,415 426,548 C430,600 420,640 405,655 L195,655 C180,640 172,600 178,545 Z" fill="#2c2b3a"/>
  <!-- 얼굴 -->
  <path d="M200,530 C200,440 250,410 302,410 C356,410 404,440 404,530 C404,640 356,690 302,690 C248,690 200,640 200,530 Z" fill="#f7d7bd"/>
  <!-- 앞머리 -->
  <path d="M196,520 C190,430 250,385 305,388 C365,386 418,432 408,522 C392,470 360,450 320,446 C300,470 245,468 222,470 C208,482 200,500 196,520 Z" fill="#2c2b3a"/>
  <!-- 귀 -->
  <path d="M200,545 C182,540 180,585 204,588" fill="#f7d7bd"/>
  <path d="M404,545 C422,540 424,585 400,588" fill="#f7d7bd"/>
  <!-- 눈썹 (무표정) -->
  <line x1="232" y1="512" x2="278" y2="516" stroke-width="8"/>
  <line x1="326" y1="516" x2="372" y2="512" stroke-width="8"/>
  <!-- 안경 -->
  <rect x="222" y="528" width="68" height="52" rx="18" fill="#ffffff" fill-opacity="0.55" stroke-width="6"/>
  <rect x="314" y="528" width="68" height="52" rx="18" fill="#ffffff" fill-opacity="0.55" stroke-width="6"/>
  <line x1="290" y1="548" x2="314" y2="548" stroke-width="6"/>
  <line x1="222" y1="546" x2="202" y2="540" stroke-width="6"/>
  <line x1="382" y1="546" x2="402" y2="540" stroke-width="6"/>
  <!-- 눈 (반쯤 감긴 눈) -->
  <path d="M238,552 L274,552" stroke-width="7"/>
  <circle cx="258" cy="560" r="8" fill="{INK}" stroke="none"/>
  <path d="M330,552 L366,552" stroke-width="7"/>
  <circle cx="350" cy="560" r="8" fill="{INK}" stroke="none"/>
  <!-- 코, 입 -->
  <path d="M300,580 C292,600 294,608 306,608" fill="none" stroke-width="5"/>
  <path d="M278,642 L326,640" fill="none" stroke-width="7"/>
  <!-- 볼터치 -->
  <ellipse cx="232" cy="606" rx="18" ry="10" fill="#f3a9a0" stroke="none" opacity="0.6"/>
  <ellipse cx="372" cy="606" rx="18" ry="10" fill="#f3a9a0" stroke="none" opacity="0.6"/>
</g>

<!-- ===================== 환자 (오른쪽, 주식 중독자) ===================== -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
  <!-- 후드 모자: 목 뒤로 넘어가 접힌 상태. 앞에서 보면 목 중간 높이까지만, 폭은 어깨 안쪽(x 692~888)까지만 (몸통보다 먼저 그림) -->
  <path d="M692,796 C668,762 690,722 740,714 L840,714 C890,722 912,762 888,796 Z" fill="#8a8f9c"/>
  <!-- 모자 바깥 음영: 왼쪽 어둡게, 오른쪽 밝게 -->
  <path d="M692,796 C668,762 690,722 740,714 C710,730 700,764 712,792 Z" fill="#6f7482" stroke="none"/>
  <path d="M888,796 C912,762 890,722 840,714 C870,730 880,764 868,792 Z" fill="#9da2ae" stroke="none"/>
  <!-- 모자 안쪽(어두운 안감) -->
  <path d="M718,784 C704,762 716,738 750,732 L830,732 C864,738 876,762 862,784 Z" fill="#555a68" stroke-width="5"/>
  <path d="M730,780 C722,764 730,748 754,744 L826,744 C850,748 858,764 850,780 Z" fill="#474c59" stroke="none"/>
  <path d="M692,796 C668,762 690,722 740,714 L840,714 C890,722 912,762 888,796" fill="none"/>
  <!-- 몸통: 후드티 -->
  <path d="M580,1010 C580,830 630,760 715,738 L865,738 C950,760 1010,830 1010,1010 Z" fill="#8a8f9c"/>
  <!-- 목 -->
  <path d="M752,680 L752,750 C775,772 805,772 828,750 L828,680 Z" fill="#edc19f"/>
  <!-- 턱 아래 목 그림자 -->
  <path d="M752,684 L828,684 L828,712 C805,730 775,730 752,712 Z" fill="#d6a685" stroke="none"/>
  <!-- 어깨 위 모자 그림자 -->
  <path d="M692,798 C716,776 736,758 752,748 L752,756 C744,790 732,802 708,812 Z" fill="#000" opacity="0.14" stroke="none"/>
  <path d="M888,798 C864,776 844,758 828,748 L828,756 C836,790 848,802 872,812 Z" fill="#000" opacity="0.14" stroke="none"/>
  <!-- 앞으로 내려온 모자 깃 (좌우가 가슴에서 만남) -->
  <path d="M704,746 C716,740 740,740 752,746 C760,776 772,794 792,808 L790,840 C746,822 718,792 704,746 Z" fill="#7d8290"/>
  <path d="M876,746 C864,740 840,740 828,746 C820,776 808,794 788,808 L790,840 C834,822 862,792 876,746 Z" fill="#989daa"/>
  <path d="M720,756 C732,790 754,812 784,828" fill="none" stroke-width="4" stroke="#5f6472"/>
  <path d="M860,756 C848,790 826,812 796,828" fill="none" stroke-width="4" stroke="#6f7482"/>
  <!-- 끈 구멍 + 후드 끈 -->
  <circle cx="760" cy="804" r="6" fill="#474c59" stroke-width="3"/>
  <circle cx="820" cy="804" r="6" fill="#474c59" stroke-width="3"/>
  <path d="M760,808 C756,842 762,872 756,900" fill="none" stroke="#f1f1f1" stroke-width="6"/>
  <path d="M820,808 C824,842 818,872 824,900" fill="none" stroke="#f1f1f1" stroke-width="6"/>
  <circle cx="756" cy="905" r="6" fill="#f1f1f1" stroke-width="3"/>
  <circle cx="824" cy="905" r="6" fill="#f1f1f1" stroke-width="3"/>
  <!-- 얼굴 -->
  <path d="M686,548 C686,455 738,425 790,425 C844,425 894,455 894,548 C894,655 846,708 790,708 C734,708 686,655 686,548 Z" fill="#f4cfae"/>
  <!-- 귀 -->
  <path d="M686,560 C668,555 666,602 690,605" fill="#f4cfae"/>
  <path d="M894,560 C912,555 914,602 890,605" fill="#f4cfae"/>
  <!-- 부스스한 머리 -->
  <path d="M676,540 C650,470 668,420 700,410 C690,385 720,365 745,378 C752,348 792,340 808,366 C832,342 872,356 870,388 C900,384 922,412 906,440 C928,462 918,510 902,540
           C898,500 880,476 858,470 C850,488 826,482 820,466 C806,486 778,486 770,466 C756,486 726,484 722,468 C700,478 684,504 676,540 Z" fill="#3a2c26"/>
  <!-- 삐친 머리 -->
  <path d="M760,360 C756,335 770,322 782,318" fill="none" stroke-width="6"/>
  <path d="M822,362 C830,340 846,334 856,336" fill="none" stroke-width="6"/>
  <!-- 눈썹 (팔자) -->
  <path d="M716,520 L762,506" stroke-width="8"/>
  <path d="M818,506 L864,520" stroke-width="8"/>
  <!-- 다크서클 -->
  <path d="M712,590 C725,612 760,612 772,590" fill="#b99ab0" stroke="none" opacity="0.75"/>
  <path d="M808,590 C820,612 855,612 868,590" fill="#b99ab0" stroke="none" opacity="0.75"/>
  <!-- 눈 (충혈된 큰 눈) -->
  <ellipse cx="742" cy="562" rx="32" ry="30" fill="#ffffff" stroke-width="6"/>
  <ellipse cx="838" cy="562" rx="32" ry="30" fill="#ffffff" stroke-width="6"/>
  <g stroke="#e2483d" stroke-width="3" fill="none">
    <path d="M714,556 L724,560 L720,566"/><path d="M768,574 L760,570 L764,564"/>
    <path d="M810,556 L820,560 L816,566"/><path d="M864,574 L856,570 L860,564"/>
  </g>
  <circle cx="748" cy="564" r="8" fill="{INK}" stroke="none"/>
  <circle cx="832" cy="564" r="8" fill="{INK}" stroke="none"/>
  <!-- 코 -->
  <path d="M790,592 C782,612 784,620 796,620" fill="none" stroke-width="5"/>
  <!-- 입 (떨리는 미소) -->
  <path d="M750,652 C762,668 776,650 790,664 C804,650 818,668 830,652" fill="none" stroke-width="7"/>
  <!-- 수염 자국 -->
  <g fill="#8a6f60" stroke="none">
    <circle cx="740" cy="676" r="3"/><circle cx="756" cy="686" r="3"/><circle cx="774" cy="692" r="3"/>
    <circle cx="792" cy="694" r="3"/><circle cx="810" cy="692" r="3"/><circle cx="828" cy="686" r="3"/>
    <circle cx="842" cy="676" r="3"/><circle cx="766" cy="676" r="3"/><circle cx="816" cy="676" r="3"/>
  </g>
  <!-- 식은땀 -->
  <path d="M916,470 C902,496 902,514 916,518 C930,514 930,496 916,470 Z" fill="#9ed8f5" stroke-width="5"/>
</g>

<!-- ===================== 책상 ===================== -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
  <rect x="-10" y="990" width="1100" height="380" fill="url(#desk)"/>
  <line x1="-10" y1="1020" x2="1100" y2="1020" stroke="#8a6238" stroke-width="5"/>

  <!-- 혈압계 본체 (가운데) -->
  <g transform="translate(455,860)">
    <rect x="0" y="0" width="190" height="140" rx="16" fill="#eef1f4"/>
    <rect x="18" y="18" width="154" height="78" rx="8" fill="#1f2a33"/>
    <text x="95" y="60" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="38" fill="#ff5a4e" stroke="none">168</text>
    <text x="95" y="90" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="26" fill="#ff5a4e" stroke="none">105</text>
    <path d="M150,34 L158,48 L142,48 Z" fill="#ff5a4e" stroke="none"/>
    <circle cx="48" cy="118" r="10" fill="#4fb36c" stroke-width="4"/>
    <circle cx="142" cy="118" r="10" fill="#e2483d" stroke-width="4"/>
  </g>
  <!-- 혈압계 튜브 -> 환자 팔 -->
  <path d="M645,930 C700,930 690,960 740,950" fill="none" stroke="#4a5568" stroke-width="9"/>

  <!-- 의사 손 + 차트 -->
  <g>
    <path d="M150,1000 C150,960 200,948 240,958 L300,975 L300,1010 Z" fill="#ffffff"/>
    <rect x="215" y="930" width="190" height="130" rx="8" fill="#b9814f" transform="rotate(-6 310 995)"/>
    <rect x="228" y="945" width="164" height="104" rx="4" fill="#fff1b8" transform="rotate(-6 310 995)"/>
    <g stroke="#9aa7b3" stroke-width="5" transform="rotate(-6 310 995)">
      <line x1="244" y1="970" x2="372" y2="970"/><line x1="244" y1="992" x2="372" y2="992"/>
      <line x1="244" y1="1014" x2="330" y2="1014"/>
    </g>
    <rect x="282" y="922" width="56" height="20" rx="6" fill="#8d99a6" transform="rotate(-6 310 995)"/>
    <ellipse cx="232" cy="1002" rx="34" ry="26" fill="#f7d7bd"/>
  </g>

  <!-- 환자 팔 + 혈압 커프 + 휴대폰 -->
  <g>
    <!-- 왼팔(커프) -->
    <path d="M640,1010 C640,965 690,935 760,945 L790,1010 Z" fill="#8a8f9c"/>
    <rect x="668" y="930" width="92" height="74" rx="12" fill="#3e6fb5" transform="rotate(-12 714 967)"/>
    <line x1="690" y1="940" x2="682" y2="1000" stroke="#2a4f86" stroke-width="5"/>
    <!-- 오른팔 -->
    <path d="M1010,1010 C1010,950 950,925 900,945 L870,1010 Z" fill="#8a8f9c"/>
    <!-- 휴대폰 -->
    <g transform="rotate(8 880 930)">
      <rect x="812" y="838" width="136" height="200" rx="18" fill="#22252c"/>
      <rect x="824" y="852" width="112" height="172" rx="8" fill="#0f1a2b"/>
      <!-- 떨어지는 파란 차트 -->
      <text x="880" y="884" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="28" fill="#3b8cff" stroke="none">-50%</text>
      <polyline points="832,900 850,908 864,904 882,926 898,920 914,946 928,968" fill="none" stroke="#3b8cff" stroke-width="7"/>
      <path d="M932,978 L918,962 L938,958 Z" fill="#3b8cff" stroke="none"/>
    </g>
    <!-- 휴대폰 쥔 손 -->
    <ellipse cx="850" cy="1000" rx="36" ry="27" fill="#f4cfae"/>
    <ellipse cx="930" cy="1008" rx="34" ry="26" fill="#f4cfae"/>
  </g>
</g>
'''

# 말풍선 위치: (cx, cy, rx, ry, tail)
B = [
    (272, 166, 250, 142, (290, 370, 296, 300, 388)),   # 의사 1
    (808, 166, 250, 142, (730, 815, 296, 790, 350)),   # 환자 1
    (272, 1184, 250, 144, (275, 355, 1062, 345, 978)),  # 의사 2
    (808, 1184, 250, 144, (735, 815, 1062, 770, 985)),  # 환자 2
]


def build(i, lines4):
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', SCENE]
    for (cx, cy, rx, ry, tail), t in zip(B, lines4):
        parts.append(bubble(cx, cy, rx, ry, tail, t))
    parts.append("</svg>")
    svg = f"{OUT}/_{i:02d}.svg"
    png = f"{OUT}/주식중독자_건강검진_{i:02d}.png"
    open(svg, "w").write("\n".join(parts))
    subprocess.run(["rsvg-convert", "-w", str(W), "-h", str(H), svg, "-o", png], check=True)
    os.remove(svg)
    return png


if __name__ == "__main__":
    for i, s in enumerate(SCRIPT, 1):
        print(build(i, s))
