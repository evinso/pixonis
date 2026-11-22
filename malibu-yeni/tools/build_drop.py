# Malibu Craft "Yeni stickerlar geldi" — energetic drop Reel, cut to a 120 BPM grid (one beat = 0.5 s).
import os
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAVY="#29314b"; SALMON="#e1a8a4"; KRAFT="#d8b38a"; B=0.5
FAN=["coquette","y2k","van-gogh","retro","mistik"]
GROUPS=[("Pembe sevenlere","#f3b3c0",["coquette","gamer-girl","junk-journal","altin-cerceve"]),
        ("Sanat sevenlere",NAVY,["van-gogh","van-gogh-2","sanat","vintage-kagit"]),
        ("Retro ruhlara","#a8dcc6",["y2k","retro","muzik","kamera"]),
        ("Mizah sevenlere","#ffd45c",["hic-halim-yok","geliyorum","tatli-komik","motivasyon"])]
ALL=["coquette","gamer-girl","junk-journal","altin-cerceve","van-gogh","van-gogh-2","sanat","vintage-kagit","y2k","retro","muzik","kamera",
     "hic-halim-yok","geliyorum","tatli-komik","motivasyon","washi","vintage-journal","cerceve","london","kiraz","limon","mistik"]
HERO=["kiraz","limon","mistik"]
js=[]; J=js.append; snd=[]   # snd: (kind, picture time)
def shake(t,amp=14):
    J(f'tl.to("#dr-cam", {{ keyframes: {{ x: [0, {-amp}, {amp*0.8:.0f}, {-amp*0.5:.0f}, {amp*0.3:.0f}, 0], y: [0, {amp*0.6:.0f}, {-amp*0.7:.0f}, {amp*0.4:.0f}, {-amp*0.2:.0f}, 0] }}, duration: 0.32, ease: "none" }}, {t:.2f});')
def slap(sel,t,rot,frm=1.4,d=0.2,kind="pop"):
    J(f'tl.fromTo("{sel}", {{ scale: {frm}, rotation: {rot+8}, opacity: 0 }}, {{ scale: 1, rotation: {rot}, opacity: 1, duration: {d}, ease: "power3.in", immediateRender: false }}, {t-d:.2f});')
    J(f'tl.to("{sel}", {{ scale: 0.96, duration: 0.04, ease: "none" }}, {t:.2f});')
    J(f'tl.to("{sel}", {{ scale: 1, duration: 0.12, ease: "power2.out" }}, {t+0.04:.2f});')
    if kind: snd.append((kind,t))

# background stripes drift for the whole film; colour changes per section
# (the drift is written after the end-card time is known: it settles as the end card lands, so the closing lines sit on a still ground)

# ---- HOOK 0-2: frame 0 complete (title, fan, price)
fanrot=[-22,-11,0,11,22]; fanx=[-190,-95,0,95,190]
for i,n in enumerate(FAN): J(f'tl.set("#dr-f{i}", {{ rotation: {fanrot[i]}, x: {fanx[i]} }}, 0);')
J('tl.set("#dr-badge", { rotation: 12 }, 0);'); J('tl.set("#dr-geldi", { rotation: -4 }, 0);')
J('tl.to("#dr-hook", { scale: 1.04, duration: 1.5, ease: "none" }, 0);')
J(f'tl.fromTo("#dr-yeni", {{ scale: 1.18 }}, {{ scale: 1, duration: 0.25, ease: "power3.out", immediateRender: false }}, {B:.2f});'); snd.append(("impact",B)); shake(B,10)
for i in range(5): J(f'tl.to("#dr-f{i}", {{ rotation: {fanrot[i]*1.6:.0f}, x: {fanx[i]*1.7:.0f}, y: {abs(i-2)*30}, duration: 0.22, ease: "back.out(2)" }}, {2*B-0.05:.2f});')
J(f'tl.to("#dr-badge", {{ scale: 1.2, rotation: -8, duration: 0.12, ease: "power2.out" }}, {2*B:.2f});'); J(f'tl.to("#dr-badge", {{ scale: 1, rotation: 12, duration: 0.2, ease: "power2.inOut" }}, {2*B+0.12:.2f});'); snd.append(("pop",2*B))
# blast out
J(f'tl.to(["#dr-yeni", "#dr-st", "#dr-geldi"], {{ y: -900, duration: 0.32, ease: "power3.in", stagger: 0.03 }}, {3*B+0.1:.2f});')
for i in range(5): J(f'tl.to("#dr-f{i}", {{ y: 1500, x: {fanx[i]*4}, rotation: {fanrot[i]*3}, duration: 0.34, ease: "power3.in" }}, {3*B+0.12+i*0.015:.3f});')
J(f'tl.to("#dr-badge", {{ x: 700, rotation: 90, duration: 0.3, ease: "power3.in" }}, {3*B+0.1:.2f});'); snd.append(("whoosh",3*B+0.35))

