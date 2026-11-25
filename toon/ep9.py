import sys, lib, lib2, lib3, db
INK=lib.INK
E=db.load(9); SCRIPT=E["script"]
SK="#efc6a4"
TIE=f'''<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <path d="M774,822 L806,822 L812,850 L790,862 L768,850 Z" fill="#b8323a"/>
 <path d="M776,858 L804,858 L818,960 L790,992 L762,960 Z" fill="#b8323a"/></g>'''
VISIT=f'''<g stroke="{INK}" stroke-width="5" stroke-linejoin="round">
 <path d="M742,790 L716,872" fill="none" stroke="#4fb36c" stroke-width="8"/><path d="M770,800 L746,872" fill="none" stroke="#4fb36c" stroke-width="8"/>
 <rect x="690" y="866" width="84" height="86" rx="8" fill="#ffffff"/>
 <rect x="690" y="866" width="84" height="26" rx="8" fill="#4fb36c"/>
 <text x="732" y="935" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="24" fill="{INK}" stroke="none">방문</text></g>'''
SCENE=f'''
<defs>
 <linearGradient id="w9" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9e4da"/><stop offset="1" stop-color="#d9d1c2"/></linearGradient>
 <linearGradient id="s9" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9fc9ec"/><stop offset="1" stop-color="#e2f1fb"/></linearGradient>
 <linearGradient id="t9" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a5a3a"/><stop offset="1" stop-color="#6b4229"/></linearGradient>
</defs>
<rect width="1080" height="1350" fill="url(#w9)"/>
<rect y="770" width="1080" height="12" fill="#b8ab95"/><rect y="782" width="1080" height="600" fill="#c9bca5"/>
<!-- 큰 창 + 도시 -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <rect x="420" y="292" width="270" height="330" rx="6" fill="url(#s9)"/>
 <g stroke="none"><rect x="432" y="470" width="50" height="146" fill="#b4c3d3"/><rect x="488" y="410" width="62" height="206" fill="#a2b3c6"/><rect x="556" y="450" width="48" height="166" fill="#c3cfdc"/><rect x="610" y="390" width="70" height="226" fill="#98aac0"/>
 <g fill="#eef6fc"><rect x="500" y="430" width="12" height="14"/><rect x="524" y="430" width="12" height="14"/><rect x="500" y="460" width="12" height="14"/><rect x="524" y="460" width="12" height="14"/><rect x="624" y="410" width="14" height="14"/><rect x="652" y="410" width="14" height="14"/><rect x="624" y="440" width="14" height="14"/><rect x="652" y="440" width="14" height="14"/></g></g>
 <line x1="555" y1="292" x2="555" y2="622" stroke-width="5"/>
 <rect x="420" y="292" width="270" height="330" rx="6" fill="none"/>
</g>
<!-- 다른 회사 문양 (초록 원 + 금색 막대) -->
<g transform="translate(40,320)" stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <rect width="140" height="140" rx="12" fill="#ffffff"/>
 <circle cx="50" cy="70" r="30" fill="#4fb36c"/>
 <rect x="90" y="40" width="14" height="60" rx="6" fill="#e9b949" stroke-width="4"/><rect x="110" y="56" width="14" height="44" rx="6" fill="#e9b949" stroke-width="4"/>
</g>
<!-- 최종 면접 안내 팻말 -->
<g transform="translate(930,320)" stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <rect width="112" height="150" rx="8" fill="#fff7ea"/>
 <rect x="16" y="18" width="80" height="26" rx="6" fill="#e2483d" stroke="none"/>
 <g stroke="#9aa7b3" stroke-width="5" stroke-linecap="round"><line x1="20" y1="70" x2="92" y2="70"/><line x1="20" y1="94" x2="92" y2="94"/><line x1="20" y1="118" x2="70" y2="118"/></g>
</g>

<!-- 회장님 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <path d="M95,1010 C95,820 150,745 235,725 L365,725 C450,745 505,820 505,1010 Z" fill="#4a4f5c"/>
 <path d="M245,727 L300,840 L355,727 Z" fill="#ffffff"/>
 <path d="M287,770 L313,770 L326,900 L300,935 L274,900 Z" fill="#2b3a55"/>
 <rect x="282" y="842" width="36" height="8" rx="3" fill="#e9b949" stroke-width="3"/>
 <path d="M235,725 L300,880 L246,930 L196,765 Z" fill="#3c414d"/>
 <path d="M365,725 L300,880 L354,930 L404,765 Z" fill="#3c414d"/>
 <path d="M262,660 L262,735 C285,760 315,760 338,735 L338,660 Z" fill="#e3b391"/>
 <path d="M200,530 C200,440 250,410 302,410 C356,410 404,440 404,530 C404,640 356,690 302,690 C248,690 200,640 200,530 Z" fill="{SK}"/>
 <path d="M200,545 C182,540 180,585 204,588" fill="{SK}"/><path d="M404,545 C422,540 424,585 400,588" fill="{SK}"/>
 <!-- 백발 올백 -->
 <path d="M192,522 C178,430 240,382 305,382 C372,380 430,430 412,522 C400,470 370,446 304,444 C240,446 208,470 192,522 Z" fill="#f1f1f4"/>
 <path d="M228,470 C250,430 300,420 330,428" fill="none" stroke="#b9bcc6" stroke-width="5"/>
 <path d="M262,452 C290,428 340,426 372,446" fill="none" stroke="#b9bcc6" stroke-width="5"/>
 <path d="M300,444 C330,430 372,438 394,470" fill="none" stroke="#b9bcc6" stroke-width="5"/>
 <path d="M196,520 C194,540 196,556 202,566 L210,566 C206,548 206,530 210,512 Z" fill="#f1f1f4" stroke-width="5"/>
 <path d="M408,520 C410,540 408,556 402,566 L394,566 C398,548 398,530 394,512 Z" fill="#f1f1f4" stroke-width="5"/>
 <!-- 흰 눈썹 -->
 <path d="M226,516 L282,526" stroke="#d9dbe0" stroke-width="12"/><path d="M322,526 L378,516" stroke="#d9dbe0" stroke-width="12"/>
 <path d="M226,516 L282,526" stroke-width="3" fill="none"/><path d="M322,526 L378,516" stroke-width="3" fill="none"/>
 <!-- 금테 안경 -->
 <rect x="222" y="536" width="68" height="46" rx="14" fill="#ffffff" fill-opacity="0.45" stroke="#c9a227" stroke-width="6"/>
 <rect x="314" y="536" width="68" height="46" rx="14" fill="#ffffff" fill-opacity="0.45" stroke="#c9a227" stroke-width="6"/>
 <line x1="290" y1="556" x2="314" y2="556" stroke="#c9a227" stroke-width="6"/>
 <circle cx="256" cy="560" r="8" fill="{INK}" stroke="none"/><circle cx="348" cy="560" r="8" fill="{INK}" stroke="none"/>
 <path d="M300,582 C290,606 292,614 308,614" fill="none" stroke-width="5"/>
 <path d="M240,600 C246,616 254,626 264,632" fill="none" stroke="#c49a7c" stroke-width="4"/><path d="M364,600 C358,616 350,626 340,632" fill="none" stroke="#c49a7c" stroke-width="4"/>
 <path d="M276,652 L328,652" fill="none" stroke-width="7"/>
</g>

{lib.CHAR}
{TIE}
{VISIT}

<!-- 원목 테이블 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <rect x="-10" y="990" width="1100" height="380" fill="url(#t9)"/>
 <line x1="-10" y1="1022" x2="1100" y2="1022" stroke="#4e2f1c" stroke-width="5"/>
 <!-- 서류철 -->
 <g transform="rotate(-4 520 980)"><rect x="440" y="950" width="160" height="50" rx="6" fill="#f3f0e6"/><rect x="440" y="950" width="160" height="14" rx="4" fill="#35507a" stroke-width="5"/></g>
 <!-- 회장님 팔뚝 (짙은 회색 정장) -->
 <path d="M96,1016 C98,966 160,950 262,962 L262,1024 L96,1024 Z" fill="#4a4f5c"/>
 <!-- 만년필 (손보다 먼저) -->
 <g transform="rotate(-62 300 990)"><rect x="296" y="900" width="14" height="140" rx="6" fill="#1f2430"/><rect x="296" y="900" width="14" height="22" rx="6" fill="#e9b949" stroke-width="4"/><path d="M296,1040 L303,1062 L310,1040 Z" fill="#e9b949" stroke-width="4"/></g>
</g>
{lib.hand(292,992,flip=False,rot=90,skin=SK)}
{lib.cuff(262,993,rot=2,color="#ffffff")}
{lib.NMR_FRONT}
'''
B=lib.B2; P="09화_최종면접"; LB="나물려의 회사생활 ③"; NX=E["next_title"]+" 편"
if sys.argv[1]=="test":
    lib2._png(lib._svg(SCENE+lib2.wm(),B,SCRIPT[0]),1080,1350,"/tmp/t9.png")
    lib2._png(lib3.cover_svg(9,"최종 면접",SCENE,SCRIPT[0],B,LB,"몰래 본 이직 면접"),1080,1350,"/tmp/t9c.png")
    lib2._png(lib3._frame("주식 중독자의 최종 면접",9,LB,lib._svg(SCENE,B,SCRIPT[1],4)),1080,1920,"/tmp/t9r.png")
elif sys.argv[1]=="full":
    lib3.covers(9,"최종 면접",SCENE,SCRIPT[0],B,P,LB,"몰래 본 이직 면접")
    lib2.cards(SCENE,B,SCRIPT,P,E["next_n"],NX)
    print(lib3.reel(SCENE,B,SCRIPT,"주식 중독자의 최종 면접",P,9,LB,E["next_n"],NX))
