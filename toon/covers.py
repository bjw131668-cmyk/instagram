import sys, os
sys.argv=["x","test"]
import make, lib, lib2, ep2, ep3, ep4
for f in ("out/t2_01.png","out/t3_01.png"):
    if os.path.exists(f): os.remove(f)
F=lib2.F; B=make.B
EPS=[(1,"건강검진",make.SCENE,make.SCRIPT[0]),(2,"면접",ep2.SCENE.replace('<ellipse cx="720" cy="1000" rx="34" ry="26" fill="#f4cfae"/>',""),ep2.SCRIPT[0]),(3,"소개팅",ep3.SCENE,ep3.SCRIPT[0]),(4,"팀장 면담",ep4.SCENE,ep4.SCRIPT[0])]
def cover(n,name,scene,s):
    b=[make.bubble(*B[2][:4],B[2][4],s[0]), make.bubble(*B[3][:4],B[3][4],s[1])]
    return f'''{scene}{lib2.wm()}
<rect width="1080" height="262" fill="#101726"/>
<rect x="40" y="38" width="200" height="64" rx="32" fill="#3b8cff"/>
<text x="140" y="84" text-anchor="middle" {F} font-weight="900" font-size="40" fill="#fff">{n}화</text>
<text x="262" y="84" {F} font-weight="900" font-size="38" fill="#6fa8ff">나물려 · {lib2.HANDLE}</text>
<text x="540" y="206" text-anchor="middle" {F} font-weight="900" font-size="84" fill="#ffffff">주식 중독자의 {name}</text>
{''.join(b)}'''
for n,name,scene,s in EPS:
    c=cover(n,name,scene,s); nm=name.replace(" ","")
    lib2._png(c,1080,1350,f"out/표지_{n:02d}화_{nm}_게시물.png")
    lib2._png(f'<rect width="1080" height="1920" fill="#101726"/><svg x="0" y="285" width="1080" height="1350" viewBox="0 0 1080 1350">{c}</svg>',1080,1920,f"out/표지_{n:02d}화_{nm}_릴스.png")
