# Malibu Craft x GTA 6 launch week — an open-world "mission" parody in the brand's own style
# (no Rockstar logo, font, characters or art; generic game tropes: mission card, phone, GPS route, pickups, wanted stars, mission passed).
import os, math
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAVY="#29314b"; SALMON="#e1a8a4"; PINK="#ff4f9a"; GOLD="#ffd56b"
js=[]; J=js.append; snd=[]
def slap(sel,t,rot,frm=1.4,d=0.2,kind="pop"):
    J(f'tl.fromTo("{sel}", {{ scale: {frm}, rotation: {rot+8}, opacity: 0 }}, {{ scale: 1, rotation: {rot}, opacity: 1, duration: {d}, ease: "power3.in", immediateRender: false }}, {t-d:.2f});')
    J(f'tl.to("{sel}", {{ scale: 0.96, duration: 0.04, ease: "none" }}, {t:.2f});'); J(f'tl.to("{sel}", {{ scale: 1, duration: 0.12, ease: "power2.out" }}, {t+0.04:.2f});')
    if kind: snd.append((kind,t))
def fade_in(sel,t,d=0.25,y=30):
    J(f'tl.fromTo("{sel}", {{ opacity: 0, y: {y} }}, {{ opacity: 1, y: 0, duration: {d}, ease: "power3.out", immediateRender: false }}, {t:.2f});')
def out(sel,t,d=0.2,y=-40):
    J(f'tl.to("{sel}", {{ opacity: 0, y: {y}, duration: {d}, ease: "power2.in" }}, {t:.2f});')

def palm(x,base,h,flip=1):
    tx=x+flip*h*0.18; ty=base-h
    trunk=f'<path d="M{x-16} {base} Q {x+flip*h*0.05} {base-h*0.5}, {tx-8} {ty} L {tx+8} {ty} Q {x+flip*h*0.05+20} {base-h*0.5}, {x+16} {base} Z" fill="#1a0b2e"/>'
    fr=""
    for a,l in [(-160,260),(-130,300),(-95,240),(-60,300),(-25,270),(10,230),(-200,220)]:
        ang=math.radians(a if flip==1 else 180-a); ex=tx+l*math.cos(ang); ey=ty+l*math.sin(ang)
        cx=tx+l*0.55*math.cos(ang)+0; cy=ty+l*0.55*math.sin(ang)-60
        fr+=f'<path d="M{tx} {ty} Q {cx:.0f} {cy:.0f}, {ex:.0f} {ey+40:.0f} Q {cx:.0f} {cy+40:.0f}, {tx} {ty+10} Z" fill="#1a0b2e"/>'
    return trunk+fr

# ---------------- timeline
# perspective floor grid: lines placed from one tween value (seek-safe), no CSS 3D
J('const gp = { p: 0 }; placeGrid(gp.p);')
J('tl.to(gp, { p: 14, duration: 22, ease: "none", onUpdate: () => placeGrid(gp.p) }, 0);')
J('tl.to("#sun", { y: -18, duration: 22, ease: "none" }, 0);')
# S1 hook 0-2.4 (complete at frame 0)
for i,s in enumerate(["#h-s1","#h-s2"]):
    J(f'tl.to("{s}", {{ y: -22, rotation: {(-1)**i*3}, duration: 0.8, ease: "sine.inOut", yoyo: true, repeat: 2 }}, 0);')
