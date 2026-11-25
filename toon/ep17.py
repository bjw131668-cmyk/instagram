import sys, lib, lib2, lib4, db
INK=lib.INK
E=db.load(17); SCRIPT=E["script"]; TH=E["thumb"]
SK="#efc6a4"; SH="#a9c8ea"; SH2="#bcd6f1"
SCENE=f'''
<defs><linearGradient id="t15" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ece6d8"/><stop offset="1" stop-color="#d6cfbe"/></linearGradient></defs>
<rect width="1080" height="1350" fill="#eef0f2"/>
<rect y="770" width="1080" height="12" fill="#c3c9d0"/><rect y="782" width="1080" height="600" fill="#d6dbe0"/>
<!-- 칸막이 -->
<rect x="0" y="600" width="1080" height="180" fill="#c9d1da"/><line x1="0" y1="600" x2="1080" y2="600" stroke="{INK}" stroke-width="6"/>
<g stroke="#b3bcc7" stroke-width="4"><line x1="360" y1="604" x2="360" y2="770"/><line x1="720" y1="604" x2="720" y2="770"/></g>
<!-- 블라인드 창 -->
<g transform="translate(40,250)" stroke="{INK}" stroke-width="6"><rect width="170" height="250" rx="6" fill="#d7e8f1"/>
 <g stroke="#a8c0cc" stroke-width="4"><line x1="6" y1="40" x2="164" y2="40"/><line x1="6" y1="80" x2="164" y2="80"/><line x1="6" y1="120" x2="164" y2="120"/><line x1="6" y1="160" x2="164" y2="160"/><line x1="6" y1="200" x2="164" y2="200"/></g></g>
<!-- 벽 달력 (빨간 동그라미 한 칸) -->
<g transform="translate(450,300)" stroke="{INK}" stroke-width="6">
 <rect width="180" height="200" rx="6" fill="#ffffff"/><rect width="180" height="44" rx="6" fill="#e2483d"/>
 <g stroke="#b9c0c8" stroke-width="3">
  <line x1="10" y1="80" x2="170" y2="80"/><line x1="10" y1="115" x2="170" y2="115"/><line x1="10" y1="150" x2="170" y2="150"/>
  <line x1="50" y1="50" x2="50" y2="190"/><line x1="90" y1="50" x2="90" y2="190"/><line x1="130" y1="50" x2="130" y2="190"/></g>
 <circle cx="110" cy="132" r="17" fill="none" stroke="#e2483d" stroke-width="6"/></g>
<!-- 화분 -->
<g transform="translate(960,520)" stroke="{INK}" stroke-width="5"><path d="M-36,0 L36,0 L28,70 L-28,70 Z" fill="#d98d5f"/>
 <ellipse cx="-22" cy="-30" rx="16" ry="34" fill="#7fbf7a" transform="rotate(-25 -22 -30)"/><ellipse cx="20" cy="-36" rx="16" ry="38" fill="#8fcf8a" transform="rotate(20 20 -36)"/><ellipse cx="0" cy="-44" rx="14" ry="40" fill="#6fae6a"/></g>
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
  <!-- 서류함 -->
 <path d="M440,930 L600,930 L590,992 L450,992 Z" fill="#9fb3c8"/><rect x="458" y="912" width="124" height="22" rx="3" fill="#ffffff"/><rect x="466" y="900" width="110" height="16" rx="3" fill="#f6e6b4"/>
 <!-- 머그 -->
 <path d="M620,930 L676,930 L672,992 L624,992 Z" fill="#ffffff"/><path d="M676,944 C700,944 700,976 674,976" fill="none"/>
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
B=lib.B2; P="17화_연차신청"; NX=E["next_title"]+" 편"
if sys.argv[1]=="test":
    lib2._png(lib._svg(SCENE+lib2.wm(),B,SCRIPT[9]),1080,1350,"/tmp/t17.png")
elif sys.argv[1]=="full":
    lib4.covers("연차 신청",SCENE,TH,B,P)
    lib4.cards(SCENE,B,SCRIPT,P,E["next_n"],NX)
    print(lib4.reel(SCENE,B,SCRIPT,"주식 중독자의 연차 신청",P,E["next_n"],NX))
