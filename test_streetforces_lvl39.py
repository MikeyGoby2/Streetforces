import pyautogui as pt
from time import sleep
import keyboard
import win32gui, win32con

sleep(0.2)

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

pt.FAILSAFE = True

# select streetforces level 39
while 1:
    print("start slecting streetforces level 40")
    
    # move to loop
    print("move to loop")
    sleep(0.3)
    pt.moveTo(1116,913)
    sleep(0.3)
    pt.click(1116,913)

    # new screen
    sleep(0.3)
    
    # select streetforces
    print("select streetforces")
    pt.moveTo(871,431)
    sleep(0.2)
    pt.click()
    sleep(0.2)
    
    # set level 39
    print("select level 39")
    pt.moveTo(1312,690)
    sleep(0.2)
    pt.click()
    
    # remove numbers
    pt.press("backspace")
    sleep(0.2)
    pt.press("backspace")
    sleep(0.2)
    pt.press("3")
    sleep(0.2)
    pt.press("9")

    # exit screen
    print("exit screen")
    pt.moveTo(1349,343)
    sleep(0.2)
    pt.click()
    sleep(1)
    break
    
while 1:
    print("start killing streetforces level 39")
    
    # move to loop
    print("move to loop")
    sleep(0.3)
    pt.moveTo(1116,913)
    sleep(0.3)
    pt.click(1116,913)

    # new screen
    sleep(0.3)

    # move to search
    print("move to search")
    pt.moveTo(1086,794)
    sleep(0.2)
    pt.click(1086,794)
    sleep(0.3)

    # break no troops
    NoMore = pt.locateCenterOnScreen("imgs/NoMoreTroops.png", grayscale=False, confidence=0.75)
    if NoMore is not None:
        print("no more left")
        print(" end killing streetforces level 39")
        
        # exit screen
        pt.moveTo(1348,345)
        sleep(0.2)
        pt.click()
        break
      
    # new screen
    sleep(0.4)

  # move to attack
    print("move to attack")
    pt.moveTo(959,788)
    sleep(0.4)
    pt.click(959,788)
    sleep(0.6)
    
    # if no more energy
    Energy = pt.locateOnScreen("imgs/Energy.png", grayscale=False, confidence=0.70)
    if Energy is not None:
        print("no more energy")
        # click on use 100 energy
        pt.moveTo(1270,643)
        sleep(0.2)
        pt.click(1270,643)
        
        # new screen
        sleep(1)
        
        # move to use
        pt.moveTo(954,699)
        sleep(0.2)
        pt.click(954,699)
        

    # if no more crew left
    AllTroopsOut = pt.locateOnScreen("imgs/AllTroopsOut.png", grayscale=False, confidence=0.70)
    if AllTroopsOut is not None:
        print("all buzzy")
        sleep(3)

    # if kill 100 SF
    SF_100 = pt.locateOnScreen("imgs/SF_100.png", grayscale=False, confidence=0.70)
    if AllTroopsOut is not None:
        print("kill 100 SF")
        sleep(0.1)
        pt.moveTo(957,699)
        sleep(0.3)
        pt.click(957,699)
        sleep(0.2)

    # new screen
    sleep(0.1)

    # move to time attack
    print("move to time attack")
    pt.moveTo(1113,903)
    sleep(0.1)
    pt.click(1113,903)
    sleep(0.3)