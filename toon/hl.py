import sys; sys.argv=["x","none"]
import lib, lib2
INK=lib.INK
src=open("ep3.py").read(); a=src.index("<!-- 소개팅 상대 -->"); b=src.index("{lib.CHAR}",a)
HANNA=src[a:b].replace("{INK}",INK).replace('<path d="M280,644 L324,642" fill="none" stroke-width="7"/>','<path d="M276,640 C290,654 314,654 328,640" fill="none" stroke-width="7"/>')
TIE=f'''<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <path d="M774,822 L806,822 L812,850 L790,862 L768,850 Z" fill="#b8323a"/>
 <path d="M776,858 L804,858 L818,960 L790,992 L762,960 Z" fill="#b8323a"/></g>'''
BADGE=f'''<g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <path d="M716,800 L742,900" fill="none" stroke="#2f6fd0" stroke-width="9"/><path d="M864,800 L838,900" fill="none" stroke="#2f6fd0" stroke-width="9"/>
 <rect x="836" y="896" width="76" height="92" rx="8" fill="#ffffff" transform="translate(-46,0)"/>
 <circle cx="828" cy="928" r="13" fill="#3a2c26"/><rect x="804" y="952" width="48" height="10" rx="5" fill="#9aa7b3" stroke="none"/><rect x="810" y="968" width="36" height="8" rx="4" fill="#9aa7b3" stroke="none"/></g>'''
def sheet(bg, ring, inner, path):
    svg=f'''<rect width="1080" height="1920" fill="{bg}"/>
<circle cx="540" cy="960" r="500" fill="{ring}"/>
<defs><clipPath id="c"><circle cx="540" cy="960" r="500"/></clipPath></defs>
<g clip-path="url(#c)">{inner}</g>'''
    lib2._png(svg,1080,1920,path)
# 회사생활: 나물려 + 넥타이 + 사원증, 뒤에 서류가방 실루엣과 하락 그래프
s=1.55
work=f'''<polyline points="60,760 260,820 380,780 560,900 700,860 1020,1080" fill="none" stroke="#9db8e6" stroke-width="34" stroke-linejoin="round" opacity="0.7"/>
<g transform="translate(160,1150)" stroke="{INK}" stroke-width="7" stroke-linejoin="round" opacity="0.9">
 <rect x="0" y="40" width="170" height="120" rx="16" fill="#8a5a3c"/><path d="M55,40 L55,18 C55,6 115,6 115,18 L115,40" fill="none"/><line x1="0" y1="92" x2="170" y2="92"/></g>
<g transform="translate({540-790*s},{960-640*s}) scale({s})">{lib.CHAR}{TIE}{BADGE}</g>'''
sheet("#35507a","#d6e6ff",work,"out/하이라이트커버_나물려의회사생활.png")
# 사랑: 한나(왼쪽) + 나물려(오른쪽)를 가깝게, 사이에 큰 하트
s2=1.2
love=f'''<g transform="translate({540-546*s2},{1060-600*s2}) scale({s2})"><g transform="translate(150,0)">{HANNA}</g><g transform="translate(-80,0)">{lib.CHAR}</g></g>
<g transform="translate(540,650) scale(1.45)" stroke="{INK}" stroke-width="6" stroke-linejoin="round">
 <path d="M0,40 C-70,-10 -60,-80 -12,-74 C-4,-72 0,-66 0,-60 C0,-66 4,-72 12,-74 C60,-80 70,-10 0,40 Z" fill="#ff5a6e"/>
 <path d="M-30,-36 L-12,-22 L4,-34 L26,-12" fill="none" stroke="#ffffff" stroke-width="6"/><path d="M26,-12 L12,-12 M26,-12 L26,-26" fill="none" stroke="#ffffff" stroke-width="6"/></g>'''
sheet("#e8577a","#ffe3ea",love,"out/하이라이트커버_나물려의사랑.png")
