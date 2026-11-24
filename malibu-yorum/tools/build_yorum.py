# Malibu Craft "Birkaç kötü yorum aldık…" — 1-star "complaints" that are really praise (humblebrag trend), swiped like a carousel.
import os
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAVY="#29314b"; SALMON="#e1a8a4"; KRAFT="#d8b38a"; CREAM="#fbf7ee"; GOLD="#f2b01e"
# Personas are clearly characters (no realistic customer names); every joke rests on a true product fact.
REVIEWS=[("A","Ajanda Bağımlısı","Bir sticker yapıştırayım dedim, bütün ajanda doldu. Yenisini almam lazım.","#efe8f7"),
         ("K","Kararsız Müşteri","Parlak mı mat mı seçemedim. İkisini de aldım, bütçem bitti.","#f6d6d3"),
         ("M","Emekli Makas","Kesimler o kadar düzgün ki makasımı emekliye ayırdım.","#cfeee2"),
         ("T","Toplantı Mağduru","Laptopuma Van Gogh yapıştırdım. Toplantıda kimse sunumu dinlemedi.","#ecdcc4"),
         ("C","Cüzdanı Ağlayan","33 tasarımın hepsini beğendim. Sepetim taştı, cüzdanım ağladı.",NAVY)]
D=3.7; T0=2.8
starts=[T0+i*D for i in range(len(REVIEWS))]
TA=T0+len(REVIEWS)*D          # apology
TB=TA+3.9                     # brand card
TOTAL=round(TB+4.3,1)
js=[]; J=js.append; snd=[]
def slap(sel,t,rot,frm=1.4,d=0.2,kind="pop"):
    J(f'tl.fromTo("{sel}", {{ scale: {frm}, rotation: {rot+8}, opacity: 0 }}, {{ scale: 1, rotation: {rot}, opacity: 1, duration: {d}, ease: "power3.in", immediateRender: false }}, {t-d:.2f});')
    J(f'tl.to("{sel}", {{ scale: 0.96, duration: 0.04, ease: "none" }}, {t:.2f});'); J(f'tl.to("{sel}", {{ scale: 1, duration: 0.12, ease: "power2.out" }}, {t+0.04:.2f});')
    if kind: snd.append((kind,t))
def swipe_in(sel,t): J(f'tl.fromTo("{sel}", {{ x: 1150 }}, {{ x: 0, duration: 0.36, ease: "power3.inOut", immediateRender: false }}, {t-0.36:.2f});')
# in and out share start, length and ease, so the two pages travel together like a carousel strip
def swipe_out(sel,t): J(f'tl.to("{sel}", {{ x: -1150, duration: 0.36, ease: "power3.inOut" }}, {t-0.36:.2f});')

# background colour per scene
J(f'tl.set("#bg", {{ backgroundColor: "{NAVY}" }}, 0);')
for i,(_,_,_,col) in enumerate(REVIEWS): J(f'tl.to("#bg", {{ backgroundColor: "{col}", duration: 0.3, ease: "none" }}, {starts[i]-0.33:.2f});')
J(f'tl.to("#bg", {{ backgroundColor: "{CREAM}", duration: 0.3, ease: "none" }}, {TA-0.33:.2f});')
J(f'tl.to("#bg", {{ backgroundColor: "{NAVY}", duration: 0.3, ease: "none" }}, {TB-0.33:.2f});')

# ---- hook: five stars, four fall off, one is left
for k in range(1,5):
    t=0.45+(4-k)*0.18
    J(f'tl.to("#hs{k}", {{ y: 1700, rotation: {(-1)**k*70}, opacity: 0, duration: 0.6, ease: "power2.in" }}, {t:.2f});')
    J(f'tl.to("#hsf{k}", {{ fill: "#4a5170", duration: 0.05, ease: "none" }}, {t:.2f});')
