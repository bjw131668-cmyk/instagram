# 9화부터: 시리즈 표시 + 릴스 상단 팔로우 띠 + 표지 부제
import subprocess, os, make, lib, lib2
INK=lib.INK; F=lib2.F; OUT=lib.OUT; HANDLE=lib2.HANDLE
def cover_svg(n,name,scene,s,B,label,sub=None):
    b=[make.bubble(*B[2][:4],B[2][4],s[0]), make.bubble(*B[3][:4],B[3][4],s[1])]
    t="주식 중독자의 "+name
    ty,ts=(186,lib2._fit(t,76,1000)) if sub else (206,lib2._fit(t,84,1000))
    subt=f'<text x="540" y="244" text-anchor="middle" {F} font-weight="900" font-size="32" fill="#ffb347">{sub}</text>' if sub else ""
    return f'''{scene}{lib2.wm()}
<rect width="1080" height="262" fill="#101726"/>
<rect x="40" y="38" width="200" height="64" rx="32" fill="#3b8cff"/>
<text x="140" y="84" text-anchor="middle" {F} font-weight="900" font-size="40" fill="#fff">{n}화</text>
<text x="262" y="84" {F} font-weight="900" font-size="{lib2._fit(label+' · '+HANDLE,38,780)}" fill="#6fa8ff">{label} · {HANDLE}</text>
<text x="540" y="{ty}" text-anchor="middle" {F} font-weight="900" font-size="{ts}" fill="#ffffff">{t}</text>{subt}
{''.join(b)}'''
def covers(n,name,scene,s,B,prefix,label,sub=None):
    c=cover_svg(n,name,scene,s,B,label,sub)
    lib2._png(c,1080,1350,f"{OUT}/{prefix}_00_표지_게시물.png")
    lib2._png(f'<rect width="1080" height="1920" fill="#101726"/><svg x="0" y="285" width="1080" height="1350" viewBox="0 0 1080 1350">{c}</svg>',1080,1920,f"{OUT}/{prefix}_릴스커버.png")
K=0.95
def _frame(title,ep,label,inner):
    pill="팔로우하고 다음 화 보기 · "+HANDLE
    return f'''<rect width="1080" height="1920" fill="#101726"/>
<text x="540" y="168" text-anchor="middle" {F} font-weight="900" font-size="{lib2._fit(title,60,1000)}" fill="#ffffff">{title}</text>
<text x="540" y="218" text-anchor="middle" {F} font-weight="700" font-size="32" fill="#6fa8ff">나물려 {ep}화 · {label}</text>
<rect x="190" y="238" width="700" height="58" rx="29" fill="#ffd66b"/>
<text x="540" y="278" text-anchor="middle" {F} font-weight="900" font-size="30" fill="{INK}">{pill}</text>
<svg x="{(1080-1080*K)/2}" y="318" width="{1080*K}" height="{1350*K}" viewBox="0 0 1080 1350">{inner}</svg>'''
def _enc(png,d,out):
    tmp=out.replace("/s_","/tmp_")
    subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate","30","-i",png,"-vf",f"format=yuv420p,loop=-1:1,trim=duration={d}","-c:v","libx264","-crf","18","-preset","veryfast","-pix_fmt","yuv420p",tmp],check=True)
    os.rename(tmp,out)
def reel(scene,B,script,title,prefix,ep,label,next_n,next_title,dur=(0.8,1.1,0.9,1.7),last=2.6,end=2.4):
    D=f"/home/claude/toon/reel_{prefix}"; os.makedirs(D,exist_ok=True); lst=[]
    for i,s in enumerate(script):
        for n in range(1,5):
            p=f"{D}/f_{i:02d}_{n}.png"; lib2._png(_frame(title,ep,label,lib._svg(scene,B,s,n)),1080,1920,p)
            o=f"{D}/s_{i:02d}_{n}.mp4"; _enc(p,last if (i==len(script)-1 and n==4) else dur[n-1],o); lst.append(o)
    p=f"{D}/f_end.png"; lib2._png(_frame(title,ep,label,lib2.outro(next_n,next_title)),1080,1920,p)
    o=f"{D}/s_end.mp4"; _enc(p,end,o); lst.append(o)
    open(f"{D}/list.txt","w").write("".join(f"file '{x}'\n" for x in lst))
    out=f"{OUT}/{prefix}_릴스.mp4"
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",f"{D}/list.txt","-c","copy","-movflags","+faststart",out],check=True)
    return out
