import pyautogui as pt
from time import sleep
import win32gui, win32con

sleep(0.2)

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)


# select streetforces blaze
print("-----START BLAZE-----")
pt.FAILSAFE = True
while 1:
    print("start slecting streetforces blaze")
    
    # move to loop
    print("move to loop")
    sleep(0.3)
    pt.moveTo(1116,913)
    sleep(0.3)
    pt.click(1116,913)

    # new screen search
    sleep(1)
    
    # check screen search
    if pt.pixel(687,345)[0] != 85:
        print("-----check screen event NOT OK-----")
        
        # click to loop
        sleep(0.3)
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)
        print("clickt on loop rescue")
        print("end loop check screen event")
    
    # click on event
    pt.moveTo(676,553)
    sleep(0.2)
    pt.click()
    print("clickt on event")
    
    # select blaze
    pt.moveTo(1016,432)
    sleep(0.2)
    pt.click()
    print("select blaze")
    
    # exit screen
    print("exit screen")
    pt.moveTo(1349,343)
    sleep(0.2)
    pt.click()
    sleep(1)

    print("start killing streetforces blaze")
    
    # click to loop
    sleep(0.3)
    pt.moveTo(1116,913)
    sleep(0.3)
    pt.click(1116,913)
    print("clickt on loop")

    # new screen
    sleep(0.5)
    
    # check new screen event
    print("check new screen event")
    if pt.pixel(687,345)[0] == 85:
        print("check screen event OK")
        print("end loop check screen event")
        
    if pt.pixel(687,345)[0] != 85:
        print("-----check screen event NOT OK-----")
        
        # click to loop
        sleep(0.3)
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)
        print("clickt on loop rescue")
        print("end loop check screen event")
            
    # click on event
    pt.moveTo(676,553)
    sleep(0.2)
    pt.click()
    print("clickt on event")
    
    # new screen
    sleep(0.5)
    
    # click on event
    pt.moveTo(676,553)
    sleep(0.2)
    pt.click()
    print("clickt on event")
    
    # select blaze
    pt.moveTo(1016,432)
    sleep(0.2)
    pt.click()
    print("select blaze")

    # click to search
    pt.moveTo(1086,794)
    sleep(0.2)
    pt.click(1086,794)
    print("clickt on search")
    sleep(0.3)

    # no troops
    NoMore = pt.locateCenterOnScreen("imgs/NoMoreTroops.png", grayscale=False, confidence=0.75)
    if NoMore is not None:
        print("no more left")
        print("end killing streetforces blaze")
        
        # exit screen
        pt.moveTo(1348,345)
        sleep(0.2)
        pt.click()
        break
      
    # new screen
    sleep(0.4)
    
    # check gray button limit
    print("check gray button limit")
    if pt.pixel(907,780)[0] == 102:
        print("end blaze")
        
        # exit screen attack
        pt.moveTo(1352,363)
        sleep(0.2)
        pt.click()
        print("exit attack limit")
        break
    
    if pt.pixel(907,780)[0] != 102:
        print("no gray button")

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
        
        # loop check
        print("start loop check")
        pt.FAILSAFE = True
        while 1:
            
            # check screen use
            if pt.pixel(656,291)[0] == 117:
                print("check screen use OK")
                print("end loop check")
                break
                
            if pt.pixel(656,291)[0] != 117:
                print("-----check screen use NOT OK-----")
                sleep(0.5)  
                break
            
        # click to use
        pt.moveTo(954,699)
        sleep(0.2)
        pt.click(954,699)
        print("clickt on use")
        
        #click on ok
        sleep(0.2)
        pt.click(954,699)
        print("clickt on ok")
        
        # exit screen energy
        pt.moveTo(1379,293)
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

    # move to time attack
    print("move to time attack")
    pt.moveTo(1113,903)
    sleep(0.1)
    pt.click(1113,903)
    sleep(0.3)
    
    # check gray button
    if pt.pixel(1062,897)[0] != 125:
        print("check gray button OK")
        
    if pt.pixel(1062,897)[0] == 125:
        print("-----check gray button NOT OK-----")
        
        # exit time attack
        pt.moveTo(1406,223)
        sleep(0.2)
        pt.click()
        print("exit time attack")
    
    print("-----END BLAZE-----")
    break