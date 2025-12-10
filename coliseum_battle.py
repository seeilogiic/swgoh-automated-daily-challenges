from pywinauto import Application, Desktop
import pyautogui
import time

TITLE_PATTERN = ".*BlueStacks.*"  # adjust after inspecting titles

def find_app_player_window():
    desktop = Desktop(backend="win32")
    windows = desktop.windows()  # no filter yet; we’ll debug titles

    # Debug: print candidate windows that contain "BlueStacks"
    for w in windows:
        text = w.window_text()
        if "BlueStacks" in text:
            print("Found candidate:", hex(w.handle), repr(text))

    # Now actually filter by title regex
    candidates = desktop.windows(title_re=TITLE_PATTERN)

    if not candidates:
        raise RuntimeError("No BlueStacks windows found (check title pattern).")

    # If there are multiple, pick App Player if possible
    for w in candidates:
        if "App Player" in w.window_text():
            return w

    return candidates[0]

# Give BlueStacks a moment to be ready, if you’re launching it just before
time.sleep(1)

win = find_app_player_window()
win.set_focus()

# Optional small delay to ensure focus actually changed
time.sleep(0.2)
pyautogui.press("f")
