import pyautogui as pygui
print(pygui.size())
import time
while True:
    pygui.moveTo(700,200, duration = 2)
    time.sleep(10)
    pygui.moveTo(400,300, duration = 2)
    #pygui.scroll(-100)
