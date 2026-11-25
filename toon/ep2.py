import sys, lib
INK=lib.INK
SCRIPT=[
 ("5년 뒤 본인의\n모습은요?","본전이요.","...포부가\n그게 다예요?","저한텐 그게\n제일 큰 꿈입니다."),
 ("본인의 장점이\n뭔가요?","손실을 잘\n견딥니다.","얼마나\n견디셨는데요?","3년째\n-31%입니다."),
 ("스트레스는\n어떻게 푸세요?","주식 앱을\n지웁니다.","그럼 좀\n괜찮아지세요?","5분 뒤에\n다시 깝니다."),
 ("지원 동기가\n뭔가요?","월급이\n필요합니다.","솔직하시네요.\n어디 쓰시게요?","물을 더\n타야 해서요."),
 ("희망 연봉은\n얼마예요?","평단가까지만\n부탁드립니다.","그게\n얼만데요?","말하면 안\n뽑으실 거예요."),
 ("실패했던 경험\n있으세요?","어느 종목\n말씀이세요?","...여러 개\n있으세요?","계좌를\n보여드릴까요?"),
 ("끈기가 있는\n편인가요?","한번 사면\n절대 안 팝니다.","소신이\n있으시네요.","못 파는\n겁니다."),
 ("위기 대처는\n어떻게 하세요?","눈을\n감습니다.","그게\n대처예요?","안 보면\n안 떨어진 겁니다."),
 ("야근도\n가능하세요?","네, 어차피\n미국장 봐야죠.","그건 근무가\n아닌데요?","저한텐\n본업입니다."),
 ("언제부터 출근\n가능하세요?","오후 3시 반\n이후요.","...저도 그때부터\n일합니다.","혹시 뭐\n들고 계세요?"),
]
SCENE=f'''
<defs>
 <linearGradient id="w2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#efe9df"/><stop offset="1" stop-color="#e2dacb"/></linearGradient>
 <linearGradient id="t2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e3e7ec"/><stop offset="1" stop-color="#c3cad3"/></linearGradient>
</defs>
<rect width="1080" height="1350" fill="url(#w2)"/>
<rect y="770" width="1080" height="12" fill="#c9bfae"/><rect y="782" width="1080" height="600" fill="#d6cdbd"/>
<!-- 회사 간판(가상) -->
<g transform="translate(440,330)" stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <rect width="230" height="150" rx="10" fill="#ffffff"/>
 <circle cx="70" cy="75" r="34" fill="#f2a53b"/>
 <rect x="120" y="50" width="80" height="14" rx="7" fill="#35507a" stroke="none"/>
 <rect x="120" y="74" width="60" height="14" rx="7" fill="#35507a" stroke="none"/>
 <rect x="120" y="98" width="72" height="14" rx="7" fill="#35507a" stroke="none"/>
</g>
<!-- 화분 -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <path d="M70,560 C30,500 40,440 78,400 C82,450 96,500 92,560 Z" fill="#5fae6a"/>
 <path d="M100,560 C100,480 130,420 168,400 C170,470 150,520 122,560 Z" fill="#4c9a58"/>
 <path d="M60,560 L140,560 L128,650 L72,650 Z" fill="#c9764a"/>
</g>
<!-- 시계 10:10 -->
<g transform="translate(985,390)">
 <circle r="58" fill="#fff" stroke="{INK}" stroke-width="6"/>
 <line x1="0" y1="0" x2="-24" y2="-16" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
 <line x1="0" y1="0" x2="34" y2="-22" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
 <circle r="5" fill="#e2483d"/>
</g>

<!-- 면접관 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <path d="M95,1010 C95,820 150,745 235,725 L365,725 C450,745 505,820 505,1010 Z" fill="#2b3a55"/>
 <path d="M245,727 L300,840 L355,727 Z" fill="#ffffff"/>
 <path d="M287,770 L313,770 L326,900 L300,935 L274,900 Z" fill="#b8323a"/>
 <path d="M235,725 L300,880 L246,930 L196,765 Z" fill="#22304a"/>
 <path d="M365,725 L300,880 L354,930 L404,765 Z" fill="#22304a"/>
 <path d="M262,660 L262,735 C285,760 315,760 338,735 L338,660 Z" fill="#e9bd9c"/>
 <path d="M200,530 C200,440 250,410 302,410 C356,410 404,440 404,530 C404,640 356,690 302,690 C248,690 200,640 200,530 Z" fill="#f1cba9"/>
 <path d="M200,545 C182,540 180,585 204,588" fill="#f1cba9"/>
 <path d="M404,545 C422,540 424,585 400,588" fill="#f1cba9"/>
 <!-- 가르마 머리 -->
 <path d="M192,520 C176,430 240,380 305,382 C372,378 432,430 410,522 C404,480 388,462 372,452 C330,470 270,462 240,440 C222,462 204,486 192,520 Z" fill="#23232b"/>
 <path d="M240,440 C262,420 300,410 340,414" fill="none" stroke="#4a4a58" stroke-width="5"/>
 <!-- 눈썹(찌푸림) -->
 <path d="M228,520 L280,534" stroke-width="9"/><path d="M324,534 L376,520" stroke-width="9"/>
 <ellipse cx="256" cy="560" rx="9" ry="11" fill="{INK}" stroke="none"/>
 <ellipse cx="348" cy="560" rx="9" ry="11" fill="{INK}" stroke="none"/>
 <path d="M236,582 L276,582" stroke="#b08a74" stroke-width="4"/><path d="M328,582 L368,582" stroke="#b08a74" stroke-width="4"/>
 <path d="M300,574 C290,602 292,612 308,612" fill="none" stroke-width="5"/>
 <path d="M274,652 C290,640 314,640 330,652" fill="none" stroke-width="7"/>
</g>

{lib.CHAR}
<!-- 후드티 위 넥타이 -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <path d="M774,822 L806,822 L812,850 L790,862 L768,850 Z" fill="#b8323a"/>
 <path d="M776,858 L804,858 L818,960 L790,992 L762,960 Z" fill="#b8323a"/>
</g>

<!-- 책상 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <rect x="-10" y="990" width="1100" height="380" fill="url(#t2)"/>
 <line x1="-10" y1="1022" x2="1100" y2="1022" stroke="#a9b1bb" stroke-width="5"/>
 <!-- 물컵 -->
 <path d="M520,900 L590,900 L582,996 L528,996 Z" fill="#eaf6fb"/>
 <path d="M526,940 L584,940 L582,996 L528,996 Z" fill="#a9dcf3" stroke="none"/>
 <path d="M520,900 L590,900 L582,996 L528,996 Z" fill="none"/>
 <!-- 명패 -->
 <path d="M400,996 L420,940 L510,940 L490,996 Z" fill="#35507a" transform="translate(-10,0)"/>
 <text x="445" y="982" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="26" fill="#fff" stroke="none">면접관</text>
 <!-- 면접관 팔 + 이력서 -->
 <path d="M150,1000 C150,960 200,948 240,958 L300,975 L300,1010 Z" fill="#2b3a55"/>
 <g transform="rotate(-7 300 960)">
  <rect x="222" y="880" width="170" height="150" rx="6" fill="#ffffff"/>
  <rect x="238" y="896" width="44" height="54" fill="#cfd6de" stroke-width="4"/>
  <g stroke="#9aa7b3" stroke-width="5"><line x1="296" y1="904" x2="376" y2="904"/><line x1="296" y1="926" x2="376" y2="926"/><line x1="296" y1="948" x2="350" y2="948"/><line x1="238" y1="974" x2="376" y2="974"/><line x1="238" y1="996" x2="376" y2="996"/></g>
 </g>
 <ellipse cx="232" cy="1002" rx="34" ry="26" fill="#f1cba9"/>
 <!-- 나물려 팔 -->
 <path d="M640,1010 C640,965 690,935 760,945 L790,1010 Z" fill="#8a8f9c"/>
 <path d="M1010,1010 C1010,950 950,925 900,945 L870,1010 Z" fill="#8a8f9c"/>
</g>
{lib.PHONE}
<g stroke="{INK}" stroke-width="7"><ellipse cx="850" cy="1000" rx="36" ry="27" fill="#f4cfae"/><ellipse cx="930" cy="1008" rx="34" ry="26" fill="#f4cfae"/>
<ellipse cx="720" cy="1000" rx="34" ry="26" fill="#f4cfae"/></g>
'''
B=lib.make.B
if sys.argv[1]=="test":
    import subprocess
    r=lib.cards(SCENE,B,SCRIPT[:1],"t2"); print(r)
else:
    lib.cards(SCENE,B,SCRIPT,"02화_면접")
    print(lib.reel(SCENE,B,SCRIPT,"주식 중독자의 면접","02화_면접"))
