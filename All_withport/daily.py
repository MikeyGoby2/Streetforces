import pyautogui as pt
from time import sleep
from sys import exit
import win32gui, win32con

sleep(0.2)

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

sleep(0.5)

# all                                                                                                                               start while 2
print("##### WHILE 1 #####")
print("START ALL")
print("")
pt.FAILSAFE = True
while 1:
    ######################################################################################################################
    # streetforces level 40 ##############################################################################################
    ######################################################################################################################          start while 2
    print("##### WHILE 2 #####")
    print("START STREETFORCES LEVEL 40")

    # select streetforces level 40
    print("loop select streetforces level 40")
    pt.FAILSAFE = True
    while 2:
        
        # click on search map
        sleep(0.3)
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)
        print("clickt search")

        # new screen search
        sleep(0.5)
        
        # click on daily
        pt.moveTo(671,411)
        sleep(0.2)
        pt.click()
        print("clickt daily")
        
        # new screen
        sleep(0.5)
        
        # while 2 ####################################################################################################          check screen search

        # check screen search
        
        # screenshot region search
        screenshot_region_search= pt.screenshot("imgs/screenshot_region_search.png", region=(1146,774,146,36))
        print("screenshot region search")
        
        # check search
        search = pt.locateCenterOnScreen("imgs/search.png", grayscale=False, region=(1146,774,146,36), confidence=0.8)
        if search is None:
            print("-----check screen search NOT OK-----")
            
            sleep(0.3)
            
            # click on search map
            pt.moveTo(1116,913)
            sleep(0.3)
            pt.click(1116,913)
            print("clickt search map rescue")
            print("end loop check screen event")
            
        
        # click on streetforces
        pt.moveTo(881,432)
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
        print("remove numbers")
        
        # enter numbers
        pt.press("4")
        sleep(0.2)
        pt.press("0")
        sleep(0.2)
        print("entered numbers")

        # click to search
        pt.moveTo(1214,792)
        sleep(0.2)
        pt.click(1214,792)
        sleep(0.3)
        print("clickt search")
        
        # while 2 ####################################################################################################          no more troops
        
        # screenshot region no more troops
        screenshot_region_no_more_troops= pt.screenshot("imgs/screenshot_region_no_more_troops.png", region=(722,530,70,82))
        print("screenshot region no more troops")
        
        # search no more troops
        NoMore = pt.locateCenterOnScreen("imgs/NoMoreTroops.png", grayscale=False, region=(722,530,70,82), confidence=0.8)
        if NoMore is not None:
            print("no more troops left")
            
            # exit screen
            pt.moveTo(1371,340)
            sleep(0.2)
            pt.click()
            print("exit screen")
            print("end killing streetforces level 40")
            break
          
        # new screen
        sleep(1)
            
        # click to attack
        pt.moveTo(959,788)
        sleep(0.4)
        pt.click(959,788)
        sleep(0.6)
        print("clickt on attack")
        
        # new screen
        sleep(0.5)
        
        # while 2 ####################################################################################################          streetforces limit
        
        streetforces_limit=pt.locateOnScreen("imgs/streetforces_limit.png", grayscale=False, confidence=0.85)
        if streetforces_limit is not None:
            print("streetforce limit")
            
            # click exit screen
            pt.moveTo(1257,425)
            sleep(0.2)
            pt.click()
            print("exit screen yes")
            
            # new screen
            sleep(0.5)
            
            # exit attack
            pt.moveTo(1352,362)
            sleep(0.2)
            pt.click()
            print("exit screen attack")
            break
        
        # while 2 ####################################################################################################          no more energy
        
        # screenshot region no more energy
        screenshot_region_200_limit= pt.screenshot("imgs/screenshot_region_200_limit.png", region=(558,362,142,114))
        
        # search for no more energy
        Energy = pt.locateOnScreen("imgs/Energy.png", grayscale=False, region=(558,362,142,114), confidence=0.85)
        if Energy is not None:
            print("no more energy")
            
            # click on use 100 energy
            pt.moveTo(1270,643)
            sleep(0.2)
            pt.click(1270,643)
            print("clickt 2th energy")
            
            # new screen use
            sleep(1)
            
            # screenshot region no more gold
            screenshot_region_no_more_gold= pt.screenshot("imgs/screenshot_region_no_more_gold.png", region=(845,659,222,65))
            print("screenshot no more gold")
            
            # search for no more energy
            no_more_gold = pt.locateOnScreen("imgs/no_more_gold.png", grayscale=False, region=(845,659,222,65), confidence=0.85)
            print("search for no more gold")
            
            if no_more_gold is not None:
                print("i see no more gold")
                break
            
            # click on use
            pt.moveTo(954,699)
            sleep(0.5)
            pt.click(954,699)
            print("clickt use")
            
            # new screen ok
            sleep(0.2)
            
            # click on ok
            pt.moveTo(954,699)
            sleep(0.2)
            pt.click(954,699)
            print("clickt use")
            
            # new screen
            sleep(0.5)
            
            # screenshot region no more gold
            screenshot_region_no_more_gold= pt.screenshot("imgs/screenshot_region_no_more_gold.png", region=(845,659,222,65))
            print("screenshot no more gold")
            
            # search for no more energy
            no_more_gold = pt.locateOnScreen("imgs/no_more_gold.png", grayscale=False, region=(845,659,222,65), confidence=0.85)
            print("search for no more gold")
            
            if no_more_gold is not None:
                print("i see no more gold")
                break
            
            # exit screen energy
            pt.moveTo(1379,292)
            sleep(0.2)
            pt.click()
            print("exit screen energy")
            
        # while 2 ####################################################################################################          all troops out
            
        # screenshot all troops out
        screenshot_region_all_troops_out= pt.screenshot("imgs/screenshot_region_all_troops_out.png", region=(755,584,309,25))
        print("screenshot region all troops out")
        
        # search for all troops out
        AllTroopsOut = pt.locateOnScreen("imgs/AllTroopsOut.png", grayscale=False, region=(755,584,309,25), confidence=0.85)
        if AllTroopsOut is not None:
            print("i see all troops out")
            
            sleep(0.5)
            
            # exit screen all troops out
            pt.moveTo(1233,427)
            sleep(0.2)
            pt.click()
            print("exit all troops out")
            
            sleep(3)
            print("break of 3 seconds")
            
        # while 2 ####################################################################################################          limit 100

        # screenshot region limit 100
        screenshot_region_limit_100= pt.screenshot("imgs/screenshot_region_limit_100.png", region=(738,529,438,57))
        print("screenshot region limit 100")
        
        # search for limit 100
        limit_100 = pt.locateOnScreen("imgs/limit_100.png", grayscale=False, region=(738,529,438,57), confidence=0.85)
        if limit_100 is not None:
            print("i see limit 100")
            
            sleep(0.5)
            
            # click on yes
            pt.moveTo(957,699)
            sleep(0.3)
            pt.click(957,699)
            sleep(0.2)
            print("clickt yes")

        # new screen
        sleep(0.3)
        
        # while 2 ####################################################################################################          gray button time attack
        
        # check gray button time attack
        pix = pt.pixelMatchesColor(1061,893, (125, 125, 125))
        if pix is True:
            print("gray time attack button")
            
            sleep(0.5)
            
            # exit time attack
            pt.moveTo(1405,222)
            sleep(0.2)
            pt.click(1405,222)
            print("exit time attack rescue")
            break

        # click on time attack
        pt.moveTo(1113,903)
        sleep(0.1)
        pt.click(1113,903)
        sleep(0.3)
        print("clickt time attack")
        break

    print("END SELECT STREETFORCES LEVEL 40")
    print("")

    ######################################################################################################################          end while 2
    # while 3
    ######################################################################################################################          start while 3 

    print("##### WHILE 3 #####")
    print("START KILLING STREETFORCES LEVEL 40")

    # loop killing streetfroces 40
    print("loop killing streetforces level 40") 
    pt.FAILSAFE = True   
    while 3:
        
        sleep(0.5)
        print("")
        
        # click on search map
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)
        print("clickt search map")

        # new screen search
        sleep(0.8)
        
        # while 3 ####################################################################################################          check screen search
        
        # check screen search
        
        # screenshot region search
        screenshot_region_search= pt.screenshot("imgs/screenshot_region_search.png", region=(1146,774,146,36))
        print("screenshot region no more troops")
        
        # check search
        search = pt.locateCenterOnScreen("imgs/search.png", grayscale=False, region=(1146,774,146,36), confidence=0.8)
        if search is None:
            print("-----check screen search NOT OK-----")
            
            sleep(0.3)
            
            # click on search map
            pt.moveTo(1116,913)
            sleep(0.3)
            pt.click(1116,913)
            print("clickt search map rescue")
            print("end loop check screen event")

        # click on search
        pt.moveTo(1214,792)
        sleep(0.2)
        pt.click(1214,792)
        sleep(0.3)
        print("clickt search")
        
        # while 3 ####################################################################################################          no more troops

        # break no troops
        NoMore = pt.locateCenterOnScreen("imgs/NoMoreTroops.png", grayscale=False, confidence=0.75)
        if NoMore is not None:
            print("no more left")
            
            sleep(0.5)
            
            # exit screen
            pt.moveTo(1371,340)
            sleep(0.2)
            pt.click()
            print("exit screen")
            print("end killing streetforces level 40")
            break
          
        # new screen
        sleep(1)
        
        # click to attack
        pt.moveTo(959,788)
        sleep(0.4)
        pt.click(959,788)
        sleep(0.6)
        print("clickt on attack")
        
        # new screen
        sleep(0.5)
        
        # while 2 ####################################################################################################          streetforces limit
        
        streetforces_limit=pt.locateOnScreen("imgs/streetforces_limit.png", grayscale=False, confidence=0.85)
        if streetforces_limit is not None:
            print("streetforce limit")
            
            # click exit screen
            pt.moveTo(1257,425)
            sleep(0.2)
            pt.click()
            print("exit screen yes")
            
            # new screen
            sleep(0.5)
            
            # exit attack
            pt.moveTo(1352,362)
            sleep(0.2)
            pt.click()
            print("exit screen attack")
            break
        
        # while 2 ####################################################################################################          no more energy
        
        # screenshot region no more energy
        screenshot_region_200_limit= pt.screenshot("imgs/screenshot_region_200_limit.png", region=(558,362,142,114))
        
        # search for no more energy
        Energy = pt.locateOnScreen("imgs/Energy.png", grayscale=False, region=(558,362,142,114), confidence=0.85)
        if Energy is not None:
            print("no more energy")
            
            # click on use 100 energy
            pt.moveTo(1270,643)
            sleep(0.2)
            pt.click(1270,643)
            print("clickt 2th energy")
            
            # new screen use
            sleep(1)
            
            # screenshot region no more gold
            screenshot_region_no_more_gold= pt.screenshot("imgs/screenshot_region_no_more_gold.png", region=(845,659,222,65))
            print("screenshot no more gold")
            
            # search for no more energy
            no_more_gold = pt.locateOnScreen("imgs/no_more_gold.png", grayscale=False, region=(845,659,222,65), confidence=0.85)
            print("search for no more gold")
            
            if no_more_gold is not None:
                print("i see no more gold")
                break
            
            # click on use
            pt.moveTo(954,699)
            sleep(0.5)
            pt.click(954,699)
            print("clickt use")
            
            # new screen ok
            sleep(0.2)
            
            # click on ok
            pt.moveTo(954,699)
            sleep(0.2)
            pt.click(954,699)
            print("clickt use")
            
            # new screen
            sleep(0.5)
            
            # screenshot region no more gold
            screenshot_region_no_more_gold= pt.screenshot("imgs/screenshot_region_no_more_gold.png", region=(845,659,222,65))
            print("screenshot no more gold")
            
            # search for no more energy
            no_more_gold = pt.locateOnScreen("imgs/no_more_gold.png", grayscale=False, region=(845,659,222,65), confidence=0.85)
            print("search for no more gold")
            
            if no_more_gold is not None:
                print("i see no more gold")
                break
            
            # exit screen energy
            pt.moveTo(1379,292)
            sleep(0.2)
            pt.click()
            print("exit screen energy")
            
        # while 2 ####################################################################################################          all troops out
            
        # screenshot all troops out
        screenshot_region_all_troops_out= pt.screenshot("imgs/screenshot_region_all_troops_out.png", region=(755,584,309,25))
        print("screenshot region all troops out")
        
        # search for all troops out
        AllTroopsOut = pt.locateOnScreen("imgs/AllTroopsOut.png", grayscale=False, region=(755,584,309,25), confidence=0.85)
        if AllTroopsOut is not None:
            print("i see all troops out")
            
            sleep(0.5)
            
            # exit screen all troops out
            pt.moveTo(1233,427)
            sleep(0.2)
            pt.click()
            print("exit all troops out")
            
            sleep(3)
            print("break of 3 seconds")
            
        # while 2 ####################################################################################################          limit 100

        # screenshot region limit 100
        screenshot_region_limit_100_2= pt.screenshot("imgs/screenshot_region_limit_100_2.png", region=(738,529,438,57))
        print("screenshot region limit 100")
        
        # search for limit 100
        limit_100 = pt.locateOnScreen("imgs/limit_100.png", grayscale=False, region=(738,529,438,57), confidence=0.85)
        if limit_100 is not None:
            print("i see limit 100")
            
            sleep(0.5)
            
            # click on yes
            pt.moveTo(957,699)
            sleep(0.3)
            pt.click(957,699)
            sleep(0.2)
            print("clickt yes")

        # new screen
        sleep(0.3)
        
        # while 2 ####################################################################################################          gray button time attack
        
        # check gray button time attack
        pix = pt.pixelMatchesColor(1061,893, (125, 125, 125))
        if pix is True:
            print("gray time attack button")
            
            sleep(0.5)
            
            # exit time attack
            pt.moveTo(1405,222)
            sleep(0.2)
            pt.click(1405,222)
            print("exit time attack rescue")
            break

        # click on time attack
        pt.moveTo(1113,903)
        sleep(0.1)
        pt.click(1113,903)
        sleep(0.3)
        print("clickt time attack")
        print("#####")
        print("")
       
    print("END STREETFORCES LEVEL 40")
    print("")

    ##################################################################################################################
    # haunter ########################################################################################################          haunter
    ##################################################################################################################          start while 2

    # start haunter
    print("START haunter")    
    sleep(0.5)

    # setup haunter
    print("start loop setting haunter")
    pt.FAILSAFE = True
    while 2:
        
        sleep(0.5)
        
        # click on search
        sleep(0.3)
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)
        print("clickt search")

        # new screen search
        sleep(1)
        
        # check search screen
        if pt.pixel(653,331)[0] != 141:
            print("check search----- NOT OK -----")
            
            sleep(0.5)
            
            # click on search
            sleep(0.3)
            pt.moveTo(1116,913)
            sleep(0.3)
            pt.click(1116,913)
            print("clickt search rescue")
            
            sleep(0.5)
            
        if pt.pixel(653,331)[0] == 141:
            print("check search OK")

        # select haunter
        haunter = pt.locateOnScreen("imgs/haunter.png", grayscale=False, confidence=0.8)
        if haunter is None:
            print("no haunter")
            
            # exit screen
            pt.moveTo(1372, 340)
            sleep(0.2)
            pt.click()
            print("exit search")
            
            print("end loop setting haunter")
            break
        
        if haunter is not None:
            print("i see haunter")
            
            #click on haunter
            pt.moveTo(haunter)
            sleep(0.2)
            pt.click()
            sleep(0.2)
            print("clickt haunter")
            
            # exit screen
            pt.moveTo(1375,342)
            sleep(0.2)
            pt.click()
            print("exit search")
            

            ##########################################################################################
            print("#####")
            ##########################################################################################
            
            # killing haunter
            print("start loop killing haunter")
            pt.FAILSAFE = True
            while 2:
                
                sleep(0.5)
                print("#####")
                
                # click on search
                sleep(0.3)
                pt.moveTo(1116,913)
                sleep(0.3)
                pt.click(1116,913)
                print("clickt search")
              
                # new screen search
                sleep(1.2)
                
                # check search screen
                if pt.pixel(653,331)[0] != 141:
                    print("check search----- NOT OK -----")
                    
                    sleep(0.5)
                    
                    # click on search
                    sleep(0.3)
                    pt.moveTo(1116,913)
                    sleep(0.3)
                    pt.click(1116,913)
                    print("clickt search rescue")
                    
                    sleep(0.5)
                    
                if pt.pixel(653,331)[0] == 141:
                    print("check search OK")
              
                # click on search button
                pt.moveTo(1214,792)
                sleep(0.2)
                pt.click(1214,792)
                sleep(0.5)
                print("clickt search button")
                
                # new screen
                sleep(0.8)
                
                # check gray button limit
                print("check gray button limit")
                if pt.pixel(914,782)[0] == 101:
                    print("end blaze")
                    
                    # exit screen attack
                    pt.moveTo(1352,363)
                    sleep(0.2)
                    pt.click()
                    print("exit attack limit")
                    break
              
                # check no more
                NoMore = pt.locateCenterOnScreen("imgs/NoMoreTroops.png", grayscale=False, confidence=0.75)
                if NoMore is not None:
                    print("no more left")
              
                    # exit screen
                    pt.moveTo(1376,342)
                    sleep(0.2)
                    pt.click()
                    print("end loop killing haunter")
                    break
            
                    # new screen
                    sleep(0.4)
              
                # click on attack
                pt.moveTo(959,788)
                sleep(0.4)
                pt.click(959,788)
                sleep(0.6)
                print("clickt attack")
                
                limit_merchants = pt.locateCenterOnScreen("imgs/limit_merchants.png", grayscale=False, confidence=0.85)
                if limit_merchants is not None:
                    print("limit merchants")
                    
                    # exit screen
                    pt.moveTo(1376,342)
                    sleep(0.2)
                    pt.click()
                    print("end loop killing haunter")
                    break
              
                # check no more energy
                Energy = pt.locateOnScreen("imgs/Energy.png", grayscale=False, confidence=0.70)
                if Energy is not None:
                    print("no more energy")
                    
                    # click on use 100 energy
                    pt.moveTo(1270,643)
                    sleep(0.2)
                    pt.click(1270,643)
                    print("clickt use 100 energy")
              
                    # new screen use
                    sleep(1)
                    
                    # screenshot region no more gold
                    screenshot_region_no_more_gold= pt.screenshot("imgs/screenshot_region_no_more_gold.png", region=(845,659,222,65))
                    print("screenshot no more gold")
                    
                    # search for no more energy
                    no_more_gold = pt.locateOnScreen("imgs/no_more_gold.png", grayscale=False, region=(845,659,222,65), confidence=0.85)
                    print("search for no more gold")
                    
                    if no_more_gold is not None:
                        print("i see no more gold")
                        break
              
                    # click on use
                    pt.moveTo(954,699)
                    sleep(0.2)
                    pt.click(954,699)
                    print("clickt use")
                    
                    # new screen ok
                    sleep(0.5)
                    
                    # click on ok
                    pt.moveTo(954,699)
                    sleep(0.2)
                    pt.click(954,699)
                    print("clickt ok")
                    
                    # exit screen energy
                    pt.moveTo(1379,292)
                    sleep(0.2)
                    pt.click()
                    print("exit screen energy")
              
                # check no more crew left
                AllTroopsOut = pt.locateOnScreen("imgs/AllTroopsOut.png", grayscale=False, confidence=0.70)
                if AllTroopsOut is not None:
                    print("all buzzy")
                    
                    sleep(3)
                    print("break 3 seconds")
                
                # check gray time attack button    
                pix = pt.pixelMatchesColor(1061,893, (125, 125, 125))
                if pix is True:
                    print("gray time attack button")
                    
                    # exit time attack
                    pt.moveTo(1405,222)
                    sleep(0.2)
                    pt.click(1405,222)
                    print("exit gray time attack button")
                    break
              
                # click on time attack
                pt.moveTo(1113,903)
                sleep(0.1)
                pt.click(1113,903)
                sleep(0.7)
                print("clickt time attack")

        break
    print("END haunter")
    print("")

