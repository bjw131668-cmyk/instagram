import sys, lib, lib2, lib4, db
INK=lib.INK
E=db.load(13); SCRIPT=E["script"]; TH=E["thumb"]
SK="#f2cdae"; JK="#3d5a8a"; JK2="#324c76"
SCENE=f'''
<rect width="1080" height="1350" fill="#efe3cf"/>
<rect y="780" width="1080" height="600" fill="#d7bf9a"/>
<g stroke="#c8ad86" stroke-width="4"><line x1="120" y1="780" x2="120" y2="1000"/><line x1="300" y1="780" x2="300" y2="1000"/><line x1="480" y1="780" x2="480" y2="1000"/><line x1="660" y1="780" x2="660" y2="1000"/><line x1="840" y1="780" x2="840" y2="1000"/><line x1="1020" y1="780" x2="1020" y2="1000"/></g>
<rect y="770" width="1080" height="14" fill="#b99468"/>
<!-- 동창회 현수막 (무늬만) -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <path d="M380,300 L700,300 L690,350 L700,400 L380,400 L390,350 Z" fill="#f6d77a"/>
</g>
<g fill="#e2483d"><path d="M430,350 l8,-16 l8,16 l-16,-10 h16 z"/><path d="M634,350 l8,-16 l8,16 l-16,-10 h16 z"/></g>
<path d="M470,352 C490,336 510,368 530,352 C550,336 570,368 590,352 C600,344 606,346 612,352" fill="none" stroke="#7a5a2e" stroke-width="6" stroke-linecap="round"/>
<line x1="380" y1="300" x2="330" y2="262" stroke="{INK}" stroke-width="4"/><line x1="700" y1="300" x2="750" y2="262" stroke="{INK}" stroke-width="4"/>
<!-- 액자 두 개 -->
<g stroke="{INK}" stroke-width="6"><rect x="40" y="330" width="130" height="100" rx="6" fill="#fffaf0"/><rect x="910" y="330" width="130" height="100" rx="6" fill="#fffaf0"/></g>
<path d="M56,414 L92,370 L116,396 L132,380 L156,414 Z" fill="#9fc7a6"/><circle cx="140" cy="356" r="10" fill="#f2b84b"/>
<path d="M926,414 L962,370 L986,396 L1002,380 L1026,414 Z" fill="#a9c3e6"/><circle cx="1010" cy="356" r="10" fill="#f2b84b"/>

<!-- 동창 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <path d="M95,1010 C95,820 150,745 235,725 L365,725 C450,745 505,820 505,1010 Z" fill="{JK}"/>
 <path d="M250,728 L300,860 L350,728 Z" fill="#ffffff"/>
 <path d="M235,725 L300,860 L262,770 Z M365,725 L300,860 L338,770 Z" fill="{JK2}"/>
 <path d="M262,660 L262,735 C285,758 315,758 338,735 L338,660 Z" fill="#e9bf9e"/>
 <path d="M200,530 C200,440 250,410 302,410 C356,410 404,440 404,530 C404,640 356,690 302,690 C248,690 200,640 200,530 Z" fill="{SK}"/>
 <path d="M200,560 C206,610 212,560 202,540 M404,560 C398,610 392,560 402,540" fill="none"/>
 <path d="M196,520 C186,436 236,396 300,396 C366,396 418,436 408,520 C394,478 368,462 334,470 C312,456 270,454 244,470 C222,474 204,492 196,520 Z" fill="#2f2622"/>
 <path d="M190,560 C178,556 176,600 196,604" fill="{SK}"/><path d="M414,560 C426,556 428,600 408,604" fill="{SK}"/>
 <path d="M232,506 L276,500" stroke-width="7"/><path d="M328,500 L372,506" stroke-width="7"/>
 <rect x="226" y="526" width="64" height="48" rx="12" fill="#ffffff" fill-opacity="0.35" stroke-width="7"/>
 <rect x="316" y="526" width="64" height="48" rx="12" fill="#ffffff" fill-opacity="0.35" stroke-width="7"/>
 <line x1="290" y1="546" x2="316" y2="546" stroke-width="6"/>
 <path d="M246,552 C252,544 264,544 270,552" fill="none" stroke-width="6"/><path d="M336,552 C342,544 354,544 360,552" fill="none" stroke-width="6"/>
 <path d="M300,586 C294,604 296,610 306,610" fill="none" stroke-width="5"/>
 <path d="M262,632 C280,666 324,666 342,632 Z" fill="#ffffff"/>
</g>

{lib.CHAR}

<!-- 테이블 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <rect x="-10" y="990" width="1100" height="380" fill="#c9a274"/>
 <line x1="-10" y1="1022" x2="1100" y2="1022" stroke="#a9845a" stroke-width="5"/>
 <!-- 노가리 접시 -->
 <ellipse cx="560" cy="992" rx="80" ry="17" fill="#ffffff"/>
 <g fill="#d9a85f" stroke-width="4"><path d="M506,982 L560,966 L566,976 L512,990 Z"/><path d="M548,986 L606,970 L610,980 L554,994 Z"/><path d="M520,972 L574,960 L578,968 L524,980 Z"/></g>
 <!-- 나물려 맥주 -->
 <path d="M640,906 L696,906 L692,1000 L644,1000 Z" fill="#f6b73c"/><path d="M638,890 C642,878 664,878 668,886 C676,876 698,880 700,894 L700,908 L638,908 Z" fill="#ffffff"/>
 <!-- 동창 팔뚝 -->
 <path d="M96,1016 C98,966 160,950 262,962 L262,1024 L96,1024 Z" fill="{JK}"/>
 <!-- 동창 맥주잔 -->
 <path d="M300,900 L384,900 L380,1004 L304,1004 Z" fill="#f6b73c"/>
 <path d="M296,884 C300,866 326,866 334,876 C344,862 372,864 378,880 C392,880 392,900 384,902 L300,902 C290,900 288,888 296,884 Z" fill="#ffffff"/>
 <path d="M384,920 C414,920 414,976 382,976" fill="none"/>
</g>
{lib.hand(292,992,flip=False,rot=90,skin=SK)}
{lib.cuff(262,993,rot=2,color=JK2)}
{lib.NMR_FRONT}
'''
B=lib.B2; P="13화_동창회"; NX=E["next_title"]+" 편"
if sys.argv[1]=="test":
    lib2._png(lib._svg(SCENE+lib2.wm(),B,SCRIPT[0]),1080,1350,"/tmp/t13.png")
elif sys.argv[1]=="full":
    lib4.covers("동창회",SCENE,TH,B,P)
    lib4.cards(SCENE,B,SCRIPT,P,E["next_n"],NX)
    print(lib4.reel(SCENE,B,SCRIPT,"주식 중독자의 동창회",P,E["next_n"],NX))
