# SPEC — "Sepet Büyüdükçe" (Storyline B)

> **Current cut (see REVIEW.md):** quality opening + "5 al 4 öde" campaign, 18.7 s, timed to a 7-line voiceover.
> A5 price is fixed at 64,90 TL (no price ladder). The shot list below is the earlier price-ladder version, kept for reference.


PRICES:  A5 size only (brand catalog): 1 = 64,90 TL, 2–4 = 59,90 TL, 5–9 = 57,90 TL per sheet; mixed designs allowed
         ("Çoklu perakende siparişlerde farklı tasarımlar seçilebilir"). Wholesale tiers are single-design and not shown.
GOAL:    The viewer sees the variety and that the unit price drops with every set added, then goes to Shopier to buy several sets at once.
OUTPUT:  HyperFrames, 1080 x 1920 (9:16 Reels), 30 fps
TIME:    17.3 s x 30 = 519 frames, timed to the voiceover (see REVIEW.md); the shot list below is the pre-voice 11.5 s cut. Beat grid 120 BPM = 15 frames per beat (for a trending audio the user adds in Instagram).

LOOK:
  ground  = a craft cutting mat, top-down: #A8DCC6 with a white grid
            (minor every 45 px at 2 px / 30% white, major every 180 px at 3 px / 55% white), 5% fibre noise.
  ink     = #29314B (brand navy) for every readable word.
  kraft   = #D8B38A paper for the price sticker (1 set, 2–4 sets) and the theme tags.
  accent  = #E1A8A4 (brand salmon), ONLY on: the payoff price sticker (57,90) and the Shopier address on the end card.
  stickers= every label is a die-cut sticker: white border (7–14 px), shadow 0 6 10 rgba(0,0,0,.18).
  photos  = each product photo is a 480 px print with a 16 px white border, 6 px radius,
            shadow while airborne 0 40 60 rgba(0,0,0,.35) → after landing 0 8 14 rgba(0,0,0,.22).
            Each print carries its theme tag (kraft, top-left corner) so the theme reads the moment it lands.
  type    = Archivo Black (titles 88 px, line height 0.98, tracking -1%; prices 104 px; wordmark Lato 900 96 px, MALIBU #E8BCAC / CRAFT white on navy);
            Nunito 900/800 (sticker lines 32–38 px, tags 36 px, URL 44 px). Turkish glyphs from Google Fonts.

OBJECTS:
  mat (with grid), 6 product photo prints (Vintage, Y2K, Kawaii, Manifest, Scrapbook, Sanatsal — swappable files
  assets/products/set-1..6.jpg), round price sticker (380 px), theme tags, "Malibu Craft" wordmark sticker (logo when supplied).

MOTION:
  camera     = opens at scale 1.45 on set 1 (x +220, y +290, origin 320/710), pulls back to 1.0 over 0.7–2.3 s power2.inOut;
               payoff punch 1 → 1.05 at 3.22 s in 0.35 s expo.out, then still.
  photo slap = from scale 1.32, y -160, rotation r+9, big shadow → resting, 0.30 s power3.in (a fall speeds up),
               then settle 0.985 → 1 (0.05 s + 0.12 s power2.out). Sets 5 and 6 are tossed in from the sides (x ±760, 0.32 s power3.in).
  sticker peel = old sticker flies up-right: x +260, y -320, rotation -28, scale 1.08, 0.28 s power3.in;
               new one slaps from scale 1.35 in 0.22 s power3.in + settle.
  count roll = one digit strip, 0.10 s power2.out per step.
  titles     = per word blur 6 → 0 px with opacity 0 → 1 in 0.13 s, 0.067 s apart, no translate; dead still after landing;
               exit blur 0 → 8 px + opacity → 0 in 0.15 s.
  exit sweep = the pile and the sticker leave downward, 0.40 s power3.in, 0.04 s stagger.

SHOTS:
  0.00–0.70  Frame 0 (thumbnail) complete and still: large Vintage print, kraft sticker "1 SET · 64,90 · TL · tek set",
             title "Tek set mi?".
  0.70–1.25  Camera starts pulling back; set 2 (Y2K) slaps at 1.00; 64,90 peels, 59,90 "2 SET · adet başı" lands 1.22.
             Title → "Ekledikçe". whoosh 1.00, pop 1.22.
  1.20–2.00  Sets 3 and 4 slap at 1.50 / 2.00; the count rolls 3, 4. whoosh on each.
  2.00–2.68  Hold before the payoff; camera settles at 1.0.
  2.68–3.62  PAYOFF: set 5 tossed in (3.00); 59,90 peels; SALMON 57,90 "5 SET" lands 3.22 with the camera punch and the impact.
             Title → "birim fiyat düşer". Set 6 tossed in (3.62), count 6.
  5.00–6.75  Title → "Tasarımları karıştır".
  6.80–7.30  The pile and sticker sweep out downward (whoosh); bare mat.
  7.30–11.5  End card on the same mat: wordmark sticker slaps 7.60 (pop); "Sepetini Shopier'de doldur" 7.85;
             salmon "shopier.com/malibucraftshop" slaps 8.35 (soft click); "Kişiye özel tasarımlar için DM" 8.55. Hold to 11.5.

SOUND:   bundled SFX only (whoosh, pop, impact, soft click), each placed so its measured peak lands one frame after its picture.
         No music bed: the user adds a trending sound in Instagram. Mix measured at -17.3 LUFS, true peak -3.2 dBTP.

SAFE:    No words above y 168 or below y 1330; no words under the right action rail (x > 960, y > 1000).

BANNED:  the spec.md defaults (dark void, glow/particles, purple/blue gradients, cream paper + serif, everything centred,
         fade-and-slide-up, moving titles, corner labels/frames, three cards in a row, a docked logo);
         pill-shaped chips; free shipping (not offered); any price or claim not in the brand brief; drawn fake sticker designs
         in place of real product photos (placeholders are labelled as placeholders).

QA:
  t=0.0   hook complete: large print + 64,90 sticker + "Tek set mi?" on one line.
  t=1.3   59,90 sticker, "Ekledikçe".
  t=3.4   pink 57,90 sticker, 5 prints, "birim fiyat düşer"; punch landed.
  t=4.5   6 prints, all 6 tags readable.
  t=11.0  end card complete, all four lines inside the safe band.
