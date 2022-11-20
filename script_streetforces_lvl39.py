import pyautogui as pt
from time import sleep
import win32gui, win32con

sleep(0.2)

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

print("START SELECT STREETFORCES LEVEL 39")

# select streetforces level 39
print("loop select streetforces level 39")
pt.FAILSAFE = True
while 1:
    
    # click on search map
    sleep(0.3)
    pt.moveTo(1116,913)
    sleep(0.3)
    pt.click(1116,913)
    print("clickt search")

    # new screen search
    sleep(0.8)
    
    # check screen search
    if pt.pixel(687,345)[0] != 85:
        print("-----check screen search NOT OK-----")
        
        sleep(0.3)
        
        # click on search map
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)
        print("clickt search map rescue")
        print("end loop check screen event")
    
    # click on daily
    pt.moveTo(669,419)
    sleep(0.2)
    pt.click()
    print("clickt daily")
    
    
    # click on streetforces
    pt.moveTo(871,431)
    sleep(0.2)
    pt.click()
    sleep(0.2)
    print("clickt streetforces")
    
    # click on select numbers
    pt.moveTo(1312,690)
    sleep(0.2)
    pt.click()
    print("clickt select numbers")
    
    # remove numbers
    pt.press("backspace")
    sleep(0.2)
    pt.press("backspace")
    sleep(0.2)
    pt.press("3")
    sleep(0.2)
    pt.press("9")
    print("remove numbers")

    # click to search
    pt.moveTo(1086,794)
    sleep(0.2)
    pt.click(1086,794)
    sleep(0.3)
    print("clickt search")

    # break no troops
    NoMore = pt.locateCenterOnScreen("imgs/NoMoreTroops.png", grayscale=False, confidence=0.75)
    if NoMore is not None:
        print("no more left")
        print(" end killing streetforces level 39")
        
        # exit screen
        pt.moveTo(1348,345)
        sleep(0.2)
        pt.click()
        print("exit screen")
        break
      
    # new screen
    sleep(0.4)

    # click to attack
    pt.moveTo(959,788)
    sleep(0.4)
    pt.click(959,788)
    sleep(0.6)
    print("clickt on attack")
    
    # if no more energy
    Energy = pt.locateOnScreen("imgs/Energy.png", grayscale=False, confidence=0.70)
    if Energy is not None:
        print("no more energy")
        # click on use 100 energy
        pt.moveTo(1270,643)
        sleep(0.2)
        pt.click(1270,643)
        print("clickt 2th energy")
        
        # new screen
        sleep(1)
        
        # click on use
        pt.moveTo(954,699)
        sleep(0.5)
        pt.click(954,699)
        sleep(0.2)
        pt.click(954,699)
        print("clickt use")
        
        # exit screen energy
        pt.moveTo(1379,292)
        sleep(0.2)
        pt.click()
        print("exit screen energy")
        

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
    
    # check gray button time attack
    pix = pt.pixelMatchesColor(1061,893, (125, 125, 125))
    if pix is True:
        print("gray time attack button")
        
        # exit time attack
        pt.moveTo(1405,222)
        sleep(0.2)
        pt.click(1405,222)
        print("exit time attack")
        
        #new screen
        sleep(1)
        
        # click on search map
        sleep(0.3)
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)
        print("clickt search map")

        # new screen
        sleep(0.3)

        # click on search
        pt.moveTo(1086,794)
        sleep(0.2)
        pt.click(1086,794)
        sleep(0.3)
        print("clickt search")

        # break no troops
        NoMore = pt.locateCenterOnScreen("imgs/NoMoreTroops.png", grayscale=False, confidence=0.75)
        if NoMore is not None:
            print("no more left")
            break

        # new screen
        sleep(0.4)

        # click on attack
        pt.moveTo(959,788)
        sleep(0.4)
        pt.click(959,788)
        sleep(0.6)
        print("clickt attack")
        
        # if no more energy
        Energy = pt.locateOnScreen("imgs/Energy.png", grayscale=False, confidence=0.70)
        if Energy is not None:
            print("no more energy")
            
            # click on use 100 energy
            pt.moveTo(1270,643)
            sleep(0.2)
            pt.click(1270,643)
            print("clickt 2th energy")
            
            # new screen
            sleep(1)
            
            # click on use
            pt.moveTo(954,699)
            sleep(0.5)
            pt.click(954,699)
            print("clickt use")
            
            # exit screen energy
            pt.moveTo(1379,292)
            sleep(0.2)
            pt.click()
            print("exit screen energy")

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

    # click on time attack
    pt.moveTo(1113,903)
    sleep(0.1)
    pt.click(1113,903)
    sleep(0.3)
    print("clickt time attack")
    break

