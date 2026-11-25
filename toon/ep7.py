import sys, lib, lib2, db
INK=lib.INK
E=db.load(7); SCRIPT=E["script"]; REEL=[SCRIPT[i-1] for i in E["reel"]]
SK="#f7d7bd"
SCENE=f'''
<defs>
 <linearGradient id="w7" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ece4f7"/><stop offset="1" stop-color="#ddd0ee"/></linearGradient>
 <linearGradient id="m7" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#eaf6fb"/><stop offset="1" stop-color="#cfe6f2"/></linearGradient>
 <linearGradient id="t7" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fbfbfd"/><stop offset="1" stop-color="#dcdfe8"/></linearGradient>
</defs>
<rect width="1080" height="1350" fill="url(#w7)"/>
<rect y="770" width="1080" height="12" fill="#c5b5dd"/><rect y="782" width="1080" height="600" fill="#d2c4e6"/>
<!-- 큰 거울 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round">
 <rect x="418" y="296" width="274" height="380" rx="26" fill="#c9a37a"/>
 <rect x="436" y="314" width="238" height="344" rx="16" fill="url(#m7)" stroke-width="5"/>
 <g stroke="#ffffff" stroke-width="8" stroke-linecap="round" opacity="0.9"><line x1="470" y1="420" x2="540" y2="344"/><line x1="486" y1="460" x2="580" y2="358"/></g>
 <g fill="#ffe9a8" stroke-width="4"><circle cx="418" cy="350" r="10"/><circle cx="418" cy="430" r="10"/><circle cx="418" cy="510" r="10"/><circle cx="418" cy="590" r="10"/><circle cx="692" cy="350" r="10"/><circle cx="692" cy="430" r="10"/><circle cx="692" cy="510" r="10"/><circle cx="692" cy="590" r="10"/></g>
</g>
<!-- 선반 + 병 -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <rect x="26" y="470" width="150" height="16" rx="4" fill="#c9a37a"/>
 <rect x="42" y="396" width="34" height="74" rx="8" fill="#ff9a8b"/><rect x="50" y="376" width="18" height="22" rx="4" fill="#fff"/>
 <rect x="88" y="414" width="30" height="56" rx="8" fill="#9ed38b"/><rect x="96" y="398" width="14" height="18" rx="4" fill="#fff"/>
 <rect x="130" y="384" width="32" height="86" rx="8" fill="#6fa8ff"/><rect x="138" y="364" width="16" height="22" rx="4" fill="#fff"/>
</g>
<!-- 벽 조명 -->
<g stroke="{INK}" stroke-width="6"><line x1="985" y1="300" x2="985" y2="350"/><path d="M940,410 C940,360 1030,360 1030,410 Z" fill="#ffd66b"/><circle cx="985" cy="418" r="12" fill="#fff7d6"/></g>

<!-- 미용사 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <!-- 묶은 머리(똥머리) -->
 <circle cx="302" cy="372" r="44" fill="#2e2a33"/>
 <path d="M190,540 C176,430 244,384 304,384 C366,384 430,430 414,540 C412,580 406,600 400,612 L204,612 C198,600 192,580 190,540 Z" fill="#2e2a33"/>
 <path d="M95,1010 C95,820 150,745 235,725 L365,725 C450,745 505,820 505,1010 Z" fill="#e8b04a"/>
 <path d="M250,727 C264,768 336,768 350,727 Z" fill="#f3cdb3"/>
 <!-- 검은 앞치마 -->
 <path d="M200,1010 L210,826 C244,806 356,806 390,826 L400,1010 Z" fill="#2b2b33"/>
 <path d="M226,818 L246,730" fill="none"/><path d="M374,818 L354,730" fill="none"/>
 <rect x="262" y="880" width="76" height="60" rx="8" fill="#3a3a44"/>
 <line x1="284" y1="868" x2="284" y2="900" stroke="#ff9a8b" stroke-width="8"/><line x1="312" y1="872" x2="312" y2="900" stroke="#cfd6de" stroke-width="8"/>
 <path d="M262,660 L262,735 C285,760 315,760 338,735 L338,660 Z" fill="#edc4a6"/>
 <path d="M200,530 C200,440 250,410 302,410 C356,410 404,440 404,530 C404,640 356,690 302,690 C248,690 200,640 200,530 Z" fill="{SK}"/>
 <path d="M200,545 C182,540 180,585 204,588" fill="{SK}"/><path d="M404,545 C422,540 424,585 400,588" fill="{SK}"/>
 <!-- 앞머리: 옆으로 넘김 -->
 <path d="M196,530 C186,440 250,392 306,394 C366,392 420,440 408,528 C398,486 372,462 330,456 C300,490 240,492 214,486 C204,498 198,512 196,530 Z" fill="#2e2a33"/>
 <!-- 눈썹/눈: 상냥한 영업 표정 -->
 <path d="M232,518 C246,510 264,510 278,516" fill="none" stroke-width="6"/><path d="M326,516 C340,510 358,510 372,518" fill="none" stroke-width="6"/>
 <path d="M236,552 C248,542 266,542 278,552" fill="none" stroke-width="7"/><path d="M326,552 C338,542 356,542 368,552" fill="none" stroke-width="7"/>
 <circle cx="257" cy="560" r="9" fill="{INK}" stroke="none"/><circle cx="347" cy="560" r="9" fill="{INK}" stroke="none"/>
 <path d="M300,578 C294,598 296,606 306,606" fill="none" stroke-width="5"/>
 <path d="M274,640 C288,656 316,656 330,640" fill="none" stroke-width="7"/>
 <ellipse cx="230" cy="606" rx="20" ry="11" fill="#f3a9a0" stroke="none" opacity="0.7"/><ellipse cx="374" cy="606" rx="20" ry="11" fill="#f3a9a0" stroke="none" opacity="0.7"/>
 <!-- 귀걸이 -->
 <circle cx="196" cy="600" r="7" fill="#ffd66b" stroke-width="4"/><circle cx="408" cy="600" r="7" fill="#ffd66b" stroke-width="4"/>
</g>

{lib.CHAR}
<!-- 미용 가운: 후드티 위에 두름. 목 뒤 후드 모자는 가운 위로 그대로 보인다 -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <path d="M580,1010 C580,832 632,772 716,752 C752,792 828,792 864,752 C948,772 1010,832 1010,1010 Z" fill="#ffffff"/>
 <path d="M716,752 C752,792 828,792 864,752 C852,822 728,822 716,752 Z" fill="#dfe6ee"/>
 <g stroke-width="4" stroke="#3a2c26"><path d="M660,880 l14,-8"/><path d="M700,930 l10,10"/><path d="M930,890 l-12,-10"/><path d="M880,960 l12,6"/><path d="M640,950 l8,10"/><path d="M790,870 l10,-4"/></g>
</g>

<!-- 미용실 선반(전경) -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <rect x="-10" y="990" width="1100" height="380" fill="url(#t7)"/>
 <line x1="-10" y1="1022" x2="1100" y2="1022" stroke="#b9bdca" stroke-width="5"/>
 <!-- 분무기 -->
 <path d="M410,1000 L414,930 L462,930 L466,1000 Z" fill="#a9dcf3"/>
 <rect x="424" y="902" width="28" height="30" rx="5" fill="#ffffff"/><path d="M452,908 L480,902 L480,918 L452,918 Z" fill="#ffffff"/>
 <!-- 빗 -->
 <g transform="rotate(-8 540 986)"><rect x="492" y="972" width="96" height="14" rx="5" fill="#ff9a8b"/>
 <g stroke-width="4"><line x1="500" y1="986" x2="500" y2="1004"/><line x1="512" y1="986" x2="512" y2="1004"/><line x1="524" y1="986" x2="524" y2="1004"/><line x1="536" y1="986" x2="536" y2="1004"/><line x1="548" y1="986" x2="548" y2="1004"/><line x1="560" y1="986" x2="560" y2="1004"/><line x1="572" y1="986" x2="572" y2="1004"/><line x1="584" y1="986" x2="584" y2="1004"/></g></g>
 <!-- 미용사 팔뚝 -->
 <path d="M96,1016 C98,966 160,950 262,962 L262,1024 L96,1024 Z" fill="#e8b04a"/>
 <!-- 가위 (손보다 먼저) -->
 <g transform="rotate(-38 300 990)">
  <path d="M300,996 L432,978 L300,984 Z" fill="#cfd6de"/><path d="M300,984 L432,1002 L300,996 Z" fill="#e9eef2"/>
  <circle cx="352" cy="990" r="5" fill="#8d99a6" stroke-width="3"/>
  <ellipse cx="282" cy="972" rx="20" ry="13" fill="none" stroke-width="8" stroke="#35507a"/><ellipse cx="282" cy="1008" rx="20" ry="13" fill="none" stroke-width="8" stroke="#35507a"/>
 </g>
</g>
{lib.hand(292,992,flip=False,rot=90,skin=SK)}
{lib.cuff(262,993,rot=2,color="#c98f2f")}
{lib.NMR_FRONT}
'''
B=lib.B2; P="07화_미용실"; T="주식 중독자의 미용실"
if sys.argv[1]=="test":
    lib2._png(lib._svg(SCENE+lib2.wm(),B,SCRIPT[0]),1080,1350,"/tmp/t7.png")
elif sys.argv[1]=="full":
    lib2.covers(7,"미용실",SCENE,SCRIPT[0],B,P)
    lib2.cards(SCENE,B,SCRIPT,P,E["next_n"],E["next_title"]+" 편")
    print(lib2.reel(SCENE,B,REEL,T,P,7,E["next_n"],E["next_title"]+" 편"))
