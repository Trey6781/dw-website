# Boat Sodas — cooler decal kit

Die-cut vinyl decal artwork for coolers. Open `index.html` for the visual
preview, mockups on a cooler, palette, and the full print/cut spec.

## Files

| File | What it is |
| --- | --- |
| `boat-sodas-badge-4.5in.svg` | Primary badge, 4.5″ circle. Lid or front panel. |
| `boat-sodas-banner-6x2in.svg` | Banner, 6″ × 2″. Long front panel. |
| `boat-sodas-mini-2in.svg` | Mini badge, 2″ circle. Ring type dropped for legibility. |
| `*.png` | 300 DPI transparent-background rasters of each, for proofing and quick sharing. |
| `index.html` | Preview, mockups, palette, and production spec sheet. |
| `build-artwork.py` | Regenerates all three SVGs. `python3 build-artwork.py` |

## Why it is built this way

- **No font dependencies.** The `BOAT SODAS` wordmark is hand-drawn vector
  paths, so nothing substitutes at the printer's RIP. Only the small ring
  type uses a bold system face — outline it before cutting.
- **Four flat colors, no gradients.** Cuts cleanly in vinyl, prints
  consistently, and holds up in sun.
- **White die-cut border is part of the art.** ~0.09″ (2.3 mm) at full size.
  Contour cut outside it; never cut to the navy.
- **Every SVG carries real-world dimensions** (`width="4.5in"`), so it
  drops into a layout at the correct size without scaling guesswork.

## Palette

| Color | Hex | Spot match |
| --- | --- | --- |
| Harbor Navy | `#0B2B45` | PMS 539 |
| Sunset Orange | `#F2711C` | PMS 165 |
| Deep Water Teal | `#16787D` | PMS 7717 |
| Sun-Bleached Cream | `#F7E7C6` | PMS 7499 |
| Cooler Coral | `#E14A32` | accent only |
| Die-Cut White | `#FFFFFF` | cut border |

## Production summary

Cast vinyl (Oracal 751 / 3M IJ180) with a gloss UV-blocking overlaminate;
contour die cut; 5–7 years outdoor. Apply to a clean, dry, untextured panel
above 50°F with 70% isopropyl prep, and keep decals off the gasket, hinge,
and latch keepers. Hand wash only. Full detail is in `index.html`.

## Scaling

The art is vector — scale freely. Suggested placements: 20–35 qt coolers get
the mini on the lid and the banner on the front; 45–65 qt get the badge on
the lid and the banner on the front; 75 qt and up take the badge at 6″.
