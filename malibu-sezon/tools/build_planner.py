import math, subprocess
P="/home/user/pixonis/malibu-sezon"
NAVY="#29314b"; SALMON="#e1a8a4"; KRAFT="#d8b38a"
R=1.35  # frame 0 shows the finished page; it rewinds at R
# ---------------- desk props (vector, flat illustration with soft shadows)
def pine(x0,y0,x1,y1,cx,cy,flip=1,n=26):
    s=[f'<path d="M{x0} {y0} Q{cx} {cy} {x1} {y1}" fill="none" stroke="#6b4a2b" stroke-width="7" stroke-linecap="round"/>']
    for i in range(1,n):
        t=i/n; bx=(1-t)**2*x0+2*(1-t)*t*cx+t*t*x1; by=(1-t)**2*y0+2*(1-t)*t*cy+t*t*y1
        dx=2*(1-t)*(cx-x0)+2*t*(x1-cx); dy=2*(1-t)*(cy-y0)+2*t*(y1-cy); a=math.atan2(dy,dx)
        L=58-30*t
        for side,col in ((1,"#2f7d4f"),(-1,"#3e9e5f")):
            for off in (0.75,1.1):
                ang=a+side*off
                s.append(f'<line x1="{bx:.1f}" y1="{by:.1f}" x2="{bx+L*math.cos(ang):.1f}" y2="{by+L*math.sin(ang):.1f}" stroke="{col}" stroke-width="6" stroke-linecap="round"/>')
    return "".join(s)
def ornament(cx,cy,r,col):
    return (f'<line x1="{cx}" y1="{cy-r-14}" x2="{cx}" y2="{cy-r-60}" stroke="#c9a227" stroke-width="3"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}"/><circle cx="{cx-r*0.35}" cy="{cy-r*0.35}" r="{r*0.28}" fill="#fff" opacity="0.35"/>'
            f'<rect x="{cx-r*0.3}" y="{cy-r-16}" width="{r*0.6}" height="18" rx="4" fill="#d4af37"/>')
def orange(cx,cy,r):
    seg="".join(f'<line x1="{cx}" y1="{cy}" x2="{cx+(r-12)*math.cos(math.radians(a)):.1f}" y2="{cy+(r-12)*math.sin(math.radians(a)):.1f}" stroke="#fde0b0" stroke-width="4"/>' for a in range(0,360,40))
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#d9661a"/><circle cx="{cx}" cy="{cy}" r="{r-8}" fill="#f39c33"/>{seg}<circle cx="{cx}" cy="{cy}" r="7" fill="#fde0b0"/>'
def mug(cx,cy):
    m="".join(f'<rect x="{cx+dx}" y="{cy+dy}" width="30" height="30" rx="7" fill="#fffaf2" transform="rotate({rot} {cx+dx+15} {cy+dy+15})"/>' for dx,dy,rot in [(-50,-30,12),(-5,-55,-8),(20,0,20),(-35,15,-15),(-70,-5,5)])
    return (f'<rect x="{cx+95}" y="{cy-28}" width="90" height="56" rx="28" fill="#f2b8bd"/>'
            f'<circle cx="{cx}" cy="{cy}" r="122" fill="#f6c7cb"/><circle cx="{cx}" cy="{cy}" r="100" fill="#7a4b33"/><circle cx="{cx-18}" cy="{cy-18}" r="64" fill="#8d5a3e"/>{m}')
def gift(x,y,w):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{w}" rx="12" fill="#d9534f"/><rect x="{x+w/2-16}" y="{y}" width="32" height="{w}" fill="#f2c14e"/>'
            f'<rect x="{x}" y="{y+w/2-16}" width="{w}" height="32" fill="#f2c14e"/>'
            f'<ellipse cx="{x+w/2-34}" cy="{y+w/2-10}" rx="38" ry="22" fill="#f2c14e" transform="rotate(-25 {x+w/2-34} {y+w/2-10})"/>'
            f'<ellipse cx="{x+w/2+34}" cy="{y+w/2-10}" rx="38" ry="22" fill="#f2c14e" transform="rotate(25 {x+w/2+34} {y+w/2-10})"/><circle cx="{x+w/2}" cy="{y+w/2}" r="20" fill="#e0a92e"/>')
