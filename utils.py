import os
import time
from pathlib import Path

import pyautogui

# Default asset location; override with ASSETS_DIR env var if needed.
ASSETS_DIR = Path(os.getenv("ASSETS_DIR", "images"))
BATTLE_BUTTON = ASSETS_DIR / "coliseum_battle_button.png"


def locate_image_on_screen(
    image_path: str | Path,
    region=None,
    confidence: float = 0.9,
    attempts: int = 10,
    delay: float = 5.0,
):
    """
    Look for an image on screen with retries. Returns a point or None.
    Never raises if the image is missing.
    """
    image = os.path.splitext(os.path.basename(str(image_path)))[0]
    image_path = Path(image_path)

    for attempt in range(attempts):
        try:
            point = pyautogui.locateCenterOnScreen(
                image_path.as_posix(),
                confidence=confidence,
                region=region,
            )
        except pyautogui.ImageNotFoundException:
            point = None

        if point:
            print(f"[INFO] Found image: {image}")
            return point

        if attempt < attempts - 1:
            print(f"[INFO] Could not find image: {image} | Try {attempt + 1}/{attempts}")
            time.sleep(delay)

    print(f"[WARN] Giving up finding image: {image}")
    return None


def click_battle_button(
    region=None,
    confidence: float = 0.9,
    attempts: int = 10,
    delay: float = 10.0,
    pause: float = 0.2,
):
    """
    Look for the battle button image and click it when found.
    Retries up to `attempts` with `delay` seconds between tries.
    Does not raise if the button is never found.
    """
    point = locate_image_on_screen(
        BATTLE_BUTTON,
        region=region,
        confidence=confidence,
        attempts=attempts,
        delay=delay,
    )

    if not point:
        print("[WARN] Battle button not found after retries; continuing without click.")
        return None

    pyautogui.click(point)
    time.sleep(pause)
    return point


if __name__ == "__main__":
    # Standalone usage: look for the battle button and click if present.
    click_battle_button()