J('tl.fromTo("#h1", { scale: 1.12 }, { scale: 1, duration: 0.25, ease: "power3.out", immediateRender: false }, 0.5);'); snd.append(("impact",0.5))
S2=2.4
out(["#h1","#h2","#h3"],S2-0.25,0.22,-60) if False else None
J(f'tl.to(["#h1", "#h2", "#h3"], {{ opacity: 0, y: -60, duration: 0.22, ease: "power2.in", stagger: 0.04 }}, {S2-0.3:.2f});')
J(f'tl.to(["#h-s1", "#h-s2"], {{ opacity: 0, y: 300, duration: 0.25, ease: "power2.in" }}, {S2-0.3:.2f});'); snd.append(("whoosh",S2-0.1))
# S2 mission card 2.4-5.0
J(f'tl.fromTo("#m-dim", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.25, ease: "none", immediateRender: false }}, {S2-0.1:.2f});')
J(f'tl.fromTo("#bar-t", {{ y: -230 }}, {{ y: 0, duration: 0.3, ease: "power3.out", immediateRender: false }}, {S2-0.1:.2f});')
J(f'tl.fromTo("#bar-b", {{ y: 230 }}, {{ y: 0, duration: 0.3, ease: "power3.out", immediateRender: false }}, {S2-0.1:.2f});')
fade_in("#m1",S2+0.15,0.2,0); slap("#m2",S2+0.55,-4,1.5,0.22,"impact")
fade_in("#m3",S2+0.9); fade_in("#m4",S2+1.1)
S3=5.0
J(f'tl.to(["#m1", "#m2", "#m3", "#m4", "#m-dim"], {{ opacity: 0, duration: 0.2, ease: "power2.in" }}, {S3-0.22:.2f});')
J(f'tl.to("#bar-t", {{ y: -230, duration: 0.25, ease: "power2.in" }}, {S3-0.22:.2f});'); J(f'tl.to("#bar-b", {{ y: 230, duration: 0.25, ease: "power2.in" }}, {S3-0.22:.2f});')
# S3 phone 5.0-7.9
J(f'tl.fromTo("#phone", {{ y: 1300, rotation: 8 }}, {{ y: 0, rotation: -3, duration: 0.4, ease: "back.out(1.3)", immediateRender: false }}, {S3:.2f});'); snd.append(("whoosh",S3+0.1))
slap("#b1",S3+0.6,0,1.25,0.16,"notify"); slap("#b2",S3+1.15,0,1.25,0.16,"notify2"); slap("#b3",S3+1.6,0,1.2,0.16,None)
S4=7.9
J(f'tl.to("#phone", {{ scale: 2.4, y: 300, opacity: 0, duration: 0.3, ease: "power2.in" }}, {S4-0.3:.2f});'); snd.append(("whoosh",S4-0.1))
# S4 map 7.9-10.9
J(f'tl.fromTo("#map", {{ clipPath: "circle(0% at 50% 60%)" }}, {{ clipPath: "circle(120% at 50% 60%)", duration: 0.35, ease: "power2.in", immediateRender: false }}, {S4-0.2:.2f});')
slap("#mapcap",S4+0.3,-2,1.3,0.18,"click")
RT=[(230,1240),(230,990),(560,990),(560,720),(860,720),(860,540)]
L=sum(math.dist(RT[i],RT[i+1]) for i in range(len(RT)-1))
J(f'tl.fromTo("#route", {{ strokeDashoffset: {L:.0f} }}, {{ strokeDashoffset: 0, duration: 1.6, ease: "power1.inOut", immediateRender: false }}, {S4+0.4:.2f});')
xs=[p[0]-30 for p in RT]; ys=[p[1]-30 for p in RT]
J(f'tl.fromTo("#arrow", {{ x: {xs[0]}, y: {ys[0]} }}, {{ keyframes: {{ x: {xs}, y: {ys} }}, duration: 1.6, ease: "none", immediateRender: false }}, {S4+0.4:.2f});')
slap("#pin",S4+2.05,0,1.6,0.2,"pop")
J(f'tl.to("#pin", {{ y: -16, duration: 0.3, ease: "sine.inOut", yoyo: true, repeat: 1 }}, {S4+2.3:.2f});')
S5=10.9
J(f'tl.to("#map", {{ clipPath: "circle(0% at 80% 28%)", duration: 0.3, ease: "power2.in" }}, {S5-0.3:.2f});'); snd.append(("whoosh",S5-0.1))
# S5 pickups 10.9-14.5
LOOT=[("gamer-girl",150,450,-5),("y2k",630,450,5),("retro",150,880,4),("muzik",630,880,-4)]
slap("#lcap",S5+0.2,-2,1.3,0.18,None)
for i,(n,x,y,r) in enumerate(LOOT):
    J(f'tl.fromTo("#l{i}", {{ y: 400, opacity: 0, rotation: {r} }}, {{ y: 0, opacity: 1, rotation: {r}, duration: 0.3, ease: "back.out(1.6)", immediateRender: false }}, {S5+i*0.08:.2f});')
    J(f'tl.fromTo("#lr{i}", {{ opacity: 0, scale: 0.6 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "power2.out", immediateRender: false }}, {S5+i*0.08:.2f});')
    tc=S5+0.9+i*0.6; b0=S5+0.35+i*0.08; avail=tc-b0-0.02; cyc=max(1,int(avail/0.9)); d=avail/(2*cyc)
    J(f'tl.to("#l{i}", {{ y: -18, duration: {d:.3f}, ease: "sine.inOut", yoyo: true, repeat: {2*cyc-1} }}, {b0:.2f});')
    J(f'tl.to("#l{i}", {{ scale: 0.15, x: {900-(x+150)+i*0}, y: {200-(y+200)}, opacity: 0, rotation: {r+180}, duration: 0.3, ease: "power3.in" }}, {tc:.2f});')
    J(f'tl.to("#lr{i}", {{ opacity: 0, scale: 1.6, duration: 0.3, ease: "power2.out" }}, {tc:.2f});')
    J(f'tl.fromTo("#lb{i}", {{ opacity: 0.9, scale: 0.3 }}, {{ opacity: 0, scale: 1.5, duration: 0.45, ease: "power2.out", immediateRender: false }}, {tc:.2f});')
    J(f'tl.fromTo("#star{i}", {{ fill: "rgba(255,255,255,0)", scale: 1 }}, {{ fill: "{GOLD}", scale: 1.35, duration: 0.12, ease: "power2.out", immediateRender: false }}, {tc+0.3:.2f});')
    J(f'tl.to("#star{i}", {{ scale: 1, duration: 0.15, ease: "power2.inOut" }}, {tc+0.42:.2f});')
    snd.append(("sparkle-soft",tc+0.05)); snd.append(("click",tc+0.3))
