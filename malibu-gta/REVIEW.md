# REVIEW — Malibu Craft Reels "GTA 6 çıktı, bizim görev hazır" (launch-week trend)

Render: `renders/malibucraft-gorev.mp4` (1080x1920, 30 fps, 22.0 s, H.264 + AAC, SFX only). Not committed (renders/ is ignored).
Cover: `instagram/kapak.png` (frame 0). Caption: `instagram/aciklama.txt`. Generator: `tools/build_gta.py` → `compositions/gta.html`, `index.html`.

## Context (checked 23.11.2026)

Grand Theft Auto VI launched on PS5 / Xbox Series X|S on 19.11.2026. The video names the game once ("GTA 6 çıktı!") as the news hook
and otherwise parodies generic open-world tropes in the brand's own style. No Rockstar logo, font, characters, artwork, music or map;
the caption says the shop is not affiliated with Rockstar Games.

## Story

| Time | Picture | Words |
| --- | --- | --- |
| 0–2.4 | Neon sunset, palms, moving perspective grid; gamer-girl and Y2K sheets floating | "GTA 6 ÇIKTI!", "Herkes oyunda…", "Bizim de bir görevimiz var" |
| 2.4–5.0 | Letterbox mission card | "YENİ GÖREV", "Ajandayı Kurtar", "Hedef: Malibu Craft", "Ödül: 33 yeni tasarım" |
| 5.0–7.9 | Phone slides in, messages from Malibu Craft with a location card | "Yeni setler geldi!", "Konum attım, hemen gel." |
| 7.9–10.9 | City map, GPS route draws, player arrow drives to the pin | "Rota: Malibu Craft" |
| 10.9–14.6 | Gamer girl, Y2K, retro, müzik sheets as glowing pickups, collected one by one; wanted stars fill to five | "Herkes setini soruyor!" |
| 14.6–17.0 | Mission passed with burst | "GÖREV TAMAMLANDI!", "Ajanda +100", "Stil +100" |
| 17.0–22.0 | End card on the neon sunset | MALIBU CRAFT, "Görevin: setini seç!", "Tanesi 64,90 TL", shopier.com/malibucraftshop, "Kişiye özel tasarımlar için DM" |

## Build notes

- Floor grid is SVG lines placed from one tween value (seek-safe); an earlier CSS 3D plane painted over later layers in the renderer.
- Fonts: Pacifico (OFL, `assets/fonts/`, Turkish glyphs checked), Archivo Black, Nunito, Lato.
- SFX only (bundled library), -18.2 LUFS, -7.3 dBFS peak, low under the music added in Instagram.

## Measured vs looked at

- `hyperframes check`: 0 errors, 0 warnings.
- Snapshots at 0, 0.5, 1.2, 3.6, 6.9, 9.0, 10.5, 11.6, 13.9, 15.6, 18.4, 21.75, 21.9 s; render frames at 3.6, 12.4, 15.6 s.