# ---- CAROUSEL 2-10: one sheet per beat, whip-panned in and out; caption per group of four
DIRS=[(1250,0,14),(-1250,0,-14),(0,1950,8),(0,-1950,-8)]
order=[n for g in GROUPS for n in g[2]]
T0=4*B
for gi,(cap,col,names) in enumerate(GROUPS):
    tg=T0+gi*4*B
    J(f'tl.to("#dr-bg", {{ backgroundColor: "{col}", duration: 0.12, ease: "none" }}, {tg-0.12:.2f});')
    slap(f"#dr-c{gi}",tg+0.22,(-2 if gi%2 else 2),1.35,0.2,"pop")
    J(f'tl.to("#dr-c{gi}", {{ y: -40, opacity: 0, duration: 0.15, ease: "power2.in" }}, {tg+4*B-0.17:.2f});')
rest=[2,-2,1.5,-1.5]
for k,n in enumerate(order):
    t=T0+k*B; dx,dy,r=DIRS[k%4]; rr=rest[k%4]
    J(f'tl.fromTo("#dr-s{k}", {{ x: {dx}, y: {dy}, rotation: {r+rr}, scale: 1.08, opacity: 1 }}, {{ x: 0, y: 0, rotation: {rr}, scale: 1, opacity: 1, duration: 0.2, ease: "power4.out", immediateRender: false }}, {t-0.2:.2f});')
    J(f'tl.to("#dr-s{k}", {{ scale: 1.035, duration: 0.28, ease: "none" }}, {t:.2f});')
    J(f'tl.to("#dr-s{k}", {{ x: {-dx}, y: {-dy}, rotation: {rr-r}, duration: 0.2, ease: "power3.in" }}, {t+B-0.2:.2f});')
    J(f'tl.fromTo("#dr-burst{k}", {{ scale: 0.5, opacity: 0.55, rotation: {k*17} }}, {{ scale: 1.35, opacity: 0, rotation: {k*17+25}, duration: 0.4, ease: "power2.out", immediateRender: false }}, {t-0.04:.2f});')
    snd.append(("whoosh-soft",t-0.08))
TM=T0+len(order)*B   # 10.0

# ---- WALL 10-13: every design scrolling in four columns, "33 yeni tasarım"
J(f'tl.to("#dr-bg", {{ backgroundColor: "{SALMON}", duration: 0.12, ease: "none" }}, {TM-0.12:.2f});')
J(f'tl.fromTo("#dr-wall", {{ scale: 1.7 }}, {{ scale: 1, duration: 0.35, ease: "power3.out", immediateRender: false }}, {TM-0.2:.2f});')
J(f'tl.fromTo("#dr-wall", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.1, ease: "none", immediateRender: false }}, {TM-0.2:.2f});'); snd.append(("whoosh",TM-0.05))
for c in range(4):
    J(f'tl.fromTo("#dr-col{c}", {{ y: {(-300 if c%2 else -900)} }}, {{ y: {(-900 if c%2 else -300)}, duration: 3.4, ease: "none", immediateRender: false }}, {TM-0.2:.2f});')