tc=S5+0.9+4*0.6
J(f'tl.fromTo("#star4", {{ fill: "rgba(255,255,255,0)", scale: 1 }}, {{ fill: "{GOLD}", scale: 1.35, duration: 0.12, ease: "power2.out", immediateRender: false }}, {tc:.2f});'); J(f'tl.to("#star4", {{ scale: 1, duration: 0.15 }}, {tc+0.12:.2f});'); snd.append(("click",tc))
J(f'tl.to("#stars", {{ keyframes: {{ x: [0, -10, 10, -6, 4, 0] }}, duration: 0.3, ease: "none" }}, {tc+0.05:.2f});')
S6=14.6
J(f'tl.to(["#lcap", "#stars"], {{ opacity: 0, duration: 0.2, ease: "power2.in" }}, {S6-0.2:.2f});')
# S6 mission passed 14.6-16.9
J(f'tl.fromTo("#p-dim", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, ease: "none", immediateRender: false }}, {S6-0.1:.2f});')
slap("#p1",S6+0.25,-3,1.7,0.24,"impact")
fade_in("#p2",S6+0.65,0.2,20); fade_in("#p3",S6+0.85,0.2,20); snd.append(("pop",S6+0.7)); snd.append(("pop",S6+0.9))
J(f'tl.fromTo("#p-burst", {{ opacity: 0.85, scale: 0.4, rotation: 0 }}, {{ opacity: 0, scale: 1.6, rotation: 40, duration: 0.6, ease: "power2.out", immediateRender: false }}, {S6+0.22:.2f});')
S7=17.0
J(f'tl.to(["#p1", "#p2", "#p3"], {{ opacity: 0, y: -60, duration: 0.2, ease: "power2.in", stagger: 0.04 }}, {S7-0.3:.2f});')
J(f'tl.to("#p-dim", {{ opacity: 0, duration: 0.25, ease: "none" }}, {S7-0.2:.2f});'); snd.append(("whoosh",S7-0.05))
# S7 end card
slap("#e-mark",S7+0.25,-3,1.45,0.22,"impact")
fade_in("#e1",S7+0.5); slap("#e2",S7+0.85,-2,1.3,0.18,"pop"); slap("#e3",S7+1.1,2,1.3,0.18,"pop"); fade_in("#e4",S7+1.3)
for i in range(2): J(f'tl.fromTo("#e-s{i}", {{ y: 500, rotation: {(-12,12)[i]} }}, {{ y: 0, rotation: {(-8,8)[i]}, duration: 0.4, ease: "back.out(1.4)", immediateRender: false }}, {S7+0.6+i*0.12:.2f});')
snd.append(("sparkle",S7+0.4))
TOTAL=round(S7+5.0,1)
js="\n    ".join(js)
NG=10
grid_static="".join(f'<line x1="540" y1="-30" x2="{540+k*260}" y2="740" stroke="rgba(255,79,154,0.85)" stroke-width="4"/>' for k in range(-9,10))
grid_h="".join(f'<line id="gh{i}" x1="0" y1="0" x2="1080" y2="0" stroke="rgba(255,79,154,0.9)" stroke-width="3"/>' for i in range(NG))

