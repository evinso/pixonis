# REVIEW — Malibu Craft Reels "Yeni stickerlar geldi" (new collection drop)

Render: `renders/malibucraft-yeni-koleksiyon.mp4` (1080x1920, 30 fps, 20.2 s, H.264 + AAC, SFX only). Not committed (renders/ is ignored).
Cover: `instagram/kapak.png` (frame 0). Caption: `instagram/aciklama.txt`. Generator: `tools/build_drop.py` → `compositions/drop.html`, `index.html`.

Cut on a 120 BPM grid (one beat = 0.5 s) so a trending sound at ~120 BPM added in Instagram lands on the cuts.

| Time | Picture |
| --- | --- |
| 0–2.0 | Frame 0 complete: "YENİ / STICKERLAR / GELDİ!", a fan of five sheets, navy "64,90 TL" badge. Beat 1 punch + shake, beat 2 fan spreads, beat 3 everything blasts out |
| 2.0–10.0 | One sheet per beat, whip-panned in and out from alternating sides, light burst on each landing; four groups with their own background colour and caption: Pembe sevenlere / Sanat sevenlere / Retro ruhlara / Mizah sevenlere |
| 10.0–13.0 | Wall of all 23 shown designs in four columns scrolling in opposite directions; "33 YENİ TASARIM" slams in with a shake |
| 13.0–15.6 | "Hangisi senin?"; cherry picnic, lemon and mystic sheets slam in on half-beats; "TANESİ 64,90 TL" badge with burst + shake |
| 15.6–20.2 | Navy end card: MALIBU CRAFT wordmark, "Yeni koleksiyon Shopier'de", shopier.com/malibucraftshop, "Kişiye özel tasarımlar için DM", three sheets at the bottom |

## Source and choices

- Sheets: the owner's catalogue PDF (33 pages, one sheet per page). Each page image was extracted and the sheet cut out of the white
  page (`assets/sheets/*.webp`, 1200 px tall); page 19 is a hand-held photo inside the PDF, so the rendered page was used instead.
- "33 yeni tasarım" = the catalogue's page count. Price 64,90 TL per the owner.
- Left out of the video: the sheets built on licensed characters and brands (Snoopy/Hot Wheels, Hello Kitty/Spider-Man, Cars,
  Stitch, Harry Potter, Stranger Things, Cookie Monster, Hello Kitty/Kuromi ×2) and the grocery sheet with Pocky packaging, so a
  rights-holder complaint cannot take the post down. 23 sheets are shown.

## Measured vs looked at

- `hyperframes check`: 0 errors, 0 warnings. (The background stripes settle as the end card lands; while they kept moving under the
  closing lines the checker read the lines as appearing late.)
- Snapshots inspected at 0, 0.6, 1.1, 1.7, 2.1, 2.9, 4.3, 6.3, 8.3, 9.85, 9.9, 10.05, 10.6, 12.0, 13.4, 13.5, 14.2, 14.6, 14.8, 15.0,
  15.2, 16.0, 17.0, 17.5, 18.0, 18.7, 18.9, 18.95, 19.5, 19.8, 20.1 s; render frames at 6.3 and 11.2 s.
- Audio measured, not heard: SFX only, -18.3 LUFS, -7.1 dBFS peak, kept low under the music added in Instagram.

## Weakest points

- 9.8–9.9 s: the wall cuts in over the last carousel sheet for three frames.
- The price scene leaves the lower third empty (Instagram's caption overlay sits there).
- File is 39.5 MB (busy, moving texture); Instagram re-encodes on upload.
