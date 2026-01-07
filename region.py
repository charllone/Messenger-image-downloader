import pyautogui
import time

print("Move mouse to TOP-LEFT of button area")
time.sleep(5)
x1, y1 = pyautogui.position()
print("Top-left:", x1, y1)

print("Move mouse to BOTTOM-RIGHT of button area")
time.sleep(5)
x2, y2 = pyautogui.position()
print("Bottom-right:", x2, y2)

print("Region =", (x1, y1, x2 - x1, y2 - y1))