snd.append(("whoosh",0.75)); snd.append(("impact",1.25))
J('tl.to("#hs0", { scale: 1.25, duration: 0.12, ease: "power2.out", yoyo: true, repeat: 1 }, 1.2);')
J('tl.to("#hook", { keyframes: { x: [0, -14, 12, -8, 5, 0] }, duration: 0.3, ease: "none" }, 1.25);')
J('tl.fromTo("#hsub", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.25, ease: "power3.out", immediateRender: false }, 1.45);')
swipe_out("#hook",T0); snd.append(("whoosh",T0-0.15))

# ---- reviews
for i,(ini,name,text,col) in enumerate(REVIEWS):
    t0=starts[i]
    swipe_in(f"#rv{i}",t0)
    if i: snd.append(("whoosh",t0-0.15))
    J(f'tl.fromTo("#rv{i} .s1", {{ scale: 2.2, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.18, ease: "power3.in", immediateRender: false }}, {t0+0.05:.2f});'); snd.append(("thud",t0+0.23))
    J(f'tl.fromTo("#rv{i} .w", {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: 0.14, stagger: 0.03, ease: "power2.out", immediateRender: false }}, {t0+0.25:.2f});')
    swipe_out(f"#rv{i}",t0+D)
# V0 ajanda overflows with stickers
t0=starts[0]
for k,(rot) in enumerate([-12,10,-6]): slap(f"#v0s{k}",t0+1.0+k*0.35,rot,1.6,0.18,"pop")
J(f'tl.to("#v0page", {{ keyframes: {{ rotation: [-4, -6, -2, -4] }}, duration: 0.5, ease: "none" }}, {t0+1.75:.2f});')
# V1 glossy or matte -> both
t0=starts[1]
for k in range(2): J(f'tl.to("#v1c{k}", {{ rotation: {(-1)**k*7}, duration: 0.3, ease: "sine.inOut", yoyo: true, repeat: 3 }}, {t0+0.4+k*0.15:.2f});')
J(f'tl.fromTo("#v1shine", {{ x: -300 }}, {{ x: 1200, duration: 0.8, ease: "power1.inOut", immediateRender: false }}, {t0+0.5:.2f});')
slap("#v1stamp",t0+1.75,-8,1.8,0.2,"impact")
# V2 the sticker peels off the sheet: clean die-cut edge
t0=starts[2]
J(f'tl.set("#v2cut", {{ transformPerspective: 700, transformOrigin: "50% 100%" }}, 0);')
J(f'tl.to("#v2cut", {{ rotationX: 38, y: -30, duration: 0.35, ease: "power2.out" }}, {t0+0.7:.2f});'); snd.append(("click",t0+0.75))
J(f'tl.to("#v2cut", {{ rotationX: 0, y: -170, x: 170, rotation: -12, scale: 1.5, filter: "drop-shadow(0px 30px 24px rgba(0,0,0,0.35))", duration: 0.5, ease: "power2.inOut" }}, {t0+1.1:.2f});'); snd.append(("whoosh",t0+1.3))
J(f'tl.to("#v2cut", {{ rotation: -4, duration: 0.6, ease: "sine.inOut", yoyo: true, repeat: 2 }}, {t0+1.6:.2f});')
J(f'tl.fromTo("#v2zz", {{ opacity: 0, y: 10 }}, {{ opacity: 1, y: -10, duration: 0.4, ease: "power1.out", immediateRender: false }}, {t0+1.5:.2f});')
J(f'tl.to("#v2sc", {{ rotation: 80, y: 30, duration: 0.5, ease: "back.out(1.5)" }}, {t0+1.3:.2f});')
# V3 laptop lid gets Van Gogh, the meeting looks at it
t0=starts[3]
slap("#v3st",t0+0.75,-6,1.7,0.2,"pop")
slap("#v3b0",t0+1.35,-3,1.3,0.15,"click"); slap("#v3b1",t0+1.8,3,1.3,0.15,"click")
# V4 everything into the cart
t0=starts[4]
for c in range(3): J(f'tl.fromTo("#v4col{c}", {{ y: {-120 if c%2 else -520} }}, {{ y: {-520 if c%2 else -120}, duration: {D+0.6:.2f}, ease: "none", immediateRender: false }}, {t0-0.4:.2f});')
for k in range(5):
    J(f'tl.fromTo("#v4f{k}", {{ x: {[-260,260,-160,200,0][k]}, y: -520, rotation: {[-30,25,-10,15,0][k]}, opacity: 1 }}, {{ x: 0, y: 0, rotation: {[-12,10,-4,8,2][k]}, opacity: 1, duration: 0.3, ease: "power2.in", immediateRender: false }}, {t0+0.6+k*0.22:.2f});')
    snd.append(("pop-soft",t0+0.9+k*0.22))
