# Malibu Craft x "kaçan aslan" — a cartoon lion caught on the shop's security camera, taking the lion's share of stickers.
import os, math
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAVY="#29314b"; SALMON="#e1a8a4"; KRAFT="#d8b38a"

def lion_svg(pfx, hearts_on=False):
    """Flat cartoon lion, side body facing right with a front-facing head. viewBox 600x520, feet on y=490."""
    G="#e8a33d"; G2="#cf8a2e"; BELLY="#f2be63"; M1="#b9561f"; M2="#cc6a2a"; FACE="#f0b04a"; MUZ="#fbe6be"
    hx,hy=440,205
    mane="".join(f'<circle cx="{hx+118*math.cos(math.radians(a)):.1f}" cy="{hy+118*math.sin(math.radians(a)):.1f}" r="36" fill="{M1 if k%2 else M2}"/>' for k,a in enumerate(range(0,360,24)))
    def leg(id_,x,col):
        return (f'<g id="{pfx}-{id_}"><rect x="{x}" y="330" width="54" height="150" rx="27" fill="{col}"/>'
                f'<ellipse cx="{x+30}" cy="482" rx="38" ry="18" fill="{col}"/>'
                f'<path d="M{x+16} 478 v10 M{x+30} 476 v12 M{x+44} 478 v10" stroke="{M1}" stroke-width="3" stroke-linecap="round" opacity="0.5"/></g>')
    heart=lambda cx,cy,s: f'<path d="M{cx} {cy+9*s} C {cx-22*s} {cy-6*s}, {cx-12*s} {cy-22*s}, {cx} {cy-10*s} C {cx+12*s} {cy-22*s}, {cx+22*s} {cy-6*s}, {cx} {cy+9*s} Z" fill="#e0435b"/>'
    return f'''<svg viewBox="0 0 600 520" width="600" height="520" style="overflow: visible">
      <g id="{pfx}-tail"><path d="M108 300 C 60 296, 26 262, 34 196" stroke="{G}" stroke-width="20" fill="none" stroke-linecap="round"/>
        <ellipse cx="36" cy="182" rx="24" ry="32" fill="{M1}"/></g>
      {leg("lb2",150,G2)}{leg("lf2",356,G2)}
      <ellipse cx="262" cy="322" rx="178" ry="104" fill="{G}"/>
      <ellipse cx="272" cy="368" rx="124" ry="48" fill="{BELLY}"/>
      {leg("lb1",104,G)}{leg("lf1",398,G)}
      <g id="{pfx}-head">
        <circle cx="{hx}" cy="{hy}" r="124" fill="{M1}"/>{mane}
        <circle cx="{hx-48}" cy="{hy-80}" r="28" fill="{G}"/><circle cx="{hx-48}" cy="{hy-80}" r="14" fill="{BELLY}"/>
        <circle cx="{hx+50}" cy="{hy-80}" r="28" fill="{G}"/><circle cx="{hx+50}" cy="{hy-80}" r="14" fill="{BELLY}"/>
        <circle cx="{hx}" cy="{hy+6}" r="90" fill="{FACE}"/>
        <ellipse cx="{hx-46}" cy="{hy+40}" rx="16" ry="10" fill="#f29a8f" opacity="0.7"/><ellipse cx="{hx+46}" cy="{hy+40}" rx="16" ry="10" fill="#f29a8f" opacity="0.7"/>
        <g id="{pfx}-eyes" style="opacity: {0 if hearts_on else 1}">
          <ellipse cx="{hx-30}" cy="{hy-12}" rx="11" ry="15" fill="#2b1a10"/><circle cx="{hx-26}" cy="{hy-18}" r="4" fill="#fff"/>
          <ellipse cx="{hx+30}" cy="{hy-12}" rx="11" ry="15" fill="#2b1a10"/><circle cx="{hx+34}" cy="{hy-18}" r="4" fill="#fff"/>
        </g>
        <g id="{pfx}-hearts" style="opacity: {1 if hearts_on else 0}">{heart(hx-30,hy-12,1.15)}{heart(hx+30,hy-12,1.15)}</g>
        <path d="M{hx-46} {hy-40} q 14 -10 28 -2 M{hx+18} {hy-42} q 14 -8 28 2" stroke="#8a4a1e" stroke-width="5" fill="none" stroke-linecap="round"/>
        <circle cx="{hx-17}" cy="{hy+38}" r="25" fill="{MUZ}"/><circle cx="{hx+17}" cy="{hy+38}" r="25" fill="{MUZ}"/>
        <path d="M{hx-15} {hy+14} h30 q 4 0 0 6 l-11 12 q -4 4 -8 0 l-11 -12 q -4 -6 0 -6 z" fill="#6b3420"/>
        <path d="M{hx} {hy+32} v10 M{hx} {hy+42} q -12 12 -22 2 M{hx} {hy+42} q 12 12 22 2" stroke="#6b3420" stroke-width="4" fill="none" stroke-linecap="round"/>
        <circle cx="{hx-32}" cy="{hy+36}" r="2.5" fill="#8a4a1e"/><circle cx="{hx-26}" cy="{hy+46}" r="2.5" fill="#8a4a1e"/>
        <circle cx="{hx+32}" cy="{hy+36}" r="2.5" fill="#8a4a1e"/><circle cx="{hx+26}" cy="{hy+46}" r="2.5" fill="#8a4a1e"/>
      </g>
    </svg>'''

