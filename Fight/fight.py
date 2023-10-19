import pgzrun
import os
from pgzhelper import *
#_____________Display______________
os.environ["SDL_VIDEO_CENTERED"] = "1"
WIDTH = 1000
HEIGHT = 562
TITLE = "AmirReza Fight Game"
x = 10
#_____________Sound________________
sounds.menu.play()
#_____________Actor________________
menu = Actor("main_menu" , (500 , 281))
soundButton = Actor("mini_button" , (827 , 50))
soundMute = Actor("mini_button" , (877 , 50))
shop = Actor("main_shop" , (500 , 281))
notice = Actor("notice" , (500 , 281))
exitQuestion = Actor("exit_question" , (500 , 281))
controlls = Actor("controlls" , (500 , 281))
selectPlace = Actor("main_select" , (500 , 281))
pause = Actor("pause" , (500 , 281))
loading = Actor("loading" , (500 , 281))
loadingBar = Actor("loading_bar" , (500 , 470))
loadingBarAnimate = Actor("loading_bar_animate" , (-550 , 470))
result = Actor("loading" , (500 , -281))
gameCoin = Actor("coin" , (107 , 42))
buttonResultAgain = Actor("button" , (880 , 505))
buttonResultBack = Actor("button" , (120 , 505))
buttonNotice = Actor("mini_button" , (500 , 330))
buttonStart = Actor("button" , (165 , 500))
buttonSelectBack = Actor("mini_button" , (100 , 53))
buttonPlay = Actor("mini_button" , (910 , 53))
buttonShop = Actor("button" , (385 , 500))
buttonShopBack = Actor("mini_button" , (910 , 53))
buttonControlls = Actor("button" , (605 , 500))
buttonControllsBack =Actor("mini_button" , (900 , 505))
buttonPauseResume = Actor("button" , (500 , 265))
buttonPauseBack = Actor("button" , (500 , 335))
buttonExit = Actor("button" , (825 , 500))
buttonExitNo = Actor("mini_button" , (560 , 330))
buttonExitYes = Actor("mini_button" , (440 , 330))
buttonShopIcon1 = Actor("button" , (325 , 515))
buttonShopIcon2 = Actor("button" , (675 , 290))
buttonShopIcon3 = Actor("button" , (325 , 290))
buttonShopIcon4 = Actor("button" , (675 , 515))
unlockIcon1 = Actor("unlock" , (362 , 512))
unlockIcon2 = Actor("unlock" , (720 , 288))
unlockIcon3 = Actor("unlock" , (365 , 288))
unlockIcon4 = Actor("unlock" , (720 , 512))
lockIcon2 = Actor("lock" , (710 , 288))
lockIcon3 = Actor("lock" , (362 , 288))
lockIcon4 = Actor("lock" , (710 , 512))
map = Actor("winter_jungle" , (500 , 281))
timeBackGround = Actor("time_background" , (485 , 65))
shopIcon1 = Actor("winter_jungle_icon" , (325 , 400))
shopIcon2 = Actor("winter_mountain_icon" , (675 , 180))
shopIcon3 = Actor("winter_city_icon" , (325 , 180))
shopIcon4 = Actor("winter_house_icon" , (675 , 400))
healthLeft = Actor("health_left" , (89 , 50))
healthRight = Actor("health_right" , (912 , 50))
healthBarLeft = Actor("health_bar_left" , (89 , 50))
healthBarRight = Actor("health_bar_right" , (912 , 50))
victorRun = Actor("victor_stand" , (150 , 498))
victorBack = Actor("victor_stand")
victorAttack = Actor("victor_stand")
victorAttack2 = Actor("victor_stand")
victorHurt = Actor("victor_stand")
victorDead = Actor("victor_stand")
guardianRun = Actor("guardian_stand" , (840 , 440))
guardianBack = Actor("guardian_stand")
guardianAttack = Actor("guardian_stand")
guardianShot = Actor("guardian_stand")
guardianHurt = Actor("guardian_stand")
guardianDead = Actor("guardian_stand")
shot = Actor("shot")
characterMarkVictor = Actor("triangle")
characterMarkGuardian = Actor("triangle")
player1Mark = Actor("player1_mark")
player2Mark = Actor("player2_mark")
#____________Animation_____________
victorRun.images = ["victor_run1" , "victor_run2" , "victor_run3" , "victor_run4" , "victor_run5" , "victor_run6" , "victor_run7" , "victor_run8"]
victorBack.images = ["victor_walk7" , "victor_walk6" , "victor_walk5" , "victor_walk4" , "victor_walk3" , "victor_walk2" , "victor_walk1"]
victorAttack.images = ["victor_attack1" , "victor_attack2" , "victor_attack3" , "victor_attack4" , "victor_attack5"]
victorAttack2.images = ["victor2attack1" , "victor2attack2" , "victor2attack3" , "victor2attack4" , "victor2attack5"]
victorHurt.images = ["victor_hurt"]
victorDead.images = ["victor_dead1" , "victor_dead2" , "victor_dead3" , "victor_dead4"]
guardianRun.images = ["guardian_run1" , "guardian_run2" , "guardian_run3" , "guardian_run4" , "guardian_run5" , "guardian_run6" ,"guardian_run7" , "guardian_run8"]
guardianBack.images = ["guardian_walk7" , "guardian_walk6" , "guardian_walk5" , "guardian_walk4" , "guardian_walk3" , "guardian_walk2" , "guardian_walk1"]
guardianAttack.images = ["guardian_attack1" , "guardian_attack2" , "guardian_attack3" , "guardian_attack4"]
guardianShot.images = ["guardian_shot1" , "guardian_shot2" , "guardian_shot3" , "guardian_shot4"]
guardianHurt.images = ["guardian_hurt1" , "guardian_hurt2" , "guardian_hurt3" , "guardian_hurt4" , "guardian_hurt5" , "guardian_hurt6" , "guardian_hurt7" , "guardian_hurt8" , "guardian_hurt9"]
guardianDead.images = ["guardian_dead1" , "guardian_dead2" , "guardian_dead3" , "guardian_dead4" , "guardian_dead5"]
victorRun.fps = 10
victorBack.fps = 10
victorAttack.fps = 10
victorAttack2.fps = 10
victorHurt.fps = 10
victorDead.fps = 10
guardianRun.fps = 10
guardianBack.fps = 10
guardianAttack.fps = 10
guardianShot.fps = 10
guardianHurt.fps = 10
guardianDead.fps = 10
#________________ Marker _______________________
victorRunFlag = True
victorJumpFlag = False
victorPunchFlag = False
victorPunchFlag2 = False
victorHurtFlag = False
victorDeadFlag = True
guardianRunFlag = True
guardianJumpFlag = False
guardianPunchFlag = False
guardianShotFlag = False
guardianHurtFlag = False
guardianDeadFlag = True
shotFlag = False
sound = True
dictMenu = {
    "gameMenu" : True,
    "start" : False,
    "shop" : False,
    "exit" : False,
    "controlls" : False,
    "gameNotice" : False,
    "main_select" : False,
    "loading" : False,
    "pause" : False
}
dictShop = {
    "winterJungle" : True,
    "winterMountain" : False,
    "winterCity" : False,
    "winterHouse" : False
}
dictSelect = {
    "winterJungleSelect" : True,
    "winterMountainSelect" : False,
    "winterCitySelect" : False,
    "winterHouseSelect" : False
}
time = 60
coin = 1000
def update():
    global victorRunFlag , victorJumpFlag , victorPunchFlag , victorPunchFlag2 , victorHurtFlag , victorDeadFlag , guardianRunFlag , guardianJumpFlag , guardianPunchFlag , guardianShotFlag , guardianHurtFlag , guardianDeadFlag , shotFlag
    if dictMenu["loading"] == True:
        loadingBarAnimate.x += 10
        if loadingBarAnimate.x >= 500:
            loadingBarAnimate.x = -550
            dictMenu["loading"] = False
            dictMenu["start"] = True