def cinnamon(x,y):
    out=""
    for i,dy in enumerate((0,30,60)):
        out+=f'<rect x="{x}" y="{y+dy}" width="220" height="30" rx="15" fill="#9c5a2b"/><path d="M{x+10} {y+dy+15} H{x+210}" stroke="#7a4220" stroke-width="3"/>'
    return out+f'<rect x="{x+95}" y="{y-8}" width="18" height="106" rx="4" fill="#d8c3a0"/>'
def pen(x,y,h,rot):
    return (f'<g transform="rotate({rot} {x} {y})"><rect x="{x-14}" y="{y}" width="28" height="{h}" rx="12" fill="#b9a7ec"/>'
            f'<rect x="{x-14}" y="{y+h-70}" width="28" height="14" fill="#d4af37"/><polygon points="{x-14},{y+h-4} {x+14},{y+h-4} {x},{y+h+40}" fill="#f6e3c5"/>'
            f'<polygon points="{x-5},{y+h+26} {x+5},{y+h+26} {x},{y+h+40}" fill="{NAVY}"/></g>')
props=(f'<svg class="pl-props" viewBox="0 0 1080 1920" width="1080" height="1920" data-layout-ignore>'
       f'<g filter="url(#pl-sh)">{pine(-40,150,340,30,120,30)}{ornament(330,150,40,"#c0392b")}{ornament(205,230,30,"#d4af37")}'
       f'{orange(1000,300,62)}{mug(1060,760)}{pen(70,600,500,7)}{gift(40,1560,240)}{cinnamon(330,1720)}'
       f'{pine(1130,1640,720,1830,950,1600)}{ornament(840,1690,44,"#c0392b")}{orange(140,1430,56)}{ornament(990,1520,32,"#d4af37")}</g>'
       f'<defs><filter id="pl-sh" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="0" dy="8" stdDeviation="7" flood-color="#3a2410" flood-opacity="0.28"/></filter></defs></svg>')

# ---------------- planner page content (page-local coords, page 720 x 1010)
DAYS=["Pt","Sa","Ça","Pe","Cu","Ct","Pz"]
cal_cells=[]
for i,d in enumerate(DAYS):
    cal_cells.append(f'<div class="pl-cd pl-ch" style="left:{12+i*48}px;top:12px">{d}</div>')
for day in range(1,32):
    idx=4+day-1; r=idx//7; c=idx%7
    cal_cells.append(f'<div class="pl-cd pl-cn" style="left:{12+c*48}px;top:{60+r*46}px">{day}</div>')
cal="".join(cal_cells)
GOALS=["Daha çok kitap okumak","Yeni bir hobi edinmek","Kendime zaman ayırmak","Bol bol gezmek"]
goals="".join(f'<div class="pl-goal" id="pl-g{i}" style="top:{600+i*62}px"><span class="pl-box"></span>{g}</div>' for i,g in enumerate(GOALS))
STK=[("lav-dahlia",40,185,190,-8),("jj-camera",95,382,170,6),("jj-orange",592,34,108,10),("disco-heart",560,515,130,-10),
     ("jj-envelope",542,655,160,-4),("jj-heart",582,812,115,8),("vg-starry",36,852,200,-5),("jj-cute",262,878,230,4)]
def sticker(name,x,y,w,rot):
    return f'<img id="pl-s-{name}" class="pl-stk" src="assets/stickers/{name}.png" alt="" style="left:{x}px;top:{y}px;width:{w}px;transform-origin:50% 50%" data-rot="{rot}" />'
stickers="".join(sticker(*s) for s in STK)

# ---------------- timeline
js=[]; J=js.append
J('// frame 0 = the finished page (result first); at 0.9 it rewinds to a blank page, then builds up again')
for name,x,y,w,rot in STK:
    J(f'tl.set("#pl-s-{name}", {{ rotation: {rot} }}, 0);')
# rewind (0.9-1.45)
for i,(name,x,y,w,rot) in enumerate(STK):
    J(f'tl.to("#pl-s-{name}", {{ y: -900, x: {(i%2*2-1)*240}, rotation: {rot+(i%2*2-1)*40}, opacity: 0, duration: 0.32, ease: "power3.in" }}, {R+i*0.025:.3f});')
