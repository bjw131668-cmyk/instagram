import sys, lib, lib2, lib4, db
INK=lib.INK
E=db.load(15); SCRIPT=E["script"]; TH=E["thumb"]
SK="#efc6a4"; SH="#a9c8ea"; SH2="#bcd6f1"
SCENE=f'''
<defs><linearGradient id="t15" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ece6d8"/><stop offset="1" stop-color="#d6cfbe"/></linearGradient></defs>
<rect width="1080" height="1350" fill="#e3e7ec"/>
<rect y="770" width="1080" height="12" fill="#bcc4cd"/><rect y="782" width="1080" height="600" fill="#cdd3da"/>
<!-- 화이트보드: 위 화살표 + % (글자 없음) -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
 <rect x="410" y="300" width="290" height="290" rx="8" fill="#ffffff"/>
 <rect x="410" y="590" width="290" height="14" fill="#9aa7b3"/>
 <path d="M460,540 L540,470 L580,500 L650,400" fill="none" stroke="#e2483d" stroke-width="10"/>
 <path d="M620,396 L654,394 L652,428" fill="none" stroke="#e2483d" stroke-width="10"/>
 <circle cx="478" cy="368" r="14" fill="none" stroke="#2f6fd0" stroke-width="7"/><circle cx="530" cy="420" r="14" fill="none" stroke="#2f6fd0" stroke-width="7"/>
 <line x1="534" y1="356" x2="474" y2="432" stroke="#2f6fd0" stroke-width="7"/>
</g>
<!-- 블라인드 창 -->
<g transform="translate(36,326)" stroke="{INK}" stroke-width="6"><rect width="130" height="210" rx="6" fill="#cfe2ec"/>
 <g stroke="#9db6c2" stroke-width="4"><line x1="6" y1="35" x2="124" y2="35"/><line x1="6" y1="70" x2="124" y2="70"/><line x1="6" y1="105" x2="124" y2="105"/><line x1="6" y1="140" x2="124" y2="140"/><line x1="6" y1="175" x2="124" y2="175"/></g></g>
<!-- 시계 -->
<g transform="translate(985,390)"><circle r="58" fill="#fff" stroke="{INK}" stroke-width="6"/>
 <line x1="0" y1="0" x2="27" y2="6" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
 <line x1="0" y1="0" x2="35" y2="20" stroke="{INK}" stroke-width="5" stroke-linecap="round"/><circle r="5" fill="#e2483d"/></g>

<!-- 팀장 (웃는 얼굴) -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <path d="M95,1010 C95,820 150,745 235,725 L365,725 C450,745 505,820 505,1010 Z" fill="{SH}"/>
 <path d="M248,727 L300,800 L352,727 Z" fill="#f3cdb3"/>
 <path d="M235,725 L300,810 L262,850 L205,750 Z" fill="{SH2}"/><path d="M365,725 L300,810 L338,850 L395,750 Z" fill="{SH2}"/>
 <g transform="rotate(0 300 790)"><path d="M288,786 L312,786 L316,808 L300,816 L284,808 Z" fill="#2f4f7f" stroke-width="5"/><path d="M290,812 L310,812 L320,900 L300,924 L280,900 Z" fill="#2f4f7f" stroke-width="5"/></g>
 <path d="M262,660 L262,735 C285,760 315,760 338,735 L338,660 Z" fill="#e6b796"/>
 <path d="M200,530 C200,440 250,410 302,410 C356,410 404,440 404,530 C404,640 356,690 302,690 C248,690 200,640 200,530 Z" fill="{SK}"/>
 <path d="M200,545 C182,540 180,585 204,588" fill="{SK}"/><path d="M404,545 C422,540 424,585 400,588" fill="{SK}"/>
 <path d="M196,520 C186,450 214,410 250,400 C240,430 236,460 222,480 C210,490 202,504 196,520 Z" fill="#3b3b44"/>
 <path d="M408,520 C418,450 390,410 354,400 C364,430 368,460 382,480 C394,490 402,504 408,520 Z" fill="#3b3b44"/>
 <path d="M262,404 C280,392 324,392 342,404" fill="none" stroke-width="6"/>
 <path d="M276,420 C292,412 312,412 328,420" fill="none" stroke-width="5"/>
 <path d="M230,520 C246,512 266,512 282,518" fill="none" stroke-width="8"/><path d="M322,518 C338,512 358,512 374,520" fill="none" stroke-width="8"/>
 <rect x="222" y="534" width="70" height="44" rx="6" fill="#fff" fill-opacity="0.5" stroke-width="6"/>
 <rect x="312" y="534" width="70" height="44" rx="6" fill="#fff" fill-opacity="0.5" stroke-width="6"/>
 <line x1="292" y1="552" x2="312" y2="552" stroke-width="6"/>
 <circle cx="258" cy="558" r="8" fill="{INK}" stroke="none"/><circle cx="348" cy="558" r="8" fill="{INK}" stroke="none"/>
 <path d="M300,582 C290,604 292,612 308,612" fill="none" stroke-width="5"/>
 <path d="M268,638 C284,664 320,664 336,638" fill="none" stroke-width="7"/>
 <ellipse cx="236" cy="612" rx="20" ry="10" fill="#f0a0a0" stroke="none" opacity="0.5"/><ellipse cx="368" cy="612" rx="20" ry="10" fill="#f0a0a0" stroke="none" opacity="0.5"/>
</g>
{lib.CHAR}
<!-- 사원증 -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <path d="M740,790 L776,900" fill="none" stroke="#2f6fd0" stroke-width="9"/><path d="M840,790 L804,900" fill="none" stroke="#2f6fd0" stroke-width="9"/>
 <rect x="752" y="896" width="76" height="92" rx="8" fill="#ffffff"/>
 <circle cx="790" cy="928" r="13" fill="#3a2c26"/><rect x="766" y="952" width="48" height="10" rx="5" fill="#9aa7b3" stroke="none"/><rect x="772" y="968" width="36" height="8" rx="4" fill="#9aa7b3" stroke="none"/>
</g>
<!-- 회의 테이블 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <rect x="-10" y="990" width="1100" height="380" fill="url(#t15)"/>
 <line x1="-10" y1="1022" x2="1100" y2="1022" stroke="#b9ad92" stroke-width="5"/>
 <!-- 연봉 계약서 봉투 -->
 <g transform="rotate(-4 520 960)"><rect x="440" y="910" width="170" height="96" rx="6" fill="#e9d3a6"/><path d="M440,914 L525,968 L610,914" fill="none" stroke-width="5"/></g>
 <!-- 계산기 -->
 <g transform="rotate(6 660 950)"><rect x="620" y="880" width="86" height="120" rx="-20" fill="#5d6673"/><rect x="632" y="892" width="62" height="26" rx="-26" fill="#cfe6c8"/>
  <g fill="#e8ecf0" stroke-width="3"><rect x="634" y="928" width="16" height="14" rx="-27"/><rect x="655" y="928" width="16" height="14" rx="-27"/><rect x="676" y="928" width="16" height="14" rx="-27"/><rect x="634" y="950" width="16" height="14" rx="-27"/><rect x="655" y="950" width="16" height="14" rx="-27"/><rect x="676" y="950" width="16" height="14" rx="-27"/><rect x="634" y="972" width="16" height="14" rx="-27"/><rect x="655" y="972" width="16" height="14" rx="-27"/><rect x="676" y="972" width="16" height="14" rx="-27" fill="#e2483d"/></g></g>
 <!-- 팀장 팔뚝 -->
 <path d="M96,1016 C98,966 160,950 262,962 L262,1024 L96,1024 Z" fill="{SH}"/>
 <!-- 팀장 서류 (손보다 먼저) -->
 <g transform="rotate(-8 340 940)"><rect x="288" y="860" width="120" height="150" rx="4" fill="#ffffff"/>
  <g stroke="#a7b0ba" stroke-width="5"><line x1="304" y1="890" x2="390" y2="890"/><line x1="304" y1="914" x2="380" y2="914"/><line x1="304" y1="938" x2="390" y2="938"/><line x1="304" y1="962" x2="360" y2="962"/></g></g>
</g>
{lib.hand(292,992,flip=False,rot=90,skin=SK)}
{lib.cuff(262,993,rot=2,color=SH2)}
{lib.NMR_FRONT}
'''
B=lib.B2; P="15화_연봉협상"; NX=E["next_title"]+" 편"
if sys.argv[1]=="test":
    lib2._png(lib._svg(SCENE+lib2.wm(),B,SCRIPT[9]),1080,1350,"/tmp/t15.png")
elif sys.argv[1]=="full":
    lib4.covers("연봉 협상",SCENE,TH,B,P)
    lib4.cards(SCENE,B,SCRIPT,P,E["next_n"],NX)
    print(lib4.reel(SCENE,B,SCRIPT,"주식 중독자의 연봉 협상",P,E["next_n"],NX))