#________________Victor Movements_______________
    if keyboard.d and victorRun.x < guardianRun.x and victorRun.x < 950 and victorDeadFlag == True and dictMenu["pause"] == False:
        victorRun.animate()
        victorRun.x += 2
        victorRunFlag = True
    else:
        victorRun.image = "victor_stand"
        victorRunFlag = True
    if keyboard.a and victorRun.x > 20 and victorDeadFlag == True and dictMenu["pause"] == False:
         victorRunFlag = False
         victorBack.animate()
         victorRun.x -= 1
         victorBack.x = victorRun.x
         victorBack.y = victorRun.y
    if keyboard.x and victorRun.image == "victor_stand" and dictMenu["pause"] == False:
        victorRun.image = "victor_defend"
    if victorJumpFlag == True and victorDeadFlag == True:
        if victorRun.y != 390:
            victorRun.image = "victor_jump1"
            victorBack.image = "victor_jump2"
            victorRun.y -= 5
        if victorRun.y <= 390:
            victorJumpFlag = False
    if victorJumpFlag == False:
        if victorRun.y != 498:
            victorRun.y += 5
    if victorPunchFlag == True and victorDeadFlag == True:
        victorAttack.animate()
        victorAttack.x = victorRun.x
        victorAttack.y = victorRun.y
        if victorAttack.image == "victor_attack5":
            victorPunchFlag = False
        if victorAttack.colliderect(guardianRun) and not guardianRun.image == "guardian_defend":
            sounds.guardian_hurt.play()
            healthBarRight.x += 0.3
            guardianHurtFlag = True
            guardianRun.image = "guardian_hurt1"
            guardianHurt.x = guardianRun.x
            guardianHurt.y = guardianRun.y
        else:
            guardianHurtFlag = False
    if victorPunchFlag2 == True and victorDeadFlag == True:
        victorAttack2.animate()
        victorAttack2.x = victorRun.x
        victorAttack2.y = victorRun.y
        if victorAttack2.image == "victor2attack5":
            victorPunchFlag2 = False
        if victorAttack2.colliderect(guardianRun) and not guardianRun.image == "guardian_defend":
            sounds.guardian_hurt.play()
            healthBarRight.x += 0.3
            guardianHurtFlag = True
            guardianRun.image = "guardian_hurt1"
            guardianHurt.x = guardianRun.x
            guardianHurt.y = guardianRun.y
        else:
            guardianHurtFlag = False
    if healthBarLeft.x <= -85 and victorDeadFlag == True:
            victorDead.x = victorRun.x
            victorDead.y = victorRun.y
            victorDead.animate()
            if victorDead.image == "victor_dead4":
                victorDeadFlag = False
