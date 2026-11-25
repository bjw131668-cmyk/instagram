import sys, lib, lib2, db
INK=lib.INK
E=db.load(11); SCRIPT=E["script"]; TH=E["thumb"]
SK="#efc6a4"
SCENE=f'''
<defs><linearGradient id="t11" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9a6a42"/><stop offset="1" stop-color="#7a4f2e"/></linearGradient></defs>
<rect width="1080" height="1350" fill="#6e4a33"/>
<g stroke="#5a3b28" stroke-width="5"><line x1="0" y1="330" x2="1080" y2="330"/><line x1="0" y1="430" x2="1080" y2="430"/><line x1="0" y1="530" x2="1080" y2="530"/><line x1="0" y1="630" x2="1080" y2="630"/><line x1="0" y1="730" x2="1080" y2="730"/></g>
<rect y="780" width="1080" height="600" fill="#5a3b28"/>
<!-- 네온 간판 (맥주잔 무늬, 글자 없음) -->
<g fill="none" stroke-linecap="round" stroke-linejoin="round">
 <rect x="430" y="300" width="220" height="150" rx="20" stroke="#ff5fa2" stroke-width="16" opacity="0.35"/>
 <rect x="430" y="300" width="220" height="150" rx="20" stroke="#ff9cc8" stroke-width="7"/>
 <path d="M496,334 L496,420 L568,420 L568,334" stroke="#ffd66b" stroke-width="16" opacity="0.35"/>
 <path d="M496,334 L496,420 L568,420 L568,334 M568,354 C600,354 600,400 568,400 M500,346 C516,334 548,334 564,346" stroke="#ffe9a8" stroke-width="7"/>
</g>
<!-- 메뉴판 (선) + 등 -->
<g stroke="{INK}" stroke-width="6"><rect x="30" y="300" width="140" height="190" rx="8" fill="#f3e3c3"/><rect x="910" y="300" width="140" height="190" rx="8" fill="#f3e3c3"/></g>
<g stroke="#9a7b55" stroke-width="5" stroke-linecap="round"><line x1="50" y1="340" x2="150" y2="340"/><line x1="50" y1="370" x2="130" y2="370"/><line x1="50" y1="400" x2="150" y2="400"/><line x1="50" y1="430" x2="120" y2="430"/><line x1="930" y1="340" x2="1030" y2="340"/><line x1="930" y1="370" x2="1010" y2="370"/><line x1="930" y1="400" x2="1030" y2="400"/><line x1="930" y1="430" x2="1000" y2="430"/></g>
<g fill="#e2483d" stroke="none"><rect x="50" y="458" width="60" height="14" rx="4"/><rect x="930" y="458" width="60" height="14" rx="4"/></g>

<!-- 팀장 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <path d="M95,1010 C95,820 150,745 235,725 L365,725 C450,745 505,820 505,1010 Z" fill="#a9c8ea"/>
 <path d="M248,727 L300,800 L352,727 Z" fill="#f3cdb3"/>
 <path d="M235,725 L300,810 L262,850 L205,750 Z" fill="#bcd6f1"/><path d="M365,725 L300,810 L338,850 L395,750 Z" fill="#bcd6f1"/>
 <line x1="300" y1="810" x2="300" y2="900" stroke-width="5"/>
 <g transform="rotate(14 300 790)"><path d="M288,786 L312,786 L316,808 L300,816 L284,808 Z" fill="#c0392b" stroke-width="5"/><path d="M290,812 L310,812 L320,900 L300,924 L280,900 Z" fill="#c0392b" stroke-width="5"/></g>
 <path d="M262,660 L262,735 C285,760 315,760 338,735 L338,660 Z" fill="#e6b796"/>
 <path d="M200,530 C200,440 250,410 302,410 C356,410 404,440 404,530 C404,640 356,690 302,690 C248,690 200,640 200,530 Z" fill="#efc6a4"/>
 <path d="M200,545 C182,540 180,585 204,588" fill="#efc6a4"/><path d="M404,545 C422,540 424,585 400,588" fill="#efc6a4"/>
 <!-- 머리: 숱 적은 옆머리 -->
 <path d="M196,520 C186,450 214,410 250,400 C240,430 236,460 222,480 C210,490 202,504 196,520 Z" fill="#3b3b44"/>
 <path d="M408,520 C418,450 390,410 354,400 C364,430 368,460 382,480 C394,490 402,504 408,520 Z" fill="#3b3b44"/>
 <path d="M262,404 C280,392 324,392 342,404" fill="none" stroke-width="6"/>
 <path d="M276,420 C292,412 312,412 328,420" fill="none" stroke-width="5"/>
 <!-- 눈썹/안경/눈 -->
 <path d="M228,516 L282,526" stroke-width="9"/><path d="M322,526 L376,516" stroke-width="9"/>
 <rect x="222" y="534" width="70" height="44" rx="6" fill="#fff" fill-opacity="0.5" stroke-width="6"/>
 <rect x="312" y="534" width="70" height="44" rx="6" fill="#fff" fill-opacity="0.5" stroke-width="6"/>
 <line x1="292" y1="552" x2="312" y2="552" stroke-width="6"/>
 <circle cx="258" cy="558" r="8" fill="{INK}" stroke="none"/><circle cx="348" cy="558" r="8" fill="{INK}" stroke="none"/>
 <path d="M300,580 C290,604 292,612 308,612" fill="none" stroke-width="5"/>
 <path d="M270,640 C286,664 318,664 334,640" fill="none" stroke-width="7"/>
 <ellipse cx="236" cy="610" rx="24" ry="13" fill="#ef7f7f" stroke="none" opacity="0.75"/><ellipse cx="368" cy="610" rx="24" ry="13" fill="#ef7f7f" stroke="none" opacity="0.75"/>
 
</g>
{lib.CHAR}
<!-- 사원증 -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <path d="M740,790 L776,900" fill="none" stroke="#2f6fd0" stroke-width="9"/><path d="M840,790 L804,900" fill="none" stroke="#2f6fd0" stroke-width="9"/>
 <rect x="752" y="896" width="76" height="92" rx="8" fill="#ffffff"/>
 <circle cx="790" cy="928" r="13" fill="#3a2c26"/><rect x="766" y="952" width="48" height="10" rx="5" fill="#9aa7b3" stroke="none"/><rect x="772" y="968" width="36" height="8" rx="4" fill="#9aa7b3" stroke="none"/>
</g>


<!-- 호프 테이블 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <rect x="-10" y="990" width="1100" height="380" fill="url(#t11)"/>
 <line x1="-10" y1="1022" x2="1100" y2="1022" stroke="#5a3b28" stroke-width="5"/>
 <!-- 치킨 -->
 <ellipse cx="560" cy="992" rx="86" ry="18" fill="#ffffff"/>
 <path d="M500,984 C496,950 530,936 552,950 C566,930 604,936 608,962 C626,964 628,986 616,990 Z" fill="#d98a3a"/>
 <path d="M540,960 C548,954 556,956 560,962 M576,950 C584,946 590,950 592,956" fill="none" stroke="#a8601f" stroke-width="4"/>
 <!-- 맥주 피처 -->
 <path d="M636,880 L700,880 L704,1000 L632,1000 Z" fill="#f6b73c"/><path d="M632,880 L704,880 L704,904 L632,904 Z" fill="#ffffff"/>
 <path d="M704,906 C736,906 736,966 704,966" fill="none"/>
 <!-- 팀장 팔뚝 (셔츠) -->
 <path d="M96,1016 C98,966 160,950 262,962 L262,1024 L96,1024 Z" fill="#a9c8ea"/>
 <!-- 팀장 맥주잔 (손보다 먼저) -->
 <path d="M300,900 L384,900 L380,1004 L304,1004 Z" fill="#f6b73c"/>
 <path d="M296,884 C300,866 326,866 334,876 C344,862 372,864 378,880 C392,880 392,900 384,902 L300,902 C290,900 288,888 296,884 Z" fill="#ffffff"/>
 <path d="M384,920 C414,920 414,976 382,976" fill="none"/>
 <g stroke="#ffffff" stroke-width="4" opacity="0.7"><line x1="324" y1="930" x2="324" y2="980"/></g>
</g>
{lib.hand(292,992,flip=False,rot=90,skin=SK)}
{lib.cuff(262,993,rot=2,color="#bcd6f1")}
{lib.NMR_FRONT}
'''
B=lib.B2; P="11화_회식"; NX=E["next_title"]+" 편"
if sys.argv[1]=="test":
    lib2._png(lib._svg(SCENE+lib2.wm(),B,SCRIPT[0]),1080,1350,"/tmp/t11.png")
    lib2._png(lib2.cover_svg(11,"회식",SCENE,TH,B),1080,1350,"/tmp/t11c.png")
    lib2._png(lib2._frame("주식 중독자의 회식",11,"",lib._svg(SCENE,B,SCRIPT[9],4)),1080,1920,"/tmp/t11r.png")
elif sys.argv[1]=="full":
    lib2.covers(11,"회식",SCENE,TH,B,P)
    lib2.cards(SCENE,B,SCRIPT,P,E["next_n"],NX)
    print(lib2.reel(SCENE,B,SCRIPT,"주식 중독자의 회식",P,11,E["next_n"],NX))