J(f'tl.to("#v4cart", {{ keyframes: {{ x: [0, -10, 9, -6, 4, 0], rotation: [0, -2, 2, -1, 1, 0] }}, duration: 0.35, ease: "none" }}, {t0+1.75:.2f});')
slap("#v4tasti",t0+1.95,-6,1.6,0.18,"impact")

# ---- apology
swipe_in("#apo",TA)
J(f'tl.fromTo("#apo .aw", {{ opacity: 0, y: 24 }}, {{ opacity: 1, y: 0, duration: 0.2, stagger: 0.12, ease: "power3.out", immediateRender: false }}, {TA+0.05:.2f});')
slap("#acta",TA+1.0,0,1.25,0.18,"pop")
for k in range(3): slap(f"#ad{k}",TA+1.4+k*0.2,[-10,6,-6][k],1.5,0.16,"pop-soft")
J(f'tl.to("#apo", {{ opacity: 0, scale: 0.95, duration: 0.25, ease: "power2.in" }}, {TB-0.25:.2f});'); snd.append(("whoosh",TB-0.1))
# ---- brand card
slap("#bmark",TB+0.25,-3,1.45,0.22,"impact")
slap("#bprice",TB+0.6,-2,1.3,0.18,"pop"); slap("#burl",TB+0.85,2,1.3,0.18,"pop")
J(f'tl.fromTo("#bdm", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, ease: "power1.out", immediateRender: false }}, {TB+1.05:.2f});')
for k in range(3): J(f'tl.fromTo("#bs{k}", {{ y: 600, rotation: {[-16,0,16][k]} }}, {{ y: 0, rotation: {[-10,0,10][k]}, duration: 0.45, ease: "back.out(1.4)", immediateRender: false }}, {TB+0.4+k*0.1:.2f});')
snd.append(("sparkle",TB+0.5))
js="\n    ".join(js)

# ---------------- markup
STARP="M50 6 L62 38 L96 38 L68 58 L79 92 L50 72 L21 92 L32 58 L4 38 L38 38 Z"
def stars(size):
    out=f'<svg class="s1" viewBox="0 0 100 100" width="{size}" height="{size}"><path d="{STARP}" fill="{GOLD}"/></svg>'
    out+="".join(f'<svg viewBox="0 0 100 100" width="{size}" height="{size}"><path d="{STARP}" fill="#d9d3c7"/></svg>' for _ in range(4))
    return f'<div class="stars">{out}</div>'
def words(t): return " ".join(f'<span class="w">{w}</span>' for w in t.split())
def card(i,ini,name,text):
    return f'''<div class="card">
          <div class="chead"><div class="ava">{ini}</div><div><div class="cname">{name}</div>{stars(34)}</div></div>
          <div class="ctext">{words(text)}</div>
          <div class="cfoot"><span>FAYDALI</span><span>PAYLAŞ</span></div>
        </div>
        <div class="count">{i+1}/{len(REVIEWS)}</div>'''
