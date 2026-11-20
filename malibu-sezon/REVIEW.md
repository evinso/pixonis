# REVIEW — Malibu Craft Reels "2027 ajandanı benimle süsle" (plan-with-me)

Render: `renders/malibucraft-2027-ajanda.mp4` (1080x1920, 30 fps, 19.7 s, H.264 + AAC, SFX only). Not committed (renders/ is ignored).
Cover: `instagram/kapak.png` (frame 0). Caption: `instagram/aciklama.txt`. Generator: `tools/build_planner.py` → `compositions/planner.html`, `index.html`.

## Story

| Time | Picture |
| --- | --- |
| 0–1.35 | Frame 0 = the finished January 2027 page on a winter desk; label "2027 ajandanı benimle süsle"; a light pass crosses the page |
| 1.35–2.0 | Rewind: the stickers fly off, the handwriting wipes away, blank dotted page |
| 2.05–12.2 | Build-up: washi tape, "Ocak 2027" written in, the January 2027 calendar pops in (1 Jan = Friday), dahlia, camera, orange stickers, "2027 hedeflerim" + four goals written, then disco heart, envelope, gingham heart, Starry Night, CUTE, second tape |
| 12.2–13.9 | Light pass, label "Yeni yıl, yeni sayfa" |
| 13.9–14.4 | The page is swept off the desk |
| 14.4–19.7 | Brand card slapped on: MALIBU CRAFT wordmark, "Ajandan için sticker setleri", "A5 set · 64,90 TL", shopier.com/malibucraftshop, "Kişiye özel tasarımlar için DM"; three more real stickers (lavender, Van Gogh, red heart) |

## Visuals

- Every sticker on screen is the brand's own design, cut out of the product sheets sent in chat (`assets/stickers/`, white die-cut edge rebuilt).
  No stock or third-party sticker art.
- The desk and the seasonal decor (wood, pine, ornaments, dried oranges, cocoa, gift box, cinnamon, pencil, washi tape) are drawn in
  SVG/CSS so they stay sharp at 1080 px. Stock flat-lay sites (StockSnap, rawpixel, Wikimedia via Openverse) refused automated
  downloads; their protection was not bypassed. A real desk photo can replace `.pl-desk` later.
- Handwriting: Caveat (Google Fonts, OFL, `assets/fonts/`). Labels: Nunito/Lato 900, brand navy, kraft, salmon.

## Facts on screen

- Only confirmed facts: A5 set 64,90 TL, Shopier address, custom designs via DM. "5 al 4 öde" is left out until the owner confirms it is still running.

## Measured vs looked at

- `hyperframes check`: ok, 0 errors, 0 warnings (2 info: text mid-wipe at 3.28 and 7.66 s, intended).
- Snapshots inspected at 0, 0.6, 1.5, 2.4, 3.0, 4, 6, 7.8, 9.85, 12.4, 12.6, 13.6, 13.95, 14.1, 14.6, 14.9, 15.5, 16.5, 19.5 s; render frames at 7 and 18 s.
- Audio measured, not heard: SFX only (whoosh, click-soft, pop, sparkle), -27 LUFS integrated so a trending sound added in Instagram stays on top.

## Weakest points

- The bottom third (below y 1330) holds only decor; Instagram's caption overlay sits there.
- Stickers come from 458 px sheet photos; the largest ones (Starry Night, CUTE) are slightly soft at full size.
