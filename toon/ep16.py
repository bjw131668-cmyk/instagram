import sys, lib, lib2, lib4, db
INK=lib.INK
E=db.load(16); SCRIPT=E["script"]; TH=E["thumb"]
SK="#f2cdae"; JK="#34507e"; JK2="#2b4369"
TIE=f'''<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <path d="M774,822 L806,822 L812,850 L790,862 L768,850 Z" fill="#b8323a"/>
 <path d="M776,858 L804,858 L818,960 L790,992 L762,960 Z" fill="#b8323a"/></g>'''
FRIEND=f'''<!-- 동창 -->
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

<g stroke="{INK}" stroke-width="5" stroke-linejoin="round"><path d="M290,770 L310,770 L314,790 L300,798 L286,790 Z" fill="#9aa9c4"/><path d="M291,796 L309,796 L316,850 L300,866 L284,850 Z" fill="#9aa9c4"/></g>'''
SCENE=f'''
<rect width="1080" height="1350" fill="#f3ede6"/>
<rect y="780" width="1080" height="600" fill="#e6dccf"/>
<rect y="770" width="1080" height="12" fill="#d3c4b0"/>
<!-- 샹들리에 -->
<g stroke="{INK}" stroke-width="5" stroke-linecap="round">
 <line x1="540" y1="0" x2="540" y2="60"/>
 <path d="M440,90 C470,120 610,120 640,90" fill="none"/>
 <line x1="540" y1="60" x2="540" y2="112"/>
 <g fill="#fff3c4"><circle cx="440" cy="84" r="12"/><circle cx="490" cy="104" r="12"/><circle cx="540" cy="112" r="12"/><circle cx="590" cy="104" r="12"/><circle cx="640" cy="84" r="12"/></g>
</g>
<!-- 꽃 아치 -->
<g stroke="{INK}" stroke-width="6" fill="none"><path d="M380,770 L380,330 C380,200 700,200 700,330 L700,770" stroke="#c8b49a" stroke-width="14"/></g>
<g stroke="{INK}" stroke-width="4">
 <circle cx="420" cy="262" r="20" fill="#f6c6cf"/><circle cx="480" cy="226" r="18" fill="#ffffff"/>
 <circle cx="540" cy="214" r="22" fill="#f6c6cf"/><circle cx="600" cy="226" r="18" fill="#ffffff"/><circle cx="660" cy="262" r="20" fill="#f6c6cf"/>
</g>
<g fill="#9cc49a"><ellipse cx="452" cy="240" rx="14" ry="7"/><ellipse cx="628" cy="240" rx="14" ry="7"/></g>
<!-- 양쪽 꽃병 -->
<g stroke="{INK}" stroke-width="5"><path d="M70,560 L130,560 L120,660 L80,660 Z" fill="#ffffff"/><circle cx="84" cy="536" r="18" fill="#f6c6cf"/><circle cx="116" cy="530" r="18" fill="#ffffff"/><circle cx="100" cy="508" r="18" fill="#f6c6cf"/>
 <path d="M950,560 L1010,560 L1000,660 L960,660 Z" fill="#ffffff"/><circle cx="964" cy="536" r="18" fill="#ffffff"/><circle cx="996" cy="530" r="18" fill="#f6c6cf"/><circle cx="980" cy="508" r="18" fill="#ffffff"/></g>
{FRIEND}
{lib.CHAR}
{TIE}
<!-- 하객 테이블 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <rect x="-10" y="990" width="1100" height="380" fill="#ffffff"/>
 <path d="M-10,1022 L1100,1022" stroke="#e3dbd2" stroke-width="5"/>
 <g stroke="#e3dbd2" stroke-width="4"><path d="M120,1030 L110,1340"/><path d="M360,1030 L356,1340"/><path d="M720,1030 L724,1340"/><path d="M960,1030 L970,1340"/></g>
 <!-- 케이크 접시 -->
 <ellipse cx="560" cy="992" rx="78" ry="16" fill="#ffffff"/>
 <path d="M520,984 L520,950 L600,936 L600,980 Z" fill="#fbe7c2"/><path d="M520,950 L600,936 L600,946 L520,960 Z" fill="#f6c6cf" stroke-width="5"/>
 <circle cx="578" cy="930" r="8" fill="#e2483d" stroke-width="4"/>
 <!-- 친구 팔뚝 -->
 <path d="M96,1016 C98,966 160,950 262,962 L262,1024 L96,1024 Z" fill="{JK}"/>
 <!-- 친구 샴페인 잔 -->
 <path d="M318,880 L374,880 C374,920 360,940 346,944 C332,940 318,920 318,880 Z" fill="#fbe7a6"/>
 <line x1="346" y1="944" x2="346" y2="990"/><path d="M322,992 L370,992" />
</g>
{lib.hand(292,992,flip=False,rot=90,skin=SK)}
{lib.cuff(262,993,rot=2,color=JK2)}
<g stroke="{INK}" stroke-width="5"><rect x="238" y="972" width="18" height="40" rx="5" fill="#cfd6df"/><circle cx="247" cy="992" r="9" fill="#ffffff"/></g>
{lib.NMR_FRONT}
'''
B=lib.B2; P="16화_동기결혼식"; NX=E["next_title"]+" 편"
if sys.argv[1]=="test":
    lib2._png(lib._svg(SCENE+lib2.wm(),B,SCRIPT[4]),1080,1350,"/tmp/t16.png")
elif sys.argv[1]=="full":
    lib4.covers("동기 결혼식",SCENE,TH,B,P)
    lib4.cards(SCENE,B,SCRIPT,P,E["next_n"],NX)
    print(lib4.reel(SCENE,B,SCRIPT,"주식 중독자의 동기 결혼식",P,E["next_n"],NX))
