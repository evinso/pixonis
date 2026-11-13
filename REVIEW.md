# REVIEW — Malibu Craft Reels "Kalite + 5 al 4 öde"

Render: `renders/malibucraft-reels.mp4` (1080x1920, 30 fps, 21.8 s, H.264 + AAC, Turkish voiceover). Not committed (renders/ is ignored).

## Facts on screen (from the brand)

- A5 unit price is fixed: 64,90 TL. Campaign: 5 al 4 öde — the 5th sticker set is free. No price ladder, no free shipping.
- Quality claims only from the brief: glossy and matte photo paper; cut on the brand's own equipment ("hassas kesim").
- Mixing designs is allowed (price catalog: "Çoklu perakende siparişlerde farklı tasarımlar seçilebilir").

## Voice (current)

- First person plural, the brand speaking ("basıyoruz", "kesiyoruz", "setimiz var", "bizden", "seni bekliyoruz"), per the owner.
- One continuous Eleven v4 take, voice Laura (`FGY2WhTYpPnrIDTdsKH5`), split only at two true silences (7.115 s, 14.95 s) into
  `assets/voice/vo-1..3.mp3` placed at 0.20 / 7.75 / 16.57 s, so the pull-back and the sweep get room without breaking the flow.
- TTS spelling for pronunciation: "Van Gog'dan" (Van Gogh'tan; heard as "Vangok'tan", the everyday Turkish form — the owner flagged the
  earlier "Van Gogh'tan" as mispronounced, so part 2 was re-recorded alone), "kavayiye" (kawaii'ye), "Şopiyer" (Shopier).
- Anchors: push-in on "Parlak" 1.74, peel on "hassasça" 5.97, Kawaii on "kawaii'ye" 8.55, 64,90 on "var" 10.55, offer on "beş" 11.93,
  counters over "al, dört öde", 5th set on "beşinci" 13.28, BEDAVA on "bedava" 14.83, wordmark on "Malibu" 16.6, Shopier label 17.62.
- Part 2 re-take placed at 7.75 s; later anchors moved +0.1–0.2 s (BEDAVA 14.97, sweep 15.96, end card 16.51, film 21.81 s).
- Final mix: -14.3 LUFS, -1.0 dBTP; Whisper on the render returns the full script in order. Jessica take of the same script kept as an alternative.

## Structure (earlier 7-clip version; timings superseded by the anchors above)

| Time | Voice (Jessica, ElevenLabs) | Picture |
| --- | --- | --- |
| 0.2 | Şu kaliteye bir bak! | Van Gogh sheet up close (frame 0 = thumbnail), light streak crosses it; title "Kalite detayda" |
| 1.5 | Parlak ve mat fotoğraf kâğıtlarına basılıyor, | camera pushes in; tag "Parlak & mat kâğıt"; second light pass |
| 3.85 | kendi ekipmanlarımızla hassasça kesiliyor. | the Van Gogh portrait sticker peels off the sheet (3D lift, the empty spot shows); tag "Hassas kesim" |
| 6.1 | — | the sticker is carried away, the camera pulls back to the mat |
| 6.55 | Van Gogh'tan kawaii'ye, her tarzda set var. | Van Gogh tag pops; Kawaii, Disco Pop, Junk Journal land on their beats, each with a shine; "Hangi tarz senin?"; A5 · 64,90 TL sticker |
| 9.35 | Üstelik şimdi beş al, dört öde: | 64,90 peels, salmon "5 AL 4 ÖDE" lands on "beş"; counters 1-2-3-4 pop on the sheets |
| 11.1 | beşinci set bedava! | Cute Duck tossed in with counter 5; "BEDAVA" stamp on "bedava" + camera punch; light ripple over all sheets |
| 13.1 | — | pile swept off the mat |
| 14.0 | Malibu Craft, Shopier mağazamızda seni bekliyor. | MALIBU CRAFT wordmark, CTA, Shopier label on "Shopier", 5 AL 4 ÖDE badge, DM line, three real stickers stuck on the mat |

Continuous motion so no product image sits still: shine passes, the camera push and pull, a slow drift of the mat (1.2° over 6.4 s),
tag pops on spoken names, counters, the stamp, and the final light ripple.

## Assets

- Sheets: `assets/products/set-1..5.jpg` (Van Gogh, Disco Pop, Kawaii, Junk Journal, Cute Duck; set-6 Lavanta unused). Sources were
  458 px from chat, upscaled 2.36x — the close-up at 1.5–1.75x is soft; original high-res files would make the quality shot crisper.
- Cutouts: `assets/cutouts/*.png` cut from the sheets (background removed, white die-cut edge rebuilt) + matching "hole" images.
- Voice: `assets/voice/vo-1..7.mp3`, Jessica (`cgSgspJ2msm6clMCkdW9`), `eleven_multilingual_v2`, each line checked with Whisper
  and regenerated until it read back word for word ("Şu kaliteye bak!" and "her tarza bir set" were rephrased because they slurred).
- SFX: HyperFrames bundled library (Pixabay licence, `assets/sfx/CREDITS.md`).

## Measured vs looked at

- `hyperframes check`: 0 errors, 0 warnings. Snapshots at 0, 2.6, 3.6, 5.2, 5.6, 5.85, 5.95, 6.6, 7.4, 8.1, 8.7, 10.6, 11.4, 12.0, 12.1, 18.45 s inspected.
- Audio measured, not heard: -17.4 LUFS, -1.1 dBTP; Whisper on the rendered file returns all seven lines in order.

## Weakest points

- Soft close-up (source resolution, see above).
- During the camera punch (11.7–13.1 s) the left tags sit just outside the 90% action-safe box; they stay in frame.
- No burned-in captions; titles, tags and the offer badge carry the message muted.
