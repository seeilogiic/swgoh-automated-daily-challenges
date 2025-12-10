from pywinauto import Application
import pyautogui

app = Application(backend="uia").connect(title_re="BlueStacks App Player")
win = app.window(title_re="BlueStacks App Player")
win.set_focus()
pyautogui.press("f")
