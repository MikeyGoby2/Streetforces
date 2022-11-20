import pyautogui as pt
from time import sleep
import keyboard
import win32gui, win32con

sleep(0.2)

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

pt.FAILSAFE = True

#general loop
while 1:
    sleep(1)
    
    # select streetforces level 39
    while 1:
        print("start selecting streetforces level 39")
        
        # move to loop
        print("move to loop")
        sleep(0.3)
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)
    
        # new screen
        sleep(0.3)
        
        # select daily
        pt.moveTo(669,419)
        sleep(0.2)
        pt.click()
        
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
        
    ##############################################################################################
    
    # select streetforces level 40
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
        
        # set level 40
        print("select level 40")
        pt.moveTo(1312,690)
        sleep(0.2)
        pt.click()
        
        # remove numbers
        pt.press("backspace")
        sleep(0.2)
        pt.press("backspace")
        sleep(0.2)
        pt.press("4")
        sleep(0.2)
        pt.press("0")
        
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
        break
        
    while 1:
        print("start killing streetforces level 40")
        
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
            print(" end killing streetforces level 40")
            
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
        
    ##############################################################################################
    
    # setup varian
    while 1:
        # move to loop
        print("start selecting varian")
        print("move to loop")
        sleep(0.3)
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)

        # new screen
        sleep(0.3)

        # select varian
        varian = pt.locateOnScreen("imgs/varian.png", grayscale=False, confidence=0.8)
        if varian is None:
            print("no varian")
            
            # exit screen
            pt.moveTo(1349,343)
            sleep(0.2)
            pt.click()
            break
        
        if varian is not None:
            print("i see varian")
            pt.moveTo(varian)
            sleep(0.2)
            pt.click()
            sleep(0.2)
            
            # exit screen
            pt.moveTo(1348,345)
            sleep(0.2)
            pt.click()
            print("selected varian")
            print("end selecting varian")
            sleep(1)
            

            # killing varian
            # move to loop
            print("start killing varian")
            while 2:
                sleep(1)
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
                sleep(0.5)
          
                # break no troops
                NoMore = pt.locateCenterOnScreen("imgs/NoMoreTroops.png", grayscale=False, confidence=0.75)
                if NoMore is not None:
                    print("no more left")
                    print("end killing varian")
          
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
                
                if pt.pixel(913,778)[0] == 102:
                    print("no more varian")
                    sleep(0.5)
                    
                    # exit screen
                    pt.click(1353,361)
                    sleep(0.2)
                    pt.click()
                    print("exit screen")
                    break
          
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
                    
                    if pt.pixel(913,778)[0] == 102:
                        print("no more varian")
                        sleep(0.5)
                        
                        # exit screen
                        pt.click(1353,361)
                        sleep(0.2)
                        pt.click()
                        print("exit screen")
                        break
                    
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
                sleep(0.7)
      
        break
        
    ###############################################################################################
    
    # setup haunter
    while 1:
        # move to loop
        print("start selecting haunter")
        print("move to loop")
        sleep(0.3)
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)

        # new screen
        sleep(0.3)

        # select haunter
        haunter = pt.locateOnScreen("imgs/haunter.png", grayscale=False, confidence=0.8)
        if haunter is None:
            print("no haunter")
            
            # exit screen
            pt.moveTo(1349,343)
            sleep(0.2)
            pt.click()
            break
        
        if haunter is not None:
            print("i see haunter")
            pt.moveTo(haunter)
            sleep(0.2)
            pt.click()
            sleep(0.2)
            
            # exit screen
            pt.moveTo(1348,345)
            sleep(0.2)
            pt.click()
            print("selected haunter")
            print("end selecting haunter")
            sleep(1)
            

            # killing haunter
            # move to loop
            print("start killing haunter")
            while 2:
                sleep(1)
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
                sleep(0.5)
          
                # break no troops
                NoMore = pt.locateCenterOnScreen("imgs/NoMoreTroops.png", grayscale=False, confidence=0.75)
                if NoMore is not None:
                    print("no more left")
                    print("end killing haunter")
          
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
                
                if pt.pixel(913,778)[0] == 102:
                    print("no more varian")
                    sleep(0.5)
                    
                    # exit screen
                    pt.click(1353,361)
                    sleep(0.2)
                    pt.click()
                    print("exit screen")
                    break
          
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
                    
                    if pt.pixel(913,778)[0] == 102:
                        print("no more varian")
                        sleep(0.5)
                        
                        # exit screen
                        pt.click(1353,361)
                        sleep(0.2)
                        pt.click()
                        print("exit screen")
                        break
                    
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
                sleep(0.7)
      
        break
     