PAW='<svg viewBox="0 0 100 100" width="{w}" height="{w}"><g fill="{c}"><ellipse cx="50" cy="66" rx="24" ry="20"/><ellipse cx="22" cy="40" rx="10" ry="13"/><ellipse cx="40" cy="24" rx="10" ry="13"/><ellipse cx="60" cy="24" rx="10" ry="13"/><ellipse cx="78" cy="40" rx="10" ry="13"/></g></svg>'

# ---------------- room (vector) + product sheets (kept unaltered, lit)
SHELF=[("retro",620,330),("mistik",760,330),("kiraz",900,330),("limon",620,560),("muzik",760,560),("london",900,560)]
STAND=[("van-gogh",600,660,-6),("coquette",760,650,0),("y2k",920,660,6)]
LION_X,LION_Y=40,640           # lion container (600x520), feet at y 1130
STACK=[("retro",0),("van-gogh",1),("mistik",2),("coquette",3),("kiraz",4),("y2k",5),("limon",6)]
SRC={n:(x,y,120) for n,x,y in SHELF}; SRC.update({n:(x,y,150) for n,x,y,r in STAND})
STK_LX,STK_LY=300,300          # stack slot inside the lion container
js=[]; J=js.append; snd=[]
def cap(cid,t0,t1,rot=-2):
    J(f'tl.fromTo("#{cid}", {{ scale: 1.3, rotation: {rot+6}, opacity: 0 }}, {{ scale: 1, rotation: {rot}, opacity: 1, duration: 0.2, ease: "power3.in", immediateRender: false }}, {t0:.2f});')
    J(f'tl.to("#{cid}", {{ scale: 0.97, duration: 0.04, ease: "none" }}, {t0+0.2:.2f});'); J(f'tl.to("#{cid}", {{ scale: 1, duration: 0.12, ease: "power2.out" }}, {t0+0.24:.2f});')
    J(f'tl.to("#{cid}", {{ y: 30, opacity: 0, duration: 0.15, ease: "power2.in" }}, {t1-0.16:.2f});'); snd.append(("click",t0+0.2))

# idle life for the whole CCTV part: tail swish, breathing
J('tl.to("#ln-tail", { rotation: 14, svgOrigin: "108 300", duration: 0.5, ease: "sine.inOut", yoyo: true, repeat: 15 }, 0);')
J('tl.to("#ln-head", { y: -6, duration: 0.6, ease: "sine.inOut", yoyo: true, repeat: 6 }, 0);')
J('tl.to("#rm-light", { opacity: 0.85, duration: 0.3, ease: "none", yoyo: true, repeat: 1 }, 1.2);')
# blink (instant)
for t in (1.3,):
    J(f'tl.set("#ln-eyes", {{ scaleY: 0.12, svgOrigin: "440 193" }}, {t});'); J(f'tl.set("#ln-eyes", {{ scaleY: 1, svgOrigin: "440 193" }}, {t+0.1:.2f});')
