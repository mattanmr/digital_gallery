# 📺 Family Gallery — USB Setup Guide

## Folder structure on your USB stick

```
USB:/
├── gallery.html        ← The app (open this on the TV)
├── tags.local.json     ← Your saved tags (created automatically by local server)
├── tags.template.json  ← Optional tracked template tags file
└── photos/
    ├── IMG_2023_beach.jpg
    ├── Hanukkah_2022.jpg
    └── ...
```

---

## First-time setup

1. Copy `gallery.html` to the USB stick root.
2. Create a folder called `photos/` and copy all your images into it.
3. Safely eject the USB from your computer.
4. Plug the USB into your Toshiba TV (usually a USB port on the side or back).
5. On the TV, open the **browser** (look for "Internet" or "Browser" in the Smart TV menu).
6. In the browser address bar, type the path to the file. Try one of:
   - `file:///media/usb/gallery.html`
   - `file:///mnt/usb/gallery.html`
   - Or navigate using the TV browser's file manager if it has one.
7. The gallery now auto-scans `photos/` every ~10 seconds and adds new files automatically.
8. Optional fallback: you can still click the drop zone to load files manually.

### Quick launch scripts

- macOS: double-click [run-gallery-mac.command](run-gallery-mac.command)
- Windows: double-click [run-gallery-windows.bat](run-gallery-windows.bat)

Both scripts:
- start a local server in this project folder
- refresh `photos/manifest.local.json` automatically on startup
- create/update `tags.local.json` automatically on startup
- open [gallery.html](gallery.html)
- auto-open the gallery when photos are detected
- keep the server running until you close the terminal window or press `Ctrl+C`

### Auto-scan note (important)

Automatic folder polling works when the gallery is opened through a local web server (for example `http://127.0.0.1:4173/gallery.html`).
On strict `file:///` environments, some browsers block folder listing — manual file loading remains available.

### Manifest fallback (recommended)

This project keeps a tracked template at `photos/manifest.template.json` and uses an ignored local file at `photos/manifest.local.json` for real updates.

If your server/browser does not expose a directory listing for `photos/`, create `photos/manifest.local.json`:

```json
{
  "files": [
    "IMG_2023_beach.jpg",
    "Hanukkah_2022.jpg"
  ]
}
```

The gallery checks `photos/`, then `photos/manifest.local.json`, then `photos/manifest.template.json` during auto-scan.

To rebuild the manifest after adding/removing files:

1. Open the gallery via `http://...` (local server mode).
2. Click **🗂 Refresh Manifest** in the control bar.
3. The local server updates `photos/manifest.local.json` directly.

If the gallery is running on a plain static server without the included Python launcher, the button falls back to downloading `manifest.local.json` and you must place it inside `photos/` manually.

---

## How tags are saved between sessions

This project keeps a tracked template at `tags.template.json` and uses an ignored local file at `tags.local.json` for real updates.

When using the included local server:
- `tags.local.json` is created automatically on startup if needed
- the gallery auto-loads tags from `tags.template.json` and `tags.local.json`
- clicking **💾 Save Tags** updates `tags.local.json` directly

On a plain static server, **💾 Save Tags** falls back to downloading `tags.local.json`, and you can place it next to [gallery.html](gallery.html) manually.

Manual import via **Import tags.json** still works if you want to bring in an older exported tags file.

---

## Tagging tips

- **Year**: You can set it manually, or if your photo filename contains a year like
  `Photo_2021_summer.jpg`, the gallery detects it automatically.
- **Themes**: Use consistent names like `Beach`, `Kids`, `Travel`, `Holidays` —
  the filter dropdown is populated from whatever you type.
- **Caption**: Shows below the frame — great for short descriptions like "Mattan's birthday 2023".

---

## Pixel Shift (burn-in protection)

The gallery automatically shifts the entire image by a few pixels every 30 seconds.
This prevents screen burn-in on plasma and OLED TVs.
You can toggle it on/off from the bottom control bar badge (⬚ Pixel Shift: ON/OFF).

---

## Controls

| Action            | How                              |
|-------------------|----------------------------------|
| Cycle photos      | Automatic across all frames      |
| Speed             | Slider (4s – 40s per cycle)      |
| Shuffle           | 🔀 button                        |
| Add photos        | ＋ Photos button                 |
| Auto add from folder | Drop files into `photos/` (polled every ~10s) |
| Manifest fallback | List filenames in `photos/manifest.local.json` |
| Rebuild manifest  | 🗂 Refresh Manifest (updates `photos/manifest.local.json`) |
| Filter by year    | Year dropdown                    |
| Filter by theme   | Theme dropdown                   |
| Tag current photo | Frame hover → “🏷️ edit tags”    |
| Save tags         | 💾 Save Tags (updates `tags.local.json`) |
| Toggle pixel shift| ⬚ Pixel Shift ON/OFF             |
| Shuffle shortcut  | S key                            |
| Close modal       | Esc key                          |

Hover anywhere on screen to reveal the control bar.

---

## Tips for Toshiba Smart TV browsers

- If the font doesn't load (no internet on TV), the gallery still works fine — it falls back to a serif font.
- If the browser blocks local file access, try a different browser app on the TV, or use a laptop connected to the TV via HDMI instead.
- If auto-scan doesn't detect files on TV browser, use `photos/manifest.local.json` or the manual file picker.
- For the best experience, put the TV browser in **fullscreen mode** (usually F11 or the TV remote's full-screen button).