slap("#dr-33",TM+0.5,-3,1.6,0.22,"impact"); shake(TM+0.5,18)
J(f'tl.to("#dr-33", {{ scale: 1.06, duration: 0.1, ease: "power2.out" }}, {TM+1.5:.2f});'); J(f'tl.to("#dr-33", {{ scale: 1, duration: 0.15, ease: "power2.in" }}, {TM+1.6:.2f});'); snd.append(("click",TM+1.5))
TP=TM+6*B   # 13.0
J(f'tl.to(["#dr-wall", "#dr-33"], {{ scale: 2.6, opacity: 0, duration: 0.28, ease: "power2.in" }}, {TP-0.28:.2f});'); snd.append(("whoosh",TP-0.1))

# ---- PRICE 13-15.5: three sheets slam in a row, then the price
J(f'tl.to("#dr-bg", {{ backgroundColor: "#efe8f7", duration: 0.12, ease: "none" }}, {TP-0.12:.2f});')
herorot=[-10,8,-2]
slap("#dr-pcap",TP+0.3,-2,1.35,0.2,None)
for i in range(3): slap(f"#dr-h{i}",TP+0.12+i*B*0.5,herorot[i],1.5,0.16,"pop")
slap("#dr-price",TP+3*B,10,1.8,0.22,"impact"); shake(TP+3*B,20)
J(f'tl.fromTo("#dr-pburst", {{ scale: 0.4, opacity: 0.9, rotation: 0 }}, {{ scale: 1.6, opacity: 0, rotation: 30, duration: 0.5, ease: "power2.out", immediateRender: false }}, {TP+3*B-0.02:.2f});')
TE=TP+5*B+0.1   # 15.6
J(f'tl.to(["#dr-h0", "#dr-h1", "#dr-h2", "#dr-price", "#dr-pcap"], {{ y: 1700, rotation: 20, duration: 0.32, ease: "power3.in", stagger: 0.02 }}, {TE-0.32:.2f});'); snd.append(("whoosh",TE-0.12))

# ---- END CARD
J(f'tl.to("#dr-bg", {{ backgroundColor: "{NAVY}", duration: 0.12, ease: "none" }}, {TE-0.12:.2f});')
slap("#dr-mark",TE+0.22,-3,1.45,0.22,"impact")
J(f'tl.fromTo("#dr-ecta .w", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: 0.16, stagger: 0.08, ease: "back.out(2)" }}, {TE+0.45:.2f});')
slap("#dr-url",TE+1.0,-2,1.3,0.2,"pop")
J(f'tl.fromTo("#dr-dm", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, ease: "power1.out" }}, {TE+1.25:.2f});')
for i in range(3): slap(f"#dr-e{i}",TE+1.5+i*0.18,[-12,4,14][i],1.3,0.18,"pop" if i==0 else None)
snd.append(("sparkle",TE+1.0))
TOTAL=round(TE+4.6,1)
J(f'tl.to("#dr-stripes", {{ x: -1900, duration: {TE+0.6:.2f}, ease: "power1.out" }}, 0);')
js="\n    ".join(js)

