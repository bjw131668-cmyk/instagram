import sys, lib, lib2, lib3, lib4, db
INK=lib.INK
E=db.load(18); SCRIPT=E["script"]; TH=E["thumb"]
# 상한나 기본 옷(캐릭터 시트): 분홍 카디건 + 크림색 안쪽 옷
SK="#f9dcc6"; CARD="#f2b8c0"; CARD2="#eaa3ad"; INNER="#fff7ea"
SCENE=f'''
<defs>
 <linearGradient id="sky18" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6d9c4"/><stop offset="0.6" stop-color="#f9e6d6"/><stop offset="1" stop-color="#fbeee2"/></linearGradient>
 <linearGradient id="river18" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b9cfdc"/><stop offset="1" stop-color="#a6c0cf"/></linearGradient>
</defs>
<!-- 노을 하늘 (채도 낮게) -->
<rect width="1080" height="1350" fill="url(#sky18)"/>
<circle cx="540" cy="560" r="70" fill="#f7c6a0" opacity="0.8"/>
<!-- 다리 -->
<g stroke="#8f8a92" stroke-width="6" fill="none" opacity="0.75">
 <line x1="0" y1="600" x2="1080" y2="600" stroke-width="12"/>
 <path d="M0,600 C90,520 180,520 270,600 C360,520 450,520 540,600 C630,520 720,520 810,600 C900,520 990,520 1080,600"/>
 <g stroke-width="4"><line x1="135" y1="540" x2="135" y2="600"/><line x1="405" y1="540" x2="405" y2="600"/><line x1="675" y1="540" x2="675" y2="600"/><line x1="945" y1="540" x2="945" y2="600"/></g>
</g>
<g fill="#8f8a92" opacity="0.75"><rect x="255" y="600" width="30" height="40"/><rect x="525" y="600" width="30" height="40"/><rect x="795" y="600" width="30" height="40"/></g>
<!-- 강물 -->
<rect y="640" width="1080" height="200" fill="url(#river18)"/>
<g stroke="#ffffff" stroke-width="4" stroke-linecap="round" opacity="0.5">
 <line x1="80" y1="690" x2="170" y2="690"/><line x1="420" y1="720" x2="520" y2="720"/><line x1="620" y1="680" x2="700" y2="680"/><line x1="860" y1="730" x2="960" y2="730"/>
 <line x1="490" y1="660" x2="590" y2="660" stroke="#f7c6a0"/>
</g>
<!-- 강변 산책로 -->
<rect y="800" width="1080" height="600" fill="#d9d3c4"/>
<line x1="0" y1="800" x2="1080" y2="800" stroke="#bdb5a3" stroke-width="6"/>

<!-- 상한나 (살짝 웃는 표정) -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <path d="M176,540 C160,400 250,356 305,358 C372,356 446,404 428,548 C440,660 446,760 420,800 L182,800 C158,760 164,660 176,540 Z" fill="#5a3a2a"/>
 <path d="M95,1010 C95,820 150,745 235,725 L365,725 C450,745 505,820 505,1010 Z" fill="{CARD}"/>
 <path d="M248,727 L300,830 L352,727 Z" fill="{INNER}"/>
 <path d="M235,725 L300,840 L276,1010 L230,1010 L205,760 Z" fill="{CARD2}"/>
 <path d="M365,725 L300,840 L324,1010 L370,1010 L395,760 Z" fill="{CARD2}"/>
 <g fill="#ffffff" stroke-width="4"><circle cx="292" cy="880" r="7"/><circle cx="292" cy="930" r="7"/></g>
 <path d="M262,660 L262,735 C285,760 315,760 338,735 L338,660 Z" fill="#f3cdb3"/>
 <path d="M200,530 C200,440 250,410 302,410 C356,410 404,440 404,530 C404,640 356,690 302,690 C248,690 200,640 200,530 Z" fill="{SK}"/>
 <path d="M194,540 C184,430 250,384 305,386 C366,384 424,432 410,540 C400,490 380,462 350,450 C330,480 260,486 228,470 C210,490 200,512 194,540 Z" fill="#5a3a2a"/>
 <path d="M232,508 C246,500 264,500 278,506" fill="none" stroke-width="6"/>
 <path d="M326,500 C340,490 358,490 372,498" fill="none" stroke-width="6"/>
 <path d="M236,550 C248,540 266,540 278,550" fill="none" stroke-width="7"/>
 <path d="M326,550 C338,540 356,540 368,550" fill="none" stroke-width="7"/>
 <circle cx="257" cy="558" r="9" fill="{INK}" stroke="none"/><circle cx="347" cy="558" r="9" fill="{INK}" stroke="none"/>
 <path d="M300,578 C294,598 296,606 306,606" fill="none" stroke-width="5"/>
 <path d="M280,640 C292,656 312,656 324,640" fill="none" stroke-width="7"/>
 <ellipse cx="230" cy="606" rx="20" ry="11" fill="#f3a9a0" stroke="none" opacity="0.7"/>
 <ellipse cx="374" cy="606" rx="20" ry="11" fill="#f3a9a0" stroke="none" opacity="0.7"/>
</g>

{lib.CHAR}

<!-- 편의점 파라솔 테이블 (흰 플라스틱) -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <rect x="-10" y="990" width="1100" height="380" fill="#eceae4"/>
 <line x1="-10" y1="1022" x2="1100" y2="1022" stroke="#c9c5ba" stroke-width="5"/>
 <!-- 컵라면 두 개 (강한 색은 소품에만) -->
 <g transform="translate(470,912)">
  <path d="M0,0 L74,0 L64,80 L10,80 Z" fill="#e2483d"/><rect x="-6" y="-12" width="86" height="16" rx="4" fill="#ffffff"/>
  <path d="M14,30 L60,30" stroke="#ffffff" stroke-width="6"/>
  <line x1="50" y1="-12" x2="66" y2="-62" stroke-width="5"/><line x1="58" y1="-12" x2="78" y2="-58" stroke-width="5"/>
 </g>
 <g transform="translate(570,920)">
  <path d="M0,0 L66,0 L58,72 L8,72 Z" fill="#f2a33a"/><rect x="-6" y="-12" width="78" height="16" rx="4" fill="#ffffff"/>
  <path d="M12,28 L54,28" stroke="#ffffff" stroke-width="6"/>
 </g>
 <!-- 상한나 팔뚝 -->
 <path d="M96,1016 C98,966 160,950 262,962 L262,1024 L96,1024 Z" fill="{CARD}"/>
 <!-- 캔커피 (손보다 먼저) -->
 <rect x="306" y="900" width="70" height="104" rx="10" fill="#6d4c3d"/>
 <rect x="306" y="930" width="70" height="40" fill="#f3e6cf"/>
 <ellipse cx="341" cy="900" rx="35" ry="8" fill="#c9ccd2"/>
</g>
{lib.hand(292,992,flip=False,rot=90,skin=SK)}
{lib.cuff(262,993,rot=2,color=CARD2)}
{lib.NMR_FRONT}
'''
B=lib.B2; P="18화_다시고백"; NX=E["next_title"]+" 편"
if sys.argv[1]=="test":
    lib2._png(lib._svg(SCENE+lib2.wm(),B,SCRIPT[9]),1080,1350,"/tmp/t18.png")
elif sys.argv[1]=="full":
    lib4.covers("다시 고백",SCENE,TH,B,P)
    lib4.cards(SCENE,B,SCRIPT,P,E["next_n"],NX)
    print(lib4.reel(SCENE,B,SCRIPT,"주식 중독자의 다시 고백",P,E["next_n"],NX))
