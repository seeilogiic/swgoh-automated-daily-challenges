import os
import time
from pathlib import Path

import pyautogui

# Default asset location; override with ASSETS_DIR env var if needed.
ASSETS_DIR = Path(os.getenv("ASSETS_DIR", "images"))


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
    image_path = Path(image_path)
    image = image_path.stem

    if not image_path.exists():
        print(f"[FAIL] Image file not found: {image_path}")
        return None

    for attempt in range(attempts):
        try:
            point = pyautogui.locateCenterOnScreen(
                image_path.as_posix(),
                confidence=confidence,
                region=region,
            )
        except (pyautogui.ImageNotFoundException, OSError, pyautogui.PyAutoGUIException) as exc:
            # Treat any locate/read error as a miss, but do not raise.
            print(f"[WARN] Error locating image {image}: {exc}")
            point = None

        if point:
            print(f"[INFO] Found image: {image}")
            return point

        if attempt < attempts - 1:
            print(f"[INFO] Could not find image: {image} | Try {attempt + 1}/{attempts}")
            time.sleep(delay)

    print(f"[FAIL] Giving up finding image: {image}")
    return None


def click_image(
    image_path: str | Path,
    region=None,
    confidence: float = 0.9,
    attempts: int = 10,
    delay: float = 3.0,
    pause: float = 0.2,
):
    """
    Locate an image and click it if found. Returns the point or None.
    Does not raise if not found.
    """
    point = locate_image_on_screen(
        image_path,
        region=region,
        confidence=confidence,
        attempts=attempts,
        delay=delay,
    )

    if not point:
        print(f"[FAIL] Could not find: {image_path}")
        return None

    pyautogui.click(point)
    time.sleep(pause)
    print(f"[INFO] Clicked: {os.path.basename(str(image_path))}")
    return point


if __name__ == "__main__":
    # Example standalone usage: update the image path as needed.
    example_image = ASSETS_DIR / "coliseum_battle_button.png"
    click_image(example_image)
