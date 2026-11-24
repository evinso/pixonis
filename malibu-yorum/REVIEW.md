# REVIEW — Malibu Craft Reels "Birkaç kötü yorum aldık…" (1-star praise trend)

Render: `renders/malibucraft-kotu-yorumlar.mp4` (1080x1920, 30 fps, 29.5 s, H.264 + AAC, SFX only). Not committed (renders/ is ignored).
Cover: `instagram/kapak.png` (frame 0). Caption: `instagram/aciklama.txt`. Generator: `tools/build_yorum.py` → `compositions/yorum.html`, `index.html`.

## Format

Modelled on the "1-star complaints that are really praise" carousel trend (reference: a café's 8-slide post). Our own copy throughout;
the reviewers are obvious personas ("Ajanda Bağımlısı", "Kararsız Müşteri", …), not realistic names, so nothing reads as a genuine
review. Each joke rests on a fact from the brand: stickers fill a planner, glossy and matte photo paper, precise cutting on own
equipment, Van Gogh designs, 33 designs in the catalogue.

| Time | Scene |
| --- | --- |
| 0–2.8 | Navy; five gold stars, four fall off; "Birkaç kötü yorum aldık…", "Hepsini dürüstçe paylaşıyoruz." |
| 2.8–6.5 | 1/5 Ajanda Bağımlısı: planner page (from the 2027 planner Reel) gets three more stickers slapped on |
| 6.5–10.2 | 2/5 Kararsız Müşteri: coquette and Y2K sheets, "Parlak mı?" / "Mat mı?", light pass, "İKİSİ DE!" stamp |
| 10.2–13.9 | 3/5 Emekli Makas: the Van Gogh portrait sticker peels off its sheet (clean die-cut hole), scissors fall asleep "Zzz" |
| 13.9–17.6 | 4/5 Toplantı Mağduru: Starry Night sticker slapped on a laptop lid, bubbles "Bu ne güzel!", "Nereden aldın?" |
| 17.6–21.3 | 5/5 Cüzdanı Ağlayan: catalogue wall, five sheets drop into a cart, "TAŞTI!" |
| 21.3–25.2 | Cream: "ÖZÜR DİLERİZ", "Daha sıradan stickerlar yapmayı deneyeceğiz.", "Ama elimiz gitmiyor.", tag-a-friend button |
| 25.2–29.5 | Navy end card: MALIBU CRAFT, "33 yeni tasarım · Tanesi 64,90 TL", shopier.com/malibucraftshop, DM line |

Cards swipe left like carousel pages (in and out share start, length and ease). Each card: 1 gold star lands with a thud, the text
reveals word by word and holds about 3 s.

## Measured vs looked at

- `hyperframes check`: 0 errors, 0 warnings.
- Snapshots at 0, 1.6, 4.6, 6.3, 8.4, 9.0, 12.2, 12.6, 13.0, 15.8, 16.3, 19.6, 20.0, 22.6, 23.6, 27.0, 29.25, 29.4 s;
  render frames at 5.0, 9.2, 16.6, 23.8 s.
- SFX only (bundled library), -18.4 LUFS, -7.0 dBFS peak, low under music added in Instagram.

## Weakest points

- 29.5 s is long for a Reel; each card needs ~3 s to be read. A carousel version of the same cards would suit the format too.
- The Van Gogh sheet photo (set-1.jpg) is the old 458 px source, upscaled; slightly soft at 600 px.