#_____________Guardian movements____________
    if keyboard.left and guardianRun.x > victorRun.x and guardianRun.x > 20 and guardianDeadFlag == True and dictMenu["pause"] == False:
        guardianRun.animate()
        guardianRun.x -= 2
        guardianRunFlag = True
    else:
        guardianRun.image = "guardian_stand"
        guardianRunFlag = True
    if keyboard.right and guardianRun.x < 980 and guardianDeadFlag == True and dictMenu["pause"] == False:
        guardianRunFlag = False
        guardianBack.animate()
        guardianRun.x += 1
        guardianBack.x = guardianRun.x
        guardianBack.y = guardianRun.y
    if keyboard.i and guardianRun.image == "guardian_stand" and dictMenu["pause"] == False:
        guardianRun.image = "guardian_defend"
    if guardianJumpFlag == True and guardianDeadFlag == True:
        if guardianRun.y != 350:
            guardianRun.image = "guardian_jump1"
            guardianBack.image = "guardian_jump2"
            guardianRun.y -= 5
        if guardianRun.y == 350:
            guardianJumpFlag = False
    if guardianJumpFlag == False:
        if guardianRun.y != 440:
            guardianRun.y += 5
    if guardianShotFlag == True and guardianDeadFlag == True:
        guardianShot.animate()
        guardianShot.x = guardianRun.x
        guardianShot.y = guardianRun.y
        if guardianShot.image == "guardian_shot4":
            guardianShotFlag = False
    if guardianPunchFlag == True and guardianDeadFlag == True:
        guardianAttack.animate()
        guardianAttack.x = guardianRun.x
        guardianAttack.y = guardianRun.y
        if guardianAttack.image == "guardian_attack4":
            guardianPunchFlag = False
        if guardianAttack.colliderect(victorRun) and not victorRun.image == "victor_defend":
            sounds.victor_hurt.play()
            healthBarLeft.x -= 0.3
            victorHurtFlag = True
            victorRun.image = "victor_hurt"
            if victorHurt.image == "victor_hurt":
                victorHurtFlag = False
    if healthBarRight.x >= 1090 and guardianDeadFlag == True:
            guardianDead.x = guardianRun.x
            guardianDead.y = guardianRun.y
            guardianDead.animate()
            if guardianDead.image == "guardian_dead5":
                guardianDeadFlag = False
    if shotFlag:
        shot.x -= 5
        if shot.colliderect(victorRun) and not victorRun.image == "victor_defend":
            sounds.victor_hurt.play()
            healthBarLeft.x -= 20
            shotFlag = False
            victorHurtFlag = True
            victorRun.image = "victor_hurt"
            if victorHurt.image == "victor_hurt":
                victorHurtFlag = False
        if shot.x <= -10:
            shotFlag = False
    else:
        shot.x = -10
        shot.y = guardianRun.y + 25