def sheet(id_,n,x,y,w,extra=""):
    return f'<div id="{id_}" class="sh" style="left: {x}px; top: {y}px; width: {w}px; height: {round(w*1.34)}px; background-image: url(assets/sheets/{n}.webp){extra}"></div>'
STAR='<svg viewBox="0 0 100 100" width="84" height="84" style="overflow: visible"><path id="star{i}" d="M50 6 L62 38 L96 38 L68 58 L79 92 L50 72 L21 92 L32 58 L4 38 L38 38 Z" fill="rgba(255,255,255,0)" stroke="#ffffff" stroke-width="6" stroke-linejoin="round" style="transform-origin: 50px 50px"/></svg>'
loot="".join(f'<div id="lr{i}" class="ring" style="left: {x+20}px; top: {y+380}px"></div><div id="lb{i}" class="lburst" style="left: {x-50}px; top: {y-20}px"></div>'+sheet(f"l{i}",n,x,y,300,"; opacity: 0") for i,(n,x,y,r) in enumerate(LOOT))
pts=" ".join(f"{x},{y}" for x,y in RT)
roads="".join(f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="#3a4170" stroke-width="34" stroke-linecap="round"/>' for a,b,c,d in
  [(230,1500,230,300),(560,1500,560,300),(860,1500,860,300),(80,990,1000,990),(80,720,1000,720),(80,540,1000,540),(80,1240,1000,1240)])
blocks="".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#2a2f55"/>' for x,y,w,h in
  [(270,560,250,120),(600,560,220,120),(270,760,250,190),(600,760,220,190),(270,1030,250,170),(600,1030,220,170),(900,760,150,190),(900,1030,150,170),(80,760,110,190),(80,560,110,120)])