J('tl.to("#pl-shine", { x: 1240, duration: 0.9, ease: "power1.inOut" }, 0.15);')
J('tl.set("#pl-shine", { x: 0 }, 1.2);')
J(f'tl.to(["#pl-head", "#pl-gtitle", ".pl-goal"], {{ clipPath: "inset(0px 100% 0px 0px)", duration: 0.25, ease: "power2.in" }}, {R+0.05:.2f});')
J(f'tl.to(["#pl-cal", "#pl-wt1", "#pl-wt2"], {{ opacity: 0, duration: 0.2, ease: "power1.in" }}, {R+0.05:.2f});')
J(f'tl.to("#pl-title1", {{ opacity: 0, scale: 0.9, duration: 0.2, ease: "power2.in" }}, {R+0.3:.2f});')
# build-up
t=R+0.7; steps=[]
J(f'tl.fromTo("#pl-wt1", {{ opacity: 1, scaleX: 0 }}, {{ opacity: 1, scaleX: 1, duration: 0.28, ease: "power2.out", immediateRender: false }}, {t});'); steps.append(("tape",t)); t+=0.7
J(f'tl.fromTo("#pl-head", {{ clipPath: "inset(0px 100% 0px 0px)" }}, {{ clipPath: "inset(0px 0% 0px 0px)", duration: 0.75, ease: "power1.inOut", immediateRender: false }}, {t});'); steps.append(("write",t)); t+=0.85
J(f'tl.fromTo("#pl-cal", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, immediateRender: false }}, {t});')
J(f'tl.fromTo("#pl-cal .pl-cd", {{ opacity: 0, scale: 0.4 }}, {{ opacity: 1, scale: 1, duration: 0.14, stagger: 0.012, ease: "back.out(2)", immediateRender: false }}, {t+0.05:.2f});'); steps.append(("cal",t)); t+=0.75
order=["lav-dahlia","jj-camera","jj-orange"]
def place(name,t):
    s=[x for x in STK if x[0]==name][0]; rot=s[4]
    J(f'tl.fromTo("#pl-s-{name}", {{ x: 0, y: 260, scale: 1.3, rotation: {rot+16}, opacity: 1, filter: "drop-shadow(0px 30px 22px rgba(0,0,0,0.35))" }}, '
      f'{{ x: 0, y: 0, scale: 1, rotation: {rot}, opacity: 1, filter: "drop-shadow(0px 4px 4px rgba(0,0,0,0.25))", duration: 0.26, ease: "power3.in", immediateRender: false }}, {t:.2f});')
    J(f'tl.to("#pl-s-{name}", {{ scale: 0.96, duration: 0.04, ease: "none" }}, {t+0.26:.2f});')
    J(f'tl.to("#pl-s-{name}", {{ scale: 1, duration: 0.12, ease: "power2.out" }}, {t+0.3:.2f});')
    steps.append(("stk",t+0.26))
for n in order: place(n,t); t+=0.7
J(f'tl.fromTo("#pl-gtitle", {{ clipPath: "inset(0px 100% 0px 0px)" }}, {{ clipPath: "inset(0px 0% 0px 0px)", duration: 0.6, ease: "power1.inOut", immediateRender: false }}, {t:.2f});'); steps.append(("write",t)); t+=0.6
for i in range(len(GOALS)):
    J(f'tl.fromTo("#pl-g{i}", {{ clipPath: "inset(0px 100% 0px 0px)" }}, {{ clipPath: "inset(0px 0% 0px 0px)", duration: 0.45, ease: "power1.inOut", immediateRender: false }}, {t+i*0.32:.2f});')