################################################################################################################
# Reaper #######################################################################################################
################################################################################################################
    
    # start reaper
    print("START reaper")    
    sleep(0.5)

    # setup reaper
    print("start loop setting reaper")
    pt.FAILSAFE = True
    while 2:
        
        sleep(0.5)
        
        # click on search
        sleep(0.3)
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)
        print("clickt search")

        # new screen search
        sleep(1)
        
        # check search screen
        if pt.pixel(653,331)[0] != 141:
            print("check search----- NOT OK -----")
            
            sleep(0.5)
            
            # click on search
            sleep(0.3)
            pt.moveTo(1116,913)
            sleep(0.3)
            pt.click(1116,913)
            print("clickt search rescue")
            
            sleep(0.5)
            
        if pt.pixel(653,331)[0] == 141:
            print("check search OK")

        # select reaper
        reaper = pt.locateOnScreen("imgs/reaper.png", grayscale=False, confidence=0.8)
        if reaper is None:
            print("no reaper")
            
            # exit screen
            pt.moveTo(1372, 340)
            sleep(0.2)
            pt.click()
            print("exit search")
            
            print("end loop setting reaper")
            break
        
        if reaper is not None:
            print("i see reaper")
            
            #click on reaper
            pt.moveTo(reaper)
            sleep(0.2)
            pt.click()
            sleep(0.2)
            print("clickt reaper")
            
            # exit screen
            pt.moveTo(1375,342)
            sleep(0.2)
            pt.click()
            print("exit search")
            

            ##########################################################################################
            print("#####")
            ##########################################################################################
            
            # killing reaper
            print("start loop killing reaper")
            pt.FAILSAFE = True
            while 2:
                
                sleep(0.5)
                print("#####")
                
                # click on search
                sleep(0.3)
                pt.moveTo(1116,913)
                sleep(0.3)
                pt.click(1116,913)
                print("clickt search")
              
                # new screen search
                sleep(1.2)
                
                # check search screen
                if pt.pixel(653,331)[0] != 141:
                    print("check search----- NOT OK -----")
                    
                    sleep(0.5)
                    
                    # click on search
                    sleep(0.3)
                    pt.moveTo(1116,913)
                    sleep(0.3)
                    pt.click(1116,913)
                    print("clickt search rescue")
                    
                    sleep(0.5)
                    
                if pt.pixel(653,331)[0] == 141:
                    print("check search OK")
              
                # click on search button
                pt.moveTo(1214,792)
                sleep(0.2)
                pt.click(1214,792)
                sleep(0.5)
                print("clickt search button")
                
                # new screen
                sleep(0.8)
                
                # check gray button limit
                print("check gray button limit")
                if pt.pixel(914,782)[0] == 101:
                    print("end blaze")
                    
                    # exit screen attack
                    pt.moveTo(1352,363)
                    sleep(0.2)
                    pt.click()
                    print("exit attack limit")
                    break
              
                # check no more
                NoMore = pt.locateCenterOnScreen("imgs/NoMoreTroops.png", grayscale=False, confidence=0.75)
                if NoMore is not None:
                    print("no more left")
              
                    # exit screen
                    pt.moveTo(1376,342)
                    sleep(0.2)
                    pt.click()
                    print("end loop killing reaper")
                    break
            
                    # new screen
                    sleep(0.4)
              
                # click on attack
                pt.moveTo(959,788)
                sleep(0.4)
                pt.click(959,788)
                sleep(0.6)
                print("clickt attack")
                
                limit_merchants = pt.locateCenterOnScreen("imgs/limit_merchants.png", grayscale=False, confidence=0.85)
                if limit_merchants is not None:
                    print("limit merchants")
                    
                    # exit screen
                    pt.moveTo(1376,342)
                    sleep(0.2)
                    pt.click()
                    print("end loop killing reaper")
                    break
              
                # check no more energy
                Energy = pt.locateOnScreen("imgs/Energy.png", grayscale=False, confidence=0.70)
                if Energy is not None:
                    print("no more energy")
                    
                    # click on use 100 energy
                    pt.moveTo(1270,643)
                    sleep(0.2)
                    pt.click(1270,643)
                    print("clickt use 100 energy")
              
                    # new screen use
                    sleep(1)
                    
                    # screenshot region no more gold
                    screenshot_region_no_more_gold= pt.screenshot("imgs/screenshot_region_no_more_gold.png", region=(845,659,222,65))
                    print("screenshot no more gold")
                    
                    # search for no more energy
                    no_more_gold = pt.locateOnScreen("imgs/no_more_gold.png", grayscale=False, region=(845,659,222,65), confidence=0.85)
                    print("search for no more gold")
                    
                    if no_more_gold is not None:
                        print("i see no more gold")
                        break
              
                    # click on use
                    pt.moveTo(954,699)
                    sleep(0.2)
                    pt.click(954,699)
                    print("clickt use")
                    
                    # new screen ok
                    sleep(0.5)
                    
                    # click on ok
                    pt.moveTo(954,699)
                    sleep(0.2)
                    pt.click(954,699)
                    print("clickt ok")
                    
                    # exit screen energy
                    pt.moveTo(1379,292)
                    sleep(0.2)
                    pt.click()
                    print("exit screen energy")
              
                # check no more crew left
                AllTroopsOut = pt.locateOnScreen("imgs/AllTroopsOut.png", grayscale=False, confidence=0.70)
                if AllTroopsOut is not None:
                    print("all buzzy")
                    
                    sleep(3)
                    print("break 3 seconds")
                
                # check gray time attack button    
                pix = pt.pixelMatchesColor(1061,893, (125, 125, 125))
                if pix is True:
                    print("gray time attack button")
                    
                    # exit time attack
                    pt.moveTo(1405,222)
                    sleep(0.2)
                    pt.click(1405,222)
                    print("exit gray time attack button")
                    break
              
                # click on time attack
                pt.moveTo(1113,903)
                sleep(0.1)
                pt.click(1113,903)
                sleep(0.7)
                print("clickt time attack")

        break
    print("END reaper")
    print("")
    