def sheet(id_,n,x,y,w,extra="",cls="sh"):
    return f'<div id="{id_}" class="{cls}" style="left: {x}px; top: {y}px; width: {w}px; height: {round(w*1.34)}px; background-image: url(assets/sheets/{n}.webp){extra}"></div>'
def bgcut(id_,f,x,y,w,h):
    return f'<div id="{id_}" class="cutimg" style="left: {x}px; top: {y}px; width: {w}px; height: {h}px; opacity: 0; background: url(assets/cutouts/{f}.png) center / contain no-repeat"></div>'
def cut(id_,f,x,y,w,extra=""):
    return f'<img id="{id_}" class="cutimg" src="assets/cutouts/{f}.png" alt="" style="left: {x}px; top: {y}px; width: {w}px{extra}" />'

V=[]
V.append(f'''<img id="v0page" class="vis" src="assets/img/ajanda.jpg" alt="" style="left: 300px; top: 650px; width: 480px; transform-origin: 50% 50%" />
        {cut("v0s0","jj-hibiscus",230,1020,210,"; opacity: 0")}{cut("v0s1","lav-pansy",640,700,200,"; opacity: 0")}{cut("v0s2","red-heart",600,1110,190,"; opacity: 0")}''')
V.append(f'''{sheet("v1c0","coquette",110,730,380)}{sheet("v1c1","y2k",590,730,380)}
        <div class="chip" style="left: 170px; top: 645px; background: #ffffff">Parlak mı?</div><div class="chip" style="left: 680px; top: 645px; background: #ffffff">Mat mı?</div>
        <div id="v1shine" class="shine"></div>
        <div id="v1stamp" class="stamp" style="left: 300px; top: 900px">İKİSİ DE!</div>''')
V.append(f'''<div class="vis" style="left: 240px; top: 660px; width: 600px; height: 600px; border-radius: 10px; overflow: visible; box-shadow: 0 18px 30px rgba(0,0,0,0.25)">
          <img src="assets/img/van-gogh-sheet.jpg" alt="" style="position: absolute; inset: 0; width: 600px; height: 600px; border-radius: 10px" />
          <img src="assets/cutouts/vg-portrait-hole.png" alt="" style="position: absolute; left: 227px; top: 152px; width: 139px" />
          <img id="v2cut" src="assets/cutouts/vg-portrait.png" alt="" style="position: absolute; left: 227px; top: 152px; width: 139px; filter: drop-shadow(0px 1px 1px rgba(0,0,0,0.15))" />
        </div>
        <svg id="v2sc" viewBox="0 0 120 120" width="150" style="position: absolute; left: 80px; top: 1150px; transform-origin: 50% 50%">
          <circle cx="30" cy="92" r="18" fill="none" stroke="{NAVY}" stroke-width="9"/><circle cx="90" cy="92" r="18" fill="none" stroke="{NAVY}" stroke-width="9"/>
          <path d="M42 80 L96 8 M78 80 L24 8" stroke="#9aa0b8" stroke-width="10" stroke-linecap="round"/></svg>
        <div id="v2zz" class="zz" style="left: 200px; top: 1090px">Zzz</div>''')
V.append(f'''<svg class="vis" viewBox="0 0 700 560" width="700" style="left: 190px; top: 700px">
          <rect x="50" y="10" width="600" height="400" rx="26" fill="#3b3f4e"/><rect x="66" y="26" width="568" height="368" rx="16" fill="#4a4f62"/>
          <circle cx="350" cy="210" r="22" fill="#5b6177"/>
          <path d="M0 470 L50 410 H650 L700 470 Z" fill="#2c303d"/><rect x="0" y="470" width="700" height="26" rx="10" fill="#22252f"/></svg>
        {cut("v3st","vg-starry",385,780,310,"; opacity: 0")}
        <div id="v3b0" class="bubble" style="left: 90px; top: 640px">Bu ne güzel!</div>
        <div id="v3b1" class="bubble" style="left: 610px; top: 640px">Nereden aldın?</div>''')
