# REVIEW — Malibu Craft Reels "Kaçan aslan Malibu Craft'ta görüldü" (trend video)

Render: `renders/malibucraft-kacan-aslan.mp4` (1080x1920, 30 fps, 18.7 s, H.264 + AAC, SFX only). Not committed (renders/ is ignored).
Cover: `instagram/kapak.png` (frame 0). Caption: `instagram/aciklama.txt`. Generator: `tools/build_aslan.py` → `compositions/aslan.html`, `index.html`.

## Context (checked 23.11.2026)

A lion escaped in Sarıyer (Uskumruköy) on 22.11.2026 and was seen on security cameras; the governor's office said its area was found
and the aim is to capture it alive; no capture announced at the time of writing. The video jokes only about our cartoon lion and the
shop; it states nothing about the real event, names no owner, and the end card and caption carry "Gerçek aslanı görürsen yaklaşma,
112'yi ara." Re-check the news before posting: if the story turns sad, do not post.

## Story

| Time | Picture | Words |
| --- | --- | --- |
| 0–2.6 | Security-camera view of the shop at night (REC · KAMERA 2, 23.11.2026, running clock); the cartoon lion already at the sticker stand; brand-styled breaking-news banner | MALIBU HABER · SON DAKİKA: "Kaçan aslan Malibu Craft'ta görüldü!", crawl: "Görgü tanıkları: Gözü stickerlardaydı", "Van Gogh setinden ayrılamadı" |
| 2.45–5.0 | Lion leans in, eyes turn to hearts, hearts float up | "Gözü hemen stickerlara takıldı" |
| 5.0–8.0 | Seven sheets fly from the shelves and the stand into a stack against its chest | "Ve aslan payını aldı!" |
| 8.0–9.55 | Lion turns and trots out, a paw-print note flutters onto the table | "Giderken not bırakmış…" |
| 9.4–10.0 | Camera zooms into the note, white flash | — |
| 9.95–13.1 | The note close up: "Kükreten kalite!", five stars, "Aslan payımı aldım. – A.", paw stamp | "Masada şu not vardı:" |
| 13.1–18.7 | Salmon end card, the lion with heart eyes | "Aslan bile dayanamadı!", "Yeni koleksiyon · Tanesi 64,90 TL", shopier.com/malibucraftshop, "Kişiye özel tasarımlar için DM", "Gerçek aslanı görürsen yaklaşma, 112'yi ara." |

## Build

- Lion: original flat vector drawn in SVG (no real lion footage or photos). Tail swish, breathing, blink, heart eyes, walk cycle.
- Registry blocks, edited for 9:16 and the brand: `camcorder-hud` (REC/time HUD) and `news-ticker` (banner, complete at frame 0,
  leaves at 2.3 s). The room is vector; the product sheets on the shelves and stand are the real catalogue sheets, not tinted.
- SFX only (bundled library), -18.5 LUFS, -6.2 dBFS peak, low under the music added in Instagram.

## Measured vs looked at

- `hyperframes check`: ok, 0 errors, 0 warnings.
- Snapshots inspected at 0, 1.0, 1.35, 2.9, 3.6, 5.9, 7.4, 7.6, 8.5, 9.2, 9.6, 10.0, 10.4, 10.6, 12.0, 12.9, 13.0, 13.4, 17.9, 18.6 s;
  render frames at 3.5, 6.5, 8.6 and 11.8 s.

## Weakest points

- Below y 1330 the room is plain floor (Instagram's caption overlay sits there); the paw-print trail is mostly under the captions.
- The lion's head stays front-facing while it walks away (cartoon convention).