#################################################################################################################
# Varian ########################################################################################################
#################################################################################################################
    
    # start varian
    print("START varian")    
    sleep(0.5)

    # setup varian
    print("start loop setting varian")
    pt.FAILSAFE = True
    while 2:
        
        sleep(0.5)
        
        # click on search
        sleep(0.3)
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)
        print("clickt search")

        # new screen search
        sleep(1)
        
        # check search screen
        if pt.pixel(653,331)[0] != 141:
            print("check search----- NOT OK -----")
            
            sleep(0.5)
            
            # click on search
            sleep(0.3)
            pt.moveTo(1116,913)
            sleep(0.3)
            pt.click(1116,913)
            print("clickt search rescue")
            
            sleep(0.5)
            
        if pt.pixel(653,331)[0] == 141:
            print("check search OK")

        # select varian
        varian = pt.locateOnScreen("imgs/varian.png", grayscale=False, confidence=0.8)
        if varian is None:
            print("no varian")
            
            # exit screen
            pt.moveTo(1372, 340)
            sleep(0.2)
            pt.click()
            print("exit search")
            
            print("end loop setting varian")
            break
        
        if varian is not None:
            print("i see varian")
            
            #click on varian
            pt.moveTo(varian)
            sleep(0.2)
            pt.click()
            sleep(0.2)
            print("clickt varian")
            
            # exit screen
            pt.moveTo(1375,342)
            sleep(0.2)
            pt.click()
            print("exit search")
            

            ##########################################################################################
            print("#####")
            ##########################################################################################
            
            # killing varian
            print("start loop killing varian")
            pt.FAILSAFE = True
            while 2:
                
                sleep(0.5)
                print("#####")
                
                # click on search
                sleep(0.3)
                pt.moveTo(1116,913)
                sleep(0.3)
                pt.click(1116,913)
                print("clickt search")
              
                # new screen search
                sleep(1.2)
                
                # check search screen
                if pt.pixel(653,331)[0] != 141:
                    print("check search----- NOT OK -----")
                    
                    sleep(0.5)
                    
                    # click on search
                    sleep(0.3)
                    pt.moveTo(1116,913)
                    sleep(0.3)
                    pt.click(1116,913)
                    print("clickt search rescue")
                    
                    sleep(0.5)
                    
                if pt.pixel(653,331)[0] == 141:
                    print("check search OK")
              
                # click on search button
                pt.moveTo(1214,792)
                sleep(0.2)
                pt.click(1214,792)
                sleep(0.5)
                print("clickt search button")
                
                # new screen
                sleep(0.8)
                
                # check gray button limit
                print("check gray button limit")
                if pt.pixel(914,782)[0] == 101:
                    print("end blaze")
                    
                    # exit screen attack
                    pt.moveTo(1352,363)
                    sleep(0.2)
                    pt.click()
                    print("exit attack limit")
                    break
              
                # check no more
                NoMore = pt.locateCenterOnScreen("imgs/NoMoreTroops.png", grayscale=False, confidence=0.75)
                if NoMore is not None:
                    print("no more left")
              
                    # exit screen
                    pt.moveTo(1376,342)
                    sleep(0.2)
                    pt.click()
                    print("end loop killing varian")
                    break
            
                    # new screen
                    sleep(0.4)
              
                # click on attack
                pt.moveTo(959,788)
                sleep(0.4)
                pt.click(959,788)
                sleep(0.6)
                print("clickt attack")
                
                limit_merchants = pt.locateCenterOnScreen("imgs/limit_merchants.png", grayscale=False, confidence=0.85)
                if limit_merchants is not None:
                    print("limit merchants")
                    
                    # exit screen
                    pt.moveTo(1376,342)
                    sleep(0.2)
                    pt.click()
                    print("end loop killing varian")
                    break
              
                # check no more energy
                Energy = pt.locateOnScreen("imgs/Energy.png", grayscale=False, confidence=0.70)
                if Energy is not None:
                    print("no more energy")
                    
                    # click on use 100 energy
                    pt.moveTo(1270,643)
                    sleep(0.2)
                    pt.click(1270,643)
                    print("clickt use 100 energy")
              
                    # new screen use
                    sleep(1)
                    
                    # screenshot region no more gold
                    screenshot_region_no_more_gold= pt.screenshot("imgs/screenshot_region_no_more_gold.png", region=(845,659,222,65))
                    print("screenshot no more gold")
                    
                    # search for no more energy
                    no_more_gold = pt.locateOnScreen("imgs/no_more_gold.png", grayscale=False, region=(845,659,222,65), confidence=0.85)
                    print("search for no more gold")
                    
                    if no_more_gold is not None:
                        print("i see no more gold")
                        break
              
                    # click on use
                    pt.moveTo(954,699)
                    sleep(0.2)
                    pt.click(954,699)
                    print("clickt use")
                    
                    # new screen ok
                    sleep(0.5)
                    
                    # click on ok
                    pt.moveTo(954,699)
                    sleep(0.2)
                    pt.click(954,699)
                    print("clickt ok")
                    
                    # exit screen energy
                    pt.moveTo(1379,292)
                    sleep(0.2)
                    pt.click()
                    print("exit screen energy")
              
                # check no more crew left
                AllTroopsOut = pt.locateOnScreen("imgs/AllTroopsOut.png", grayscale=False, confidence=0.70)
                if AllTroopsOut is not None:
                    print("all buzzy")
                    
                    sleep(3)
                    print("break 3 seconds")
                
                # check gray time attack button    
                pix = pt.pixelMatchesColor(1061,893, (125, 125, 125))
                if pix is True:
                    print("gray time attack button")
                    
                    # exit time attack
                    pt.moveTo(1405,222)
                    sleep(0.2)
                    pt.click(1405,222)
                    print("exit gray time attack button")
                    break
              
                # click on time attack
                pt.moveTo(1113,903)
                sleep(0.1)
                pt.click(1113,903)
                sleep(0.7)
                print("clickt time attack")

        break
    print("END varian")
    print("")
    
