# Broad River Boat Soda Club — cooler decal kit

Die-cut vinyl decal artwork for the club's coolers. Open `index.html` for the
visual preview, cooler mockups, palette, and the full print/cut spec.

> If anybody asks, it's a soda.

## Files

| File | What it is |
| --- | --- |
| `brbsc-roundel-4.5in.svg` | Roundel, 4.5″ circle. The lid mark — scene-forward, club name in the ring. |
| `brbsc-crest-4x5in.svg` | Crest, 4 × 5″ shield. Type-forward, carries the tagline on the ribbon. |
| `brbsc-banner-6x2in.svg` | Banner, 6 × 2″. Long front panel of the cooler. |
| `brbsc-mini-2in.svg` | Mini, 2″ circle. BRBSC monogram — member sticker for tumblers, rod tubes, back glass. |
| `*.png` | 300 DPI transparent-background rasters for proofing and quick sharing. |
| `index.html` | Preview, mockups, palette, and production spec sheet. |
| `build-artwork.py` | Regenerates all four SVGs. `python3 build-artwork.py` |

The roundel and the crest are two treatments of the same mark, not a first and
second draft — pick one for the coolers and the other looks right on a truck
window or a hat patch.

## Why it is built this way

- **No font dependencies.** The `BOAT SODA CLUB` wordmark and the `BRBSC`
  monogram are hand-drawn vector paths, so nothing substitutes at a printer's
  RIP. Only the curved ring type and the tagline use a bold system face —
  outline those before cutting.
- **Flat color, no gradients.** Cuts cleanly in vinyl, prints consistently,
  and holds up in sun.
- **The white die-cut border is part of the art.** ~0.09″ (2.3 mm) at full
  size. Contour cut outside it; never cut to the navy.
- **Every SVG declares real-world dimensions** (`width="4.5in"`), so it drops
  into a layout at the correct size without scaling guesswork.

## Palette

| Color | Hex | Spot match |
| --- | --- | --- |
| River Navy | `#0B2B45` | PMS 539 |
| Sunset Orange | `#F2711C` | PMS 165 |
| Pine Green | `#14503F` | PMS 7484 |
| Broad River Teal | `#16787D` | PMS 7717 |
| Sun-Bleached Cream | `#F7E7C6` | PMS 7499 |
| Can Coral | `#D93D2B` | PMS 7597 |

Supporting tints: `#F6A623` water shimmer, `#2FA0A0` river highlight,
`#0E3B2E` back treeline, `#EFD39B` cream shade, `#FFFFFF` die-cut border.

## Production summary

Cast vinyl (Oracal 751 / 3M IJ180) with a gloss UV-blocking overlaminate;
contour die cut; 5–7 years outdoor. Apply to a clean, dry, untextured panel
above 50°F with 70% isopropyl prep, and keep decals off the gasket, hinge, and
latch keepers. Hand wash only. Full detail is in `index.html`.

## Scaling

The art is vector — scale freely. Suggested placements: 20–35 qt coolers get
the mini on the lid and the banner on the front; 45–65 qt get the roundel or
crest on the lid and the banner on the front; 75 qt and up take the roundel
at 6″.