cols=[]
for c in range(3):
    names=["coquette","van-gogh","y2k","retro","mistik","kiraz","limon","muzik","gamer-girl","london","sanat","washi"]
    items="".join(f'<div class="wimg" style="background-image: url(assets/sheets/{names[(c*4+j)%len(names)]}.webp)"></div>' for j in range(6))
    cols.append(f'<div id="v4col{c}" class="col" style="left: {60+c*340}px">{items}</div>')
falls="".join(sheet(f"v4f{k}",n,[330,520,420,610,470][k],[960,950,930,920,900][k],150,"; opacity: 0") for k,n in enumerate(["coquette","van-gogh","y2k","retro","mistik"]))
V.append(f'''<div class="wall">{"".join(cols)}</div>
        <div id="v4cart" class="vis" style="left: 250px; top: 860px; width: 640px; height: 470px">
          <div style="position: absolute; inset: 0; transform: translate(-250px, -860px)">{falls}</div>
          <svg viewBox="0 0 640 470" width="640" height="470" style="position: absolute; left: 0; top: 0">
            <path d="M20 40 H120 L170 330 H560 L610 120 H140" fill="none" stroke="#ffffff" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M150 170 H590 M160 250 H575" stroke="#ffffff" stroke-width="8" opacity="0.6"/>
            <circle cx="220" cy="410" r="34" fill="#ffffff"/><circle cx="500" cy="410" r="34" fill="#ffffff"/></svg>
        </div>
        <div id="v4tasti" class="stamp" style="left: 330px; top: 760px; background: {SALMON}; color: {NAVY}">TAŞTI!</div>''')

rv="\n".join(f'''    <div id="rs{i}" class="slot clip" data-start="{starts[i]-0.38:.2f}" data-duration="{D+0.4:.2f}" data-track-index="{2+i}">
      <div id="rv{i}" class="slot" data-layout-allow-overflow>
        {card(i,ini,name,text)}
        <div data-layout-ignore>{V[i]}</div>
      </div>
    </div>''' for i,(ini,name,text,col) in enumerate(REVIEWS))

