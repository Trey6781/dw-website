# The Carousel — a family slide projector

An old-school Kodak-carousel slide show for family photos, meant to be watched
on a TV. One file, no build step, no dependencies.

**Live:** https://davenportandwillingham.com/slideshow/

It is deliberately not linked from the main site's navigation.

## Your photos stay on your device

The page reads photos straight off the device it is running on, through the
browser's file picker or drag-and-drop. **Nothing is uploaded and nothing is
committed to this repo.** Reloading the page clears them — you pick the folder
again each time.

That matters here: this repo is published to a public domain, so any photo
committed into it would be public. Don't commit family photos unless you
genuinely want them public.

## Watching it on the TV

Pick whichever is easiest:

- **Smart TV browser** — open `davenportandwillingham.com/slideshow/`, then use
  the TV's own file picker if it has one. Support varies a lot by TV.
- **Laptop plugged into the TV via HDMI** *(most reliable, best picture)* —
  open the page, choose your photo folder, press `F` for full screen.
- **Cast a browser tab** from Chrome to a Chromecast / Google TV.
- **Apple TV** — AirPlay-mirror a Mac or iPad.

The page asks for a screen wake lock while playing, so the TV shouldn't blank
out mid-show.

## Controls

Everything is reachable from a keyboard, and most TV remotes' d-pads register
as arrow keys.

| Key | Does |
| --- | --- |
| `Space` / `Enter` | Play / pause |
| `←` `→` (or `↑` `↓`) | Back / forward a slide |
| `Home` / `End` | First / last slide |
| `F` | Full screen |
| `M` | Projector sound on/off |
| `G` | Film grain and dust on/off |
| `K` | Slow zoom (Ken Burns) on/off |
| `D` | Advance style — carousel clunk vs. slow dissolve |
| `S` | Shuffle |
| `L` | Load different photos |
| `Esc` | Pause |

Clicking the picture also pauses. The controls and the mouse pointer hide
themselves a few seconds into playback.

## What it does with your photos

- **Orders them by when they were taken**, reading the EXIF `DateTimeOriginal`
  out of each JPEG. Files without EXIF fall back to their modified date. You can
  switch to newest-first, file name, or shuffle.
- **Stamps the capture date** in the corner, like the orange date-back burn-in
  on a drugstore print.
- **Keeps only a few slides in memory at a time**, so a folder with thousands of
  photos won't sink the browser.
- **Skips anything it can't display** rather than showing a blank slide.

## The projector effects

All synthesized in the browser — there are no image or audio assets to ship.

- The **ka-chunk** on every advance: a solenoid snap, the slide landing in the
  gate, and the tray's rattle, built from Web Audio oscillators and noise.
- A **cooling-fan and lamp hum** underneath the whole show.
- The gate goes **dark between slides** while the tray rotates; the next slide
  drops in from above and settles.
- **Gate weave** — the slow mechanical drift of a real projector.
- **Dust, hairs and scratches** redrawn on every advance, the way real grit
  shifts between slides.
- **Film grain**, lamp flicker, a warm halation glow, and the cardboard
  **slide mount** around each picture.

`G` turns the grain and dust off; `M` turns the sound off.

## HEIC photos

iPhones save as HEIC by default and **browsers can't display HEIC**. The page
detects them, skips them, and says so.

To fix it, either set *Settings → Camera → Formats → **Most Compatible*** on the
iPhone so new photos are saved as JPEG, or export the existing ones as JPEG.

## Optional: a committed album

`photos.json` sits next to the page and is empty (`[]`) by default. If you ever
want an album that just plays on its own with no folder-picking — and you're
fine with those photos being **public** — put the images in this folder and list
them:

```json
[
  "reunion-2019.jpg",
  { "src": "beach.jpg", "caption": "Edisto, summer 2011", "date": "2011-07-04" }
]
```

`caption` and `date` are optional. When the list is non-empty the page skips the
load screen and starts playing on its own — which also makes it a decent kiosk
or waiting-room display.