t+=len(GOALS)*0.32+0.25
for n in ["disco-heart","jj-envelope","jj-heart","vg-starry","jj-cute"]: place(n,t); t+=0.62
J(f'tl.fromTo("#pl-wt2", {{ opacity: 1, scaleX: 0 }}, {{ opacity: 1, scaleX: 1, duration: 0.28, ease: "power2.out", immediateRender: false }}, {t:.2f});'); steps.append(("tape",t)); t+=0.5
DONE=round(t,2)
# finished: shine across the page + title
J(f'tl.to("#pl-shine", {{ x: 1240, duration: 0.9, ease: "power1.inOut" }}, {DONE:.2f});')
J(f'tl.fromTo("#pl-title2", {{ scale: 1.35, rotation: 6, opacity: 0 }}, {{ scale: 1, rotation: -3, opacity: 1, duration: 0.24, ease: "power3.in" }}, {DONE+0.1:.2f});')
J(f'tl.to("#pl-title2", {{ scale: 0.97, duration: 0.04, ease: "none" }}, {DONE+0.34:.2f});')
J(f'tl.to("#pl-title2", {{ scale: 1, duration: 0.12, ease: "power2.out" }}, {DONE+0.38:.2f});')
END0=round(DONE+2.2,2); TOTAL=round(END0+5.3,1)
J(f'tl.to("#pl-title2", {{ opacity: 0, scale: 0.9, duration: 0.18, ease: "power2.in" }}, {END0-0.5:.2f});')
# the finished page is swept off the desk, then the brand card is slapped on like a big sticker
J(f'tl.to("#pl-move", {{ y: 2150, rotation: 9, duration: 0.45, ease: "power3.in" }}, {END0-0.5:.2f});')
J(f'tl.fromTo("#pl-card", {{ scale: 1.3, rotation: 6, opacity: 0 }}, {{ scale: 1, rotation: -2, opacity: 1, duration: 0.26, ease: "power3.in", immediateRender: false }}, {END0:.2f});')
J(f'tl.to("#pl-card", {{ scale: 0.975, duration: 0.04, ease: "none" }}, {END0+0.26:.2f});')
J(f'tl.to("#pl-card", {{ scale: 1, duration: 0.14, ease: "power2.out" }}, {END0+0.3:.2f});')
J(f'tl.fromTo("#pl-mark", {{ scale: 1.4, rotation: 6, opacity: 0 }}, {{ scale: 1, rotation: -3, opacity: 1, duration: 0.22, ease: "power3.in" }}, {END0+0.5:.2f});')
J(f'tl.fromTo("#pl-card .pl-line", {{ opacity: 0, y: 0, filter: "blur(6px)" }}, {{ opacity: 1, filter: "blur(0px)", duration: 0.18, stagger: 0.18, ease: "power2.out" }}, {END0+0.75:.2f});')
ENDSTK=[("lav-bunch",120,1150,210,-8),("vg-portrait",440,1170,190,5),("red-heart",735,1150,210,-6)]
for i,(n,x,y,w,rot) in enumerate(ENDSTK):
    tt=END0+1.35+i*0.25
    J(f'tl.fromTo("#pl-e{i}", {{ scale: 1.4, rotation: {rot+9}, opacity: 0 }}, {{ scale: 1, rotation: {rot}, opacity: 1, duration: 0.2, ease: "power3.in", immediateRender: false }}, {tt:.2f});')
    J(f'tl.to("#pl-e{i}", {{ scale: 0.97, duration: 0.04, ease: "none" }}, {tt+0.2:.2f});')
    J(f'tl.to("#pl-e{i}", {{ scale: 1, duration: 0.12, ease: "power2.out" }}, {tt+0.24:.2f});')
    steps.append(("end",tt+0.2))
endstk="".join(f'<img id="pl-e{i}" class="pl-stk" src="assets/stickers/{n}.png" alt="" style="left:{x}px;top:{y}px;width:{w}px;opacity:0" data-layout-ignore />' for i,(n,x,y,w,rot) in enumerate(ENDSTK))
js="\n    ".join(js)

