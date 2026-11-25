import sys, lib, lib2, lib3, db
INK=lib.INK
E=db.load(10); SCRIPT=E["script"]; TH=E["thumb"]
SK="#f9dcc6"; KNIT="#a9cdec"; KNIT2="#93bde2"
SCENE=f'''
<defs>
 <linearGradient id="w10" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6e7cf"/><stop offset="1" stop-color="#ead5b5"/></linearGradient>
 <linearGradient id="s10" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd9a8"/><stop offset="1" stop-color="#ffeccc"/></linearGradient>
 <linearGradient id="t10" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a87245"/><stop offset="1" stop-color="#875632"/></linearGradient>
</defs>
<rect width="1080" height="1350" fill="url(#w10)"/>
<!-- 아래 벽: 나무 판넬 -->
<rect y="780" width="1080" height="600" fill="#c99a6b"/>
<g stroke="#b2845a" stroke-width="4"><line x1="90" y1="780" x2="90" y2="1000"/><line x1="270" y1="780" x2="270" y2="1000"/><line x1="450" y1="780" x2="450" y2="1000"/><line x1="630" y1="780" x2="630" y2="1000"/><line x1="810" y1="780" x2="810" y2="1000"/><line x1="990" y1="780" x2="990" y2="1000"/></g>
<rect y="770" width="1080" height="14" fill="#a87245"/>
<!-- 펜던트 조명 -->
<g stroke="{INK}" stroke-width="5"><line x1="100" y1="0" x2="100" y2="300"/><line x1="980" y1="0" x2="980" y2="300"/></g>
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round"><path d="M64,330 C64,300 136,300 136,330 Z" fill="#2f6b5a"/><path d="M944,330 C944,300 1016,300 1016,330 Z" fill="#2f6b5a"/></g>
<ellipse cx="100" cy="338" rx="22" ry="9" fill="#ffe08a"/><ellipse cx="980" cy="338" rx="22" ry="9" fill="#ffe08a"/>
<!-- 창문 (노을 거리) -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <rect x="420" y="300" width="240" height="300" rx="8" fill="url(#s10)"/>
 <g stroke="none"><rect x="430" y="470" width="50" height="124" fill="#e7b98c"/><rect x="486" y="430" width="60" height="164" fill="#d9a77a"/><rect x="552" y="480" width="46" height="114" fill="#efc79c"/><rect x="604" y="440" width="50" height="154" fill="#d49e70"/></g>
 <line x1="540" y1="300" x2="540" y2="600" stroke-width="5"/><line x1="420" y1="450" x2="660" y2="450" stroke-width="5"/>
 <rect x="420" y="300" width="240" height="300" rx="8" fill="none"/>
 <rect x="408" y="598" width="264" height="16" rx="4" fill="#a87245"/>
</g>
<!-- 선반 + 화분 -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <rect x="10" y="470" width="170" height="14" rx="4" fill="#a87245"/>
 <path d="M40,470 L48,420 L92,420 L100,470 Z" fill="#e2895a"/><path d="M70,420 C50,390 46,370 60,350 M70,420 C80,380 96,370 110,372 M70,420 C66,396 72,380 84,366" fill="none" stroke="#3f8f57" stroke-width="7"/>
 <rect x="118" y="436" width="34" height="34" rx="4" fill="#fff7ea"/><rect x="118" y="436" width="34" height="8" fill="#6b4229" stroke="none"/>
 <rect x="900" y="470" width="170" height="14" rx="4" fill="#a87245"/>
 <rect x="924" y="412" width="40" height="58" rx="5" fill="#fff7ea"/><rect x="972" y="424" width="34" height="46" rx="5" fill="#cfe4f5"/>
 <path d="M1018,470 L1024,430 L1058,430 L1064,470 Z" fill="#e2895a"/><circle cx="1041" cy="414" r="20" fill="#5aa86a"/>
</g>

<!-- 상한나 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <path d="M176,540 C160,400 250,356 305,358 C372,356 446,404 428,548 C440,660 446,760 420,800 L182,800 C158,760 164,660 176,540 Z" fill="#5a3a2a"/>
 <path d="M95,1010 C95,820 150,745 235,725 L365,725 C450,745 505,820 505,1010 Z" fill="{KNIT}"/>
 <path d="M248,728 C270,760 330,760 352,728" fill="{KNIT2}"/>
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
 <path d="M282,646 L322,644" fill="none" stroke-width="7"/>
 <ellipse cx="230" cy="606" rx="20" ry="11" fill="#f3a9a0" stroke="none" opacity="0.7"/>
 <ellipse cx="374" cy="606" rx="20" ry="11" fill="#f3a9a0" stroke="none" opacity="0.7"/>
</g>

{lib.CHAR}

<!-- 카페 테이블 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <rect x="-10" y="990" width="1100" height="380" fill="url(#t10)"/>
 <line x1="-10" y1="1022" x2="1100" y2="1022" stroke="#6b4229" stroke-width="5"/>
 <!-- 조각 케이크 -->
 <ellipse cx="560" cy="996" rx="70" ry="14" fill="#ffffff"/>
 <path d="M520,990 L520,950 L600,936 L600,980 Z" fill="#fff1d6"/><path d="M520,950 L600,936 L600,948 L520,962 Z" fill="#f2b8c0" stroke-width="5"/>
 <circle cx="566" cy="930" r="10" fill="#e2483d" stroke-width="5"/>
 <!-- 나물려 아이스커피 -->
 <path d="M640,900 L694,900 L687,1000 L647,1000 Z" fill="#e9f5fb"/><path d="M644,930 L690,930 L687,1000 L647,1000 Z" fill="#7a4a2b" stroke="none"/><path d="M640,900 L694,900 L687,1000 L647,1000 Z" fill="none"/><path d="M670,900 L682,852" fill="none" stroke-width="6"/>
 <!-- 상한나 팔뚝 (니트) -->
 <path d="M96,1016 C98,966 160,950 262,962 L262,1024 L96,1024 Z" fill="{KNIT}"/>
 <!-- 라테 머그 (손보다 먼저) -->
 <path d="M300,930 L392,930 L384,1004 L308,1004 Z" fill="#ffffff"/>
 <path d="M390,946 C420,946 418,986 384,986" fill="none"/>
 <ellipse cx="346" cy="932" rx="46" ry="9" fill="#c8915e"/>
 <path d="M336,930 C340,924 352,924 356,930" fill="none" stroke="#fff7ea" stroke-width="4"/>
 <path d="M330,912 C322,898 338,892 330,876 M362,912 C354,898 370,892 362,876" fill="none" stroke-width="4" stroke="#8d99a6"/>
</g>
{lib.hand(292,992,flip=False,rot=90,skin=SK)}
{lib.cuff(262,993,rot=2,color=KNIT2)}
{lib.NMR_FRONT}
'''
B=lib.B2; P="10화_고백"; LB="나물려의 사랑 ③"; NX=E["next_title"]+" 편"
if sys.argv[1]=="test":
    lib2._png(lib._svg(SCENE+lib2.wm(),B,SCRIPT[0]),1080,1350,"/tmp/t10.png")
    lib2._png(lib3.cover_svg(10,"고백",SCENE,TH,B,LB),1080,1350,"/tmp/t10c.png")
    lib2._png(lib3._frame("주식 중독자의 고백",10,LB,lib._svg(SCENE,B,SCRIPT[9],4)),1080,1920,"/tmp/t10r.png")
elif sys.argv[1]=="full":
    lib3.covers(10,"고백",SCENE,TH,B,P,LB)
    lib2.cards(SCENE,B,SCRIPT,P,E["next_n"],NX)
    print(lib3.reel(SCENE,B,SCRIPT,"주식 중독자의 고백",P,10,LB,E["next_n"],NX))
