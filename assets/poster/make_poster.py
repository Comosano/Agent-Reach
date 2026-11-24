import math, sys
W,H=1200,1600
ox,oy=600,1380
RX,RY=400,880
names=["Web","Exa","RSS","GitHub","YouTube","Bilibili","Xiaoyuzhou","Twitter","Reddit","V2EX","LinkedIn","Facebook","Instagram","Xiaohongshu","Xueqiu"]
n=len(names)
a0,a1=22,158
svg=[]
def pt(t,k=1.0,off=0.0):
    x,y=RX*k*math.cos(t),RY*k*math.sin(t)
    if off:
        L=math.hypot(x,y); x+=off*x/L; y+=off*y/L
    return ox+x,oy-y
for i in range(1,9):
    k=i/8
    svg.append(f'<path d="M{ox-RX*k},{oy} A{RX*k},{RY*k} 0 0 1 {ox+RX*k},{oy}" fill="none" stroke="#e9e4d8" stroke-opacity="{0.10 if k<1 else 0.28}" stroke-width="1"/>')
for d in range(0,181,3):
    t=math.radians(d); l=14 if d%15==0 else 6
    x1,y1=pt(t); x2,y2=pt(t,1,l)
    svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#e9e4d8" stroke-opacity="0.35" stroke-width="1"/>')
for i,nm in enumerate(names):
    d=a0+(a1-a0)*i/(n-1); t=math.radians(d)
    ex,ey=pt(t)
    svg.append(f'<line x1="{ox}" y1="{oy}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="#e9e4d8" stroke-opacity="0.45" stroke-width="1"/>')
    svg.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="6" fill="#0d1014" stroke="#e8b04a" stroke-width="1.5"/>')
    svg.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="2" fill="#e8b04a"/>')
    ang=math.degrees(math.atan2(oy-ey,ex-ox))
    lx,ly=pt(t,1,30)
    rot=-ang; anchor="start"
    if ang>90: rot=-ang+180; anchor="end"
    svg.append(f'<text transform="translate({lx:.1f},{ly:.1f}) rotate({rot:.1f})" text-anchor="{anchor}" dominant-baseline="middle" class="lab">{nm.upper()}</text>')
    nx,ny=pt(t,0.82)
    svg.append(f'<text transform="translate({nx:.1f},{ny:.1f}) rotate({-ang+(180 if ang>90 else 0):.1f})" text-anchor="middle" dominant-baseline="middle" class="num">{i+1:02d}</text>')
svg.append(f'<circle cx="{ox}" cy="{oy}" r="30" fill="none" stroke="#e8b04a" stroke-opacity="0.35"/>')
svg.append(f'<circle cx="{ox}" cy="{oy}" r="9" fill="#e8b04a"/>')
html=f'''<!doctype html><meta charset=utf-8><style>
html,body{{margin:0;background:#0d1014}}
.lab{{font:500 13px "JetBrains Mono",monospace;letter-spacing:.18em;fill:#e9e4d8}}
.num{{font:400 11px "JetBrains Mono",monospace;fill:#e9e4d8;fill-opacity:.35;letter-spacing:.1em}}
.t{{font:200 118px "Inter Display","Inter",sans-serif;fill:#e9e4d8;letter-spacing:-.02em}}
.s{{font:400 14px "JetBrains Mono",monospace;fill:#e9e4d8;fill-opacity:.55;letter-spacing:.22em}}
</style>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" fill="#0d1014"/>
<rect x="40" y="40" width="{W-80}" height="{H-80}" fill="none" stroke="#e9e4d8" stroke-opacity=".18"/>
<text x="90" y="170" class="t">Agent Reach</text>
<line x1="94" y1="206" x2="214" y2="206" stroke="#e8b04a" stroke-width="2"/>
<text x="94" y="244" class="s">ONE INSTALL · 15 PLATFORMS</text>
{''.join(svg)}
<text x="{ox}" y="{oy+70}" text-anchor="middle" class="s">agent-reach install</text>
<text x="90" y="{H-78}" class="s" fill-opacity=".35">READ · SEARCH · EVERYWHERE</text>
<text x="{W-90}" y="{H-78}" text-anchor="end" class="s" fill-opacity=".35">MIT</text>
</svg>'''
open("poster.html","w").write(html)