# 2.4 caption 1, 3.0 heart eyes
cap("cp1",2.45,5.0)
J('tl.to("#ln-head", { rotation: 6, svgOrigin: "440 300", duration: 0.35, ease: "power2.out" }, 2.6);')
J('tl.set("#ln-eyes", { opacity: 0 }, 3.0);')
J('tl.fromTo("#ln-hearts", { opacity: 1, scale: 0.2, svgOrigin: "440 193" }, { opacity: 1, scale: 1, svgOrigin: "440 193", duration: 0.3, ease: "back.out(3)", immediateRender: false }, 3.0);'); snd.append(("pop",3.05))
J('tl.to("#ln-hearts", { scale: 1.18, svgOrigin: "440 193", duration: 0.25, ease: "sine.inOut", yoyo: true, repeat: 5 }, 3.3);')
for i in range(3):
    J(f'tl.fromTo("#fh{i}", {{ y: 0, opacity: 0, scale: 0.4 }}, {{ y: -260, opacity: 0, scale: 1.2, duration: 1.4, ease: "power1.out", keyframes: {{ opacity: [0, 1, 1, 0] }}, immediateRender: false }}, {3.1+i*0.3:.2f});')
snd.append(("sparkle",3.1))
# 5.0 grab: caption 2; sheets fly into the stack against the lion's chest
cap("cp2",5.0,8.0,2)
J('tl.to("#ln-head", { rotation: -4, svgOrigin: "440 300", duration: 0.3, ease: "power2.out" }, 5.0);')
for k,(n,_) in enumerate(STACK):
    t=5.25+k*0.3; sx,sy,sw=SRC[n]
    # stack item lives in the lion container; start it exactly over its source sheet
    lx,ly=STK_LX+k*4, STK_LY-k*5
    dx=(sx+sw/2)-(LION_X+lx+60); dy=(sy+sw*1.34/2)-(LION_Y+ly+80)
    J(f'tl.set("#src-{n}", {{ opacity: 0 }}, {t:.2f});')
    J(f'tl.fromTo("#st{k}", {{ x: {dx:.0f}, y: {dy:.0f}, scale: {sw/120:.2f}, rotation: 0, opacity: 1 }}, {{ x: 0, y: 0, scale: 1, rotation: {(-1)**k*5}, opacity: 1, duration: 0.24, ease: "power3.in", immediateRender: false }}, {t:.2f});')
    snd.append(("whoosh-soft",t+0.08)); snd.append(("pop-soft",t+0.24))
J('tl.to("#ln-head", { rotation: 0, svgOrigin: "440 300", duration: 0.3, ease: "power2.out" }, 7.5);')
# 8.0 leave: turn, walk out left; note flutters onto the table
cap("cp3",8.0,9.55,-2)
J('tl.to("#ln-flip", { scaleX: -1, transformOrigin: "50% 50%", duration: 0.16, ease: "power2.inOut" }, 8.05);')
J('tl.to("#ln-stackfix", { scaleX: -1, transformOrigin: "390px 330px", duration: 0.16, ease: "power2.inOut" }, 8.05);')
for leg,ph in (("lf1",1),("lb1",-1),("lf2",-1),("lb2",1)):
    x0={"lf1":398,"lb1":104,"lf2":356,"lb2":150}[leg]
    J(f'tl.fromTo("#ln-{leg}", {{ rotation: {-18*ph} }}, {{ rotation: {18*ph}, svgOrigin: "{x0+27} 340", duration: 0.18, ease: "sine.inOut", yoyo: true, repeat: 6, immediateRender: false }}, 8.25);')
