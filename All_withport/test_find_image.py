import pyautogui as pt
from time import sleep
import keyboard
import win32api, win32con, win32gui


sleep(0.2)

#hwnd = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

sleep(0.2)

pt.FAILSAFE = True 

while 1:
    
    sleep(0.5)
    
    limit_100 = pt.locateOnScreen("imgs/limit_100.png", grayscale=False, region=(738,529,438,57), confidence=0.85)
    if limit_100 is not None:
        print("i see limit 100")
        
    if limit_100 is None:
        print("i not see limit 100")