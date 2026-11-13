# REVIEW — Malibu Craft Reels "Sepet Büyüdükçe"

Render: `renders/malibucraft-sepet-buyudukce.mp4` (1080x1920, 30 fps, 11.5 s, H.264 + AAC). Not committed (renders/ is ignored).

## Creative calls

- Built storyline **B** (price ladder) instead of the recommended A: A needs production footage (printing, Cricut, packing)
  that has not arrived; B works from the product photos the brand already has. A and C remain in `STORYLINES.md`.
- Shortened from the planned 13 s to 11.5 s; theme tags ride on each print (read as it lands) instead of a separate tag beat.
- Frame 0 opens tight on set 1 (camera 1.45x) and pulls back as the pile grows — a strong thumbnail instead of a small photo in an empty frame.
- Free shipping left out (the brand confirmed it is not offered). Prices are the brand's own tiers: 64,90 / 59,90 / 57,90 TL.
- The wordmark is typeset (MALIBU salmon / CRAFT white on a navy die-cut sticker, Lato 900 — the brand's own style from its price catalog).

## PLACEHOLDERS — must be replaced before posting

- `assets/products/set-1.jpg` … `set-6.jpg` are labelled placeholders ("FOTOĞRAF YERİ"). Replace each with a real
  product photo of that set (square crop works best; any size, `object-fit: cover`), keep the file names, re-render.
- Tag names are variables `tag1..tag6` in `compositions/pile.html`; change them if the photos are different themes.
- Logo: when supplied, replace the typeset wordmark in `compositions/endcard.html`.

## Measured vs looked at

- `hyperframes check`: 0 errors, 0 warnings; 57/57 text checks pass WCAG AA.
- Snapshots at 0, 0.9, 1.3, 1.8, 2.4, 3.4, 4.5, 5.6, 7.0, 8.0, 10.5, 11.25 s and one frame of the rendered MP4 (3.5 s) were inspected.
- Audio measured, not heard: -17.3 LUFS integrated, -3.2 dBTP true peak; hits at 1.0, 1.5, 2.0, 3.0, 3.22, 3.6, 7.0, 7.6, 8.4 s.
  SFX are the HyperFrames bundled library (Pixabay licence, see `assets/sfx/CREDITS.md`). No music bed by design.

## Weakest shot

- 3.6–6.8 s: the pile is complete and still while only the title changes (~3 s). With real photos this reads as a showcase;
  with more time, a slow push across the pile or one print lifting per title would keep it alive.
- The end card is text on the mat; a real logo and one product print peeking in would make it stronger.