J('tl.to("#ln", { x: -900, duration: 1.2, ease: "power1.in" }, 8.3);')
J('tl.to("#ln-body", { y: -10, duration: 0.18, ease: "sine.inOut", yoyo: true, repeat: 6 }, 8.25);')
for t in (8.35,8.7,9.05): snd.append(("step",t))
J('tl.fromTo("#note", { x: -260, y: -360, rotation: -30, opacity: 1 }, { x: 0, y: 0, rotation: -8, opacity: 1, duration: 0.9, ease: "sine.inOut", immediateRender: false }, 8.4);')
J('tl.to("#note", { keyframes: { x: [-200, -120, -60, -20, 0] }, duration: 0.9, ease: "none" }, 8.4);')
snd.append(("whoosh-soft",8.9))
# 9.45 zoom into the note, white flash, cut
J('tl.to("#scene", { scale: 4.2, transformOrigin: "700px 1010px", duration: 0.5, ease: "power2.in" }, 9.4);'); snd.append(("whoosh",9.75))
J('tl.fromTo("#flash", { opacity: 0 }, { opacity: 1, duration: 0.08, ease: "none", immediateRender: false }, 9.86);')
J('tl.to("#flash", { opacity: 0, duration: 0.3, ease: "power1.out" }, 9.98);'); snd.append(("impact",9.95))
# 9.95-12.5 the note, close up and in colour
T2=9.95
cap("cp4",T2+0.15,13.05,-2)
J(f'tl.fromTo("#bignote", {{ scale: 1.25, rotation: 4, opacity: 0 }}, {{ scale: 1, rotation: -3, opacity: 1, duration: 0.22, ease: "power3.in", immediateRender: false }}, {T2:.2f});')
J(f'tl.fromTo("#bn1", {{ clipPath: "inset(-20px 100% -20px -20px)" }}, {{ clipPath: "inset(-20px -40px -20px -20px)", duration: 0.55, ease: "power1.inOut", immediateRender: false }}, {T2+0.35:.2f});'); snd.append(("key",T2+0.4))
J(f'tl.fromTo("#bn2 .st", {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.16, stagger: 0.09, ease: "back.out(3)", immediateRender: false }}, {T2+0.95:.2f});'); snd.append(("pop",T2+1.0))
J(f'tl.fromTo("#bn3", {{ clipPath: "inset(-20px 100% -20px -20px)" }}, {{ clipPath: "inset(-20px -40px -20px -20px)", duration: 0.6, ease: "power1.inOut", immediateRender: false }}, {T2+1.45:.2f});'); snd.append(("key",T2+1.5))
J(f'tl.fromTo("#bnpaw", {{ scale: 1.8, rotation: 20, opacity: 0 }}, {{ scale: 1, rotation: -12, opacity: 1, duration: 0.18, ease: "power3.in", immediateRender: false }}, {T2+2.05:.2f});'); snd.append(("impact-soft",T2+2.23))
# 12.5 end card
TE=13.1
J(f'tl.fromTo("#endbg", {{ scale: 0 }}, {{ scale: 1, duration: 0.45, ease: "power3.in" }}, {TE-0.3:.2f});'); snd.append(("whoosh",TE-0.05))
J(f'tl.fromTo("#le", {{ y: 760 }}, {{ y: 0, duration: 0.45, ease: "back.out(1.4)" }}, {TE+0.1:.2f});')
J(f'tl.fromTo("#e1", {{ scale: 1.5, rotation: 6, opacity: 0 }}, {{ scale: 1, rotation: -3, opacity: 1, duration: 0.22, ease: "power3.in", immediateRender: false }}, {TE+0.3:.2f});'); snd.append(("impact",TE+0.52))
J(f'tl.to("#e1", {{ scale: 0.96, duration: 0.04, ease: "none" }}, {TE+0.52:.2f});'); J(f'tl.to("#e1", {{ scale: 1, duration: 0.12, ease: "power2.out" }}, {TE+0.56:.2f});')
for i,(sel,t) in enumerate([("#e2",TE+0.95),("#e3",TE+1.25)]):
    J(f'tl.fromTo("{sel}", {{ scale: 1.35, rotation: {6 if i else -4}, opacity: 0 }}, {{ scale: 1, rotation: {2 if i else -2}, opacity: 1, duration: 0.2, ease: "power3.in", immediateRender: false }}, {t-0.2:.2f});'); snd.append(("pop",t))
