import time

import pyautogui
from pywinauto import Desktop

TITLE_PATTERN = ".*BlueStacks.*"  # adjust if your window title differs


def find_app_player_window():
    desktop = Desktop(backend="win32")
    candidates = desktop.windows(title_re=TITLE_PATTERN)
    if not candidates:
        raise RuntimeError("No BlueStacks windows found (check title pattern).")

    for w in candidates:
        if "App Player" in w.window_text():
            return w

    return candidates[0]


def main():
    time.sleep(1)
    win = find_app_player_window()
    win.set_focus()
    time.sleep(0.2)
    pyautogui.press("y")
    print("[INFO] Sent 'y' keypress for Galactic Battles start.")


if __name__ == "__main__":
    main()
