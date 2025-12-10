# swgoh-automated-daily-challenges

Helpers for automating the Star Wars: Galaxy of Heroes daily flow inside BlueStacks using pywinauto + pyautogui (with OpenCV for confidence matching).

## Quick start

1. Install dependencies in your environment:
   ```bash
   pip install pywinauto pyautogui opencv-python
   ```
2. Capture the buttons you need to click as PNG/JPG assets and drop them in `assets/` (or your chosen assets dir).
3. Optionally set environment variables for convenience:
   - `BLUESTACKS_PATH` (path to BlueStacks or a shortcut)
   - `BLUESTACKS_TITLE` (window title)
   - `ASSETS_DIR` (folder for your assets)
   - `HD_PLAYER_PATH` (default `C:\Program Files\BlueStacks_nxt\HD-Player.exe`)
4. Update the constants at the bottom of `automation.py` if you prefer hard-coded values over env vars.
5. Run the script:
   ```bash
   python automation.py
   ```

## Launch SWGOH directly via HD-Player

If you just want to start the game without image clicks, use `launch_swgoh.py`. Set `HD_PLAYER_PATH` in your environment (default: `C:\Program Files\BlueStacks_nxt\HD-Player.exe`). Optional: `BLUESTACKS_INSTANCE` if you have a named instance. Then run:
```bash
python launch_swgoh.py
```

## How it works

- `connect_bluestacks` connects to an existing BlueStacks window (or starts it if you provide the executable path) and focuses it.
- `locate_image_on_screen` wraps `pyautogui.locateCenterOnScreen` with retries, configurable attempts/delay, and confidence.
- `click_image` uses the current BlueStacks window bounds to limit searches and clicks matching images.
- `run_sequence` chains multiple image clicks in order and stops on the first miss.

Tune attempts/delay/confidence/pause arguments at call time to match your setup. Add or reorder steps in `launch_steps` (and any custom sequences) to automate more in-game actions.