J(f'tl.fromTo(["#e4", "#e5"], {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, stagger: 0.25, ease: "power1.out", immediateRender: false }}, {TE+1.5:.2f});')
J(f'tl.to("#le-tail", {{ rotation: 14, svgOrigin: "108 300", duration: 0.5, ease: "sine.inOut", yoyo: true, repeat: 3 }}, {TE+0.6:.2f});')
snd.append(("sparkle",TE+0.6))
TOTAL=round(TE+5.6,1)
js="\n    ".join(js)

def sheet(id_,n,x,y,w,extra=""):
    return f'<div id="{id_}" class="sh" style="left: {x}px; top: {y}px; width: {w}px; height: {round(w*1.34)}px; background-image: url(assets/sheets/{n}.webp){extra}"></div>'
shelf_html="".join(sheet(f"src-{n}",n,x,y,120) for n,x,y in SHELF)
stand_html="".join(sheet(f"src-{n}",n,x,y,150,f"; transform: rotate({r}deg)") for n,x,y,r in STAND)
stack_html="".join(sheet(f"st{k}",n,STK_LX+k*4,STK_LY-k*5,120,"; opacity: 0") for k,(n,_) in enumerate(STACK))
fh="".join(f'<svg id="fh{i}" class="fh" viewBox="0 0 40 40" width="{[56,44,64][i]}" style="left: {[470,560,400][i]}px; top: {[700,720,740][i]}px"><path d="M20 34 C 2 22, 6 6, 20 14 C 34 6, 38 22, 20 34 Z" fill="#ff6b81"/></svg>' for i in range(3))

