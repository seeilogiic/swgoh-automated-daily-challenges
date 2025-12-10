import time

import pyautogui
from pywinauto import Desktop

from utils import ASSETS_DIR, click_image, locate_image_on_screen

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


def _get_window_region(window):
    rect = window.rectangle()
    return (rect.left, rect.top, rect.width(), rect.height())


def main():
    # Give BlueStacks a moment to be ready, if you’re launching it just before
    time.sleep(1)

    win = find_app_player_window()
    win.set_focus()

    # Optional small delay to ensure focus actually changed
    time.sleep(0.2)
    pyautogui.press("f")

    region = _get_window_region(win)

    green_okay = ASSETS_DIR / "green_okay.png"
    battle_button = ASSETS_DIR / "coliseum_battle_button.png"
    auto_play = ASSETS_DIR / "auto_play_button.png"
    green_continue = ASSETS_DIR / "green_continue.png"
    home_button = ASSETS_DIR / "home_button.png"

    # Click Coliseum/Battle first, then clear any OK modal.
    click_image(battle_button, region=region, attempts=10, delay=10.0)
    click_image(green_okay, region=region, attempts=10, delay=10.0)
    click_image(battle_button, region=region, attempts=10, delay=10.0)

    auto_point = locate_image_on_screen(
        auto_play,
        region=region,
        attempts=10,
        delay=10.0,
    )
    if auto_point:
        pyautogui.press("c")

    center_point = (region[0] + region[2] // 2, region[1] + region[3] // 2)
    continued = False
    for attempt in range(30):
        pyautogui.click(center_point)
        point = click_image(green_continue, region=region, attempts=1, delay=0.0)
        if point:
            continued = True
            break
        time.sleep(10)
    if not continued:
        print("[FAIL] Could not click green_continue after retries")

    click_image(home_button, region=region, attempts=10, delay=10)
    


if __name__ == "__main__":
    main()