######################################################################################################################
# white shark ########################################################################################################
######################################################################################################################
    
    # start white_shark
    print("START white_shark")    
    sleep(0.5)

    # setup white_shark
    print("start loop setting white_shark")
    pt.FAILSAFE = True
    while 2:
        
        sleep(0.5)
        
        # click on search
        sleep(0.3)
        pt.moveTo(1116,913)
        sleep(0.3)
        pt.click(1116,913)
        print("clickt search")

        # new screen search
        sleep(1)
        
        # check search screen
        if pt.pixel(653,331)[0] != 141:
            print("check search----- NOT OK -----")
            
            sleep(0.5)
            
            # click on search
            sleep(0.3)
            pt.moveTo(1116,913)
            sleep(0.3)
            pt.click(1116,913)
            print("clickt search rescue")
            
            sleep(0.5)
            
        if pt.pixel(653,331)[0] == 141:
            print("check search OK")

        # select white_shark
        white_shark = pt.locateOnScreen("imgs/white_shark.png", grayscale=False, confidence=0.8)
        if white_shark is None:
            print("no white_shark")
            
            # exit screen
            pt.moveTo(1372, 340)
            sleep(0.2)
            pt.click()
            print("exit search")
            
            print("end loop setting white_shark")
            break
        
        if white_shark is not None:
            print("i see white_shark")
            
            #click on white_shark
            pt.moveTo(white_shark)
            sleep(0.2)
            pt.click()
            sleep(0.2)
            print("clickt white_shark")
            
            # exit screen
            pt.moveTo(1375,342)
            sleep(0.2)
            pt.click()
            print("exit search")
            

            ##########################################################################################
            print("#####")
            ##########################################################################################
            
            # killing white_shark
            print("start loop killing white_shark")
            pt.FAILSAFE = True
            while 2:
                
                sleep(0.5)
                print("#####")
                
                # click on search
                sleep(0.3)
                pt.moveTo(1116,913)
                sleep(0.3)
                pt.click(1116,913)
                print("clickt search")
              
                # new screen search
                sleep(1.2)
                
                # check search screen
                if pt.pixel(653,331)[0] != 141:
                    print("check search----- NOT OK -----")
                    
                    sleep(0.5)
                    
                    # click on search
                    sleep(0.3)
                    pt.moveTo(1116,913)
                    sleep(0.3)
                    pt.click(1116,913)
                    print("clickt search rescue")
                    
                    sleep(0.5)
                    
                if pt.pixel(653,331)[0] == 141:
                    print("check search OK")
              
                # click on search button
                pt.moveTo(1214,792)
                sleep(0.2)
                pt.click(1214,792)
                sleep(0.5)
                print("clickt search button")
                
                # new screen
                sleep(0.8)
                
                # check gray button limit
                print("check gray button limit")
                if pt.pixel(914,782)[0] == 101:
                    print("end blaze")
                    
                    # exit screen attack
                    pt.moveTo(1352,363)
                    sleep(0.2)
                    pt.click()
                    print("exit attack limit")
                    break
              
                # check no more
                NoMore = pt.locateCenterOnScreen("imgs/NoMoreTroops.png", grayscale=False, confidence=0.75)
                if NoMore is not None:
                    print("no more left")
              
                    # exit screen
                    pt.moveTo(1376,342)
                    sleep(0.2)
                    pt.click()
                    print("end loop killing white_shark")
                    break
            
                    # new screen
                    sleep(0.4)
              
                # click on attack
                pt.moveTo(959,788)
                sleep(0.4)
                pt.click(959,788)
                sleep(0.6)
                print("clickt attack")
                
                limit_merchants = pt.locateCenterOnScreen("imgs/limit_merchants.png", grayscale=False, confidence=0.85)
                if limit_merchants is not None:
                    print("limit merchants")
                    
                    # exit screen
                    pt.moveTo(1376,342)
                    sleep(0.2)
                    pt.click()
                    print("end loop killing white_shark")
                    break
              
                # check no more energy
                Energy = pt.locateOnScreen("imgs/Energy.png", grayscale=False, confidence=0.70)
                if Energy is not None:
                    print("no more energy")
                    
                    # click on use 100 energy
                    pt.moveTo(1270,643)
                    sleep(0.2)
                    pt.click(1270,643)
                    print("clickt use 100 energy")
              
                    # new screen use
                    sleep(1)
                    
                    # screenshot region no more gold
                    screenshot_region_no_more_gold= pt.screenshot("imgs/screenshot_region_no_more_gold.png", region=(845,659,222,65))
                    print("screenshot no more gold")
                    
                    # search for no more energy
                    no_more_gold = pt.locateOnScreen("imgs/no_more_gold.png", grayscale=False, region=(845,659,222,65), confidence=0.85)
                    print("search for no more gold")
                    
                    if no_more_gold is not None:
                        print("i see no more gold")
                        break
              
                    # click on use
                    pt.moveTo(954,699)
                    sleep(0.2)
                    pt.click(954,699)
                    print("clickt use")
                    
                    # new screen ok
                    sleep(0.5)
                    
                    # click on ok
                    pt.moveTo(954,699)
                    sleep(0.2)
                    pt.click(954,699)
                    print("clickt ok")
                    
                    # exit screen energy
                    pt.moveTo(1379,292)
                    sleep(0.2)
                    pt.click()
                    print("exit screen energy")
              
                # check no more crew left
                AllTroopsOut = pt.locateOnScreen("imgs/AllTroopsOut.png", grayscale=False, confidence=0.70)
                if AllTroopsOut is not None:
                    print("all buzzy")
                    
                    sleep(3)
                    print("break 3 seconds")
                
                # check gray time attack button    
                pix = pt.pixelMatchesColor(1061,893, (125, 125, 125))
                if pix is True:
                    print("gray time attack button")
                    
                    # exit time attack
                    pt.moveTo(1405,222)
                    sleep(0.2)
                    pt.click(1405,222)
                    print("exit gray time attack button")
                    break
              
                # click on time attack
                pt.moveTo(1113,903)
                sleep(0.1)
                pt.click(1113,903)
                sleep(0.7)
                print("clickt time attack")

        break
    print("END white_shark")
    print("")

########################################################################################################
# random port
########################################################################################################

    # use random port
    print("START RANDOM PORT")
    pt.FAILSAFE = True
    while 2:
        print("start selecting random port")
    
        # new screen
        sleep(70)
        
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
        print("END RANDOM PORT")
        break