html=f'''<template>
  <style>
    @font-face {{ font-family: "Caveat"; src: url("assets/fonts/Caveat.ttf") format("truetype"); font-weight: 400 700; }}
    #root {{ position: absolute; inset: 0; overflow: hidden; background: #141a2b; font-family: "Nunito", sans-serif; color: {NAVY}; }}
    .slot {{ position: absolute; inset: 0; }}
    #scene {{ position: absolute; inset: 0; }}
    .rm {{ position: absolute; }}
    .sh {{ position: absolute; background-size: contain; background-repeat: no-repeat; background-position: center; filter: drop-shadow(0px 6px 8px rgba(0,0,0,0.45)); }}
    #ln {{ position: absolute; left: {LION_X}px; top: {LION_Y}px; width: 600px; height: 520px; }}
    #ln-flip {{ position: absolute; inset: 0; }}
    #ln-body {{ position: absolute; inset: 0; }}
    #ln-stackfix {{ position: absolute; inset: 0; }}
    .fh {{ position: absolute; opacity: 0; }}
    #note {{ position: absolute; left: 650px; top: 975px; width: 100px; height: 72px; background: #f3e3c3; border-radius: 4px; box-shadow: 0 4px 6px rgba(0,0,0,0.4); opacity: 0;
      display: flex; align-items: center; justify-content: center; }}
    .capwrap {{ position: absolute; left: 0; right: 0; text-align: center; }}
    .cap {{ display: inline-block; position: relative; padding: 16px 32px 20px; background: #ffffff; border: 8px solid {NAVY}; border-radius: 20px; opacity: 0;
      box-shadow: 0 10px 18px rgba(0,0,0,0.35); font-family: "Archivo Black", sans-serif; font-size: 52px; line-height: 1; white-space: nowrap; }}
    #flash {{ position: absolute; inset: 0; background: #ffffff; opacity: 0; }}
    #notebg {{ position: absolute; inset: 0; background: #d9b48a;
      background-image: repeating-linear-gradient(90deg, rgba(120,72,30,0.10) 0 3px, transparent 3px 230px); }}
    #bignote {{ position: absolute; left: 110px; top: 470px; width: 860px; height: 700px; background: #fbf1dc; border-radius: 10px; opacity: 0;
      box-shadow: 0 24px 40px rgba(60,30,10,0.4); background-image: repeating-linear-gradient(180deg, transparent 0 86px, rgba(120,140,190,0.35) 86px 89px); }}
    #bn1, #bn3 {{ clip-path: inset(-20px 100% -20px -20px); }}
    .bn {{ position: absolute; left: 70px; font-family: "Caveat", cursive; font-weight: 700; color: #2a2f45; white-space: nowrap; line-height: 1; }}
    #bn2 .st {{ display: inline-block; position: relative; color: #f2b01e; opacity: 0; }}
    #endbg {{ position: absolute; left: -960px; top: -350px; width: 3000px; height: 3000px; border-radius: 50%; background: {SALMON};
      background-image: repeating-linear-gradient(115deg, rgba(255,255,255,0.14) 0 44px, transparent 44px 88px); }}
    #e1 {{ display: inline-block; position: relative; font-family: "Archivo Black", sans-serif; font-size: 94px; line-height: 0.98; color: {NAVY}; opacity: 0;
      text-shadow: 0 6px 0 rgba(255,255,255,0.7); }}
    #e2 {{ display: inline-block; position: relative; padding: 16px 30px 20px; background: {KRAFT}; border: 10px solid #ffffff; border-radius: 18px; opacity: 0;
      box-shadow: 0 8px 14px rgba(0,0,0,0.22); font-weight: 900; font-size: 46px; line-height: 1; white-space: nowrap; }}
    #e3 {{ display: inline-block; position: relative; padding: 16px 30px 20px; background: {NAVY}; color: #ffffff; border: 10px solid #ffffff; border-radius: 18px; opacity: 0;
      box-shadow: 0 8px 14px rgba(0,0,0,0.22); font-weight: 900; font-size: 46px; line-height: 1; white-space: nowrap; }}
    #e4 {{ font-weight: 900; font-size: 42px; line-height: 1.1; opacity: 0; }}
    #e5 {{ display: inline-block; padding: 10px 22px; border-radius: 14px; background: rgba(255,255,255,0.85); font-weight: 800; font-size: 32px; line-height: 1.1; opacity: 0; }}
    #le {{ position: absolute; left: 200px; top: 1180px; width: 600px; height: 520px; transform-origin: 50% 100%; }}
    #le-scale {{ position: absolute; inset: 0; transform: scale(1.5); transform-origin: 70% 40%; }}
  </style>

  <div id="root" data-composition-id="aslan" data-width="1080" data-height="1920">

    <div id="cctv" class="slot clip" data-start="0" data-duration="10.05" data-track-index="1">
      <div id="scene" data-layout-allow-overflow>
        <svg class="rm" viewBox="0 0 1080 1920" width="1080" height="1920" data-layout-ignore>
          <defs>
            <linearGradient id="rm-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1d2540"/><stop offset="1" stop-color="#263052"/></linearGradient>
            <radialGradient id="rm-lamp" cx="0.5" cy="0" r="1"><stop offset="0" stop-color="#ffe6a8" stop-opacity="0.55"/><stop offset="1" stop-color="#ffe6a8" stop-opacity="0"/></radialGradient>
          </defs>
          <rect width="1080" height="1920" fill="url(#rm-wall)"/>
          <rect y="1130" width="1080" height="790" fill="#2c2433"/>
          <path d="M0 1130 H1080" stroke="#3b3245" stroke-width="10"/>
          <rect x="30" y="520" width="300" height="610" rx="8" fill="#151a2c"/><rect x="48" y="540" width="264" height="590" fill="#0d1120"/>
          <circle cx="285" cy="840" r="9" fill="#a4a9bd"/>
          <rect x="560" y="300" width="500" height="14" fill="#5a4636"/><rect x="560" y="530" width="500" height="14" fill="#5a4636"/>
          <rect x="560" y="760" width="500" height="14" fill="#5a4636"/>
          <rect x="430" y="260" width="96" height="18" fill="#9aa0b8" opacity="0.4"/>
        </svg>
        <div class="rm" style="left: 80px; top: 330px; padding: 16px 26px 20px; border: 6px solid #e8bcac; border-radius: 18px; font-family: Lato, sans-serif; font-weight: 900; font-size: 46px; line-height: 1; color: #e8bcac; box-shadow: 0 0 24px rgba(232,188,172,0.45)">MALIBU<br><span style="color: #ffffff">CRAFT</span></div>
        <div id="rm-shelf" data-layout-ignore>{shelf_html}</div>
        <div data-layout-ignore><div class="rm" style="left: 150px; top: 1180px; transform: rotate(80deg); opacity: 0.55">{PAW.format(w=40,c="#e8bcac")}</div><div class="rm" style="left: 200px; top: 1225px; transform: rotate(80deg); opacity: 0.55">{PAW.format(w=40,c="#e8bcac")}</div><div class="rm" style="left: 255px; top: 1182px; transform: rotate(80deg); opacity: 0.55">{PAW.format(w=40,c="#e8bcac")}</div><div class="rm" style="left: 310px; top: 1228px; transform: rotate(80deg); opacity: 0.55">{PAW.format(w=40,c="#e8bcac")}</div><div class="rm" style="left: 365px; top: 1186px; transform: rotate(80deg); opacity: 0.55">{PAW.format(w=40,c="#e8bcac")}</div></div>
        <svg class="rm" viewBox="0 0 1080 1920" width="1080" height="1920" data-layout-ignore><rect x="640" y="1180" width="220" height="150" rx="6" fill="#9c7650"/><rect x="740" y="1180" width="22" height="150" fill="#c9b08a"/><rect x="860" y="1150" width="190" height="180" rx="6" fill="#8a6644"/><rect x="944" y="1150" width="22" height="180" fill="#c9b08a"/><rect x="700" y="1090" width="160" height="90" rx="6" fill="#a88360"/><rect x="770" y="1090" width="20" height="90" fill="#c9b08a"/></svg>
        <svg class="rm" viewBox="0 0 1080 1920" width="1080" height="1920" data-layout-ignore>
          <rect x="540" y="1000" width="520" height="34" rx="6" fill="#7a5638"/>
          <rect x="570" y="1034" width="26" height="96" fill="#5e412a"/><rect x="1004" y="1034" width="26" height="96" fill="#5e412a"/>
          <rect x="580" y="958" width="460" height="42" rx="6" fill="#4a3a30"/>
        </svg>
        <div id="rm-stand" data-layout-ignore>{stand_html}</div>
        <svg id="rm-light" class="rm" viewBox="0 0 1080 1920" width="1080" height="1920" data-layout-ignore>
          <path d="M840 640 L560 1010 L1080 1010 L1080 760 Z" fill="url(#rm-lamp)"/>
        </svg>
        <div id="note" data-layout-ignore>{PAW.format(w=40,c="#c0563a")}</div>
        <div id="ln" data-layout-ignore><div id="ln-flip"><div id="ln-body">{lion_svg("ln")}</div><div id="ln-stackfix">{stack_html}</div></div></div>
        {fh}
      </div>
      <div class="capwrap" style="top: 1176px"><div id="cp1" class="cap">Gözü hemen stickerlara takıldı</div></div>
      <div class="capwrap" style="top: 1176px"><div id="cp2" class="cap">Ve aslan payını aldı!</div></div>
      <div class="capwrap" style="top: 1176px"><div id="cp3" class="cap">Giderken not bırakmış…</div></div>
    </div>

    <div id="notes" class="slot clip" data-start="{T2-0.1:.2f}" data-duration="{TE-T2+0.2:.2f}" data-track-index="4">
      <div id="notebg"></div>
      <div id="bignote" data-layout-allow-overlap>
        <div class="bn" id="bn1" style="top: 70px; font-size: 120px">Kükreten kalite!</div>
        <div class="bn" id="bn2" style="top: 230px; font-size: 96px"><span class="st">★</span><span class="st">★</span><span class="st">★</span><span class="st">★</span><span class="st">★</span></div>
        <div class="bn" id="bn3" style="top: 380px; font-size: 84px">Aslan payımı aldım. – A.</div>
        <div id="bnpaw" style="position: absolute; left: 600px; top: 480px; opacity: 0" data-layout-ignore>{PAW.format(w=170,c="#c0563a")}</div>
      </div>
      <div class="capwrap" style="top: 200px"><div id="cp4" class="cap">Masada şu not vardı:</div></div>
    </div>

    <div id="ends" class="slot clip" data-start="{TE-0.32:.2f}" data-duration="{TOTAL-TE+0.32:.2f}" data-track-index="5">
      <div id="endbg" data-layout-ignore></div>
      <div class="capwrap" style="top: 196px"><div id="e1">Aslan bile<br>dayanamadı!</div></div>
      <div class="capwrap" style="top: 450px"><div id="e2">Yeni koleksiyon · Tanesi 64,90 TL</div></div>
      <div class="capwrap" style="top: 570px"><div id="e3">shopier.com/malibucraftshop</div></div>
      <div id="e4" class="capwrap" style="top: 700px">Kişiye özel tasarımlar için DM</div>
      <div class="capwrap" style="top: 776px"><div id="e5">Gerçek aslanı görürsen yaklaşma, 112'yi ara.</div></div>
      <div id="le" data-layout-ignore><div id="le-scale">{lion_svg("le", hearts_on=True)}</div></div>
    </div>

    <div id="flash" data-layout-ignore></div>
  </div>

  <script>
    const tl = gsap.timeline({{ paused: true }});
    {js}
    window.__timelines["aslan"] = tl;
  </script>
</template>
'''
open(f"{P}/compositions/aslan.html","w").write(html)

