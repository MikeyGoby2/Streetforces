import pyautogui as pt
from time import sleep
from sys import exit
import win32gui, win32con

sleep(0.2)

#hwnd = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

# all                                                                                                                               start while 2
print("##### WHILE 1 #####")
print("START ALL")
print("")
pt.FAILSAFE = True

    
# loop killing streetfroces 40
print("loop killing streetforces level 40") 
pt.FAILSAFE = True   
while 3:
    
    sleep(0.4)
    
    pt.screenshot("imgs/screenshot_region_ever_second_search_map.png", region=(828,803,67,49))
    # click on search map
    pt.moveTo (783, 751)
    sleep(0.35)
    pt.click()
    print("clickt search map")

    # new screen search
    sleep(0.3)
    
    pt.screenshot("imgs/screenshot_region_ever_second_search.png", region=(878,691,150,54))
    # click on search
    pt.moveTo (854, 656)
    sleep(0.05)
    pt.click()
    print("clickt search")
      
    # new screen
    sleep(0.8)
    
    pt.screenshot("imgs/screenshot_region_ever_second_attack.png", region=(647,685,155,56))
    # click to attack
    pt.moveTo (654, 650)
    sleep(0.3)
    pt.click()
    print("clickt on attack")
    
    # new screen
    sleep(0.3)

    pt.screenshot("imgs/screenshot_region_ever_second_time_attack.png", region=(790,786,154,54))
    # click on time attack
    pt.moveTo (775, 742)
    sleep(0.1)
    pt.click()
    print("clickt time attack")
    print("#####")
    print("")
   