# ---------------- markup
def img(id_,n,style,cls="dr-img"): return f'<img id="{id_}" class="{cls}" src="assets/sheets/{n}.webp" alt="" style="{style}" />'
def bgimg(id_,n,style,w,cls="dr-img"): return f'<div id="{id_}" class="{cls} dr-bgimg" style="{style}; width: {w}px; height: {round(w*1.34)}px; background-image: url(assets/sheets/{n}.webp)"></div>'
fan="".join(bgimg(f"dr-f{i}",n,"left: 330px; top: 760px; transform-origin: 50% 100%",420) for i,n in enumerate(FAN))
car="".join(f'<div id="dr-burst{k}" class="dr-burst" data-layout-ignore></div>'+img(f"dr-s{k}",n,"left: 180px; top: 352px; width: 720px; opacity: 0","dr-img dr-big") for k,n in enumerate(order))
caps="".join(f'<div class="dr-capwrap"><div id="dr-c{gi}" class="dr-cap" style="opacity: 0">{g[0]}</div></div>' for gi,g in enumerate(GROUPS))
cols=[]
for c in range(4):
    items=[ALL[(c*6+j*1)%len(ALL)] if c%2==0 else ALL[(c*6+j*3+1)%len(ALL)] for j in range(8)]
    cols.append(f'<div id="dr-col{c}" class="dr-col" style="left: {24+c*264}px">'+"".join(f'<div class="dr-wimg" style="background-image: url(assets/sheets/{n}.webp)"></div>' for n in items)+'</div>')
