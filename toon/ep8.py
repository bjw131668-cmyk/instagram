import sys, lib, lib2, db
INK=lib.INK
E=db.load(8); SCRIPT=E["script"]; REEL=[SCRIPT[i-1] for i in E["reel"]]
SK="#f9dcc6"
# 3화의 소개팅 상대를 그대로 가져오고, 표정만 살짝 웃게 바꾼다
src=open("/home/claude/toon/ep3.py").read()
a=src.index("<!-- 소개팅 상대 -->"); b=src.index("{lib.CHAR}",a)
WOMAN=src[a:b].replace("{INK}",INK)
old_mouth='<path d="M280,644 L324,642" fill="none" stroke-width="7"/>'
assert old_mouth in WOMAN
WOMAN=WOMAN.replace(old_mouth,'<path d="M276,640 C290,654 314,654 328,640" fill="none" stroke-width="7"/>')
SCENE=f'''
<defs>
 <linearGradient id="w8" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f7e9da"/><stop offset="1" stop-color="#efd6bd"/></linearGradient>
 <linearGradient id="s8" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5b6fb3"/><stop offset="1" stop-color="#f6b08a"/></linearGradient>
 <linearGradient id="t8" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#e6e2dc"/></linearGradient>
</defs>
<rect width="1080" height="1350" fill="url(#w8)"/>
<rect y="770" width="1080" height="12" fill="#c9a37a"/><rect y="782" width="1080" height="600" fill="#b9825a"/>
<!-- 아치 창 (저녁 하늘) -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round">
 <path d="M430,640 L430,430 C430,330 680,330 680,430 L680,640 Z" fill="url(#s8)"/>
 <line x1="555" y1="356" x2="555" y2="640" stroke-width="5"/><line x1="430" y1="500" x2="680" y2="500" stroke-width="5"/>
 <circle cx="620" cy="420" r="18" fill="#fff3c4" stroke-width="4"/>
 <rect x="416" y="640" width="278" height="18" rx="6" fill="#c9a37a"/>
</g>
<!-- 벽등 (왼쪽) -->
<g stroke="{INK}" stroke-width="6" stroke-linejoin="round"><rect x="92" y="340" width="16" height="60" rx="6" fill="#c9a37a"/><path d="M60,470 L140,470 L122,400 L78,400 Z" fill="#ffd66b"/></g>
<!-- 액자 (오른쪽) -->
<g transform="translate(930,330)" stroke="{INK}" stroke-width="6" stroke-linejoin="round"><rect width="112" height="130" rx="6" fill="#fff"/>
 <path d="M24,96 C24,60 88,60 88,96 Z" fill="#e2483d"/><path d="M40,60 C36,44 48,40 44,26 M70,60 C66,44 78,40 74,26" fill="none" stroke-width="4" stroke="#8d99a6"/></g>

{WOMAN}

{lib.CHAR}

<!-- 식탁 (흰 식탁보) -->
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
 <rect x="-10" y="990" width="1100" height="380" fill="url(#t8)"/>
 <line x1="-10" y1="1022" x2="1100" y2="1022" stroke="#cfc8be" stroke-width="5"/>
 <!-- 촛불 -->
 <rect x="542" y="930" width="26" height="70" rx="5" fill="#fff7ea"/>
 <path d="M555,928 C540,906 552,892 555,878 C558,892 570,906 555,928 Z" fill="#ffb347" stroke-width="5"/>
 <!-- 파스타 접시 (상대) -->
 <ellipse cx="420" cy="992" rx="78" ry="16" fill="#ffffff"/>
 <path d="M372,986 C380,952 460,952 468,986 Z" fill="#f2c26b"/>
 <path d="M386,978 C400,962 416,976 430,962 C442,974 452,966 458,978" fill="none" stroke="#d99a3a" stroke-width="4"/>
 <circle cx="420" cy="958" r="8" fill="#e2483d" stroke-width="4"/>
 <!-- 물잔 -->
 <path d="M470,930 L514,930 L508,996 L476,996 Z" fill="#eaf6fb"/><path d="M474,958 L510,958 L508,996 L476,996 Z" fill="#a9dcf3" stroke="none"/><path d="M470,930 L514,930 L508,996 L476,996 Z" fill="none"/>
 <!-- 상대 팔뚝 -->
 <path d="M96,1016 C98,966 160,950 262,962 L262,1024 L96,1024 Z" fill="#f2b8c0"/>
 <!-- 포크 (손보다 먼저) -->
 <g transform="rotate(14 300 990)">
  <line x1="300" y1="1040" x2="300" y2="930" stroke="#aab4be" stroke-width="9"/>
  <path d="M284,930 L284,884 M295,930 L295,880 M305,930 L305,880 M316,930 L316,884" fill="none" stroke="#aab4be" stroke-width="6"/>
  <path d="M282,930 L318,930" stroke="#aab4be" stroke-width="10"/>
 </g>
</g>
{lib.hand(292,992,flip=False,rot=90,skin=SK)}
{lib.cuff(262,993,rot=2,color="#eaa3ad")}
{lib.NMR_FRONT}
'''
B=lib.B2; P="08화_소개팅애프터"; T="주식 중독자의 소개팅 애프터"; NX=E["next_title"]+" 편"
if sys.argv[1]=="test":
    lib2._png(lib._svg(SCENE+lib2.wm(),B,SCRIPT[0]),1080,1350,"/tmp/t8.png")
    lib2._png(lib2.cover_svg(8,"소개팅 애프터",SCENE,SCRIPT[0],B),1080,1350,"/tmp/t8c.png")
elif sys.argv[1]=="full":
    lib2.covers(8,"소개팅 애프터",SCENE,SCRIPT[0],B,P)
    lib2.cards(SCENE,B,SCRIPT,P,E["next_n"],NX)
    print(lib2.reel(SCENE,B,REEL,T,P,8,E["next_n"],NX))
    print(lib2.reel(SCENE,B,SCRIPT,T,P+"_전체10세트",8,E["next_n"],NX))
