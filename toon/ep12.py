import sys, lib, lib2, lib3, lib4, db
INK=lib.INK
E=db.load(12); SCRIPT=E["script"]; TH=E["thumb"]
SK="#f9dcc6"; KNIT="#f3e6cf"; KNIT2="#e2d0b0"
SCENE=f'''
<rect width="1080" height="1350" fill="#1d2440"/>
<!-- 천막 안쪽 (주황) -->
<path d="M0,250 L1080,250 L1080,800 L0,800 Z" fill="#e8742f"/>
<path d="M0,250 L1080,250 L1080,800 L0,800 Z" fill="#000" opacity="0.18"/>
<!-- 비닐 벽 너머 밤거리 -->
<g opacity="0.9">
 <rect x="420" y="300" width="240" height="300" rx="10" fill="#2a3358" stroke="#c9d3e6" stroke-width="5" opacity="0.85"/>
 <rect x="436" y="430" width="44" height="160" fill="#3b4570"/><rect x="490" y="400" width="54" height="190" fill="#465184"/><rect x="556" y="450" width="40" height="140" fill="#3b4570"/><rect x="606" y="420" width="44" height="170" fill="#465184"/>
 <g fill="#ffd66b"><rect x="446" y="450" width="8" height="10"/><rect x="460" y="480" width="8" height="10"/><rect x="502" y="420" width="8" height="10"/><rect x="522" y="460" width="8" height="10"/><rect x="566" y="470" width="8" height="10"/><rect x="618" y="440" width="8" height="10"/><rect x="630" y="500" width="8" height="10"/></g>
 <path d="M420,330 C500,345 580,345 660,330" fill="none" stroke="#ffffff" stroke-width="4" opacity="0.35"/>
</g>
<!-- 백열전구 줄 -->
<path d="M0,280 C180,320 360,320 540,290 C720,320 900,320 1080,280" fill="none" stroke="#1b1b22" stroke-width="5"/>
<g stroke="{INK}" stroke-width="4" fill="#ffe08a">
 <circle cx="90" cy="306" r="13"/><circle cx="250" cy="316" r="13"/><circle cx="830" cy="316" r="13"/><circle cx="990" cy="306" r="13"/>
</g>
<g fill="#ffe08a" opacity="0.25"><circle cx="90" cy="306" r="34"/><circle cx="250" cy="316" r="34"/><circle cx="830" cy="316" r="34"/><circle cx="990" cy="306" r="34"/></g>
<!-- 메뉴 판 (선) -->
<g stroke="{INK}" stroke-width="6"><rect x="30" y="380" width="140" height="150" rx="8" fill="#fff3d6"/><rect x="910" y="380" width="140" height="150" rx="8" fill="#fff3d6"/></g>
<g stroke="#c0392b" stroke-width="6" stroke-linecap="round"><line x1="52" y1="414" x2="148" y2="414"/><line x1="932" y1="414" x2="1028" y2="414"/></g>
<g stroke="#9a7b55" stroke-width="5" stroke-linecap="round"><line x1="52" y1="446" x2="130" y2="446"/><line x1="52" y1="474" x2="148" y2="474"/><line x1="52" y1="502" x2="118" y2="502"/><line x1="932" y1="446" x2="1010" y2="446"/><line x1="932" y1="474" x2="1028" y2="474"/><line x1="932" y1="502" x2="998" y2="502"/></g>
<rect y="780" width="1080" height="600" fill="#b85a22"/>

<!-- 상한나 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <path d="M176,540 C160,400 250,356 305,358 C372,356 446,404 428,548 C440,660 446,760 420,800 L182,800 C158,760 164,660 176,540 Z" fill="#5a3a2a"/>
 <path d="M95,1010 C95,820 150,745 235,725 L365,725 C450,745 505,820 505,1010 Z" fill="{KNIT}"/>
 <path d="M232,722 C260,770 340,770 368,722 L372,752 C340,800 260,800 228,752 Z" fill="#c94a4a"/>
 <path d="M330,770 L346,860 L380,856 L360,762 Z" fill="#c94a4a"/>
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

<!-- 포차 테이블 (주황 플라스틱) -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <rect x="-10" y="990" width="1100" height="380" fill="#e05a2a"/>
 <line x1="-10" y1="1022" x2="1100" y2="1022" stroke="#a83d17" stroke-width="5"/>
 <!-- 떡볶이 접시 -->
 <ellipse cx="560" cy="990" rx="80" ry="18" fill="#3fa36b"/>
 <g fill="#e2483d" stroke-width="4"><rect x="510" y="958" width="40" height="18" rx="9" transform="rotate(-12 530 967)"/><rect x="548" y="950" width="40" height="18" rx="9" transform="rotate(10 568 959)"/><rect x="580" y="962" width="40" height="18" rx="9" transform="rotate(-6 600 971)"/><rect x="530" y="972" width="40" height="18" rx="9"/></g>
 <!-- 음료 (나물려 쪽) -->
 <path d="M640,904 L692,904 L686,1000 L646,1000 Z" fill="#9fd8a6"/><rect x="652" y="884" width="28" height="22" rx="4" fill="#3b8f4f"/>
 <!-- 상한나 팔뚝 -->
 <path d="M96,1016 C98,966 160,950 262,962 L262,1024 L96,1024 Z" fill="{KNIT}"/>
 <!-- 어묵 컵 (손보다 먼저) -->
 <path d="M300,920 L384,920 L376,1004 L308,1004 Z" fill="#ffffff"/>
 <path d="M300,920 L384,920 L382,940 L302,940 Z" fill="#f2c26b"/>
 <line x1="328" y1="920" x2="320" y2="852" stroke-width="5"/><line x1="358" y1="920" x2="366" y2="856" stroke-width="5"/>
 <path d="M306,884 L322,870 L336,884 L322,898 Z M306,912 L322,898 L336,912 Z" fill="#f0c98a" stroke-width="4"/>
 <path d="M350,888 L366,874 L380,888 L366,902 Z M350,916 L366,902 L380,916 Z" fill="#f0c98a" stroke-width="4"/>
</g>
{lib.hand(292,992,flip=False,rot=90,skin=SK)}
{lib.cuff(262,993,rot=2,color=KNIT2)}
{lib.NMR_FRONT}
'''
B=lib.B2; P="12화_썸"; NX=E["next_title"]+" 편"
if sys.argv[1]=="test":
    lib2._png(lib._svg(SCENE+lib2.wm(),B,SCRIPT[0]),1080,1350,"/tmp/t12.png")
elif sys.argv[1]=="full":
    lib4.covers("썸",SCENE,TH,B,P)
    lib4.cards(SCENE,B,SCRIPT,P,E["next_n"],NX)
    print(lib4.reel(SCENE,B,SCRIPT,"주식 중독자의 썸",P,E["next_n"],NX))