def draw():
    global victorRunFlag , victorPunchFlag , victorPunchFlag2 , victorHurtFlag , victorDeadFlag , guardianRunFlag , guardianPunchFlag , guardianShotFlag , guardianHurtFlag , guardianDeadFlag , gameMenu , start , coin
    screen.clear()
    if dictMenu["loading"] == True:
        sounds.menu.stop()
    if dictMenu["gameMenu"] == True:
        menu.draw()
        soundMute.draw()
        soundButton.draw()
        screen.draw.text("Sound" , color = (255, 255, 255) , topleft = (800 , 35) , fontsize = 35 , fontname = "tjoekilkajoe")
        if sound == True:
            screen.draw.text("On" , color = (255, 255, 255) , topleft = (890 , 35) , fontsize = 35 , fontname = "tjoekilkajoe")
        else:
            screen.draw.text("Off" , color = (255, 255, 255) , topleft = (890 , 35) , fontsize = 35 , fontname = "tjoekilkajoe")
        buttonStart.draw()
        buttonShop.draw()
        buttonControlls.draw()
        buttonExit.draw()
        screen.draw.text("Fight" , color = (221, 42, 11) , topleft = (370 , 100) , fontsize = 200 , fontname = "tjoekilkajoe")
        screen.draw.text("Start" , color = (255, 255, 255) , topleft = (144 , 486) , fontsize = 35 , fontname = "tjoekilkajoe")
        screen.draw.text("Shop" , color = (255, 255, 255) , topleft = (370 , 486) , fontsize = 32 , fontname = "tjoekilkajoe")
        screen.draw.text("Controlls" , color = (255, 255, 255) , topleft = (573 , 486) , fontsize = 32 , fontname = "tjoekilkajoe")
        screen.draw.text("Exit" , color = (255, 255, 255) , topleft = (808 , 486) , fontsize = 35 , fontname = "tjoekilkajoe")
        if dictMenu["exit"] == True:
            exitQuestion.draw()
            screen.draw.text("Notice" , color = (255, 255, 255) , topleft = (365 , 210) , fontsize = 35 , fontname = "tjoekilkajoe")
            screen.draw.text("Are you sure you want to exit?" , color = (255, 255, 255) , topleft = (365 , 260) , fontsize = 25 , fontname = "tjoekilkajoe")
            buttonExitNo.draw()
            screen.draw.text("No" , color = (255, 255, 255) , topleft = (550 , 320) , fontsize = 25 , fontname = "tjoekilkajoe")
            buttonExitYes.draw()
            screen.draw.text("Yes" , color = (255, 255, 255) , topleft = (427 , 320) , fontsize = 25 , fontname = "tjoekilkajoe")
    elif dictMenu["shop"] == True:
        shop.draw()
        gameCoin.draw()
        screen.draw.text(f"{coin}" , color = (255, 255, 255) , topleft = (40 , 30) , fontsize = 35 , fontname = "tjoekilkajoe")
        buttonShopBack.draw()
        screen.draw.text("Back" , color = (255, 255, 255) , topleft = (891 , 39) , fontsize = 30 , fontname = "tjoekilkajoe")
        shopIcon1.draw()
        buttonShopIcon1.draw()
        screen.draw.text("Unlock" , color = (255, 255, 255) , topleft = (283 , 500) , fontsize = 35 , fontname = "tjoekilkajoe")
        unlockIcon1.draw()
        shopIcon2.draw()
        buttonShopIcon2.draw()
        if dictShop["winterMountain"] == False:
            lockIcon2.draw()
            screen.draw.text("300 $" , color = (255, 255, 255) , topleft = (640 , 278) , fontsize = 35 , fontname = "tjoekilkajoe")
        else:
            unlockIcon2.draw()
            screen.draw.text("Unlock" , color = (255, 255, 255) , topleft = (640 , 278) , fontsize = 35 , fontname = "tjoekilkajoe")
        shopIcon3.draw()
        buttonShopIcon3.draw()
        if dictShop["winterCity"] == False:
            lockIcon3.draw()
            screen.draw.text("500 $" , color = (255, 255, 255) , topleft = (285 , 276) , fontsize = 35 , fontname = "tjoekilkajoe")
        else:
            unlockIcon3.draw()
            screen.draw.text("Unlock" , color = (255, 255, 255) , topleft = (285 , 276) , fontsize = 35 , fontname = "tjoekilkajoe")
        shopIcon4.draw()
        buttonShopIcon4.draw()
        if dictShop["winterHouse"] == False:
            lockIcon4.draw()
            screen.draw.text("700 $" , color = (255, 255, 255) , topleft = (640 , 503) , fontsize = 35 , fontname = "tjoekilkajoe")
        else:
            unlockIcon4.draw()
            screen.draw.text("Unlock" , color = (255, 255, 255) , topleft = (640 , 500) , fontsize = 35 , fontname = "tjoekilkajoe")
        if dictMenu["gameNotice"] == True:
            notice.draw()
            screen.draw.text("Notice" , color = (255, 255, 255) , topleft = (365 , 210) , fontsize = 35 , fontname = "tjoekilkajoe")
            screen.draw.text("You don't have enough coin." , color = (255, 255, 255) , topleft = (365 , 260) , fontsize = 25 , fontname = "tjoekilkajoe")
            buttonNotice.draw()
            screen.draw.text("Ok" , color = (255, 255, 255) , topleft = (490 , 320) , fontsize = 25 , fontname = "tjoekilkajoe")
    elif dictMenu["controlls"] == True:
        controlls.draw()
        screen.draw.text("Victor" , color = (255, 255, 255) , topleft = (165 , 50) , fontsize = 70 , fontname = "tjoekilkajoe")
        screen.draw.text("Guardian" , color = (255, 255, 255) , topleft = (635 , 50) , fontsize = 70 , fontname = "tjoekilkajoe")
        screen.draw.text("Attack 1" , color = (255, 255, 255) , topleft = (860 , 395) , fontsize = 30 , fontname = "tjoekilkajoe")
        screen.draw.text("Attack 2" , color = (255, 255, 255) , topleft = (675 , 300) , fontsize = 30 , fontname = "tjoekilkajoe")
        screen.draw.text("Defend" , color = (255, 255, 255) , topleft = (610 , 500) , fontsize = 30 , fontname = "tjoekilkajoe")
        screen.draw.text("Attack 1" , color = (255, 255, 255) , topleft = (366 , 395) , fontsize = 30 , fontname = "tjoekilkajoe")
        screen.draw.text("Attack 2" , color = (255, 255, 255) , topleft = (182 , 300) , fontsize = 30 , fontname = "tjoekilkajoe")
        screen.draw.text("Defend" , color = (255, 255, 255) , topleft = (115 , 500) , fontsize = 30 , fontname = "tjoekilkajoe")
        buttonControllsBack.draw()
        screen.draw.text("Back" , color = (255, 255, 255) , topleft = (882 , 492) , fontsize = 30 , fontname = "tjoekilkajoe")
    elif dictMenu["main_select"] == True:
        selectPlace.draw()
        buttonSelectBack.draw()
        screen.draw.text("Back" , color = (255, 255, 255) , topleft = (82 , 39) , fontsize = 30 , fontname = "tjoekilkajoe")
        buttonPlay.draw()
        screen.draw.text("Play" , color = (255, 255, 255) , topleft = (893 , 36) , fontsize = 30 , fontname = "tjoekilkajoe")
        shopIcon1.draw()
        buttonShopIcon1.draw()
        if dictSelect["winterJungleSelect"] == True:
            screen.draw.text("Selected" , color = (255, 255, 255) , topleft = (283 , 500) , fontsize = 35 , fontname = "tjoekilkajoe")
        else:
            screen.draw.text("Select" , color = (255, 255, 255) , topleft = (295 , 500) , fontsize = 35 , fontname = "tjoekilkajoe")
        shopIcon2.draw()
        buttonShopIcon2.draw()
        if dictShop["winterMountain"] == False:
            lockIcon2.draw()
            screen.draw.text("Lock" , color = (255, 255, 255) , topleft = (646 , 278) , fontsize = 35 , fontname = "tjoekilkajoe")
        else:
            if dictSelect["winterMountainSelect"] == True:
                screen.draw.text("Selected" , color = (255, 255, 255) , topleft = (640 , 278) , fontsize = 35 , fontname = "tjoekilkajoe")
            else:
                screen.draw.text("Select" , color = (255, 255, 255) , topleft = (648 , 278) , fontsize = 35 , fontname = "tjoekilkajoe")
        shopIcon3.draw()
        buttonShopIcon3.draw()
        if dictShop["winterCity"] == False:
            lockIcon3.draw()
            screen.draw.text("Lock" , color = (255, 255, 255) , topleft = (298 , 276) , fontsize = 35 , fontname = "tjoekilkajoe")
        else:
            if dictSelect["winterCitySelect"] == True:
                screen.draw.text("Selected" , color = (255, 255, 255) , topleft = (285 , 276) , fontsize = 35 , fontname = "tjoekilkajoe")
            else:
              screen.draw.text("Select" , color = (255, 255, 255) , topleft = (295 , 276) , fontsize = 35 , fontname = "tjoekilkajoe")
        shopIcon4.draw()
        buttonShopIcon4.draw()
        if dictShop["winterHouse"] == False:
            lockIcon4.draw()
            screen.draw.text("Lock" , color = (255, 255, 255) , topleft = (646 , 503) , fontsize = 35 , fontname = "tjoekilkajoe")
        else:
            if dictSelect["winterHouseSelect"] == True:
                screen.draw.text("Selected" , color = (255, 255, 255) , topleft = (640 , 500) , fontsize = 35 , fontname = "tjoekilkajoe")
            else:
                screen.draw.text("Select" , color = (255, 255, 255) , topleft = (652 , 500) , fontsize = 35 , fontname = "tjoekilkajoe")
    elif dictMenu["loading"] == True:
        loading.draw()
        loadingBar.draw()
        loadingBarAnimate.draw()
        screen.draw.text("Loading..." , color = (255, 255, 255) , topleft = (345 , 210) , fontsize = 150 , fontname = "tjoekilkajoe")
    elif dictMenu["start"] == True:
        if dictSelect["winterMountainSelect"] == True:
            map.image = "winter_mountain"
        elif dictSelect["winterCitySelect"] == True:
            map.image = "winter_city"
        elif dictSelect["winterHouseSelect"] == True:
            map.image = "winter_house"
        elif dictSelect["winterJungleSelect"] == True:
            map.image = "winter_jungle"
        map.draw()
        healthBarLeft.draw()
        healthBarRight.draw()
        healthLeft.draw()
        healthRight.draw()
        timeBackGround.draw()
        characterMarkVictor.x = victorRun.x - 3
        characterMarkVictor.y = victorRun.y - 83
        characterMarkGuardian.x = guardianRun.x + 9
        characterMarkGuardian.y = guardianRun.y - 24
        characterMarkVictor.draw()
        characterMarkGuardian.draw()
        player1Mark.x = victorRun.x - 3
        player1Mark.y = victorRun.y - 115
        player2Mark.x = guardianRun.x + 9
        player2Mark.y = guardianRun.y - 56
        player1Mark.draw()
        player2Mark.draw()
        shot.draw()
        if healthBarLeft.x >= -85:
            if victorRunFlag:
                if victorHurtFlag == False:
                    if victorPunchFlag2 == False:
                        if victorPunchFlag == False:
                            victorRun.draw()
                        else:
                            victorAttack.draw()
                    else:
                        victorAttack2.draw()
                else:
                    victorHurt.draw()
            else:
                victorBack.draw()
        else:
            victorDead.x = victorRun.x
            victorDead.y = victorRun.y
            victorDead.draw()
        if healthBarRight.x <= 1087:
            if guardianRunFlag:
                if guardianHurtFlag == False:
                    if guardianPunchFlag == False:
                        if guardianShotFlag == False:
                            guardianRun.draw()
                        else:
                            guardianShot.draw()
                    else:
                        guardianAttack.draw()
                else:
                    guardianHurt.draw()
            else:
                guardianBack.draw()
        else:
            guardianDead.x = guardianRun.x
            guardianDead.y = guardianRun.y
            guardianDead.draw()
        screen.draw.text("Victor" , color = "black" , topleft = (10 , 80) , fontsize = 30 , fontname = "tjoekilkajoe")
        screen.draw.text("Guardian" , color = "black" , topleft = (920 , 80) , fontsize = 30 , fontname = "tjoekilkajoe")
        if time > 10:
            screen.draw.text(f"{time}" , color = (219 , 219 , 219) , topleft = (470 , 35) , fontsize = 80 , fontname = "tjoekilkajoe")
        else:
            screen.draw.text(f"{time}" , color = "red" , topleft = (470 , 35) , fontsize = 80 , fontname = "tjoekilkajoe")
        if healthBarLeft.x <= -85:
            result.draw()
            result.y += 5
            screen.draw.text("Guardian Win" , color = (221, 42, 11) , topleft = (280 , 230) , fontsize = 140 , fontname = "tjoekilkajoe")
            if result.y >= 281:
                result.y = 281
                buttonResultAgain.draw()
                buttonResultBack.draw()
                screen.draw.text("Play again" , color = (255, 255, 255) , topleft = (840 , 490) , fontsize = 30 , fontname = "tjoekilkajoe")
                screen.draw.text("Back to menu" , color = (255, 255, 255) , topleft = (70 , 490) , fontsize = 30 , fontname = "tjoekilkajoe")
                screen.draw.text("You get 50 coins" , color = (255, 255, 255) , topleft = (420 , 375) , fontsize = 40 , fontname = "tjoekilkajoe")
        elif healthBarRight.x >= 1087:
            result.draw()
            result.y += 5
            screen.draw.text("victor Win" , color = (221, 42, 11) , topleft = (325 , 230) , fontsize = 140 , fontname = "tjoekilkajoe")
            if result.y >= 281:
                result.y = 281
                buttonResultAgain.draw()
                buttonResultBack.draw()
                screen.draw.text("Play again" , color = (255, 255, 255) , topleft = (840 , 490) , fontsize = 30 , fontname = "tjoekilkajoe")
                screen.draw.text("Back to menu" , color = (255, 255, 255) , topleft = (70 , 490) , fontsize = 30 , fontname = "tjoekilkajoe")
                screen.draw.text("You get 50 coins" , color = (255, 255, 255) , topleft = (420 , 375) , fontsize = 40 , fontname = "tjoekilkajoe")
        elif time == 0:
            result.draw()
            result.y += 5
            screen.draw.text("Draw" , color = (221, 42, 11) , topleft = (400 , 230) , fontsize = 140 , fontname = "tjoekilkajoe")
            if result.y >= 281:
                result.y = 281
                buttonResultAgain.draw()
                buttonResultBack.draw()
                screen.draw.text("Play again" , color = (255, 255, 255) , topleft = (840 , 490) , fontsize = 30 , fontname = "tjoekilkajoe")
                screen.draw.text("Back to menu" , color = (255, 255, 255) , topleft = (70 , 490) , fontsize = 30 , fontname = "tjoekilkajoe")
                screen.draw.text("You get 50 coins" , color = (255, 255, 255) , topleft = (420 , 375) , fontsize = 40 , fontname = "tjoekilkajoe")
    if dictMenu["pause"] == True:
        pause.draw()
        screen.draw.text("Pause" , color = (255, 255, 255) , topleft = (395 , 190) , fontsize = 30 , fontname = "tjoekilkajoe")
        buttonPauseResume.draw()
        screen.draw.text("Resume" , color = (255, 255, 255) , topleft = (470 , 250) , fontsize = 35 , fontname = "tjoekilkajoe")
        buttonPauseBack.draw()
        screen.draw.text("Back to menu" , color = (255, 255, 255) , topleft = (447 , 320) , fontsize = 35 , fontname = "tjoekilkajoe")
