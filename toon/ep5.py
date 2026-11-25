import sys, lib, lib2
INK=lib.INK
SCRIPT=[
 ("롤러코스터\n안 무서우세요?","매일\n타는데요.","연간회원\n이세요?","아뇨,\n제 계좌요."),
 ("안전바 내려\n드릴게요.","오, 이런 게\n있군요.","처음\n타보세요?","제 계좌엔\n없어서요."),
 ("키 제한이\n있어요.","하한가 제한도\n있습니다.","...네?","하루 30%까지만\n빠져요."),
 ("자유이용권으로\n하시겠어요?","네, 자유 낙하\n전문입니다.","떨어지는 거\n좋아하세요?","좋아하진 않는데\n자주 합니다."),
 ("대기 시간은\n2시간입니다.","짧네요.","2시간이\n짧으세요?","저는 3년째\n기다리는 중이라."),
 ("귀신의 집도\n가보세요.","무서운 건\n익숙합니다.","담력이\n세시네요.","매일 아침 9시에\n계좌를 열거든요."),
 ("풍선 하나\n드릴까요?","아뇨, 터질까 봐\n무섭습니다.","풍선이요?","거품은 꼭\n터지더라고요."),
 ("사진 찍어\n드릴까요?","표정이 안\n좋을 텐데요.","웃어보세요!\n김치~","손절~"),
 ("야간 개장도\n하니까 오세요.","밤에는 미국장\n봐야 합니다.","놀이공원이\n더 재밌어요!","거기도 롤러\n코스터예요."),
 ("내려갈 땐 소리\n지르셔도 돼요.","3년째 조용히\n내려가는 중입니다.","...손님, 저도\n같이 타도 될까요?","직원분도\n물리셨군요."),
]
REEL=[SCRIPT[i] for i in (0,2,4,5,7,9)]
SCENE=f'''
<defs>
 <linearGradient id="sk5" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bfe6fb"/><stop offset="1" stop-color="#eaf8ff"/></linearGradient>
 <linearGradient id="c5" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3fb7a8"/><stop offset="1" stop-color="#2a8f84"/></linearGradient>
</defs>
<rect width="1080" height="1350" fill="url(#sk5)"/>
<rect y="770" width="1080" height="600" fill="#9ed38b"/><rect y="770" width="1080" height="12" fill="#7fbf6c"/>
<!-- 구름 -->
<g fill="#ffffff" opacity="0.9"><ellipse cx="90" cy="640" rx="70" ry="24"/><ellipse cx="130" cy="622" rx="46" ry="22"/><ellipse cx="1000" cy="620" rx="64" ry="22"/></g>
<!-- 관람차 -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round" fill="none">
 <path d="M505,770 L555,470 L605,770" stroke-width="8"/>
 <circle cx="555" cy="470" r="140"/><circle cx="555" cy="470" r="18" fill="#f2a53b"/>
 <g stroke-width="4"><line x1="555" y1="330" x2="555" y2="610"/><line x1="415" y1="470" x2="695" y2="470"/><line x1="456" y1="371" x2="654" y2="569"/><line x1="654" y1="371" x2="456" y2="569"/></g>
 <g stroke-width="5"><rect x="535" y="318" width="40" height="30" rx="6" fill="#e2483d"/><rect x="535" y="596" width="40" height="30" rx="6" fill="#3b8cff"/><rect x="398" y="456" width="40" height="30" rx="6" fill="#ffd66b"/><rect x="672" y="456" width="40" height="30" rx="6" fill="#4fb36c"/>
 <rect x="438" y="356" width="40" height="30" rx="6" fill="#b06fd8"/><rect x="632" y="356" width="40" height="30" rx="6" fill="#ff9a8b"/><rect x="438" y="556" width="40" height="30" rx="6" fill="#ff9a8b"/><rect x="632" y="556" width="40" height="30" rx="6" fill="#b06fd8"/></g>
</g>
<!-- 롤러코스터 레일 (왼쪽) -->
<g fill="none" stroke-linecap="round">
 <path d="M-20,560 C40,300 150,300 180,520 C200,660 250,700 300,760" stroke="{INK}" stroke-width="16"/>
 <path d="M-20,560 C40,300 150,300 180,520 C200,660 250,700 300,760" stroke="#e2483d" stroke-width="8"/>
 <g stroke="{INK}" stroke-width="5"><line x1="30" y1="420" x2="30" y2="770"/><line x1="100" y1="340" x2="100" y2="770"/><line x1="170" y1="460" x2="170" y2="770"/></g>
</g>
<!-- 풍선 (오른쪽) -->
<g stroke="{INK}" stroke-width="5" stroke-linejoin="round">
 <path d="M960,470 C962,560 990,640 985,760" fill="none" stroke-width="3"/><path d="M1010,450 C1005,560 990,640 985,760" fill="none" stroke-width="3"/><path d="M1040,500 C1020,580 995,660 985,760" fill="none" stroke-width="3"/>
 <ellipse cx="958" cy="420" rx="38" ry="48" fill="#e2483d"/><ellipse cx="1012" cy="398" rx="38" ry="48" fill="#ffd66b"/><ellipse cx="1046" cy="452" rx="36" ry="46" fill="#3b8cff"/>
</g>

<!-- 놀이공원 직원 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <path d="M95,1010 C95,820 150,745 235,725 L365,725 C450,745 505,820 505,1010 Z" fill="#ffffff"/>
 <g stroke="none" fill="#e2483d"><path d="M150,790 L190,752 L190,1006 L150,1006 Z"/><path d="M230,728 L270,726 L270,1006 L230,1006 Z"/><path d="M330,726 L370,728 L370,1006 L330,1006 Z"/><path d="M410,752 L450,790 L450,1006 L410,1006 Z"/></g>
 <path d="M95,1010 C95,820 150,745 235,725 L365,725 C450,745 505,820 505,1010 Z" fill="none"/>
 <path d="M246,727 L300,800 L354,727 Z" fill="#f3cdb3"/>
 <path d="M235,725 L300,812 L258,846 L204,750 Z" fill="#ffffff"/><path d="M365,725 L300,812 L342,846 L396,750 Z" fill="#ffffff"/>
 <rect x="384" y="860" width="70" height="40" rx="6" fill="#ffd66b"/>
 <path d="M262,660 L262,735 C285,760 315,760 338,735 L338,660 Z" fill="#edc4a6"/>
 <path d="M200,530 C200,440 250,410 302,410 C356,410 404,440 404,530 C404,640 356,690 302,690 C248,690 200,640 200,530 Z" fill="#f7d7bd"/>
 <path d="M200,545 C182,540 180,585 204,588" fill="#f7d7bd"/><path d="M404,545 C422,540 424,585 400,588" fill="#f7d7bd"/>
 <!-- 옆머리 -->
 <path d="M198,520 C196,500 200,480 208,470 L226,470 C216,490 208,504 204,524 Z" fill="#3a2c26"/><path d="M406,520 C408,500 404,480 396,470 L378,470 C388,490 396,504 400,524 Z" fill="#3a2c26"/>
 <!-- 모자 -->
 <path d="M196,476 C190,400 250,366 302,366 C356,366 414,400 408,476 Z" fill="#e2483d"/>
 <path d="M176,476 C240,452 364,452 428,476 C440,482 438,496 424,494 C360,480 244,480 180,494 C166,496 164,482 176,476 Z" fill="#ffffff"/>
 <circle cx="302" cy="412" r="20" fill="#ffd66b"/>
 <!-- 서비스 미소 -->
 <path d="M232,522 C246,512 266,512 280,522" fill="none" stroke-width="6"/><path d="M324,522 C338,512 358,512 372,522" fill="none" stroke-width="6"/>
 <path d="M236,562 C246,546 268,546 278,562" fill="none" stroke-width="8"/><path d="M326,562 C336,546 358,546 368,562" fill="none" stroke-width="8"/>
 <path d="M300,576 C294,598 296,606 306,606" fill="none" stroke-width="5"/>
 <path d="M262,630 C280,668 324,668 342,630 Z" fill="#ffffff"/>
 <ellipse cx="230" cy="606" rx="20" ry="11" fill="#f3a9a0" stroke="none" opacity="0.7"/><ellipse cx="374" cy="606" rx="20" ry="11" fill="#f3a9a0" stroke="none" opacity="0.7"/>
</g>

{lib.CHAR}
<!-- 고양이 귀 머리띠 -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <path d="M690,430 C720,360 860,356 892,430" fill="none" stroke="#2b2b3a" stroke-width="10"/>
 <path d="M704,404 L716,322 L776,372 Z" fill="#f2a53b"/><path d="M722,386 L726,346 L754,370 Z" fill="#ffd9d0" stroke-width="4"/>
 <path d="M878,404 L866,322 L806,372 Z" fill="#f2a53b"/><path d="M860,386 L856,346 L828,370 Z" fill="#ffd9d0" stroke-width="4"/>
</g>

<!-- 매표소 카운터 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <rect x="-10" y="990" width="1100" height="380" fill="url(#c5)"/>
 <rect x="-10" y="990" width="1100" height="34" fill="#ffd66b"/>
 <!-- 안내판 -->
 <path d="M500,996 L514,910 L624,910 L638,996 Z" fill="#ffffff"/>
 <text x="569" y="968" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="34" fill="#e2483d" stroke="none">매표소</text>
 <!-- 직원 팔 + 입장권 (손 1개) -->
 <path d="M150,1000 C150,960 200,948 240,958 L300,975 L300,1010 Z" fill="#ffffff"/>
 <g transform="rotate(-8 330 960)"><rect x="262" y="926" width="150" height="64" rx="8" fill="#fff1b8"/><line x1="372" y1="930" x2="372" y2="986" stroke-dasharray="6 8" stroke-width="4"/><text x="318" y="970" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="26" fill="{INK}" stroke="none">입장권</text></g>
 <ellipse cx="250" cy="1000" rx="34" ry="26" fill="#f7d7bd"/>
 <!-- 나물려 팔 -->
 <path d="M700,1010 C700,975 730,950 780,950 L800,1010 Z" fill="#8a8f9c"/>
 <path d="M1010,1010 C1010,950 950,925 900,945 L870,1010 Z" fill="#8a8f9c"/>
</g>
{lib.PHONE}
<!-- 나물려 손: 정확히 2개 -->
<g stroke="{INK}" stroke-width="7"><ellipse cx="850" cy="1000" rx="36" ry="27" fill="#f4cfae"/><ellipse cx="930" cy="1008" rx="34" ry="26" fill="#f4cfae"/></g>
'''
B=lib.make.B; P="05화_놀이공원"
if sys.argv[1]=="test":
    lib2._png(lib._svg(SCENE+lib2.wm(),B,SCRIPT[0]),1080,1350,"/tmp/t5.png")
elif sys.argv[1]=="full":
    lib2.covers(5,"놀이공원",SCENE,SCRIPT[0],B,P)
    lib2.cards(SCENE,B,SCRIPT,P,6,"집밥 편")
    print(lib2.reel(SCENE,B,REEL,"주식 중독자의 놀이공원",P,5,6,"집밥 편"))
