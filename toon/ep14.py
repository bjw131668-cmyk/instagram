import sys, lib, lib2, lib3, lib4, db
INK=lib.INK
E=db.load(14); SCRIPT=E["script"]; TH=E["thumb"]
SK="#f9dcc6"; KNIT="#f6c9d6"; KNIT2="#eab3c3"
SCENE=f'''
<!-- 왼쪽: 한나 방 -->
<rect width="540" height="1350" fill="#e9e1f0"/>
<rect y="780" width="540" height="600" fill="#d9cde6"/>
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <rect x="40" y="300" width="150" height="170" rx="8" fill="#2c3560"/>
 <line x1="115" y1="300" x2="115" y2="470" stroke-width="5"/><line x1="40" y1="385" x2="190" y2="385" stroke-width="5"/>
</g>
<circle cx="155" cy="340" r="18" fill="#fff2b3"/>
<g fill="#fff" opacity="0.8"><circle cx="70" cy="330" r="3"/><circle cx="90" cy="420" r="3"/><circle cx="160" cy="430" r="3"/></g>
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round"><path d="M440,380 L500,380 L486,440 L454,440 Z" fill="#ffd9a0"/><line x1="470" y1="440" x2="470" y2="560" stroke-width="5"/><rect x="440" y="556" width="60" height="14" rx="5" fill="#b9a3cf"/></g>
<ellipse cx="470" cy="470" rx="70" ry="50" fill="#fff2b3" opacity="0.35"/>
<!-- 오른쪽: 나물려 방 -->
<rect x="540" width="540" height="1350" fill="#d7dde8"/>
<rect x="540" y="780" width="540" height="600" fill="#c3cad8"/>
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <rect x="600" y="300" width="130" height="90" rx="6" fill="#22252c"/><rect x="610" y="310" width="110" height="70" rx="3" fill="#0f1a2b"/>
 <rect x="900" y="300" width="130" height="90" rx="6" fill="#22252c"/><rect x="910" y="310" width="110" height="70" rx="3" fill="#0f1a2b"/>
</g>
<polyline points="616,330 640,340 660,336 684,356 712,370" fill="none" stroke="#3b8cff" stroke-width="5"/>
<polyline points="916,326 944,344 968,338 990,360 1014,372" fill="none" stroke="#3b8cff" stroke-width="5"/>
<!-- 가운데 구분선 -->
<rect x="532" y="0" width="16" height="1350" fill="#1b1b22"/>

<!-- 상한나 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <path d="M176,540 C160,400 250,356 305,358 C372,356 446,404 428,548 C440,660 446,760 420,800 L182,800 C158,760 164,660 176,540 Z" fill="#5a3a2a"/>
 <path d="M95,1010 C95,820 150,745 235,725 L365,725 C450,745 505,820 505,1010 Z" fill="{KNIT}"/>
 <path d="M246,728 C270,770 330,770 354,728" fill="{KNIT2}"/>
 <path d="M282,760 L278,840 M318,760 L322,840" fill="none" stroke="#ffffff" stroke-width="6"/>
 <g stroke="{KNIT2}" stroke-width="5" fill="none"><path d="M170,830 L170,990"/><path d="M220,800 L220,990"/><path d="M380,800 L380,990"/><path d="M430,830 L430,990"/></g>
 <path d="M262,660 L262,735 C285,760 315,760 338,735 L338,660 Z" fill="#f3cdb3"/>
 <path d="M200,530 C200,440 250,410 302,410 C356,410 404,440 404,530 C404,640 356,690 302,690 C248,690 200,640 200,530 Z" fill="{SK}"/>
 <path d="M194,540 C184,430 250,384 305,386 C366,384 424,432 410,540 C400,490 380,462 350,450 C330,480 260,486 228,470 C210,490 200,512 194,540 Z" fill="#5a3a2a"/>
 <path d="M232,508 C246,500 264,500 278,506" fill="none" stroke-width="6"/>
 <path d="M326,500 C340,490 358,490 372,498" fill="none" stroke-width="6"/>
 <path d="M236,550 C248,540 266,540 278,550" fill="none" stroke-width="7"/>
 <path d="M326,550 C338,540 356,540 368,550" fill="none" stroke-width="7"/>
 <circle cx="257" cy="558" r="9" fill="{INK}" stroke="none"/><circle cx="347" cy="558" r="9" fill="{INK}" stroke="none"/>
 <path d="M300,578 C294,598 296,606 306,606" fill="none" stroke-width="5"/>
 <path d="M280,640 C292,656 312,656 324,640" fill="none" stroke-width="7"/>
 <ellipse cx="230" cy="606" rx="20" ry="11" fill="#f3a9a0" stroke="none" opacity="0.7"/>
 <ellipse cx="374" cy="606" rx="20" ry="11" fill="#f3a9a0" stroke="none" opacity="0.7"/>
</g>

{lib.CHAR}

<!-- 전경: 왼쪽 이불, 오른쪽 책상 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <path d="M-10,990 C120,960 400,970 540,990 L540,1360 L-10,1360 Z" fill="#fbf3e4"/>
 <path d="M40,1040 C160,1020 360,1030 500,1050" fill="none" stroke="#e7d8bd" stroke-width="5"/>
 <rect x="540" y="990" width="560" height="380" fill="#9aa6bd"/>
 <line x1="540" y1="1022" x2="1100" y2="1022" stroke="#7c879e" stroke-width="5"/>
 <!-- 한나 팔뚝 -->
 <path d="M96,1016 C98,966 160,950 262,962 L262,1024 L96,1024 Z" fill="{KNIT}"/>
 <!-- 한나 휴대폰 (+47%) -->
 <g transform="rotate(-6 345 930)">
  <rect x="290" y="840" width="112" height="176" rx="16" fill="#22252c"/>
  <rect x="300" y="852" width="92" height="150" rx="7" fill="#fff5f5"/>
  <text x="346" y="884" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="24" fill="#e2483d" stroke="none">+47%</text>
  <polyline points="306,980 324,966 338,970 356,944 372,950 388,920" fill="none" stroke="#e2483d" stroke-width="6"/>
 </g>
</g>
{lib.hand(292,992,flip=False,rot=90,skin=SK)}
{lib.cuff(262,993,rot=2,color=KNIT2)}
{lib.NMR_FRONT}
'''
B=lib.B2; P="14화_썸카톡"; NX=E["next_title"]+" 편"
if sys.argv[1]=="test":
    lib2._png(lib._svg(SCENE+lib2.wm(),B,SCRIPT[0]),1080,1350,"/tmp/t14.png")
elif sys.argv[1]=="full":
    lib4.covers("썸 카톡",SCENE,TH,B,P)
    lib4.cards(SCENE,B,SCRIPT,P,E["next_n"],NX)
    print(lib4.reel(SCENE,B,SCRIPT,"주식 중독자의 썸 카톡",P,E["next_n"],NX))
