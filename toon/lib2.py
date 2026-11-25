# 4화부터: 계정 아이디 표시 + 다음 화 예고(아웃트로) 포함
import subprocess, os, make, lib
INK=lib.INK; OUT=lib.OUT; HANDLE="@namullyeo_toon"
F='font-family="Noto Sans CJK KR"'
def wm():  # 카드 가운데 벽면 워터마크
    return f'<text x="545" y="742" text-anchor="middle" {F} font-weight="900" font-size="26" fill="#1b1b22" opacity="0.42">{HANDLE}</text>'
def outro(ep_next, next_title):
    return f'''<rect width="1080" height="1350" fill="#d6e6ff"/>
<polyline points="-20,330 160,420 280,385 420,560 540,520 680,760 800,720 950,960 1100,1100" fill="none" stroke="#3b8cff" stroke-width="30" stroke-linejoin="round" opacity="0.4"/>
<text x="540" y="150" text-anchor="middle" {F} font-weight="900" font-size="46" fill="#35507a">다음 화 예고</text>
<text x="540" y="262" text-anchor="middle" {F} font-weight="900" font-size="92" fill="{INK}">{ep_next}화 {next_title}</text>
<g transform="translate(-250,160)">{lib.CHAR}</g>
<rect x="0" y="1100" width="1080" height="250" fill="#101726"/>
<text x="540" y="1196" text-anchor="middle" {F} font-weight="900" font-size="60" fill="#ffffff">팔로우하면 다음 화가 뜹니다</text>
<rect x="290" y="1228" width="500" height="80" rx="40" fill="#3b8cff"/>
<text x="540" y="1284" text-anchor="middle" {F} font-weight="900" font-size="44" fill="#ffffff">{HANDLE}</text>'''
def _png(inner,w,h,path):
    open("/tmp/x.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{inner}</svg>')
    subprocess.run(["rsvg-convert","-w",str(w),"-h",str(h),"/tmp/x.svg","-o",path],check=True)
def cards(scene,B,script,prefix,ep_next,next_title):
    res=[]
    for i,s in enumerate(script,1):
        p=f"{OUT}/{prefix}_{i:02d}.png"; _png(lib._svg(scene+wm(),B,s),1080,1350,p); res.append(p)
    p=f"{OUT}/{prefix}_{len(script)+1:02d}_다음화예고.png"; _png(outro(ep_next,next_title),1080,1350,p); res.append(p)
    return res
def _frame(title,ep,sub,inner):
    return f'''<rect width="1080" height="1920" fill="#101726"/>
<text x="540" y="190" text-anchor="middle" {F} font-weight="900" font-size="62" fill="#ffffff">{title}</text>
<text x="540" y="254" text-anchor="middle" {F} font-weight="700" font-size="36" fill="#6fa8ff">나물려 {ep}화 · {HANDLE}{sub}</text>
<svg x="0" y="290" width="1080" height="1350" viewBox="0 0 1080 1350">{inner}</svg>'''
def _enc(png,d,out):
    tmp=out.replace("/s_","/tmp_")
    subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate","30","-i",png,"-vf",f"format=yuv420p,loop=-1:1,trim=duration={d}","-c:v","libx264","-crf","18","-preset","veryfast","-pix_fmt","yuv420p",tmp],check=True)
    os.rename(tmp,out)
def reel(scene,B,script,title,prefix,ep,ep_next,next_title,dur=(0.8,1.1,0.9,1.7),last=2.2,end=2.4):
    D=f"/home/claude/toon/reel_{prefix}"; os.makedirs(D,exist_ok=True); lst=[]
    for i,s in enumerate(script):
        for n in range(1,5):
            p=f"{D}/f_{i:02d}_{n}.png"; _png(_frame(title,ep,"",lib._svg(scene,B,s,n)),1080,1920,p)
            o=f"{D}/s_{i:02d}_{n}.mp4"; _enc(p,last if (i==len(script)-1 and n==4) else dur[n-1],o); lst.append(o)
    p=f"{D}/f_end.png"; _png(_frame(title,ep,"",outro(ep_next,next_title)),1080,1920,p)
    o=f"{D}/s_end.mp4"; _enc(p,end,o); lst.append(o)
    open(f"{D}/list.txt","w").write("".join(f"file '{x}'\n" for x in lst))
    o=f"{OUT}/{prefix}_릴스.mp4"
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",f"{D}/list.txt","-c","copy","-movflags","+faststart",o],check=True)
    return o

def cover_svg(n,name,scene,s,B):
    b=[make.bubble(*B[2][:4],B[2][4],s[0]), make.bubble(*B[3][:4],B[3][4],s[1])]
    return f'''{scene}{wm()}
<rect width="1080" height="262" fill="#101726"/>
<rect x="40" y="38" width="200" height="64" rx="32" fill="#3b8cff"/>
<text x="140" y="84" text-anchor="middle" {F} font-weight="900" font-size="40" fill="#fff">{n}화</text>
<text x="262" y="84" {F} font-weight="900" font-size="38" fill="#6fa8ff">나물려 · {HANDLE}</text>
<text x="540" y="206" text-anchor="middle" {F} font-weight="900" font-size="{_fit('주식 중독자의 '+name,84,1000)}" fill="#ffffff">주식 중독자의 {name}</text>
{''.join(b)}'''
def covers(n,name,scene,s,B,prefix):
    c=cover_svg(n,name,scene,s,B)
    a=f"{OUT}/{prefix}_00_표지_게시물.png"; _png(c,1080,1350,a)
    r=f"{OUT}/{prefix}_릴스커버.png"; _png(f'<rect width="1080" height="1920" fill="#101726"/><svg x="0" y="285" width="1080" height="1350" viewBox="0 0 1080 1350">{c}</svg>',1080,1920,r)
    return a,r


def _fit(text, size, maxw):
    """글자 폭이 maxw를 넘지 않도록 글자 크기를 줄인다."""
    while size>40 and make.text_w(text,size)>maxw: size-=2
    return size
