import subprocess, os, make
INK=make.INK; W,H=1080,1350
S=make.SCENE
CHAR=S[S.index("<!-- ===================== 환자"):S.index("<!-- ===================== 책상")]
PHONE='''<g transform="rotate(8 880 930)" stroke="#1b1b22" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
  <rect x="812" y="838" width="136" height="200" rx="18" fill="#22252c"/>
  <rect x="824" y="852" width="112" height="172" rx="8" fill="#0f1a2b"/>
  <text x="880" y="884" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="28" fill="#3b8cff" stroke="none">-50%</text>
  <polyline points="832,900 850,908 864,904 882,926 898,920 914,946 928,968" fill="none" stroke="#3b8cff" stroke-width="7"/>
  <path d="M932,978 L918,962 L938,958 Z" fill="#3b8cff" stroke="none"/>
</g>'''
OUT="/home/claude/toon/out"
def _svg(scene,B,s,n=4):
    return "".join([scene]+[make.bubble(cx,cy,rx,ry,t,txt) for (cx,cy,rx,ry,t),txt in list(zip(B,s))[:n]])
def cards(scene,B,script,prefix):
    res=[]
    for i,s in enumerate(script,1):
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{_svg(scene,B,s)}</svg>'
        open("/tmp/c.svg","w").write(svg); png=f"{OUT}/{prefix}_{i:02d}.png"
        subprocess.run(["rsvg-convert","-w",str(W),"-h",str(H),"/tmp/c.svg","-o",png],check=True); res.append(png)
    return res
def reel(scene,B,script,title,prefix,dur=(0.8,1.1,0.9,1.7),last=2.6):
    D=f"/home/claude/toon/reel_{prefix}"; os.makedirs(D,exist_ok=True); lst=[]
    for i,s in enumerate(script):
        for n in range(1,5):
            svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">
<rect width="1080" height="1920" fill="#101726"/>
<text x="540" y="205" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="64" fill="#ffffff">{title}</text>
<text x="540" y="262" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="700" font-size="34" fill="#6fa8ff">{i+1} / {len(script)}</text>
<svg x="0" y="290" width="1080" height="1350" viewBox="0 0 1080 1350">{_svg(scene,B,s,n)}</svg></svg>'''
            p=f"{D}/f_{i:02d}_{n}"; open(p+".svg","w").write(svg)
            subprocess.run(["rsvg-convert","-w","1080","-h","1920",p+".svg","-o",p+".png"],check=True)
            d=last if (i==len(script)-1 and n==4) else dur[n-1]
            tmp=f"{D}/tmp_{i:02d}_{n}.mp4"; out=f"{D}/s_{i:02d}_{n}.mp4"
            subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate","30","-i",p+".png","-vf",f"format=yuv420p,loop=-1:1,trim=duration={d}","-c:v","libx264","-crf","18","-preset","veryfast","-pix_fmt","yuv420p",tmp],check=True)
            os.rename(tmp,out); lst.append(out)
    open(f"{D}/list.txt","w").write("".join(f"file '{x}'\n" for x in lst))
    o=f"{OUT}/{prefix}_릴스.mp4"
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",f"{D}/list.txt","-c","copy","-movflags","+faststart",o],check=True)
    return o


def hand(cx, cy, flip=False, rot=0, skin="#f4cfae", scale=1.0):
    """손가락 5개가 보이는 손(물건을 쥔 자세). 손가락 4개가 위쪽으로 물건을 감싸고, 엄지는 안쪽(flip=False면 왼쪽)에 붙는다.
    cx,cy = 손바닥 중심. 쥐고 있는 물건보다 나중에 그려 손가락이 물건 앞면을 덮게 한다."""
    sx = -1 if flip else 1
    return f'''<g transform="translate({cx},{cy}) rotate({rot}) scale({sx*scale},{scale})" stroke="{INK}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" fill="{skin}">
  <ellipse cx="-37" cy="4" rx="11" ry="19" transform="rotate(-38 -37 4)"/>
  <rect x="-33" y="-10" width="66" height="42" rx="18"/>
  <rect x="-32" y="-25" width="16" height="32" rx="8"/>
  <rect x="-16" y="-30" width="16" height="36" rx="8"/>
  <rect x="0" y="-29" width="16" height="35" rx="8"/>
  <rect x="16" y="-23" width="16" height="30" rx="8"/>
  <rect x="-30" y="-3" width="60" height="28" rx="12" stroke="none"/>
  <path d="M-24,-2 L-24,2 M-8,-4 L-8,2 M8,-4 L8,2 M24,-2 L24,2" stroke-width="3" fill="none" opacity="0.45"/>
</g>'''


def cuff(cx, cy, rot=0, color="#747987", w=22, h=66):
    """소매 끝단. 손을 그린 뒤 손목 위에 덮어 팔과 손이 이어져 보이게 한다."""
    return f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="9" fill="{color}" stroke="{INK}" stroke-width="6" transform="rotate({rot} {cx} {cy})"/>'

# 나물려 기본 자세: 테이블 위에 올린 두 팔뚝 + 휴대폰 + 마주 보는 두 손(손가락이 안쪽을 향함) + 소매 끝단
NMR_FRONT = f'''<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
  <path d="M592,1016 C594,966 664,948 776,962 L776,1024 L592,1024 Z" fill="#8a8f9c"/>
  <path d="M1076,1022 C1074,974 1044,960 990,972 L990,1032 L1076,1032 Z" fill="#8a8f9c"/>
</g>
{PHONE}
{hand(806,992,flip=False,rot=90)}
{hand(958,1001,flip=True,rot=-90)}
{cuff(776,993,rot=2)}
{cuff(990,1002,rot=-4)}'''


# 6화부터 쓰는 말풍선 위치: 아래 말풍선 꼬리를 짧게 해서 손과 소품을 가리지 않는다
B2 = [make.B[0], make.B[1],
      (272, 1184, 250, 144, (330, 400, 1062, 410, 1026)),
      (808, 1184, 250, 144, (680, 750, 1062, 670, 1026))]  # 좌하 꼬리를 좌우 대칭한 모양