def on_key_down(key):
    global victorJumpFlag , victorPunchFlag , victorPunchFlag2 , guardianJumpFlag , guardianPunchFlag , guardianShotFlag , shotFlag
    if key == keys.W and victorRun.y == 498 and dictMenu["pause"] == False:
        victorJumpFlag = True
    elif key == keys.V and victorRunFlag == True and dictMenu["pause"] == False:
        victorPunchFlag = True
        sounds.victor_punch.play()
    elif key == keys.C and victorRunFlag == True and dictMenu["pause"] == False:
        victorPunchFlag2 = True
        sounds.victor_punch.play()
    if key == keys.UP and guardianRun.y == 440 and dictMenu["pause"] == False:
        guardianJumpFlag = True
    elif key == keys.P and guardianRunFlag == True and dictMenu["pause"] == False:
        guardianPunchFlag = True
        sounds.guardian_punch.play()
    elif key == keys.O and guardianRunFlag == True and shot.x == -10 and dictMenu["pause"] == False and guardianDeadFlag == True:
        guardianShotFlag = True
        sounds.shot.play()
        shotFlag = True
        shot.x = guardianRun.x
        shot.y = guardianRun.y + 25
    if key == keys.ESCAPE and dictMenu["pause"] == True:
        dictMenu["pause"] = False
    elif key == keys.ESCAPE and dictMenu["start"] == True:
        dictMenu["pause"] = True