F=1/30
SFX={"whoosh":("whoosh",0.162,0.57,0.2),"whoosh-soft":("whoosh",0.162,0.57,0.08),"pop":("pop",0.119,0.72,0.22),"pop-soft":("pop",0.119,0.72,0.12),
     "impact":("impact-bass-1",0.073,2.1,0.3),"impact-soft":("impact-bass-1",0.073,2.1,0.16),"click":("click",0.072,0.37,0.14),"step":("click",0.072,0.37,0.1),
     "sparkle":("sparkle",0.0,1.8,0.16),"key":("key-press",0.077,0.4,0.18)}
lines=[]
for i,(kind,t) in enumerate(snd):
    f,pk,d,v=SFX[kind]; st=round(max(0,t-pk+(F if pk else 0)),3)
    lines.append(f'      <audio id="sfx-{i}" class="clip" src="assets/sfx/{f}.mp3" data-start="{st}" data-duration="{d}" data-track-index="{40+i}" data-volume="{v}"></audio>')
lines.insert(0,'      <audio id="sfx-news" class="clip" src="assets/sfx/notification.mp3" data-start="0" data-duration="2.4" data-track-index="39" data-volume="0.18"></audio>')
root=f'''<!doctype html>
<html lang="tr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #141a2b; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
      <div id="aslan-host" data-composition-id="aslan" data-composition-src="compositions/aslan.html" data-start="0" data-duration="{TOTAL}"
        data-track-index="0" data-track-kind="graphics" data-width="1080" data-height="1920"></div>
      <div id="hud" data-composition-id="camcorder-hud" data-composition-src="compositions/camcorder-hud.html" data-start="0" data-duration="9.9"
        data-track-index="1" data-width="1080" data-height="1920"></div>
      <div id="ticker" data-composition-id="news-ticker" data-composition-src="compositions/news-ticker.html" data-start="0" data-duration="2.6"
        data-track-index="2" data-width="1080" data-height="1920"></div>
{chr(10).join(lines)}
    </div>
    <script>
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
'''
open(f"{P}/index.html","w").write(root)
print("total",TOTAL,"sfx",len(lines))
