# REVIEW — Malibu Craft Reels "2027 ajandanı benimle süsle" (plan-with-me)

Render: `renders/malibucraft-2027-ajanda.mp4` (1080x1920, 30 fps, 26.1 s, H.264 + AAC, SFX only). Not committed (renders/ is ignored).
Cover: `instagram/kapak.png` (frame 0). Caption: `instagram/aciklama.txt`. Generator: `tools/build_planner.py` → `compositions/planner.html`, `index.html`.

## Story (every phase carries an on-screen caption that says what is happening)

| Time | Caption | Picture |
| --- | --- | --- |
| 0–1.8 | 2027 ajandanı benimle süsle | Frame 0 = the finished January 2027 page on a winter desk; a light pass crosses it |
| 1.9–3.4 | Hadi baştan başlayalım | Rewind: stickers fly off, handwriting wipes away; washi tape goes on the blank page |
| 3.45–5.3 | Önce ayın adını yazıyorum | "Ocak 2027" written in |
| 5.35–6.85 | Sonra takvimi çiziyorum | January 2027 calendar pops in (1 Jan = Friday) |
| 6.9–8.95 | Stickerları yapıştırıyorum | dahlia, camera, orange |
| 9.0–11.3 | 2027 hedeflerimi yazıyorum | "2027 hedeflerim" + four goals |
| 11.35–14.6 | Kalan boşlukları dolduruyorum | disco heart, envelope, gingham heart, Starry Night, CUTE, second tape |
| 14.65–16.65 | Yeni yıl, yeni sayfa! | light pass; the page is swept off the desk |
| 16.85–20.35 | İki boyumuz var | A5 (14,8 × 21 cm) and 13 × 16 cm sheets drawn to scale (3.2 px/mm); price tags 64,90 TL / 39,90 TL |
| 20.55–26.1 | — | Brand card: MALIBU CRAFT, "A5 · 64,90 TL" + "13×16 cm · 39,90 TL", shopier.com/malibucraftshop, DM line; three real stickers |

Captions hold at least 0.5 s + 0.3 s per word; they slap in as kraft die-cut labels and lift off before the next one.

## Visuals

- Every sticker on screen is the brand's own design, cut out of the product sheets sent in chat (`assets/stickers/`, white die-cut edge rebuilt).
  No stock or third-party sticker art.
- The desk and the seasonal decor (wood, pine, ornaments, dried oranges, cocoa, gift box, cinnamon, pencil, washi tape) are drawn in
  SVG/CSS so they stay sharp at 1080 px. Stock flat-lay sites (StockSnap, rawpixel, Wikimedia via Openverse) refused automated
  downloads; their protection was not bypassed. A real desk photo can replace `.pl-desk` later.
- Handwriting: Caveat (Google Fonts, OFL, `assets/fonts/`). Labels: Nunito/Lato 900, brand navy, kraft, salmon.

## Facts on screen

- Only confirmed facts: A5 64,90 TL, 13 × 16 cm 39,90 TL (owner, chat), Shopier address, custom designs via DM.
- The size sheets are plain (dimensions and price only): which designs come in 13 × 16 cm is not confirmed, so no designs are shown on them. "5 al 4 öde" is left out until the owner confirms it is still running.

## Measured vs looked at

- `hyperframes check`: ok, 0 errors, 0 warnings.
- Snapshots inspected at 0, 2.4, 4.6, 6.5, 8.6, 10.8, 13.4, 15.4, 17.0, 18.4, 18.6, 19.9, 21.0, 23.5, 25.9 s; render frames at 4.2, 18.3 and 24 s.
- Audio measured, not heard: SFX only (whoosh, click-soft, pop, sparkle), -27.2 LUFS integrated, -10 dBFS peak so a trending sound added in Instagram stays on top.

## Weakest points

- The bottom third (below y 1330) holds only decor; Instagram's caption overlay sits there.
- Stickers come from 458 px sheet photos; the largest ones (Starry Night, CUTE) are slightly soft at full size.