print("END SELECT STREETFORCES LEVEL 39")
print("######")
print("START KILLING STREETFORCES LEVEL 39")

# loop killing streetfroces 39
print("loop killing streetforces level 39") 
pt.FAILSAFE = True   
while 1:
    
    # click on search map
    sleep(0.3)
    pt.moveTo(1116,913)
    sleep(0.3)
    pt.click(1116,913)
    print("clickt search map")

    # new screen
    sleep(0.8)
    
    # check screen search
    if pt.pixel(687,345)[0] != 85:
        print("-----check screen search NOT OK-----")
        
        # click to loop
        sleep(0.3)
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)
        print("clickt on loop rescue")
        print("end loop check screen event")

    # click on search
    pt.moveTo(1086,794)
    sleep(0.2)
    pt.click(1086,794)
    sleep(0.3)
    print("clickt search")

    # break no troops
    NoMore = pt.locateCenterOnScreen("imgs/NoMoreTroops.png", grayscale=False, confidence=0.75)
    if NoMore is not None:
        print("no more left")
        
        # exit screen
        pt.moveTo(1348,345)
        sleep(0.2)
        pt.click()
        print("exit screen")
        print(" end killing streetforces level 39")
        break
      
    # new screen
    sleep(0.4)

    # click on attack
    pt.moveTo(959,788)
    sleep(0.4)
    pt.click(959,788)
    sleep(0.6)
    print("clickt on attack")
    
    # if no more energy
    Energy = pt.locateOnScreen("imgs/Energy.png", grayscale=False, confidence=0.70)
    if Energy is not None:
        print("no more energy")
        
        # click on use 100 energy
        pt.moveTo(1270,643)
        sleep(0.2)
        pt.click(1270,643)
        print("clickt 2th energy")
        
        # new screen
        sleep(1)
        
        # click on use
        pt.moveTo(954,699)
        sleep(0.5)
        pt.click(954,699)
        sleep(0.2)
        pt.click(954,699)
        print("clickt use")
        
        # exit screen energy
        pt.moveTo(1379,292)
        sleep(0.2)
        pt.click()
        print("exit screen energy")
        

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
    
    # check for gray button time attack 
    pix = pt.pixelMatchesColor(1061,893, (125, 125, 125))
    if pix is True:
        print("i see gray time attack button")
        
        # exit screen
        pt.moveTo(1405,222)
        sleep(0.2)
        pt.click(1405,222)
        print("exit screen")
        
        #new screen
        sleep(1)
        
        # click on search map
        sleep(0.3)
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)
        print("clickt search map")

        # new screen
        sleep(0.3)

        # click on search
        pt.moveTo(1086,794)
        sleep(0.2)
        pt.click(1086,794)
        sleep(0.3)
        print("clickt search")

        # break no troops
        NoMore = pt.locateCenterOnScreen("imgs/NoMoreTroops.png", grayscale=False, confidence=0.75)
        if NoMore is not None:
            print("no more left")
            print("end killing streetforces level 39")
            break

        # new screen
        sleep(0.4)

        # click on attack
        pt.moveTo(959,788)
        sleep(0.4)
        pt.click(959,788)
        sleep(0.6)
        print("clickt attack")
        
        # if no more energy
        Energy = pt.locateOnScreen("imgs/Energy.png", grayscale=False, confidence=0.70)
        if Energy is not None:
            print("no more energy")
            
            # click on use 100 energy
            pt.moveTo(1270,643)
            sleep(0.2)
            pt.click(1270,643)
            print("clickt 2th energy")
            
            # new screen
            sleep(1)
            
            # click on use
            pt.moveTo(954,699)
            sleep(0.5)
            pt.click(954,699)
            print("clickt use")
            
            # exit screen energy
            pt.moveTo(1379,292)
            sleep(0.2)
            pt.click()
            print("exit screen energy")
              

        # if no more crew left
        AllTroopsOut = pt.locateOnScreen("imgs/AllTroopsOut.png", grayscale=False, confidence=0.70)
        if AllTroopsOut is not None:
            print("all buzzy")
            
            # take break 3 sec
            sleep(3)
            print("break 3 seconds")

        # if kill 100 SF
        SF_100 = pt.locateOnScreen("imgs/SF_100.png", grayscale=False, confidence=0.70)
        if AllTroopsOut is not None:
            print("kill 100 SF")
            sleep(0.1)
            
            # click on yes
            pt.moveTo(957,699)
            sleep(0.3)
            pt.click(957,699)
            sleep(0.2)
            print("clickt yes")

        # new screen
        sleep(0.1)

    # clik on time attack
    pt.moveTo(1113,903)
    sleep(0.1)
    pt.click(1113,903)
    sleep(0.3)
    print("clickt time attack")
    
print("END STREETFORCES LEVEL 39")