import sys, lib, lib2
INK=lib.INK
def L(t): return tuple(x.strip().replace("|","\n") for x in t.split(" / "))
SCRIPT=[L(x) for x in [
 "요즘 뭐 하고|지내니? / 기다리고|있어요. / 뭘|기다리는데? / 본전이요.",
 "밥은 잘 먹고|다니니? / 오른 날은|잘 먹어요. / 그럼|요즘은? / 다이어트|중이에요..",
 "저축은 좀|하니? / 네, 묻어|뒀어요. / 어디에? / 아주 깊은|곳에요.",
 "옆집 아들은|집 샀다더라. / 저도|샀어요. / 정말?|어디에? / 고점에요.",
 "얼굴이 왜 이리|상했니? / 파란 걸 많이|봐서요. / 바다라도|다녀왔니? / 네, 제 계좌에|바다가 있어요.",
 "반찬 좀|싸줄까? / 네, 많이|주세요. / 웬일로 사양을|안 하니? / 이번 달은|긴축이라서요..",
 "결혼은 언제|할 거니? / 수익 나면요. / 그게|언젠데? / 엄마, 그건|신도 몰라요.",
 "새벽에 왜 불|켜놓고 있니? / 공부해요. / 무슨 공부를|새벽에 해? / 미국 경제요.",
 "용돈 좀|줄까? / 아니에요,|괜찮아요. / 다 컸구나. / 주시면 또|넣을까 봐요.",
 "엄마 친구가 좋은|종목 있다더라. / 엄마,|앉아보세요. / ...사실 벌써|좀 샀어. / 유전이었네요.",
]]
REEL=[SCRIPT[i-1] for i in (1,3,4,7,9,10)]
SK="#f7d7bd"
SCENE=f'''
<defs>
 <linearGradient id="w6" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fbeec9"/><stop offset="1" stop-color="#f5dfa6"/></linearGradient>
 <linearGradient id="t6" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c58f5c"/><stop offset="1" stop-color="#9c6a3e"/></linearGradient>
</defs>
<rect width="1080" height="1350" fill="url(#w6)"/>
<rect y="770" width="1080" height="12" fill="#dcc07e"/><rect y="782" width="1080" height="600" fill="#ecd391"/>
<!-- 냉장고 -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <rect x="440" y="296" width="230" height="474" rx="14" fill="#e9eef2"/>
 <line x1="440" y1="470" x2="670" y2="470"/>
 <rect x="462" y="400" width="14" height="52" rx="7" fill="#9aa7b3"/><rect x="462" y="492" width="14" height="80" rx="7" fill="#9aa7b3"/>
 <rect x="560" y="330" width="70" height="56" rx="4" fill="#fff1b8"/><circle cx="595" cy="330" r="7" fill="#e2483d"/>
 <rect x="540" y="520" width="50" height="50" rx="4" fill="#ffd9d0"/><circle cx="565" cy="520" r="7" fill="#3b8cff"/>
</g>
<!-- 달력 -->
<g transform="translate(36,326)" stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <rect width="130" height="190" rx="6" fill="#ffffff"/><rect width="130" height="46" rx="6" fill="#e2483d"/>
 <g stroke="none" fill="#9aa7b3"><rect x="16" y="64" width="16" height="14"/><rect x="42" y="64" width="16" height="14"/><rect x="68" y="64" width="16" height="14"/><rect x="94" y="64" width="16" height="14"/>
 <rect x="16" y="92" width="16" height="14"/><rect x="42" y="92" width="16" height="14"/><rect x="68" y="92" width="16" height="14" fill="#e2483d"/><rect x="94" y="92" width="16" height="14"/>
 <rect x="16" y="120" width="16" height="14"/><rect x="42" y="120" width="16" height="14"/><rect x="68" y="120" width="16" height="14"/><rect x="94" y="120" width="16" height="14"/>
 <rect x="16" y="148" width="16" height="14"/><rect x="42" y="148" width="16" height="14"/></g>
</g>
<!-- 벽 액자 -->
<g transform="translate(934,330)" stroke="{INK}" stroke-width="6" stroke-linejoin="round"><rect width="108" height="120" rx="6" fill="#fff"/>
 <circle cx="38" cy="56" r="16" fill="#f7d7bd"/><circle cx="72" cy="60" r="14" fill="#f4cfae"/><path d="M16,104 C20,80 56,80 60,104 Z" fill="#f2b8c0"/><path d="M54,104 C58,84 88,84 92,104 Z" fill="#8a8f9c"/></g>

<!-- 어머니 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <!-- 뒷머리 파마 -->
 <g fill="#4a3a36"><circle cx="210" cy="470" r="44"/><circle cx="250" cy="420" r="46"/><circle cx="304" cy="400" r="48"/><circle cx="358" cy="420" r="46"/><circle cx="396" cy="470" r="44"/><circle cx="192" cy="530" r="38"/><circle cx="412" cy="530" r="38"/></g>
 <path d="M95,1010 C95,820 150,745 235,725 L365,725 C450,745 505,820 505,1010 Z" fill="#b98bb4"/>
 <path d="M248,727 C262,770 338,770 352,727 Z" fill="#f3cdb3"/>
 <!-- 앞치마 -->
 <path d="M196,1010 L206,820 C240,800 360,800 394,820 L404,1010 Z" fill="#fff3ec"/>
 <path d="M222,812 L244,730" fill="none"/><path d="M378,812 L356,730" fill="none"/>
 <g stroke-width="4"><circle cx="246" cy="880" r="12" fill="#ff9a8b"/><circle cx="330" cy="860" r="12" fill="#ffd66b"/><circle cx="292" cy="930" r="12" fill="#ff9a8b"/><circle cx="356" cy="950" r="12" fill="#9ed38b"/><circle cx="236" cy="968" r="12" fill="#ffd66b"/></g>
 <path d="M262,660 L262,735 C285,760 315,760 338,735 L338,660 Z" fill="#edc4a6"/>
 <path d="M200,530 C200,440 250,410 302,410 C356,410 404,440 404,530 C404,640 356,690 302,690 C248,690 200,640 200,530 Z" fill="{SK}"/>
 <path d="M200,545 C182,540 180,585 204,588" fill="{SK}"/><path d="M404,545 C422,540 424,585 400,588" fill="{SK}"/>
 <!-- 앞머리 파마 -->
 <g fill="#4a3a36"><circle cx="232" cy="458" r="34"/><circle cx="278" cy="436" r="34"/><circle cx="328" cy="436" r="34"/><circle cx="374" cy="458" r="34"/></g>
 <!-- 걱정스러운 눈썹 -->
 <path d="M230,526 L278,510" stroke-width="7"/><path d="M326,510 L374,526" stroke-width="7"/>
 <ellipse cx="256" cy="556" rx="9" ry="11" fill="{INK}" stroke="none"/><ellipse cx="348" cy="556" rx="9" ry="11" fill="{INK}" stroke="none"/>
 <path d="M236,584 C246,590 266,590 276,584" fill="none" stroke="#c9a58c" stroke-width="4"/><path d="M328,584 C338,590 358,590 368,584" fill="none" stroke="#c9a58c" stroke-width="4"/>
 <path d="M300,576 C294,598 296,606 306,606" fill="none" stroke-width="5"/>
 <path d="M280,650 C292,640 312,640 324,650" fill="none" stroke-width="7"/>
 <ellipse cx="230" cy="612" rx="20" ry="11" fill="#f3a9a0" stroke="none" opacity="0.7"/><ellipse cx="374" cy="612" rx="20" ry="11" fill="#f3a9a0" stroke="none" opacity="0.7"/>
</g>

{lib.CHAR}

<!-- 식탁 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <rect x="-10" y="990" width="1100" height="380" fill="url(#t6)"/>
 <line x1="-10" y1="1022" x2="1100" y2="1022" stroke="#7d5230" stroke-width="5"/>
 <!-- 국그릇 + 김 -->
 <path d="M372,948 L470,948 C468,990 452,1002 421,1002 C390,1002 374,990 372,948 Z" fill="#ffffff"/>
 <ellipse cx="421" cy="948" rx="49" ry="10" fill="#e9b872"/>
 <path d="M404,926 C396,912 412,906 404,890 M436,926 C428,912 444,906 436,890" fill="none" stroke-width="4" stroke="#8d99a6"/>
 <!-- 밥그릇 + 꽂힌 숟가락 -->
 <path d="M498,952 L580,952 C578,990 566,1002 539,1002 C512,1002 500,990 498,952 Z" fill="#ffffff"/>
 <path d="M500,952 C510,922 568,922 578,952 Z" fill="#fdfdfd"/>
 <line x1="552" y1="936" x2="574" y2="872" stroke="#9aa7b3" stroke-width="8"/>
 <!-- 어머니 팔뚝 -->
 <path d="M96,1016 C98,966 160,950 262,962 L262,1024 L96,1024 Z" fill="#b98bb4"/>
 <!-- 국자 (손보다 먼저) -->
 <line x1="300" y1="1030" x2="318" y2="900" stroke="#8d99a6" stroke-width="10"/>
 <path d="M294,902 C290,866 346,866 344,902 C340,918 300,918 294,902 Z" fill="#cfd6de"/>
</g>
{lib.hand(292,992,flip=False,rot=90,skin=SK)}
{lib.cuff(262,993,rot=2,color="#9a6d96")}
{lib.NMR_FRONT}
'''
B=lib.B2; P="06화_집밥"
if sys.argv[1]=="test":
    lib2._png(lib._svg(SCENE+lib2.wm(),B,SCRIPT[0]),1080,1350,"/tmp/t6.png")
elif sys.argv[1]=="full":
    lib2.covers(6,"집밥",SCENE,SCRIPT[0],B,P)
    lib2.cards(SCENE,B,SCRIPT,P,7,"미용실 편")
    print(lib2.reel(SCENE,B,REEL,"주식 중독자의 집밥",P,6,7,"미용실 편"))
