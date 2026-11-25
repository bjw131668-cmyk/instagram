import sys, lib, lib2
INK=lib.INK
SCRIPT=[
 ("화장실을 왜\n자꾸 가나?","장이 안\n좋아서요.","병원을\n가봐.","그 장이\n아니라서요.."),
 ("자네 요즘\n집중을 못 하나?","9시부터 3시\n반까지만요.","그럼 그 뒤엔\n잘하나?","그땐 복기를\n해야 해서요."),
 ("올해 목표가\n뭔가?","본전입니다.","회사 목표를\n물은 거야.","회사도 본전이면\n좋겠습니다."),
 ("모니터에 그\n그래프는 뭔가?","실적\n그래프입니다.","우리 팀 실적이\n저렇게 나쁜가?","제 실적\n입니다.."),
 ("보고서는 언제\n되나?","장 마감\n후에요.","마감은\n오전인데?","제 마감은\n3시 반입니다."),
 ("점심은 뭐\n먹을 텐가?","오늘은\n굶겠습니다.","어디\n아픈가?","계좌가요."),
 ("회의 중에 왜\n한숨을 쉬나?","방금\n떨어졌습니다.","뭐가?\n펜이?","제 노후가요."),
 ("연차는 왜\n냈나?","주주총회\n갑니다.","자네가 거길\n왜 가?","따지러요."),
 ("승진하고\n싶지 않나?","저는 상승을\n믿지 않습니다.","의욕이 그렇게\n없나?","올라가 본 적이\n없어서요."),
 ("자네, 솔직히\n말해보게.","죄송합니다.\n주식 봤습니다.","...그 종목\n나도 있어.","팀장님도\n화장실 가시죠."),
]
REEL=[SCRIPT[i] for i in (0,2,3,5,6,9)]
SCENE=f'''
<defs>
 <linearGradient id="w4" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e6ecf2"/><stop offset="1" stop-color="#d5dee8"/></linearGradient>
 <linearGradient id="t4" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1ead9"/><stop offset="1" stop-color="#d9cfb8"/></linearGradient>
</defs>
<rect width="1080" height="1350" fill="url(#w4)"/>
<rect y="770" width="1080" height="12" fill="#b9c5d2"/><rect y="782" width="1080" height="600" fill="#c8d3df"/>
<!-- 화이트보드: 회사 목표(상승 막대) -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <rect x="425" y="300" width="260" height="300" rx="8" fill="#ffffff"/>
 <g stroke="none"><rect x="456" y="500" width="34" height="60" fill="#f2a53b"/><rect x="506" y="460" width="34" height="100" fill="#f2a53b"/><rect x="556" y="410" width="34" height="150" fill="#f2a53b"/><rect x="606" y="360" width="34" height="200" fill="#e2483d"/></g>
 <line x1="446" y1="562" x2="662" y2="562" stroke-width="5"/>
 <text x="555" y="344" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="26" fill="{INK}" stroke="none">올해 목표</text>
 <rect x="425" y="600" width="260" height="14" fill="#9aa7b3"/>
</g>
<!-- 블라인드 창 -->
<g transform="translate(36,326)" stroke="{INK}" stroke-width="6"><rect width="130" height="210" rx="6" fill="#bfe3f7"/>
 <g stroke="#8fb3c4" stroke-width="4"><line x1="6" y1="35" x2="124" y2="35"/><line x1="6" y1="70" x2="124" y2="70"/><line x1="6" y1="105" x2="124" y2="105"/><line x1="6" y1="140" x2="124" y2="140"/><line x1="6" y1="175" x2="124" y2="175"/></g></g>
<!-- 시계 3:20 -->
<g transform="translate(985,390)"><circle r="58" fill="#fff" stroke="{INK}" stroke-width="6"/>
 <line x1="0" y1="0" x2="27" y2="6" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
 <line x1="0" y1="0" x2="35" y2="20" stroke="{INK}" stroke-width="5" stroke-linecap="round"/><circle r="5" fill="#e2483d"/></g>

<!-- 팀장 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <path d="M95,1010 C95,820 150,745 235,725 L365,725 C450,745 505,820 505,1010 Z" fill="#a9c8ea"/>
 <path d="M248,727 L300,800 L352,727 Z" fill="#f3cdb3"/>
 <path d="M235,725 L300,810 L262,850 L205,750 Z" fill="#bcd6f1"/><path d="M365,725 L300,810 L338,850 L395,750 Z" fill="#bcd6f1"/>
 <line x1="300" y1="810" x2="300" y2="900" stroke-width="5"/>
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
 <path d="M272,650 C290,640 314,640 332,650" fill="none" stroke-width="7"/>
 <!-- 팔짱 -->
 <path d="M130,930 C130,900 160,890 190,892 L420,900 C452,902 470,920 468,946 C466,972 446,984 420,984 L190,990 C150,990 130,966 130,930 Z" fill="#a9c8ea"/>
 <path d="M250,896 L250,988" stroke-width="5" stroke="#7fa3cc"/>
 <ellipse cx="446" cy="942" rx="34" ry="28" fill="#efc6a4"/>
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
 <rect x="-10" y="990" width="1100" height="380" fill="url(#t4)"/>
 <line x1="-10" y1="1022" x2="1100" y2="1022" stroke="#b9ad92" stroke-width="5"/>
 <!-- 노트북(뒷면) -->
 <path d="M505,996 L520,880 L640,880 L655,996 Z" fill="#8d99a6"/>
 <circle cx="580" cy="938" r="14" fill="#cfd6de"/>
 <!-- 나물려 팔 -->
 <path d="M700,1010 C700,975 730,950 780,950 L800,1010 Z" fill="#8a8f9c"/>
 <path d="M1010,1010 C1010,950 950,925 900,945 L870,1010 Z" fill="#8a8f9c"/>
</g>
{lib.PHONE}
<!-- 나물려 손: 정확히 2개 -->
<g stroke="{INK}" stroke-width="7"><ellipse cx="850" cy="1000" rx="36" ry="27" fill="#f4cfae"/><ellipse cx="930" cy="1008" rx="34" ry="26" fill="#f4cfae"/></g>
'''
B=lib.make.B
P="04화_팀장면담"
if sys.argv[1]=="test":
    lib2._png(lib._svg(SCENE+lib2.wm(),B,SCRIPT[0]),1080,1350,"/tmp/t4.png")
    lib2._png(lib2._frame("주식 중독자의 팀장 면담",4,"",lib2.outro(5,"놀이공원 편")),1080,1920,"/tmp/t4e.png")
else:
    lib2.cards(SCENE,B,SCRIPT,P,5,"놀이공원 편")
    print(lib2.reel(SCENE,B,REEL,"주식 중독자의 팀장 면담",P,4,5,"놀이공원 편"))