wall="".join(cols)
hero="".join(img(f"dr-h{i}",n,f"left: {[40,580,270][i]}px; top: {[440,500,640][i]}px; width: {[460,460,540][i]}px; opacity: 0") for i,n in enumerate(HERO))
ends="".join(bgimg(f"dr-e{i}",n,f"left: {[40,370,700][i]}px; top: {[1400,1440,1400][i]}px; opacity: 0",340,"dr-img dr-e") for i,n in enumerate(["coquette","van-gogh","y2k"]))
tracks=iter(range(1,40))
html=f'''<template>
  <style>
    #root {{ position: absolute; inset: 0; overflow: hidden; font-family: "Nunito", sans-serif; color: {NAVY}; }}
    #dr-bg {{ position: absolute; inset: 0; background-color: {SALMON}; }}
    #dr-stripes {{ position: absolute; left: 0; top: 0; width: 3400px; height: 1920px;
      background: repeating-linear-gradient(115deg, rgba(255,255,255,0.13) 0px, rgba(255,255,255,0.13) 44px, transparent 44px, transparent 88px); }}
    #dr-cam {{ position: absolute; inset: 0; }}
    .dr-slot {{ position: absolute; inset: 0; }}
    .dr-img {{ position: absolute; display: block; filter: drop-shadow(0px 16px 22px rgba(0,0,0,0.32)); }}
    .dr-bgimg {{ background-size: contain; background-repeat: no-repeat; background-position: center; }}
    .dr-center {{ position: absolute; left: 0; right: 0; text-align: center; }}
    #dr-yeni {{ display: inline-block; position: relative; font-family: "Archivo Black", sans-serif; font-size: 240px; line-height: 0.9; color: {NAVY}; }}
    #dr-st {{ display: inline-block; position: relative; font-family: "Archivo Black", sans-serif; font-size: 112px; line-height: 1; color: {NAVY};
      text-shadow: 0 6px 0 rgba(255,255,255,0.75); }}
    #dr-geldi {{ display: inline-block; position: relative; padding: 12px 36px 18px; background: {NAVY}; color: #ffffff; border: 10px solid #ffffff; border-radius: 22px;
      font-family: "Archivo Black", sans-serif; font-size: 78px; line-height: 1; box-shadow: 0 10px 16px rgba(0,0,0,0.25); }}
    #dr-badge {{ position: absolute; left: 790px; top: 630px; width: 260px; height: 260px; border-radius: 50%; background: {NAVY}; border: 12px solid #ffffff;
      box-shadow: 0 10px 18px rgba(0,0,0,0.3); color: #ffffff; display: flex; flex-direction: column; align-items: center; justify-content: center;
      font-family: "Archivo Black", sans-serif; line-height: 0.95; text-align: center; }}
    .dr-burst {{ position: absolute; left: 90px; top: 380px; width: 900px; height: 900px; opacity: 0;
      background: repeating-conic-gradient(from 0deg, rgba(255,255,255,0.9) 0deg 9deg, transparent 9deg 30deg);
      -webkit-mask-image: radial-gradient(circle, #000 0%, #000 45%, transparent 70%); mask-image: radial-gradient(circle, #000 0%, #000 45%, transparent 70%); }}
    .dr-capwrap {{ position: absolute; left: 0; right: 0; top: 176px; text-align: center; }}
    .dr-cap {{ display: inline-block; position: relative; padding: 16px 34px 20px; background: #ffffff; border-radius: 20px; border: 8px solid {NAVY};
      box-shadow: 0 10px 16px rgba(0,0,0,0.25); font-family: "Archivo Black", sans-serif; font-size: 66px; line-height: 1; white-space: nowrap; }}
    #dr-wall {{ position: absolute; inset: 0; opacity: 0; }}
    .dr-col {{ position: absolute; top: 0; width: 240px; display: flex; flex-direction: column; gap: 22px; }}
    .dr-wimg {{ width: 240px; height: 322px; flex: none; background-size: contain; background-repeat: no-repeat; background-position: center; filter: drop-shadow(0px 8px 10px rgba(0,0,0,0.28)); }}
    #dr-33 {{ display: inline-block; position: relative; padding: 26px 50px 34px; background: {NAVY}; color: #ffffff; border: 14px solid #ffffff; border-radius: 34px;
      box-shadow: 0 18px 30px rgba(0,0,0,0.4); font-family: "Archivo Black", sans-serif; line-height: 0.92; text-align: center; opacity: 0; }}
    #dr-pburst {{ position: absolute; left: 340px; top: 750px; width: 760px; height: 760px; opacity: 0;
      background: repeating-conic-gradient(from 0deg, rgba(225,168,164,0.95) 0deg 10deg, transparent 10deg 24deg);
      -webkit-mask-image: radial-gradient(circle, #000 0%, #000 40%, transparent 68%); mask-image: radial-gradient(circle, #000 0%, #000 40%, transparent 68%); }}
    #dr-price {{ position: absolute; left: 470px; top: 880px; width: 500px; height: 500px; border-radius: 50%; background: {SALMON}; border: 18px solid #ffffff; opacity: 0;
      box-shadow: 0 18px 30px rgba(0,0,0,0.35); display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center;
      font-family: "Archivo Black", sans-serif; line-height: 1.08; color: {NAVY}; }}
    #dr-pcap {{ display: inline-block; position: relative; padding: 16px 34px 20px; background: {NAVY}; color: #ffffff; border: 10px solid #ffffff; border-radius: 22px;
      box-shadow: 0 10px 16px rgba(0,0,0,0.25); font-family: "Archivo Black", sans-serif; font-size: 62px; line-height: 1; white-space: nowrap; opacity: 0; }}
    #dr-mark {{ display: inline-block; position: relative; padding: 28px 46px 32px; background: {NAVY}; border: 14px solid #ffffff; border-radius: 30px; opacity: 0;
      box-shadow: 0 10px 20px rgba(0,0,0,0.35); font-family: "Lato", sans-serif; font-weight: 900; font-size: 96px; line-height: 1; white-space: nowrap; }}
    #dr-ecta {{ font-family: "Archivo Black", sans-serif; font-size: 78px; line-height: 1.05; color: #ffffff; }}
    #dr-ecta .w {{ display: inline-block; position: relative; opacity: 0; }}
    #dr-url {{ display: inline-block; position: relative; padding: 18px 32px 22px; background: {SALMON}; border: 12px solid #ffffff; border-radius: 20px; opacity: 0;
      font-weight: 900; font-size: 50px; line-height: 1; white-space: nowrap; color: {NAVY}; }}
    #dr-dm {{ font-weight: 800; font-size: 42px; line-height: 1.2; color: #ffffff; opacity: 0; }}
  </style>

  <div id="root" data-composition-id="drop" data-width="1080" data-height="1920">
    <div id="dr-bg"></div>
    <div id="dr-stripes" data-layout-ignore></div>
    <div id="dr-cam" data-layout-allow-overflow>

      <div id="dr-hooks" class="dr-slot clip" data-start="0" data-duration="{4*B+0.1:.2f}" data-track-index="{next(tracks)}">
        <div id="dr-hook" class="dr-slot" data-layout-allow-overflow>
          <div class="dr-center" style="top: 170px"><div id="dr-yeni">YENİ</div></div>
          <div class="dr-center" style="top: 392px"><div id="dr-st">STICKERLAR</div></div>
          <div class="dr-center" style="top: 520px"><div id="dr-geldi">GELDİ!</div></div>
          <div data-layout-ignore>{fan}</div>
          <div id="dr-badge" data-layout-allow-overlap><span style="font-size: 66px">64,90</span><span style="font-size: 48px">TL</span></div>
        </div>
      </div>

      <div id="dr-cars" class="dr-slot clip" data-start="{T0-0.25:.2f}" data-duration="{TM-T0+0.3:.2f}" data-track-index="{next(tracks)}">
        <div data-layout-ignore>{car}</div>
        {caps}
      </div>

      <div id="dr-walls" class="dr-slot clip" data-start="{TM-0.22:.2f}" data-duration="{TP-TM+0.24:.2f}" data-track-index="{next(tracks)}">
        <div id="dr-wall" data-layout-ignore>{wall}</div>
        <div class="dr-center" style="top: 640px"><div id="dr-33"><span style="font-size: 260px">33</span><br><span style="font-size: 96px">YENİ</span><br><span style="font-size: 96px">TASARIM</span></div></div>
      </div>

      <div id="dr-prices" class="dr-slot clip" data-start="{TP-0.12:.2f}" data-duration="{TE-TP+0.14:.2f}" data-track-index="{next(tracks)}">
        <div data-layout-ignore>{hero}</div>
        <div id="dr-pburst" data-layout-ignore></div>
        <div id="dr-price" data-layout-allow-overlap><span style="font-size: 50px">TANESİ</span><span style="font-size: 106px">64,90</span><span style="font-size: 64px">TL</span></div>
        <div class="dr-center" style="top: 176px"><div id="dr-pcap">Hangisi senin?</div></div>
      </div>

      <div id="dr-ends" class="dr-slot clip" data-start="{TE-0.05:.2f}" data-duration="{TOTAL-TE+0.05:.2f}" data-track-index="{next(tracks)}">
        <div class="dr-center" style="top: 300px"><div id="dr-mark"><span style="color: #e8bcac">MALIBU</span> <span style="color: #ffffff">CRAFT</span></div></div>
        <div id="dr-ecta" class="dr-center" style="top: 560px"><span class="w">Yeni</span> <span class="w">koleksiyon</span><br><span class="w">Shopier'de</span></div>
        <div class="dr-center" style="top: 790px"><div id="dr-url">shopier.com/malibucraftshop</div></div>
        <div id="dr-dm" class="dr-center" style="top: 960px">Kişiye özel tasarımlar için DM</div>
        <div data-layout-ignore>{ends}</div>
      </div>
    </div>
  </div>

  <script>
    const tl = gsap.timeline({{ paused: true }});
    {js}
    window.__timelines["drop"] = tl;
  </script>
</template>
'''
open(f"{P}/compositions/drop.html","w").write(html)

F=1/30
# SFX sit under the trending sound the owner adds in Instagram, so they are mixed low
SFX={"whoosh":("whoosh",0.162,0.57,0.16),"whoosh-soft":("whoosh",0.162,0.57,0.07),"pop":("pop",0.119,0.72,0.18),"impact":("impact-bass-1",0.073,2.1,0.26),
     "click":("click",0.072,0.37,0.14),"sparkle":("sparkle",0.0,1.8,0.15)}
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
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: {SALMON}; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
      <div id="drop" data-composition-id="drop" data-composition-src="compositions/drop.html" data-start="0" data-duration="{TOTAL}"
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
print("carousel",T0,"wall",TM,"price",TP,"end",TE,"total",TOTAL,"sfx",len(snd))