hookstars="".join(f'<svg id="hs{k}" viewBox="0 0 100 100" width="130" height="130" style="position: relative; display: inline-block"><path id="hsf{k}" d="{STARP}" fill="{GOLD}"/></svg>' for k in range(5))
html=f'''<template>
  <style>
    #root {{ position: absolute; inset: 0; overflow: hidden; font-family: "Nunito", sans-serif; color: {NAVY}; }}
    #bg {{ position: absolute; inset: 0; background: {NAVY}; }}
    .slot {{ position: absolute; inset: 0; }}
    .center {{ position: absolute; left: 0; right: 0; text-align: center; }}
    #hstars {{ position: absolute; left: 0; right: 0; top: 470px; text-align: center; }}
    #hh {{ font-family: "Archivo Black", sans-serif; font-size: 118px; line-height: 1.02; color: #ffffff; }}
    #hsub {{ display: inline-block; position: relative; font-weight: 900; font-size: 48px; color: {SALMON}; opacity: 0; }}
    .card {{ position: absolute; left: 60px; top: 196px; width: 960px; padding: 36px 44px 26px; background: {CREAM}; border-radius: 28px;
      box-shadow: 0 18px 36px rgba(0,0,0,0.25); }}
    .chead {{ display: flex; align-items: center; gap: 22px; }}
    .ava {{ width: 78px; height: 78px; border-radius: 50%; background: {NAVY}; color: #ffffff; display: flex; align-items: center; justify-content: center;
      font-weight: 900; font-size: 38px; flex: none; }}
    .cname {{ font-weight: 900; font-size: 40px; line-height: 1.1; }}
    .stars {{ display: flex; gap: 4px; margin-top: 6px; }}
    .s1 {{ transform-origin: 50% 50%; }}
    .ctext {{ margin-top: 26px; font-weight: 800; font-size: 46px; line-height: 1.24; }}
    .ctext .w {{ display: inline-block; position: relative; opacity: 0; }}
    .cfoot {{ margin-top: 26px; padding-top: 18px; border-top: 3px solid #e6dfd0; display: flex; gap: 60px; font-weight: 900; font-size: 28px;
      letter-spacing: 0.14em; color: #8a8577; }}
    .count {{ position: absolute; left: 912px; top: 168px; padding: 10px 22px; border-radius: 30px; background: rgba(41,49,75,0.85); color: #ffffff;
      font-weight: 900; font-size: 32px; line-height: 1; }}
    .vis {{ position: absolute; }}
    .cutimg {{ position: absolute; filter: drop-shadow(0px 8px 10px rgba(0,0,0,0.3)); }}
    .sh, .wimg {{ background-size: contain; background-repeat: no-repeat; background-position: center; }}
    .sh {{ position: absolute; filter: drop-shadow(0px 14px 20px rgba(0,0,0,0.3)); }}
    .chip {{ position: absolute; padding: 12px 24px 16px; border: 6px solid {NAVY}; border-radius: 16px; font-weight: 900; font-size: 40px; line-height: 1; }}
    .shine {{ position: absolute; left: 0; top: 700px; width: 160px; height: 620px; transform: skewX(-18deg);
      background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.55), rgba(255,255,255,0)); }}
    .stamp {{ position: absolute; padding: 18px 40px 24px; background: {NAVY}; color: #ffffff; border: 12px solid #ffffff; border-radius: 22px; opacity: 0;
      box-shadow: 0 14px 24px rgba(0,0,0,0.35); font-family: "Archivo Black", sans-serif; font-size: 96px; line-height: 1; white-space: nowrap; }}
    .zz {{ position: absolute; font-family: "Archivo Black", sans-serif; font-size: 60px; color: {NAVY}; opacity: 0; }}
    .bubble {{ position: absolute; padding: 18px 28px 22px; background: #ffffff; border: 6px solid {NAVY}; border-radius: 30px 30px 30px 6px; opacity: 0;
      box-shadow: 0 8px 14px rgba(0,0,0,0.2); font-weight: 900; font-size: 42px; line-height: 1; white-space: nowrap; }}
    .wall {{ position: absolute; left: 0; top: 640px; width: 1080px; height: 720px; overflow: hidden; opacity: 0.35; }}
    .col {{ position: absolute; top: 0; width: 300px; display: flex; flex-direction: column; gap: 24px; }}
    .wimg {{ width: 300px; height: 402px; flex: none; }}
    #apo {{ position: absolute; inset: 0; }}
    .aw {{ position: relative; opacity: 0; }}
    #a1 {{ font-weight: 900; font-size: 36px; letter-spacing: 0.3em; color: #b06a64; }}
    #a2 {{ font-family: "Archivo Black", sans-serif; font-size: 86px; line-height: 1.04; color: {NAVY}; }}
    #a3 {{ font-weight: 800; font-size: 48px; color: {NAVY}; }}
    #acta {{ display: inline-block; position: relative; padding: 22px 34px 26px; background: {NAVY}; color: #ffffff; border-radius: 14px; opacity: 0;
      font-weight: 900; font-size: 38px; line-height: 1.2; }}
    #bmark {{ display: inline-block; position: relative; padding: 28px 46px 32px; background: {NAVY}; border: 14px solid #ffffff; border-radius: 30px; opacity: 0;
      box-shadow: 0 10px 20px rgba(0,0,0,0.35); font-family: "Lato", sans-serif; font-weight: 900; font-size: 96px; line-height: 1; white-space: nowrap; }}
    .bchip {{ display: inline-block; position: relative; padding: 16px 30px 20px; border: 10px solid #ffffff; border-radius: 18px; opacity: 0;
      box-shadow: 0 8px 14px rgba(0,0,0,0.3); font-weight: 900; font-size: 48px; line-height: 1; white-space: nowrap; color: {NAVY}; }}
    #bdm {{ font-weight: 900; font-size: 42px; color: #ffffff; opacity: 0; }}
  </style>

  <div id="root" data-composition-id="yorum" data-width="1080" data-height="1920">
    <div id="bg"></div>

    <div id="hooks" class="slot clip" data-start="0" data-duration="{T0+0.02:.2f}" data-track-index="1">
      <div id="hook" class="slot" data-layout-allow-overflow>
        <div id="hstars" data-layout-ignore>{hookstars}</div>
        <div class="center" style="top: 660px"><div id="hh">Birkaç kötü<br>yorum aldık…</div></div>
        <div class="center" style="top: 930px"><div id="hsub">Hepsini dürüstçe paylaşıyoruz.</div></div>
      </div>
    </div>

{rv}

    <div id="as" class="slot clip" data-start="{TA-0.38:.2f}" data-duration="{TB-TA+0.4:.2f}" data-track-index="8">
      <div id="apo" data-layout-allow-overflow>
        <div class="center" style="top: 470px"><div id="a1" class="aw">ÖZÜR DİLERİZ</div></div>
        <div class="center" style="top: 550px"><div id="a2" class="aw">Daha sıradan<br>stickerlar yapmayı<br>deneyeceğiz.</div></div>
        <div class="center" style="top: 880px"><div id="a3" class="aw">Ama elimiz gitmiyor.</div></div>
        <div class="center" style="top: 990px"><div id="acta">Bu mağduriyeti yaşaması gereken<br>arkadaşını etiketle</div></div>
        <div data-layout-ignore>{bgcut("ad0","vg-portrait",140,1180,220,245)}{bgcut("ad1","jj-hibiscus",430,1230,200,188)}{bgcut("ad2","red-heart",720,1180,210,198)}</div>
      </div>
    </div>

    <div id="bs" class="slot clip" data-start="{TB-0.05:.2f}" data-duration="{TOTAL-TB+0.05:.2f}" data-track-index="9">
      <div class="center" style="top: 230px"><div id="bmark"><span style="color: #e8bcac">MALIBU</span> <span style="color: #ffffff">CRAFT</span></div></div>
      <div class="center" style="top: 480px"><div id="bprice" class="bchip" style="background: {KRAFT}">33 yeni tasarım · Tanesi 64,90 TL</div></div>
      <div class="center" style="top: 610px"><div id="burl" class="bchip" style="background: {SALMON}">shopier.com/malibucraftshop</div></div>
      <div class="center" style="top: 750px"><div id="bdm">Kişiye özel tasarımlar için DM</div></div>
      <div data-layout-ignore>{sheet("bs0","coquette",90,1010,320)}{sheet("bs1","van-gogh",380,960,320)}{sheet("bs2","y2k",670,1010,320)}</div>
    </div>
  </div>

  <script>
    const tl = gsap.timeline({{ paused: true }});
    {js}
    window.__timelines["yorum"] = tl;
  </script>
</template>
'''
open(f"{P}/compositions/yorum.html","w").write(html)

F=1/30
SFX={"whoosh":("whoosh",0.162,0.57,0.18),"pop":("pop",0.119,0.72,0.22),"pop-soft":("pop",0.119,0.72,0.12),"impact":("impact-bass-1",0.073,2.1,0.3),
     "thud":("impact-bass-1",0.073,1.2,0.18),"click":("click",0.072,0.37,0.16),"sparkle":("sparkle",0.0,1.8,0.18)}
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
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: {NAVY}; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
      <div id="yorum-host" data-composition-id="yorum" data-composition-src="compositions/yorum.html" data-start="0" data-duration="{TOTAL}"
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
print("reviews",starts,"apology",TA,"brand",TB,"total",TOTAL,"sfx",len(lines))
