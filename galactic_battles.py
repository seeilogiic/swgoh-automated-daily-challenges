import time

import pyautogui
from pywinauto import Desktop

from utils import ASSETS_DIR, click_image, locate_image_on_screen

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


def _get_window_region(window):
    rect = window.rectangle()
    return (rect.left, rect.top, rect.width(), rect.height())


def main():
    time.sleep(1)
    win = find_app_player_window()
    win.set_focus()
    time.sleep(0.2)
    pyautogui.press("y")
    print("[INFO] Sent 'y' keypress for Galactic Battles start.")

    region = _get_window_region(win)

    green_enter = ASSETS_DIR / "green_enter.png"
    blue_restart = ASSETS_DIR / "blue_restart.png"
    blue_sim = ASSETS_DIR / "blue_sim.png"
    green_sim = ASSETS_DIR / "green_sim.png"
    green_continue = ASSETS_DIR / "green_continue.png"
    redeem = ASSETS_DIR / "blue_galactic_battle_redeem.png"
    green_buy_400 = ASSETS_DIR / "galactic_battle_400_buy.png"
    green_ok = ASSETS_DIR / "green_ok.png"
    green_buy = ASSETS_DIR / "green_buy.png"

    click_image(green_enter, region=region)
    click_image(blue_restart, region=region)
    click_image(blue_sim, region=region)
    click_image(green_ok, region=region, attempts=3, delay=3)
    click_image(green_sim, region=region)
    click_image(green_continue, region=region)
    click_image(redeem, region=region)
    time.sleep(10)

    rect = win.rectangle()
    start_x = rect.left + rect.width() // 2
    start_y = rect.top + rect.height() // 2

    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragRel(0, -500, duration=5, button='left')
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragRel(0, -500, duration=5, button='left')

    click_image(green_buy_400, region=region)
    click_image(green_buy, region=region)
    time.sleep(3)
    click_image(green_buy_400, region=region)
    click_image(green_buy, region=region)
    time.sleep(3)
    click_image(green_buy_400, region=region)
    click_image(green_buy, region=region)

    time.sleep(3)
    red_x = ASSETS_DIR / "red_x.png"
    click_image(red_x, region=region)

    time.sleep(3)
    home_button = ASSETS_DIR / "home_button.png"
    click_image(home_button, region=region)



if __name__ == "__main__":
    main()
