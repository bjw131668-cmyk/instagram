import subprocess, make
S = make.SCENE
char = S[S.index("<!-- ===================== 환자"):S.index("<!-- ===================== 책상")]
open("char.svgfrag","w").write(char)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1080" viewBox="0 0 1080 1080">
<rect width="1080" height="1080" fill="#d6e6ff"/>
<polyline points="-20,170 150,250 260,215 400,400 520,360 660,600 780,560 930,820 1100,980" fill="none" stroke="#3b8cff" stroke-width="30" stroke-linejoin="round" opacity="0.45"/>
<g transform="translate(-605.5,-300) scale(1.45)">{char}</g>
</svg>'''
open("p.svg","w").write(svg)
subprocess.run(["rsvg-convert","-w","1080","-h","1080","p.svg","-o","out/나물려_프로필.png"],check=True)
