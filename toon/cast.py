import sys; sys.argv=["x","none"]
import lib, lib2
INK=lib.INK; F=lib2.F
def grab(fn,start,end="{lib.CHAR}"):
    s=open(fn).read(); a=s.index(start); b=s.index(end,a); return s[a:b].replace("{INK}",INK)
HANNA=grab("ep3.py","<!-- 소개팅 상대 -->").replace('<path d="M280,644 L324,642" fill="none" stroke-width="7"/>','<path d="M276,640 C290,654 314,654 328,640" fill="none" stroke-width="7"/>')
BOSS=grab("ep4.py","<!-- 팀장 -->")
k=0.74
def place(g,hx,cx): return f'<g transform="translate({cx-hx*k},{150+ (1-k)*0}) scale({k})">{g}</g>'
cards=[("상한나","증권사 애널리스트 · 주식 고수","\"그래서 지금|몇 프로야?\"","#f2b8c0","#e8577a"),
       ("나물려","3년째 -50% · 존버 장인","\"본전이요.\"","#c9d3e6","#35507a"),
       ("장기보 팀장","20년째 장기 보유 · 나물려의 상사","\"그 종목|나도 있어.\"","#cfe3f7","#2f6fd0")]
xs=[190,540,890]
svg=f'''<rect width="1080" height="1350" fill="#f6f1e8"/>
<rect width="1080" height="190" fill="#101726"/>
<text x="540" y="92" text-anchor="middle" {F} font-weight="900" font-size="38" fill="#6fa8ff">@namullyeo_toon</text>
<text x="540" y="158" text-anchor="middle" {F} font-weight="900" font-size="64" fill="#ffffff">등장인물 소개</text>
<g opacity="0.5"><polyline points="0,300 180,360 300,330 480,470 620,430 800,600 1080,760" fill="none" stroke="#c9d3e6" stroke-width="26" stroke-linejoin="round"/></g>
{place(HANNA,302,xs[0])}{place(lib.CHAR,790,xs[1])}{place(BOSS,302,xs[2])}
'''
for (n,role,line,bg,ac),x in zip(cards,xs):
    fs=lib2._fit(n,52,320); rs=lib2._fit(role,26,320)
    r1,r2=role.split(" · ")
    svg+=f'<rect x="{x-170}" y="790" width="340" height="470" rx="28" fill="#ffffff" stroke="{INK}" stroke-width="6"/>'
    svg+=f'<rect x="{x-170}" y="790" width="340" height="110" rx="28" fill="{ac}" stroke="{INK}" stroke-width="6"/><rect x="{x-167}" y="860" width="334" height="38" fill="{ac}"/>'
    svg+=f'<text x="{x}" y="864" text-anchor="middle" {F} font-weight="900" font-size="{fs}" fill="#ffffff">{n}</text>'
    svg+=f'<text x="{x}" y="960" text-anchor="middle" {F} font-weight="700" font-size="{rs}" fill="#4a5568">{r1}</text>'
    svg+=f'<text x="{x}" y="1000" text-anchor="middle" {F} font-weight="700" font-size="{rs}" fill="#4a5568">{r2}</text>'
    svg+=f'<rect x="{x-140}" y="1050" width="280" height="150" rx="20" fill="{bg}"/>'
    parts=line.split("|")
    for i,t in enumerate(parts):
        y=1138-(len(parts)-1)*22+i*44
        svg+=f'<text x="{x}" y="{y}" text-anchor="middle" {F} font-weight="900" font-size="34" fill="{INK}">{t}</text>'
svg+=f'<text x="540" y="1318" text-anchor="middle" {F} font-weight="700" font-size="28" fill="#6b7280">나물려의 회사생활 · 나물려의 사랑 · 매일 1화</text>'
lib2._png(svg,1080,1350,"out/등장인물소개.png")
