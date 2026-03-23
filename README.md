# 📺 Family Gallery — USB Setup Guide

## Folder structure on your USB stick

```
USB:/
├── gallery.html        ← The app (open this on the TV)
├── tags.json           ← Your saved tags (created after first session)
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
7. When the gallery opens, click the drop zone and navigate to `photos/` to load your images.

---

## How tags are saved between sessions

Because the gallery is a local HTML file (not a website), it cannot save data
automatically. Here's the simple 2-step workflow for `gallery.html`:

### At the END of a session:
- Click **💾 Save Tags** in the control bar
- Click **⬇ Download tags.json**
- Copy the downloaded `tags.json` to the USB stick (replace the old one)

### At the START of the next session:
- On the welcome screen, click **Import tags.json**
- Select the `tags.json` from the USB
- Then load your photos as usual — all captions, years and themes will be applied automatically

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
| Filter by year    | Year dropdown                    |
| Filter by theme   | Theme dropdown                   |
| Tag current photo | Frame hover → “🏷️ edit tags”    |
| Save tags         | 💾 Save Tags → Download          |
| Toggle pixel shift| ⬚ Pixel Shift ON/OFF             |
| Shuffle shortcut  | S key                            |
| Close modal       | Esc key                          |

Hover anywhere on screen to reveal the control bar.

---

## Tips for Toshiba Smart TV browsers

- If the font doesn't load (no internet on TV), the gallery still works fine — it falls back to a serif font.
- If the browser blocks local file access, try a different browser app on the TV, or use a laptop connected to the TV via HDMI instead.
- For the best experience, put the TV browser in **fullscreen mode** (usually F11 or the TV remote's full-screen button).