###################################################################################################
    # setup reaper
    while 1:
        # move to loop
        print("start selecting reaper")
        print("move to loop")
        sleep(0.3)
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)

        # new screen
        sleep(0.3)

        # select reaper
        reaper = pt.locateOnScreen("imgs/reaper.png", grayscale=False, confidence=0.8)
        if reaper is None:
            print("no reaper")
            
            # exit screen
            pt.moveTo(1349,343)
            sleep(0.2)
            pt.click()
            break
        
        if reaper is not None:
            print("i see reaper")
            pt.moveTo(reaper)
            sleep(0.2)
            pt.click()
            sleep(0.2)
            
            # exit screen
            pt.moveTo(1348,345)
            sleep(0.2)
            pt.click()
            print("selected reaper")
            print("end selecting reaper")
            sleep(1)
            

            # killing reaper
            # move to loop
            print("start killing reaper")
            while 2:
                sleep(1)
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
                sleep(0.5)
          
                # break no troops
                NoMore = pt.locateCenterOnScreen("imgs/NoMoreTroops.png", grayscale=False, confidence=0.75)
                if NoMore is not None:
                    print("no more left")
                    print("end killing reaper")
          
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
                
                if pt.pixel(913,778)[0] == 102:
                    print("no more varian")
                    sleep(0.5)
                    
                    # exit screen
                    pt.click(1353,361)
                    sleep(0.2)
                    pt.click()
                    print("exit screen")
                    break
          
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
                    
                    if pt.pixel(913,778)[0] == 102:
                        print("no more varian")
                        sleep(0.5)
                        
                        # exit screen
                        pt.click(1353,361)
                        sleep(0.2)
                        pt.click()
                        print("exit screen")
                        break
                    
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
                sleep(0.7)
      
        break
 
###################################################################################################    
    
# setup white_shark
while 1:
    # move to loop
    print("start selecting white_shark")
    print("move to loop")
    sleep(0.3)
    pt.moveTo(1116,913)
    sleep(0.3)
    pt.click(1116,913)

    # new screen
    sleep(0.3)

    # select white_shark
    white_shark = pt.locateOnScreen("imgs/white_shark.png", grayscale=False, confidence=0.8)
    if white_shark is None:
        print("no white_shark")
        
        # exit screen
        pt.moveTo(1349,343)
        sleep(0.2)
        pt.click()
        break
    
    if white_shark is not None:
        print("i see white_shark")
        pt.moveTo(white_shark)
        sleep(0.2)
        pt.click()
        sleep(0.2)
        
        # exit screen
        pt.moveTo(1348,345)
        sleep(0.2)
        pt.click()
        print("selected white_shark")
        print("end selecting white_shark")
        sleep(1)
        

        # killing white_shark
        # move to loop
        print("start killing white_shark")
        while 2:
            sleep(1)
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
            sleep(0.5)
      
            # break no troops
            NoMore = pt.locateCenterOnScreen("imgs/NoMoreTroops.png", grayscale=False, confidence=0.75)
            if NoMore is not None:
                print("no more left")
                print("end killing white_shark")
      
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
            sleep(0.7)
  
    break

###################################################################################################    
    # use random port
    
    while 1:
        print("start selecting random port")
    
        # new screen
        sleep(40)
        
        # move and click on items
        print("go to items")
        pt.moveTo(857,995)
        sleep(0.2)
        pt.click(857,995)
        
        # new screen
        sleep(3)
        
        # move and click on sqaure 1, on use
        print("click on random port")
        pt.moveTo(841,388)
        sleep(0.2)
        pt.click(841,388)
        sleep(0.5)
        pt.moveTo(1313,530)
        sleep(0.2)
        pt.click(1313,530)
        
        # new screen
        sleep(1)
        
        # click on use
        print("use random port")
        pt.moveTo(951,699)
        sleep(0.2)
        pt.click(951,699)
        break