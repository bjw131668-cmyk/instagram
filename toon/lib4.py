# 12화부터: 화 번호·시리즈 표시 없는 표지와 릴스 (제목 + 아이디만). 다음 화 예고 카드는 lib2.outro 그대로
import subprocess, os, make, lib, lib2
make.FIXED = 48  # 14화부터 말풍선 글씨 크기 통일(48px 고정, 넘치는 줄은 자동 줄바꿈, 최후에만 42px까지)
INK=lib.INK; OUT=lib.OUT; HANDLE=lib2.HANDLE; F=lib2.F
def cover_svg(name,scene,s,B):
    b=[make.bubble(*B[2][:4],B[2][4],s[0]), make.bubble(*B[3][:4],B[3][4],s[1])]
    t="주식 중독자의 "+name
    return f'''{scene}{lib2.wm()}
<rect width="1080" height="262" fill="#101726"/>
<text x="540" y="150" text-anchor="middle" {F} font-weight="900" font-size="{lib2._fit(t,92,1000)}" fill="#ffffff">{t}</text>
<text x="540" y="218" text-anchor="middle" {F} font-weight="700" font-size="34" fill="#6fa8ff">{HANDLE}</text>
{''.join(b)}'''
def covers(name,scene,s,B,prefix):
    c=cover_svg(name,scene,s,B)
    lib2._png(c,1080,1350,f"{OUT}/{prefix}_00_표지_게시물.png")
    lib2._png(f'<rect width="1080" height="1920" fill="#101726"/><svg x="0" y="285" width="1080" height="1350" viewBox="0 0 1080 1350">{c}</svg>',1080,1920,f"{OUT}/{prefix}_릴스커버.png")
def outro(ep_next,next_title):
    o=lib2.outro(ep_next,next_title)
    return o+f'''<rect x="190" y="980" width="700" height="84" rx="42" fill="#ffd66b" stroke="{INK}" stroke-width="6"/>
<text x="540" y="1036" text-anchor="middle" {F} font-weight="900" font-size="40" fill="{INK}">이런 친구 있으면 보내주세요</text>'''
def cards(scene,B,script,prefix,ep_next,next_title):
    res=[]
    for i,s in enumerate(script,1):
        p=f"{OUT}/{prefix}_{i:02d}.png"; lib2._png(lib._svg(scene+lib2.wm(),B,s),1080,1350,p); res.append(p)
    p=f"{OUT}/{prefix}_{len(script)+1:02d}_다음화예고.png"; lib2._png(outro(ep_next,next_title),1080,1350,p); res.append(p)
    return res
def _frame(title,inner):
    return f'''<rect width="1080" height="1920" fill="#101726"/>
<text x="540" y="190" text-anchor="middle" {F} font-weight="900" font-size="{lib2._fit(title,62,1000)}" fill="#ffffff">{title}</text>
<text x="540" y="254" text-anchor="middle" {F} font-weight="700" font-size="36" fill="#6fa8ff">{HANDLE}</text>
<svg x="0" y="290" width="1080" height="1350" viewBox="0 0 1080 1350">{inner}</svg>'''
def reel(scene,B,script,title,prefix,next_n,next_title,dur=(0.8,1.1,0.9,1.7),last=3.2,end=2.4):
    D=f"/home/claude/toon/reel_{prefix}"; os.makedirs(D,exist_ok=True); lst=[]
    for i,s in enumerate(script):
        for n in range(1,5):
            if i==0 and n==1: continue  # 13화부터: 첫 화면에 질문+펀치를 함께 (첫 1초 훅)
            p=f"{D}/f_{i:02d}_{n}.png"; lib2._png(_frame(title,lib._svg(scene,B,s,n)),1080,1920,p)
            d=last if (i==len(script)-1 and n==4) else dur[n-1]
            if i==0 and n==2: d=dur[0]+dur[1]
            o=f"{D}/s_{i:02d}_{n}.mp4"; lib2._enc(p,d,o); lst.append(o)
    p=f"{D}/f_end.png"; lib2._png(_frame(title,outro(next_n,next_title)),1080,1920,p)
    o=f"{D}/s_end.mp4"; lib2._enc(p,end,o); lst.append(o)
    open(f"{D}/list.txt","w").write("".join(f"file '{x}'\n" for x in lst))
    out=f"{OUT}/{prefix}_릴스.mp4"
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",f"{D}/list.txt","-c","copy","-movflags","+faststart",out],check=True)
    return out
