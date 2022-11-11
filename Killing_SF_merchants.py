from os import startfile
import pyautogui as pt
from time import sleep
import keyboard
import win32gui, win32con

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

pt.FAILSAFE = True


while 1:
    # move to loop
    print("move to loop")
    sleep(0.3)
    pt.moveTo(1116,913)
    sleep(0.3)
    pt.click(1116,913)

    # new screen
    sleep(0.3)
    
    # move to event
    #print("move to event")
    #pt.moveTo(671,557)
    #sleep(0.2)
    #pt.click(671,557)
    
    # new screen
    sleep(0.2)
    
    # click on Blaze
    #print("click on Blaze")
    #pt.moveTo(1013,432)
    #sleep(0.2)
    #pt.click(1013,432)

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

    pix = pt.pixelMatchesColor(1061,893, (125, 125, 125))
    
    if pix is True:
        print("gray time attack button")
        pt.moveTo(1405,222)
        sleep(0.2)
        pt.click(1405,222)
        
        #new screen
        sleep(1)
        
        # move to loop
        print("move to loop")
        sleep(0.3)
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)

        # new screen
        sleep(0.3)
          
        # move to event
        #print("move to event")
        #pt.moveTo(671,557)
        #sleep(0.2)
        #pt.click(671,557)
        
        # new screen
        sleep(0.2)
        
        # click on Blaze
        #print("click on Blaze")
        #pt.moveTo(1013,432)
        #sleep(0.2)
        #pt.click(1013,432)

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
    