html=f'''<template>
  <style>
    @font-face {{ font-family: "Caveat"; src: url("assets/fonts/Caveat.ttf") format("truetype"); font-weight: 400 700; }}
    #root {{ position: absolute; inset: 0; overflow: hidden; font-family: "Nunito", sans-serif; color: {NAVY}; }}
    .pl-slot {{ position: absolute; inset: 0; }}
    .pl-desk {{ position: absolute; inset: 0;
      background:
        url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='540' height='540'><filter id='g'><feTurbulence type='fractalNoise' baseFrequency='0.003 0.09' numOctaves='3' seed='4'/><feColorMatrix values='0 0 0 0 0.35  0 0 0 0 0.2  0 0 0 0 0.08  0 0 0 0.16 0'/></filter><rect width='540' height='540' filter='url(%23g)'/></svg>"),
        repeating-linear-gradient(90deg, rgba(90,52,22,0.10) 0px, rgba(90,52,22,0.10) 3px, transparent 3px, transparent 270px),
        linear-gradient(180deg, #e8c294 0%, #ddb07c 55%, #d3a26d 100%); }}
    .pl-props {{ position: absolute; left: 0; top: 0; }}
    #pl-page {{ position: absolute; left: 180px; top: 300px; width: 720px; height: 1010px; transform: rotate(-2.5deg); transform-origin: 50% 50%; }}
    .pl-paper {{ position: absolute; inset: 0; border-radius: 10px; background-color: #fffdf6;
      background-image: radial-gradient(circle, #d9cfc0 2.2px, transparent 2.6px); background-size: 30px 30px; background-position: 15px 15px;
      box-shadow: 0 22px 34px rgba(58,36,16,0.32), 0 2px 0 rgba(0,0,0,0.05); }}
    .pl-ring {{ position: absolute; left: -16px; width: 34px; height: 18px; border-radius: 9px; border: 5px solid #8f97a8; background: transparent; }}
    .pl-hand {{ font-family: "Caveat", cursive; font-weight: 700; }}
    #pl-head {{ position: absolute; left: 52px; top: 6px; padding: 24px 44px 34px 0; font-size: 128px; line-height: 1; white-space: nowrap; }}
    #pl-cal {{ position: absolute; left: 318px; top: 190px; width: 360px; height: 300px; border-radius: 16px; border: 4px dashed {SALMON}; }}
    .pl-cd {{ position: absolute; width: 40px; text-align: center; font-family: "Caveat", cursive; font-weight: 700; line-height: 40px; }}
    .pl-ch {{ font-size: 30px; color: #b06a64; }}
    .pl-cn {{ font-size: 32px; color: {NAVY}; }}
    #pl-gtitle {{ position: absolute; left: 60px; top: 502px; padding: 18px 34px 20px 0; font-size: 64px; line-height: 1; color: #b06a64; white-space: nowrap; }}
    .pl-goal {{ position: absolute; left: 66px; margin-top: -16px; padding: 16px 34px 16px 0; font-family: "Caveat", cursive; font-weight: 700; font-size: 46px; line-height: 50px; white-space: nowrap; }}
    .pl-box {{ display: inline-block; width: 28px; height: 28px; margin-right: 14px; border: 4px solid {NAVY}; border-radius: 6px; vertical-align: -2px; }}
    .pl-stk {{ position: absolute; filter: drop-shadow(0px 4px 4px rgba(0,0,0,0.25)); }}
    .pl-washi {{ position: absolute; height: 58px; opacity: 0.9; transform-origin: 0% 50%;
      clip-path: polygon(0% 8%, 4% 0%, 8% 10%, 12% 0%, 100% 0%, 97% 50%, 100% 100%, 12% 100%, 8% 90%, 4% 100%, 0% 92%, 3% 50%); }}
    #pl-shine-wrap {{ position: absolute; inset: 0; overflow: hidden; border-radius: 10px; pointer-events: none; }}
    #pl-shine {{ position: absolute; top: -20%; left: -40%; width: 32%; height: 140%;
      background: linear-gradient(100deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.55) 50%, rgba(255,255,255,0) 100%); }}
    .pl-label {{ position: absolute; padding: 16px 30px 20px; background: {KRAFT}; border: 10px solid #ffffff; border-radius: 18px;
      box-shadow: 0 8px 12px rgba(0,0,0,0.22); font-weight: 900; line-height: 1; white-space: nowrap; }}
    #pl-card {{ position: absolute; left: 110px; top: 540px; opacity: 0; width: 860px; padding: 46px 40px 50px; border-radius: 34px; background: #fffaf0;
      border: 14px solid #ffffff; box-shadow: 0 22px 40px rgba(0,0,0,0.35); text-align: center; }}
    #pl-mark {{ display: inline-block; padding: 24px 40px 28px; background: {NAVY}; border: 12px solid #ffffff; border-radius: 26px;
      box-shadow: 0 6px 10px rgba(0,0,0,0.2); font-family: "Lato", sans-serif; font-weight: 900; font-size: 84px; line-height: 1; white-space: nowrap; }}
    .pl-line {{ margin-top: 26px; font-weight: 900; line-height: 1.1; }}
  </style>

  <div id="root" data-composition-id="planner" data-width="1080" data-height="1920">
    <div class="pl-desk"></div>
    {props}

    <div id="pl-move" class="pl-slot" data-layout-allow-overflow>
    <div id="pl-page" data-layout-allow-overflow>
      <div class="pl-paper"></div>
      {"".join(f'<div class="pl-ring" style="top:{60+i*80}px"></div>' for i in range(12))}
      <div id="pl-head" class="pl-hand" data-layout-allow-overlap>Ocak <span style="color:#d06b63">2027</span></div>
      <div id="pl-cal" data-layout-allow-overlap>{cal}</div>
      <div id="pl-gtitle" class="pl-hand" data-layout-allow-overlap>2027 hedeflerim</div>
      {goals}
      <div id="pl-wt1" class="pl-washi" style="left: -40px; top: -18px; width: 250px; transform: rotate(-24deg);
        background: repeating-linear-gradient(90deg, #c8b6f0 0 18px, #e7dcfb 18px 36px)" data-layout-ignore></div>
      <div id="pl-wt2" class="pl-washi" style="left: 560px; top: 1000px; width: 230px; transform: rotate(-32deg);
        background: radial-gradient(circle, #ffffff 5px, transparent 6px) 0 0 / 24px 24px, #f2b5b0" data-layout-ignore></div>
      {stickers}
      <div id="pl-shine-wrap" data-layout-ignore><div id="pl-shine"></div></div>
    </div>
    </div>

    <div id="pl-t1s" class="pl-slot clip" data-start="0" data-duration="1.45" data-track-index="1">
      <div id="pl-title1" class="pl-label" style="left: 150px; top: 176px; font-size: 54px" data-layout-allow-overlap>2027 ajandanı benimle süsle</div>
    </div>
    <div id="pl-t2s" class="pl-slot clip" data-start="{DONE:.2f}" data-duration="{END0-DONE:.2f}" data-track-index="2">
      <div id="pl-title2" class="pl-label" style="left: 230px; top: 180px; font-size: 64px" data-layout-allow-overlap>Yeni yıl, yeni sayfa</div>
    </div>
    <div id="pl-cs" class="pl-slot clip" data-start="{END0-0.05:.2f}" data-duration="{TOTAL-END0+0.05:.2f}" data-track-index="3">
      <div id="pl-card" data-layout-allow-overlap>
        <div id="pl-mark"><span style="color:#e8bcac">MALIBU</span> <span style="color:#ffffff">CRAFT</span></div>
        <div class="pl-line" style="font-size: 58px">Ajandan için sticker setleri</div>
        <div class="pl-line" style="font-size: 44px; color: #6a5a4a">A5 set · 64,90 TL</div>
        <div class="pl-line" style="font-size: 44px"><span style="background:{SALMON};padding:8px 18px;border-radius:12px">shopier.com/malibucraftshop</span></div>
        <div class="pl-line" style="font-size: 36px; font-weight: 800">Kişiye özel tasarımlar için DM</div>
      </div>
      {endstk}
    </div>
  </div>

  <script>
    const tl = gsap.timeline({{ paused: true }});
    {js}
    window.__timelines["planner"] = tl;
  </script>
</template>
'''
open(f"{P}/compositions/planner.html","w").write(html)

