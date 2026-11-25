import sys, lib
INK=lib.INK
SCRIPT=[
 ("이상형이\n어떻게 되세요?","꾸준히 우상향\n하는 분이요.","...성격\n말씀이시죠?","네, 급락만\n없으면 됩니다."),
 ("취미가\n뭐예요?","차트\n봅니다.","그림 좋아하시나\n봐요?","네, 주로\n내려가는 그림이요."),
 ("주말엔 뭐\n하세요?","월요일을\n기다립니다.","일을 좋아하시나\n봐요?","아뇨, 장이\n열려서요."),
 ("연애는 얼마나\n쉬셨어요?","장기 보유\n중입니다.","...뭘요?","솔로를요.\n5년째."),
 ("커피는 제가\n살게요.","오, 오늘\n첫 수익이네요.","...수익이요?","4,500원\n벌었습니다."),
 ("어떤 사람이\n되고 싶으세요?","배당 주는\n사람이요.","베푸는 사람\n말씀이죠?","네, 분기마다\n꼬박꼬박이요."),
 ("저는 좀\n어때요?","저평가되신 것\n같습니다.","그게\n칭찬이에요?","제 기준\n최고 등급입니다."),
 ("휴대폰 좀 그만\n보시면 안 돼요?","죄송합니다.\n3시 반까지만요.","지금 3시\n25분인데요?","가장 중요한\n5분입니다."),
 ("결혼 생각은\n있으세요?","네, 본전\n오면요.","그게\n언젠데요?","저도 3년째\n묻고 있습니다."),
 ("저 사실\n증권사 다녀요.","혹시 제 종목\n아세요?","...그 종목\n매도 의견인데요.","커피는 제가\n살게요."),
]
SCENE=f'''
<defs>
 <linearGradient id="w3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6e7d3"/><stop offset="1" stop-color="#eed7bb"/></linearGradient>
 <linearGradient id="t3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b9824f"/><stop offset="1" stop-color="#93623a"/></linearGradient>
 <linearGradient id="s3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bfe3f7"/><stop offset="1" stop-color="#f3fafd"/></linearGradient>
</defs>
<rect width="1080" height="1350" fill="url(#w3)"/>
<rect y="770" width="1080" height="12" fill="#c9a37a"/><rect y="782" width="1080" height="600" fill="#d9b78f"/>
<!-- 창문 + 거리 -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <rect x="430" y="300" width="250" height="310" rx="8" fill="url(#s3)"/>
 <g stroke="none">
  <rect x="446" y="450" width="60" height="154" fill="#c9d3dd"/><rect x="512" y="400" width="70" height="204" fill="#b4c0cc"/><rect x="590" y="470" width="76" height="134" fill="#cfd8e0"/>
  <g fill="#f3fafd"><rect x="524" y="420" width="16" height="18"/><rect x="552" y="420" width="16" height="18"/><rect x="524" y="456" width="16" height="18"/><rect x="552" y="456" width="16" height="18"/><rect x="458" y="470" width="14" height="16"/><rect x="480" y="470" width="14" height="16"/><rect x="604" y="492" width="16" height="16"/><rect x="634" y="492" width="16" height="16"/></g>
  <circle cx="640" cy="350" r="24" fill="#ffd66b"/>
 </g>
 <line x1="555" y1="300" x2="555" y2="610" stroke-width="5"/>
 <rect x="430" y="300" width="250" height="310" rx="8" fill="none"/>
</g>
<!-- 메뉴 칠판 -->
<g transform="translate(36,326)" stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <rect width="130" height="200" rx="6" fill="#35423d"/>
 <text x="65" y="46" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="28" fill="#fff" stroke="none">MENU</text>
 <g stroke="#e8efe9" stroke-width="5" stroke-linecap="round"><line x1="22" y1="78" x2="108" y2="78"/><line x1="22" y1="106" x2="92" y2="106"/><line x1="22" y1="134" x2="108" y2="134"/><line x1="22" y1="162" x2="80" y2="162"/></g>
</g>
<!-- 액자 -->
<g transform="translate(930,330)" stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <rect width="112" height="120" rx="6" fill="#fff"/>
 <path d="M30,56 L82,56 L76,96 L36,96 Z" fill="#a36a3f"/><path d="M82,62 C100,62 100,86 80,86" fill="none"/>
 <path d="M46,44 C40,34 52,30 46,20 M66,44 C60,34 72,30 66,20" fill="none" stroke-width="4"/>
</g>

<!-- 소개팅 상대 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <!-- 뒷머리(긴 머리) -->
 <path d="M176,540 C160,400 250,356 305,358 C372,356 446,404 428,548 C440,660 446,760 420,800 L182,800 C158,760 164,660 176,540 Z" fill="#5a3a2a"/>
 <!-- 가디건 -->
 <path d="M95,1010 C95,820 150,745 235,725 L365,725 C450,745 505,820 505,1010 Z" fill="#f2b8c0"/>
 <path d="M240,727 L300,860 L360,727 Z" fill="#fff7ea"/>
 <path d="M235,725 L300,900 L300,1010 L270,1010 L210,760 Z" fill="#eaa3ad"/>
 <path d="M365,725 L300,900 L300,1010 L330,1010 L390,760 Z" fill="#eaa3ad"/>
 <circle cx="300" cy="930" r="8" fill="#fff"/><circle cx="300" cy="975" r="8" fill="#fff"/>
 <path d="M262,660 L262,735 C285,760 315,760 338,735 L338,660 Z" fill="#f3cdb3"/>
 <path d="M200,530 C200,440 250,410 302,410 C356,410 404,440 404,530 C404,640 356,690 302,690 C248,690 200,640 200,530 Z" fill="#f9dcc6"/>
 <!-- 앞머리 -->
 <path d="M194,540 C184,430 250,384 305,386 C366,384 424,432 410,540 C400,490 380,462 350,450 C330,480 260,486 228,470 C210,490 200,512 194,540 Z" fill="#5a3a2a"/>
 <!-- 눈썹: 한쪽만 올라감 -->
 <path d="M232,512 C246,504 264,504 278,510" fill="none" stroke-width="6"/>
 <path d="M326,504 C340,494 358,494 372,502" fill="none" stroke-width="6"/>
 <!-- 눈 -->
 <path d="M236,550 C248,540 266,540 278,550" fill="none" stroke-width="7"/>
 <path d="M326,550 C338,540 356,540 368,550" fill="none" stroke-width="7"/>
 <circle cx="257" cy="558" r="9" fill="{INK}" stroke="none"/><circle cx="347" cy="558" r="9" fill="{INK}" stroke="none"/>
 <path d="M300,578 C294,598 296,606 306,606" fill="none" stroke-width="5"/>
 <path d="M280,644 L324,642" fill="none" stroke-width="7"/>
 <ellipse cx="230" cy="606" rx="20" ry="11" fill="#f3a9a0" stroke="none" opacity="0.7"/>
 <ellipse cx="374" cy="606" rx="20" ry="11" fill="#f3a9a0" stroke="none" opacity="0.7"/>
</g>

{lib.CHAR}

<!-- 테이블 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <rect x="-10" y="990" width="1100" height="380" fill="url(#t3)"/>
 <line x1="-10" y1="1022" x2="1100" y2="1022" stroke="#7d5230" stroke-width="5"/>
 <!-- 꽃병 -->
 <path d="M528,996 L536,930 L574,930 L582,996 Z" fill="#eaf6fb"/>
 <path d="M555,930 C552,900 548,880 556,860" fill="none" stroke="#4c9a58" stroke-width="6"/>
 <circle cx="556" cy="848" r="20" fill="#ff9a8b"/><circle cx="556" cy="848" r="7" fill="#ffd66b" stroke-width="4"/>
 <!-- 상대 커피잔 + 손 (손 1개) -->
 <path d="M150,1000 C150,960 200,948 240,958 L300,975 L300,1010 Z" fill="#f2b8c0"/>
 <path d="M300,930 L390,930 L380,1000 L310,1000 Z" fill="#ffffff"/>
 <path d="M388,944 C418,944 416,984 382,984" fill="none"/>
 <ellipse cx="345" cy="932" rx="45" ry="9" fill="#7a4a2b"/>
 <path d="M330,912 C322,898 338,892 330,876 M356,912 C348,898 364,892 356,876" fill="none" stroke-width="4" stroke="#8d99a6"/>
 <ellipse cx="262" cy="1000" rx="34" ry="26" fill="#f9dcc6"/>
 <!-- 나물려 커피잔 -->
 <path d="M640,948 L712,948 L704,1002 L648,1002 Z" fill="#ffffff"/>
 <ellipse cx="676" cy="950" rx="36" ry="8" fill="#7a4a2b"/>
 <!-- 나물려 팔 -->
 <path d="M700,1010 C700,975 730,950 780,950 L800,1010 Z" fill="#8a8f9c"/>
 <path d="M1010,1010 C1010,950 950,925 900,945 L870,1010 Z" fill="#8a8f9c"/>
</g>
{lib.PHONE}
<!-- 나물려 손: 정확히 2개 -->
<g stroke="{INK}" stroke-width="7"><ellipse cx="850" cy="1000" rx="36" ry="27" fill="#f4cfae"/><ellipse cx="930" cy="1008" rx="34" ry="26" fill="#f4cfae"/></g>
'''
B=lib.make.B
if sys.argv[1]=="test":
    print(lib.cards(SCENE,B,SCRIPT[:1],"t3"))
else:
    lib.cards(SCENE,B,SCRIPT,"03화_소개팅")
    print(lib.reel(SCENE,B,SCRIPT,"주식 중독자의 소개팅","03화_소개팅"))