def on_mouse_down(pos):
    global coin , time , sound
    if soundMute.collidepoint(pos) and dictMenu["gameMenu"] == True and dictMenu["exit"] == False and sound == False:
        sound = True
        sounds.menu.play()
    elif soundMute.collidepoint(pos) and dictMenu["gameMenu"] == True and dictMenu["exit"] == False:
        sound = False
        sounds.menu.stop()
    if buttonStart.collidepoint(pos) and dictMenu["gameMenu"] == True and dictMenu["exit"] == False:
        dictMenu["gameMenu"] = False
        dictMenu["start"] = False
        dictMenu["shop"] = False
        dictMenu["controlls"] = False
        dictMenu["main_select"] = True
        dictMenu["loading"] = False
        dictMenu["exit"] = False
    elif buttonPlay.collidepoint(pos) and dictMenu["main_select"] == True:
        time = 60
        healthBarLeft.x = 89
        healthBarLeft.y = 50
        healthBarRight.x = 912
        healthBarRight.y = 50
        victorRun.x = 150
        victorRun.y = 498
        guardianRun.x = 840
        guardianRun.y = 440
        dictMenu["gameMenu"] = False
        dictMenu["start"] = False
        dictMenu["shop"] = False
        dictMenu["controlls"] = False
        dictMenu["main_select"] = False
        dictMenu["loading"] = True
        dictMenu["pause"] = False
        dictMenu["exit"] = False
    elif buttonShop.collidepoint(pos) and dictMenu["gameMenu"] == True and dictMenu["exit"] == False:
        dictMenu["gameMenu"] = False
        dictMenu["start"] = False
        dictMenu["shop"] = True
        dictMenu["controlls"] = False
        dictMenu["main_select"] = False
        dictMenu["loading"] = False
        dictMenu["pause"] = False
        dictMenu["exit"] = False
    elif buttonControlls.collidepoint(pos) and dictMenu["gameMenu"] == True and dictMenu["exit"] == False:
        dictMenu["gameMenu"] = False
        dictMenu["start"] = False
        dictMenu["shop"] = False
        dictMenu["controlls"] = True
        dictMenu["main_select"] = False
        dictMenu["loading"] = False
        dictMenu["pause"] = False
        dictMenu["exit"] = False
    elif buttonExit.collidepoint(pos) and dictMenu["gameMenu"] == True:
        dictMenu["gameMenu"] = True
        dictMenu["start"] = False
        dictMenu["shop"] = False
        dictMenu["controlls"] = False
        dictMenu["main_select"] = False
        dictMenu["loading"] = False
        dictMenu["pause"] = False
        dictMenu["exit"] = True
    if buttonPauseResume.collidepoint(pos) and dictMenu["pause"] == True:
        dictMenu["pause"] = False
    elif buttonPauseBack.collidepoint(pos) and dictMenu["pause"] == True:
        dictMenu["gameMenu"] = True
        dictMenu["start"] = False
        dictMenu["shop"] = False
        dictMenu["controlls"] = False
        dictMenu["main_select"] = False
        dictMenu["loading"] = False
        dictMenu["pause"] = False
        if sound == True:
            sounds.menu.play()
    if buttonResultAgain.collidepoint(pos) and result.y == 281:
        result.y = -281
        time = 60
        coin += 50
        healthBarLeft.x = 89
        healthBarLeft.y = 50
        healthBarRight.x = 912
        healthBarRight.y = 50
        victorRun.x = 150
        victorRun.y = 498
        guardianRun.x = 840
        guardianRun.y = 440
        dictMenu["gameMenu"] = False
        dictMenu["start"] = False
        dictMenu["shop"] = False
        dictMenu["controlls"] = False
        dictMenu["main_select"] = False
        dictMenu["loading"] = True
        dictMenu["pause"] = False
        dictMenu["exit"] = False
    elif buttonResultBack.collidepoint(pos) and result.y == 281:
        result.y = -281
        coin += 50
        dictMenu["gameMenu"] = True
        dictMenu["start"] = False
        dictMenu["shop"] = False
        dictMenu["controlls"] = False
        dictMenu["main_select"] = False
        dictMenu["loading"] = False
        dictMenu["pause"] = False
        if sound == True:
            sounds.menu.play()
    if buttonShopIcon2.collidepoint(pos) and dictMenu["shop"] == True:
        if coin >= 300:
            if dictShop["winterMountain"] == False:
                coin -= 300
                dictShop["winterMountain"] = True
        elif dictShop["winterMountain"] == False:
            dictMenu["gameNotice"] = True
    elif buttonShopIcon3.collidepoint(pos) and dictMenu["shop"] == True:
        if coin >= 500:
            if dictShop["winterCity"] == False:
                coin -= 500
                dictShop["winterCity"] = True
        elif dictShop["winterCity"] == False:
            dictMenu["gameNotice"] = True
    elif buttonShopIcon4.collidepoint(pos) and dictMenu["shop"] == True:
        if coin >= 700:
            if dictShop["winterHouse"] == False:
                coin -= 700
                dictShop["winterHouse"] = True
        elif dictShop["winterHouse"] == False:
            dictMenu["gameNotice"] = True
    if buttonNotice.collidepoint(pos):
        dictMenu["gameNotice"] = False
    if buttonShopBack.collidepoint(pos) and dictMenu["shop"] == True:
        dictMenu["gameMenu"] = True
        dictMenu["start"] = False
        dictMenu["shop"] = False
        dictMenu["controlls"] = False
        dictMenu["main_select"] = False
        dictMenu["loading"] = False
        dictMenu["pause"] = False
    if buttonControllsBack.collidepoint(pos) and dictMenu["controlls"] == True:
        dictMenu["gameMenu"] = True
        dictMenu["start"] = False
        dictMenu["shop"] = False
        dictMenu["controlls"] = False
        dictMenu["main_select"] = False
        dictMenu["loading"] = False
        dictMenu["pause"] = False
    if buttonSelectBack.collidepoint(pos) and dictMenu["main_select"] == True:
        dictMenu["gameMenu"] = True
        dictMenu["start"] = False
        dictMenu["shop"] = False
        dictMenu["controlls"] = False
        dictMenu["main_select"] = False
        dictMenu["loading"] = False
        dictMenu["pause"] = False
    if buttonExitNo.collidepoint(pos):
        dictMenu["gameMenu"] = True
        dictMenu["start"] = False
        dictMenu["shop"] = False
        dictMenu["controlls"] = False
        dictMenu["main_select"] = False
        dictMenu["loading"] = False
        dictMenu["pause"] = False
        dictMenu["exit"] = False
    elif buttonExitYes.collidepoint(pos):
        quit()
    if buttonShopIcon1.collidepoint(pos) and dictMenu["main_select"] == True:
        dictSelect["winterJungleSelect"] = True
        dictSelect["winterMountainSelect"] = False
        dictSelect["winterCitySelect"] = False
        dictSelect["winterHouseSelect"] = False
    elif buttonShopIcon2.collidepoint(pos) and dictMenu["main_select"] == True and dictShop["winterMountain"] == True:
        dictSelect["winterJungleSelect"] = False
        dictSelect["winterMountainSelect"] = True
        dictSelect["winterCitySelect"] = False
        dictSelect["winterHouseSelect"] = False
    elif buttonShopIcon3.collidepoint(pos) and dictMenu["main_select"] == True and dictShop["winterCity"] == True:
        dictSelect["winterJungleSelect"] = False
        dictSelect["winterMountainSelect"] = False
        dictSelect["winterCitySelect"] = True
        dictSelect["winterHouseSelect"] = False
    elif buttonShopIcon4.collidepoint(pos) and dictMenu["main_select"] == True and dictShop["winterHouse"] == True:
        dictSelect["winterJungleSelect"] = False
        dictSelect["winterMountainSelect"] = False
        dictSelect["winterCitySelect"] = False
        dictSelect["winterHouseSelect"] = True
def timer():
    global time
    if time > 0 and dictMenu["start"] == True and dictMenu["pause"] == False and healthBarLeft.x >= -85 and healthBarRight.x <= 1087:
        time -= 1
clock.schedule_interval(timer , 1)
pgzrun.go()