F=1/30; pk={"whoosh":0.162,"pop":0.12,"click-soft":0.073,"sparkle":0.0,"chime":0.418}
dur={"whoosh":0.57,"pop":0.72,"click-soft":0.36,"sparkle":1.8,"chime":2.5}
cues=[("rw","whoosh",1.05,0.32)]
for i,(kind,t) in enumerate(steps):
    if kind=="stk": cues.append((f"s{i}","click-soft",t,0.5))
    elif kind=="tape": cues.append((f"tp{i}","click-soft",t+0.2,0.3))
    elif kind=="end": cues.append((f"e{i}","pop",t,0.35))
cues+=[("done","sparkle",DONE,0.3),("t2","pop",DONE+0.34,0.45),("sweep","whoosh",END0-0.15,0.3),("card","click-soft",END0+0.26,0.5),("mark","pop",END0+0.72,0.5)]
lines=[f'      <audio id="sfx-{c}" class="clip" src="assets/sfx/{k}.mp3" data-start="{round(t-pk[k]+(F if pk[k] else 0),3)}" data-duration="{dur[k]}" data-track-index="{20+i}" data-volume="{v}"></audio>' for i,(c,k,t,v) in enumerate(cues)]
root=f'''<!doctype html>
<html lang="tr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #ddb07c; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
      <div id="planner" data-composition-id="planner" data-composition-src="compositions/planner.html" data-start="0" data-duration="{TOTAL}"
        data-track-index="0" data-track-kind="graphics" data-width="1080" data-height="1920"></div>
{chr(10).join(lines)}
    </div>
    <script>
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
'''
open(f"{P}/index.html","w").write(root)
print("DONE at",DONE,"end card",END0,"total",TOTAL)
