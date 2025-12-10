import os
import subprocess
import sys
from pathlib import Path


def launch_swgoh(
    hd_player_path: str,
    package: str = "com.ea.game.starwarscapital_row",
    instance: str | None = None,
) -> int:
    if not hd_player_path:
        raise ValueError("HD-Player path is required (set HD_PLAYER_PATH).")

    exe = Path(hd_player_path)
    if not exe.exists():
        raise FileNotFoundError(f"HD-Player not found at {exe}")

    cmd = [exe.as_posix(), "--cmd", "launchApp", "--package", package]
    if instance:
        cmd.insert(1, "--instance")
        cmd.insert(2, instance)

    print("Running:", " ".join(cmd))
    return subprocess.call(cmd)


if __name__ == "__main__":
    hd_player_path = os.getenv("HD_PLAYER_PATH", r"C:\Program Files\BlueStacks_nxt\HD-Player.exe")
    instance_name = os.getenv("BLUESTACKS_INSTANCE") or None
    package = os.getenv("SWGOH_PACKAGE", "com.ea.game.starwarscapital_row")

    try:
        code = launch_swgoh(hd_player_path, package=package, instance=instance_name)
    except Exception as exc:  # pragma: no cover
        print(f"Error: {exc}")
        sys.exit(1)
    sys.exit(code)
