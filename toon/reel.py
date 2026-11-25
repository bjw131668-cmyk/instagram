import subprocess, os, sys, make
W,H=1080,1920
D="/home/claude/toon/reel"; os.makedirs(D,exist_ok=True)
DUR=[0.8,1.1,0.9,1.7]
def frame(i,n):
    s=make.SCRIPT[i]
    card=[make.SCENE]+[make.bubble(cx,cy,rx,ry,t,txt) for (cx,cy,rx,ry,t),txt in list(zip(make.B,s))[:n]]
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" fill="#101726"/>
<text x="540" y="205" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="64" fill="#ffffff">주식 중독자의 건강검진</text>
<text x="540" y="262" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="700" font-size="34" fill="#6fa8ff">{i+1} / {len(make.SCRIPT)}</text>
<svg x="0" y="290" width="1080" height="1350" viewBox="0 0 1080 1350">{''.join(card)}</svg>
</svg>'''
    p=f"{D}/f_{i:02d}_{n}"
    open(p+".svg","w").write(svg)
    subprocess.run(["rsvg-convert","-w",str(W),"-h",str(H),p+".svg","-o",p+".png"],check=True)
    return p+".png"
if sys.argv[1]=="test":
    print(frame(6,4))
else:
    lst=[]
    for i in range(len(make.SCRIPT)):
        for n in range(1,5):
            png=frame(i,n); d=DUR[n-1]
            if i==len(make.SCRIPT)-1 and n==4: d=2.6
            tmp=f"{D}/tmp_{i:02d}_{n}.mp4"; out=f"{D}/s_{i:02d}_{n}.mp4"
            subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate","30","-i",png,"-vf",f"format=yuv420p,loop=-1:1,trim=duration={d}","-c:v","libx264","-crf","18","-preset","veryfast","-pix_fmt","yuv420p",tmp],check=True)
            os.rename(tmp,out); lst.append(out)
    open(f"{D}/list.txt","w").write("".join(f"file '{x}'\n" for x in lst))
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",f"{D}/list.txt","-c","copy","-movflags","+faststart","/home/claude/toon/out/주식중독자_건강검진_릴스.mp4"],check=True)