html=f'''<template>
  <style>
    @font-face {{ font-family: "Pacifico"; src: url("assets/fonts/Pacifico-Regular.ttf") format("truetype"); font-weight: 400; }}
    #root {{ position: absolute; inset: 0; overflow: hidden; background: #1a0b3d; font-family: "Nunito", sans-serif; color: #ffffff; }}
    .slot {{ position: absolute; inset: 0; z-index: 2; }}
    #sky {{ position: absolute; inset: 0; background: linear-gradient(180deg, #170a38 0%, #3d1466 30%, #a52c86 56%, #ff6f8a 70%, #ffb46b 80%); }}
    #sun {{ position: absolute; left: 240px; top: 880px; width: 600px; height: 600px; border-radius: 50%;
      background: linear-gradient(180deg, #ffe27a 0%, #ff9f5a 45%, #ff4f9a 100%);
      -webkit-mask-image: linear-gradient(180deg, #000 0 30%, transparent 30% 32%, #000 32% 37%, transparent 37% 40%, #000 40% 44%, transparent 44% 48%, #000 48% 51%, transparent 51% 56%, #000 56%);
      mask-image: linear-gradient(180deg, #000 0 48%, transparent 48% 52%, #000 52% 58%, transparent 58% 62%, #000 62% 67%, transparent 67% 72%, #000 72% 76%, transparent 76% 82%, #000 82% 85%, transparent 85%); }}
    #floor {{ position: absolute; left: 0; top: 1180px; width: 1080px; height: 740px; overflow: hidden; background: #1a0b2e; z-index: 0; isolation: isolate; }}
    #plane-unused {{ position: absolute; left: -1000px; top: -40px; width: 3080px; height: 1400px; transform: perspective(520px) rotateX(64deg); transform-origin: 50% 0%; }}
    #grid-move-unused {{ position: absolute; left: 0; top: -480px; width: 100%; height: 2400px;
      background-image: linear-gradient(rgba(255,79,154,0.85) 4px, transparent 4px), linear-gradient(90deg, rgba(255,79,154,0.85) 4px, transparent 4px);
      background-size: 120px 120px; }}
    #horizon {{ position: absolute; z-index: 1; left: 0; top: 1176px; width: 1080px; height: 8px; background: #ff7ab8; box-shadow: 0 0 24px 6px rgba(255,79,154,0.8); }}
    .sh {{ position: absolute; background-size: contain; background-repeat: no-repeat; background-position: center; filter: drop-shadow(0px 16px 22px rgba(0,0,0,0.45)); }}
    .center {{ position: absolute; left: 0; right: 0; text-align: center; }}
    .neon {{ text-shadow: 0 0 10px rgba(255,79,154,0.9), 0 0 28px rgba(255,79,154,0.7), 0 6px 0 #3d1466; }}
    #h1 {{ display: inline-block; position: relative; font-family: "Archivo Black", sans-serif; font-size: 150px; line-height: 0.95; }}
    #h2 {{ display: inline-block; position: relative; font-family: "Pacifico", cursive; font-size: 84px; line-height: 1.2; color: {GOLD}; text-shadow: 0 5px 0 #3d1466; }}
    .lab {{ display: inline-block; position: relative; padding: 16px 32px 20px; background: #ffffff; color: {NAVY}; border: 8px solid {NAVY}; border-radius: 20px;
      box-shadow: 0 10px 18px rgba(0,0,0,0.35); font-family: "Archivo Black", sans-serif; font-size: 50px; line-height: 1; white-space: nowrap; }}
    #m-dim, #p-dim {{ position: absolute; inset: 0; background: rgba(15,6,35,0.72); opacity: 0; }}
    .bar {{ position: absolute; left: 0; width: 1080px; height: 200px; background: #000000; }}
    #m1 {{ display: inline-block; position: relative; font-family: "Archivo Black", sans-serif; font-size: 50px; letter-spacing: 0.18em; color: #ff8fc0; opacity: 0; }}
    #m2 {{ display: inline-block; position: relative; font-family: "Pacifico", cursive; font-size: 128px; line-height: 1.25; opacity: 0; }}
    .mline {{ display: inline-block; position: relative; font-weight: 900; font-size: 46px; line-height: 1.2; opacity: 0; }}
    #phone {{ position: absolute; left: 270px; top: 330px; width: 540px; height: 1000px; border-radius: 64px; background: #101425; border: 14px solid #2d3350;
      box-shadow: 0 30px 60px rgba(0,0,0,0.5); overflow: hidden; }}
    #ph-head {{ position: absolute; left: 0; right: 0; top: 0; height: 170px; background: #1c2138; display: flex; align-items: center; gap: 22px; padding: 50px 30px 0; }}
    .avatar {{ width: 84px; height: 84px; border-radius: 50%; background: {SALMON}; color: {NAVY}; display: flex; align-items: center; justify-content: center;
      font-family: "Lato", sans-serif; font-weight: 900; font-size: 34px; }}
    .bub {{ position: absolute; left: 30px; max-width: 440px; padding: 22px 28px; border-radius: 30px 30px 30px 8px; background: #2a3152; font-weight: 800; font-size: 40px;
      line-height: 1.15; opacity: 0; transform-origin: 0% 100%; }}
    #map {{ position: absolute; inset: 0; background: #1e2240; clip-path: circle(0% at 50% 60%); }}
    #arrow {{ position: absolute; left: 0; top: 0; width: 60px; height: 60px; }}
    #pin {{ position: absolute; left: 790px; top: 330px; width: 140px; opacity: 0; text-align: center; transform-origin: 50% 100%; }}
    .ring {{ position: absolute; width: 260px; height: 70px; border-radius: 50%; border: 6px solid rgba(255,214,107,0.9); box-shadow: 0 0 26px rgba(255,214,107,0.8); opacity: 0; }}
    .lburst {{ position: absolute; width: 400px; height: 440px; opacity: 0;
      background: repeating-conic-gradient(from 0deg, rgba(255,214,107,0.9) 0deg 8deg, transparent 8deg 26deg);
      -webkit-mask-image: radial-gradient(circle, #000 0%, #000 40%, transparent 68%); mask-image: radial-gradient(circle, #000 0%, #000 40%, transparent 68%); }}
    #stars {{ position: absolute; left: 0; right: 0; top: 186px; display: flex; justify-content: center; gap: 14px; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.4)); }}
    #p1 {{ display: inline-block; position: relative; font-family: "Archivo Black", sans-serif; font-size: 118px; line-height: 0.98; color: {GOLD}; opacity: 0;
      text-shadow: 0 6px 0 #3d1466, 0 0 30px rgba(255,214,107,0.6); }}
    .pline {{ display: inline-block; position: relative; font-weight: 900; font-size: 60px; line-height: 1.2; opacity: 0; }}
    .pplus {{ color: #7cf2a5; }}
    #p-burst {{ position: absolute; left: 40px; top: 260px; width: 1000px; height: 1000px; opacity: 0;
      background: repeating-conic-gradient(from 0deg, rgba(255,214,107,0.55) 0deg 7deg, transparent 7deg 22deg);
      -webkit-mask-image: radial-gradient(circle, #000 0%, #000 35%, transparent 66%); mask-image: radial-gradient(circle, #000 0%, #000 35%, transparent 66%); }}
    #e-mark {{ display: inline-block; position: relative; padding: 28px 46px 32px; background: {NAVY}; border: 14px solid #ffffff; border-radius: 30px; opacity: 0;
      box-shadow: 0 10px 20px rgba(0,0,0,0.35); font-family: "Lato", sans-serif; font-weight: 900; font-size: 96px; line-height: 1; white-space: nowrap; }}
    #e1 {{ display: inline-block; position: relative; font-family: "Pacifico", cursive; font-size: 84px; line-height: 1.2; opacity: 0; }}
    .chip {{ display: inline-block; position: relative; padding: 16px 30px 20px; border: 10px solid #ffffff; border-radius: 18px; opacity: 0;
      box-shadow: 0 8px 14px rgba(0,0,0,0.3); font-weight: 900; font-size: 48px; line-height: 1; white-space: nowrap; color: {NAVY}; }}
    #e4 {{ display: inline-block; position: relative; padding: 10px 26px 14px; border-radius: 16px; background: rgba(23,10,56,0.82); font-weight: 900; font-size: 42px; line-height: 1.2; opacity: 0; }}
  </style>

  <div id="root" data-composition-id="gta" data-width="1080" data-height="1920">
    <div id="sky"></div>
    <div id="sun" data-layout-ignore></div>
    <div id="floor" data-layout-ignore><svg viewBox="0 0 1080 740" width="1080" height="740" style="position: absolute; left: 0; top: 0">{grid_static}{grid_h}</svg></div>
    <div id="horizon" data-layout-ignore></div>
    <svg viewBox="0 0 1080 1920" width="1080" height="1920" style="position: absolute; left: 0; top: 0; z-index: 1" data-layout-ignore>{palm(70,1250,720,1)}{palm(1010,1250,640,-1)}</svg>

    <div id="s1" class="slot clip" data-start="0" data-duration="2.45" data-track-index="1">
      <div class="center" style="top: 230px"><div id="h1" class="neon">GTA 6<br>ÇIKTI!</div></div>
      <div class="center" style="top: 530px"><div id="h2">Herkes oyunda…</div></div>
      <div class="center" style="top: 680px"><div id="h3" class="lab">Bizim de bir görevimiz var</div></div>
      <div data-layout-ignore>{sheet("h-s1","gamer-girl",130,870,380,"")}{sheet("h-s2","y2k",570,900,380,"")}</div>
    </div>

    <div id="s2" class="slot clip" data-start="{S2-0.12:.2f}" data-duration="{S3-S2+0.12:.2f}" data-track-index="2">
      <div id="m-dim"></div>
      <div id="bar-t" class="bar" style="top: 0"></div><div id="bar-b" class="bar" style="top: 1720px"></div>
      <div class="center" style="top: 640px"><div id="m1">YENİ GÖREV</div></div>
      <div class="center" style="top: 720px"><div id="m2" class="neon">Ajandayı Kurtar</div></div>
      <div class="center" style="top: 960px"><div id="m3" class="mline">Hedef: Malibu Craft</div></div>
      <div class="center" style="top: 1030px"><div id="m4" class="mline" style="color: {GOLD}">Ödül: 33 yeni tasarım</div></div>
    </div>

    <div id="s3" class="slot clip" data-start="{S3-0.02:.2f}" data-duration="{S4-S3+0.04:.2f}" data-track-index="3">
      <div id="phone" data-layout-allow-overflow>
        <div id="ph-head"><div class="avatar">MC</div><div><div style="font-weight: 900; font-size: 40px; line-height: 1.1">Malibu Craft</div><div style="font-weight: 700; font-size: 28px; color: #9aa3c7">çevrimiçi</div></div></div>
        <div id="b1" class="bub" style="top: 220px">Yeni setler geldi!</div>
        <div id="b2" class="bub" style="top: 340px">Konum attım, hemen gel.</div>
        <div id="b3" class="bub" style="top: 520px; padding: 14px; background: #2a3152">
          <div style="width: 400px; height: 220px; border-radius: 20px; background: #1e2240; position: relative; overflow: hidden">
            <div style="position: absolute; left: 0; top: 100px; width: 400px; height: 24px; background: #3a4170"></div>
            <div style="position: absolute; left: 180px; top: 0; width: 24px; height: 220px; background: #3a4170"></div>
            <svg viewBox="0 0 40 52" width="52" style="position: absolute; left: 166px; top: 40px"><path d="M20 50 C 8 34, 2 26, 2 18 A 18 18 0 0 1 38 18 C 38 26, 32 34, 20 50 Z" fill="{SALMON}" stroke="#fff" stroke-width="3"/><circle cx="20" cy="18" r="7" fill="{NAVY}"/></svg>
          </div>
          <div style="padding: 14px 10px 6px; font-weight: 900; font-size: 34px">Malibu Craft · Konum</div>
        </div>
      </div>
    </div>

    <div id="s4" class="slot clip" data-start="{S4-0.22:.2f}" data-duration="{S5-S4+0.24:.2f}" data-track-index="4">
      <div id="map" data-layout-allow-overflow>
        <svg viewBox="0 0 1080 1920" width="1080" height="1920" style="position: absolute; left: 0; top: 0" data-layout-ignore>
          <path d="M0 1320 Q 300 1270, 520 1360 T 1080 1330 V1920 H0 Z" fill="#1f6f8b"/>
          <path d="M0 1320 Q 300 1270, 520 1360 T 1080 1330" stroke="#f3d9a4" stroke-width="22" fill="none"/>
          {blocks}{roads}
          <polyline id="route" points="{pts}" fill="none" stroke="{PINK}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"
            stroke-dasharray="{L:.0f}" stroke-dashoffset="{L:.0f}" style="filter: drop-shadow(0 0 8px rgba(255,79,154,0.9))"/>
        </svg>
        <svg id="arrow" viewBox="0 0 60 60" data-layout-ignore><circle cx="30" cy="30" r="26" fill="#ffffff"/><path d="M30 12 L44 44 L30 36 L16 44 Z" fill="{NAVY}"/></svg>
        <div id="pin" data-layout-allow-overlap>
          <svg viewBox="0 0 40 52" width="110"><path d="M20 50 C 8 34, 2 26, 2 18 A 18 18 0 0 1 38 18 C 38 26, 32 34, 20 50 Z" fill="{SALMON}" stroke="#fff" stroke-width="3"/><circle cx="20" cy="18" r="7" fill="{NAVY}"/></svg>
        </div>
        <div class="center" style="top: 186px"><div id="mapcap" class="lab" style="opacity: 0">Rota: Malibu Craft</div></div>
      </div>
    </div>

    <div id="s5" class="slot clip" data-start="{S5-0.05:.2f}" data-duration="{S6-S5+0.05:.2f}" data-track-index="5">
      <div id="stars">{"".join(STAR.format(i=i) for i in range(5))}</div>
      <div class="center" style="top: 300px"><div id="lcap" class="lab" style="opacity: 0">Herkes setini soruyor!</div></div>
      <div data-layout-ignore>{loot}</div>
    </div>

    <div id="s6" class="slot clip" data-start="{S6-0.12:.2f}" data-duration="{S7-S6+0.12:.2f}" data-track-index="6">
      <div id="p-dim"></div>
      <div id="p-burst" data-layout-ignore></div>
      <div class="center" style="top: 560px"><div id="p1">GÖREV<br>TAMAMLANDI!</div></div>
      <div class="center" style="top: 870px"><div id="p2" class="pline">Ajanda <span class="pplus">+100</span></div></div>
      <div class="center" style="top: 950px"><div id="p3" class="pline">Stil <span class="pplus">+100</span></div></div>
    </div>

    <div id="s7" class="slot clip" data-start="{S7-0.02:.2f}" data-duration="{TOTAL-S7+0.02:.2f}" data-track-index="7">
      <div class="center" style="top: 200px"><div id="e-mark"><span style="color: #e8bcac">MALIBU</span> <span style="color: #ffffff">CRAFT</span></div></div>
      <div class="center" style="top: 420px"><div id="e1" class="neon">Görevin: setini seç!</div></div>
      <div class="center" style="top: 600px"><div id="e2" class="chip" style="background: {GOLD}">Tanesi 64,90 TL</div></div>
      <div class="center" style="top: 720px"><div id="e3" class="chip" style="background: {SALMON}">shopier.com/malibucraftshop</div></div>
      <div class="center" style="top: 850px"><div id="e4">Kişiye özel tasarımlar için DM</div></div>
      <div data-layout-ignore>{sheet("e-s0","gamer-girl",150,1000,340,"")}{sheet("e-s1","y2k",590,1000,340,"")}</div>
    </div>
  </div>

  <script>
    function placeGrid(p) {{
      for (let i = 0; i < {NG}; i++) {{
        const u = ((i + p) % {NG}) / {NG};
        const y = 740 * Math.pow(u, 2.1);
        const el = document.getElementById("gh" + i);
        if (!el) continue;
        el.setAttribute("y1", y.toFixed(1)); el.setAttribute("y2", y.toFixed(1));
        el.setAttribute("stroke-width", (2 + 6 * u).toFixed(1)); el.setAttribute("opacity", Math.min(1, 0.25 + u * 1.2).toFixed(2));
      }}
    }}
    const tl = gsap.timeline({{ paused: true }});
    {js}
    window.__timelines["gta"] = tl;
  </script>
</template>
'''
open(f"{P}/compositions/gta.html","w").write(html)

F=1/30
SFX={"whoosh":("whoosh",0.162,0.57,0.18),"pop":("pop",0.119,0.72,0.22),"impact":("impact-bass-1",0.073,2.1,0.3),"click":("click",0.072,0.37,0.16),
     "sparkle":("sparkle",0.0,1.8,0.18),"sparkle-soft":("sparkle",0.0,1.0,0.1),"notify":("notification",0.241,1.2,0.2),"notify2":("notification",0.241,1.2,0.16)}
lines=[]
for i,(kind,t) in enumerate(snd):
    f,pk,d,v=SFX[kind]; st=round(max(0,t-pk+(F if pk else 0)),3)
    lines.append(f'      <audio id="sfx-{i}" class="clip" src="assets/sfx/{f}.mp3" data-start="{st}" data-duration="{d}" data-track-index="{40+i}" data-volume="{v}"></audio>')
root=f'''<!doctype html>
<html lang="tr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #1a0b3d; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
      <div id="gta-host" data-composition-id="gta" data-composition-src="compositions/gta.html" data-start="0" data-duration="{TOTAL}"
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
print("total",TOTAL,"sfx",len(lines))
