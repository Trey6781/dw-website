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

### From an iPhone (including photos that live in iCloud)

**Photos in iCloud are not a problem.** iCloud Photos syncs into the Photos app,
and the picker reads from Photos — so it already sees your whole iCloud library
and fetches full-size originals on demand. Nothing needs downloading first.

1. Open `davenportandwillingham.com/slideshow/` in Safari.
2. Tap **Share → Add to Home Screen**. This matters: launched from the Home
   Screen the page runs without Safari's address and toolbar, so the picture
   fills the whole screen. iPhone Safari has no full-screen button, so this is
   the only way to get there.
3. Open it from the Home Screen, tap **Choose photos**, and select.
4. Turn the phone **sideways** — landscape fills a TV properly.
5. **AirPlay-mirror** to an Apple TV: swipe down for Control Centre → Screen
   Mirroring. (Chromecast users: cast the screen from a Chrome tab instead.)

#### Picking one year without endless scrolling

The iOS picker opens newest-first, so hunting for an old year by scrolling is
miserable. Make an album once instead:

*Photos → Library → Years → **2015** → Select → Add To Album → New Album.*

Then in the slideshow picker, tap **Albums**, choose that album, and Select All.
The year menu in the control bar is a useful double-check afterwards.

#### If photos are slow to appear

With *Optimise iPhone Storage* on, full-size photos live in iCloud and are
fetched only when something asks for them. Reading capture dates forces that
download, so a large selection can sit for a while — the page shows a running
count so you can tell it is working, not stuck.

Anything that never finishes downloading arrives empty. Rather than letting it
vanish from the show, the page counts those and tells you, so you know to get on
Wi-Fi and try again rather than wondering where photos went.

**Big batches are still the weak spot here.** The iOS picker gets tedious past a
few dozen, every one has to come down from iCloud, and a phone has far less
memory than a laptop. For a whole year, the next option is better.

### From a computer (best picture, more setup)

Get the photos onto a laptop once, plug it into the TV over HDMI, open the page,
choose the folder, and press `F`. This handles thousands of photos comfortably
and gives the best image quality.

Ways to get a year out of iCloud onto a computer:

- **icloud.com/photos** in any browser — sign in, select the photos, Download.
  Works on Windows and Mac.
- **Mac Photos app** — select the year, then *File → Export → Export Unmodified
  Originals*. Keeps EXIF, so the running order and date stamps stay right.
- **iCloud for Windows** — syncs a Photos folder into File Explorer that you can
  point the folder picker straight at.

Export originals rather than anything "optimised" or resized, or you may lose
the EXIF capture dates that the ordering and the year menu depend on.

### Other routes

- **Cast a Chrome tab** to a Chromecast or Google TV.
- **Smart TV browser** — works, but TV browsers are slow and their file pickers
  are poor. Only worth it if the TV can see a USB stick of photos.

## Controls

Everything is reachable from a keyboard, and most TV remotes' d-pads register
as arrow keys.

| Key | Does |
| --- | --- |
| `Space` / `Enter` | Play / pause |
| `←` `→` (or `↑` `↓`) | Back / forward a slide |
| `Home` / `End` | First / last slide |
| `F` | Full screen *(not on iPhone — see above)* |
| `M` | Projector sound on/off |
| `G` | Film grain and dust on/off |
| `K` | Slow zoom (Ken Burns) on/off |
| `D` | Advance style — carousel clunk vs. slow dissolve |
| `S` | Shuffle |
| — | Year menu is in the control bar |
| `L` | Load different photos |
| `Esc` | Pause |

Clicking the picture also pauses. The controls and the mouse pointer hide
themselves a few seconds into playback.

## What it does with your photos

- **Orders them by when they were taken**, reading the EXIF `DateTimeOriginal`
  out of each JPEG. You can switch to newest-first, file name, or shuffle.
- **Filters to a single year.** Load the whole library, then pick a year from
  the menu to watch just that one — it lists only years actually present, with
  a count. `?year=2015` in the URL opens straight into that year, so you can
  keep a Home Screen shortcut per year.
- **Stamps the capture date** in the corner, like the orange date-back burn-in
  on a drugstore print — but **only when the date is a real capture time.**
  A file's modified date is not when the photo was taken; iOS stamps Photo
  Library exports with the moment you exported them. Photos without readable
  EXIF get no stamp and no year rather than a confidently wrong one, and if
  nothing in the batch has a capture date the year menu hides itself and the
  page says so.
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

iPhones save photos as HEIC by default, and browsers can't decode HEIC.

In practice this usually sorts itself out: when you pick from **Photo Library**
in iOS Safari, iOS hands the browser a converted JPEG. Going through the
**Files** app instead passes the raw HEIC through, which won't display.

Rather than guess from the file name, the page decodes one file to find out
whether this browser can actually read them, and only excludes them if it
genuinely can't — then it tells you. If you do hit it, either pick from Photo
Library rather than Files, or set *Settings → Camera → Formats → **Most
Compatible*** so new photos are saved as JPEG.

Note that this only changes *new* photos. Existing HEIC shots need exporting as
JPEG, which the Photo Library picker generally does for you anyway.

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
