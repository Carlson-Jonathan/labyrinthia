import random,DialogBox,randMonster,combat,\
door,pygame,time,audio,savables,finalBattle
green,yellow,orange,red = (0,225,0),(240,240,0),(255,155,0),(255,0,0)
gameDisplay = pygame.display.set_mode((900,600))
clock = pygame.time.Clock()
riposte,parry = False,False
skillBar = 0
weaponAnimations = False
bleed = 0

lightblue = (150,150,255)
greyout = 75,75,75

def fists():
    global weaponAnimations
    fistMin,fistMax = 4,12
    weaponAnimations = True
    damage = int(random.randint(fistMin,fistMax)*combat.damageReducer*combat.damageEnhancer)
    fisticuffs = ["slap","pinch","scratch","bite","kick","spit on","fart at","punch","mock","flick boogers at","give a wedgie to","trip"]
    action = random.choice(fisticuffs)
    audio.weaponSwoosh.play()
    DialogBox.displayText("You %s the %s!"%(action,randMonster.monster),yellow,
        "",yellow,"",yellow,"",yellow,False)
    if not finalBattle.punishBattle:
        time.sleep(.3)
        audio.punch.play()
        combat.monsterHealth -= damage
        combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
        DialogBox.displayText("You %s the %s!"%(action,randMonster.monster),yellow,
            "The %s takes %d damage"%(randMonster.monster,damage),orange,
            "to its health!",orange,"",yellow,False)
        monsterTakeDamage()
        weaponAnimations = False    
        DialogBox.displayText("You %s the %s!"%(action,randMonster.monster),yellow,
            "The %s takes %d damage"%(randMonster.monster,damage),orange,
            "to its health!",orange,"",yellow,False)
        time.sleep(.3)

def sword():
    global riposte,parry,skillBar,weaponAnimations,bleed
    weaponAnimations = True
    savables.swordTick -= 2
    savables.swordTick = -56 if savables.swordTick <= -56 else savables.swordTick
    skillBar = savables.swordTick
    damage = int(random.randint(savables.swordMin,savables.swordMax)*combat.damageReducer*combat.damageEnhancer)
    DialogBox.displayText("You attack the %s with"%randMonster.monster,yellow,
        "your sword.",yellow,"",yellow,"",yellow,False)
    audio.weaponSwoosh.play()
    swordAnimation()
    DialogBox.displayText("You attack the %s with"%randMonster.monster,yellow,
        "your sword.",yellow,"",yellow,"",yellow,False)
    if not finalBattle.punishBattle:
        audio.monsterHit.play()
        combat.monsterHealth -= damage
        combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
        DialogBox.displayText("You attack the %s with"%randMonster.monster,yellow,
        "your sword.",yellow,"The %s takes %d damage!"%(randMonster.monster,damage),orange,"",yellow,
        False)
        monsterTakeDamage()
        DialogBox.displayText("You attack the %s with"%randMonster.monster,yellow,
        "your sword.",yellow,"The %s takes %d damage!"%(randMonster.monster,damage),orange,"",yellow,
        False)
        roll = random.randint(1,10)
        if savables.swordSkill == 3 and roll < 5:
            bleed += random.randint(5,15) if savables.swordSkill == 3 else ""
            time.sleep(.2)
            DialogBox.displayText("You attack the %s with"%randMonster.monster,yellow,
            "your sword.",yellow,"The %s takes %d damage!"%(randMonster.monster,damage),orange,
            "The %s is wounded!"%randMonster.monster,orange,False)
            weaponAnimations = False
            time.sleep(.3)
            DialogBox.displayText("You attack the %s with"%randMonster.monster,yellow,
            "your sword.",yellow,"The %s takes %d damage!"%(randMonster.monster,damage),orange,
            "The %s is wounded!"%randMonster.monster,orange,False)
        else:
            weaponAnimations = False
            DialogBox.displayText("You attack the %s with"%randMonster.monster,yellow,
            "your sword.",yellow,"The %s takes %d damage!"%(randMonster.monster,damage),orange,"",yellow,
            False)
        time.sleep(.3)
    
def swordAnimation():
    swordPic = pygame.image.load('pictures/weapons/sword4.png')
    swX,swY,turn = 800,-350,-36
    while swY < 175 :
        clock.tick(75)
        swX += -20
        swY += 44
        turn += 8
        spin = pygame.transform.rotate(swordPic,(turn))
        gameDisplay.blit(spin,[swX,swY])
        redrawBorders()
        pygame.display.update()
        gameDisplay.blit(randMonster.monsterBackground,[250,0])
        gameDisplay.blit(randMonster.monsterPic,[250,0])
        
def redrawBorders():
    gameDisplay.blit(DialogBox.bottomBorder,[243,388])
    gameDisplay.blit(DialogBox.topBorder,[243,-3])
    gameDisplay.blit(DialogBox.leftBorder,[230,5])
    gameDisplay.blit(DialogBox.rightBorder,[880,5])
        
def monsterTakeDamage():
    blink = 0
    while blink < 9:
        clock.tick(35)
        gameDisplay.blit(randMonster.monsterBackground,[250,0])
        redrawBorders()
        pygame.display.update()
        gameDisplay.blit(randMonster.monsterPic,[250,0])
        redrawBorders()
        pygame.display.update()
        blink += 1
        
def parry():
    global weaponAnimations
    weaponAnimations = True
    DialogBox.displayText("The %s attacks!"%randMonster.monster,yellow,
        "",green,"",yellow,"",yellow,False)
    time.sleep(.3)
    audio.parryAttack.play()
    parryAni()
    weaponAnimations = False
    DialogBox.displayText("The %s attacks!"%randMonster.monster,yellow,
        "You parry the attack with your sword.",green,"",yellow,"",yellow,False)
    
def parryAni():
    shield = pygame.image.load('pictures/weapons/shield.png')
    y = 250
    while y > 200:
        gameDisplay.blit(shield,(525,y))
        pygame.display.update()
        y -= 1
        gameDisplay.blit(randMonster.monsterBackground,[250,0])
        gameDisplay.blit(randMonster.monsterPic,[250,0])
        redrawBorders()

def riposte():
    global bleed,weaponAnimations
    damage = int(random.randint(savables.swordMin,savables.swordMax)*combat.damageReducer*combat.damageEnhancer)
    weaponAnimations = True
    DialogBox.displayText("You riposte the %s's"%randMonster.monster,yellow,
    "attack with your sword!",yellow,"",yellow,"",yellow,False)
    audio.monsterHit.play()
    monsterTakeDamage()
    combat.monsterHealth -= damage
    combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
    time.sleep(.2)
    DialogBox.displayText("You riposte the %s's"%randMonster.monster,yellow,
    "attack with your sword!",yellow,
    "The %s takes %d damage!"%(randMonster.monster,damage),orange,"",yellow,False)
    roll = random.randint(1,10)
    if savables.swordSkill == 3 and roll < 5:
        time.sleep(.2)
        DialogBox.displayText("You riposte the %s's"%randMonster.monster,yellow,
        "attack with your sword!",yellow,
        "The %s takes %d damage!"%(randMonster.monster,damage),orange,
        "The %s is wounded!"%randMonster.monster,orange,False)
        bleed += (random.randint(5,15))
        weaponAnimations = False
        DialogBox.displayText("You riposte the %s's"%randMonster.monster,yellow,
        "attack with your sword!",yellow,
        "The %s takes %d damage!"%(randMonster.monster,damage),orange,
        "The %s is wounded!"%randMonster.monster,orange,False)
    else:
        weaponAnimations = False
        DialogBox.displayText("You riposte the %s's"%randMonster.monster,yellow,
        "attack with your sword!",yellow,
        "The %s takes %d damage!"%(randMonster.monster,damage),orange,"",yellow,False)
    time.sleep(.3)

def fire():
    global skillBar,weaponAnimations
    weaponAnimations = True
    savables.fireTick -= 2
    savables.fireTick = -56 if savables.fireTick <= -56 else savables.fireTick
    skillBar = savables.fireTick    
    DialogBox.displayText("You shoot fire forth from your hands...",yellow,
        "",orange,"",yellow,"",yellow,False)
    audio.inferno.play()
    fireAnimation()
    if not finalBattle.punishBattle:
        audio.monsterHit.play()
        damage = int(random.randint(savables.fireMin,savables.fireMax)*combat.damageReducer*combat.damageEnhancer)
        combat.monsterHealth -= damage
        combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
        DialogBox.displayText("You shoot fire forth from your hands...",yellow,
        "",orange,"",yellow,"",yellow,False)
        monsterTakeDamage()
        weaponAnimations = False
        DialogBox.displayText("You shoot fire forth from your hands...",yellow,
        "The %s takes %d damage!"%(randMonster.monster,damage),orange,
        "",yellow,"",yellow,False)
        roll = random.randint(1,2)
        if (roll == 1 and savables.fireSkill == 1) or savables.fireSkill >= 2:
            time.sleep(.3)
            damage = int(random.randint((savables.fireMin),(savables.fireMax))*combat.damageReducer*combat.damageEnhancer)
            damage = damage/2 if savables.fireSkill <= 2 else damage
            audio.fireBurn.play()
            time.sleep(.2)
            DialogBox.displayText("The %s ignites on fire!"%randMonster.monster,yellow,
            "",yellow,"",yellow,"",yellow,False)
            combat.monsterHealth -= damage
            combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
            monsterTakeDamage()
            time.sleep(.2)
            DialogBox.displayText("The %s ignites on fire!"%randMonster.monster,yellow,
            "The %s takes %d more!"%(randMonster.monster,damage),orange,
            "damage!",orange,"",yellow,False)
            audio.fireBurn.fadeout(1000)
        time.sleep(.3)
    
def fireAttackText():
    DialogBox.displayText("You shoot fire forth from your hands...",yellow,
    "",orange,"",yellow,"",yellow,False)
    
def fireDamageText():
    damage = int(random.randint(savables.fireMin,savables.fireMax)*combat.damageReducer*combat.damageEnhancer)
    combat.monsterHealth -= damage
    combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
    DialogBox.displayText("You shoot fire forth from your hands...",yellow,
    "The %s takes %d damage!"%(randMonster.monster,damage),orange,
    "",yellow,"",yellow,False)
        
def fireAnimation():
    firePic = pygame.image.load('pictures/weapons/fireAttack.png')
    blitX,blitY,growX,growY,turn,accelerateX,accelerateY = 575,200,0,0,0,0,0
    while blitY > -900 :
        weaponAnimations = True
        clock.tick(50)
        blitX -= (accelerateX/2)
        blitY -= (accelerateY/2)
        growX += accelerateX
        growY += accelerateY
        accelerateX += 16
        accelerateY += 16
        turn += 90
        spin = pygame.transform.rotate(firePic,(turn))
        blast = pygame.transform.scale(spin,[growX,growY])
        gameDisplay.blit(blast,[blitX,blitY])
        redrawBorders()
        fireAttackText()
        pygame.display.update()
        gameDisplay.blit(randMonster.monsterBackground,[250,0])
        gameDisplay.blit(randMonster.monsterPic,[250,0])

monsterAttackBreak = 0
def ice():
    global skillBar,weaponAnimations,monsterAttackBreak
    weaponAnimations = True
    savables.iceTick -= 2
    savables.iceTick = -56 if savables.iceTick <= -56 else savables.iceTick
    skillBar = savables.iceTick
    audio.iceAttackSound.play()
    DialogBox.displayText("Razor shards of ice spray forth!",yellow,
    "",yellow,"",yellow,"",yellow,False)
    iceAnimation()
    DialogBox.displayText("Razor shards of ice spray forth!",yellow,
    "",yellow,"",yellow,"",yellow,False)   
    if not finalBattle.punishBattle:
        audio.monsterHit.play()
        damage = int(savables.iceMax*combat.damageEnhancer*combat.damageReducer)
        combat.monsterHealth -= damage
        combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
        DialogBox.displayText("Razor shards of ice spray forth!",yellow,
        "The %s takes %d damage!"%(randMonster.monster,damage),orange,"",yellow,"",yellow,False)
        monsterTakeDamage()
        weaponAnimations = False
        DialogBox.displayText("Razor shards of ice spray forth!",yellow,
        "The %s takes %d damage!"%(randMonster.monster,damage),orange,"",yellow,"",yellow,False)
        roll = random.randint(1,4)
        if savables.iceSkill == 3 and roll == 1:
            time.sleep(.3)
            randMonster.monsterPic = randMonster.monsterFrozenPic
            gameDisplay.blit(randMonster.monsterBackground,[250,0])
            gameDisplay.blit(randMonster.monsterPic,[250,0])
            audio.freezing.play()
            DialogBox.displayText("                D E E P   F R E E Z E !",lightblue,
            "The %s is frozen solid"%randMonster.monster,green, 
            "and can't move!",green,"",yellow,False)
            combat.deepFreeze = random.randint(2,3)
        if savables.iceSkill >= 2 and roll == 2:
            time.sleep(.3)
            weaponAnimations = True
            DialogBox.displayText("            S H A T T E R   A R M O R !",lightblue,
            "The freezing affect of your ice attack",green,
            "reduces the %s's defense!"%randMonster.monster,green, 
            "",yellow,False)
            shatter()
            weaponAnimations = False
            DialogBox.displayText("            S H A T T E R   A R M O R !",lightblue,
            "The freezing affect of your ice attack",green,
            "reduces the %s's defense!"%randMonster.monster,green, 
            "",yellow,False)
            combat.damageEnhancer += .2
        if savables.iceSkill >= 2 and roll == 3:
            time.sleep(.3)
            weaponAnimations = True
            DialogBox.displayText("                  F R O S T   B I T E !",lightblue,
            "The freezing affect of your ice attack",green,
            "reduces the %s's ability"%randMonster.monster,green, 
            "to attack!",green,False)
            frostBite()
            weaponAnimations = False
            monsterAttackBreak += .05
            DialogBox.displayText("                  F R O S T   B I T E !",lightblue,
            "The freezing affect of your ice attack",green,
            "reduces the %s's ability"%randMonster.monster,green, 
            "to attack!",green,False)
        time.sleep(.3)
                
shieldFull = pygame.image.load('pictures/weapons/shield2.png')
shieldLeft = pygame.image.load('pictures/weapons/shieldLeft.png')
shieldRight = pygame.image.load('pictures/weapons/shieldRight.png')
swordFull = pygame.image.load('pictures/weapons/sword5.png')
swordRight = pygame.image.load('pictures/weapons/swordRight.png')
swordLeft = pygame.image.load('pictures/weapons/swordLeft.png')
def shatter():
    rotateL,rotateR,x1,x2,y = 0,0,532,570,200
    gameDisplay.blit(shieldFull,[533,200])
    pygame.display.update()
    time.sleep(.5)
    gameDisplay.blit(randMonster.monsterBackground,[250,0])
    gameDisplay.blit(randMonster.monsterPic,[250,0])
    redrawBorders()
    audio.shatterArmor.play()
    while rotateL < 25:
        clock.tick(50)
        rotateL += .4
        rotateR -= .45
        x1 -= 1
        x2 += .5
        y += .5
        shieldAni1 = pygame.transform.rotate(shieldLeft,(rotateL))
        shieldAni2 = pygame.transform.rotate(shieldRight,(rotateR))
        gameDisplay.blit(shieldAni1,[x1,y])
        gameDisplay.blit(shieldAni2,[x2,y])
        pygame.display.update()
        gameDisplay.blit(randMonster.monsterBackground,[250,0])
        gameDisplay.blit(randMonster.monsterPic,[250,0])
        redrawBorders()       
 
def frostBite():
    rotateL,rotateR,x1,x2,y = 0,0,430,430,200
    gameDisplay.blit(swordFull,[430,200])
    pygame.display.update()
    time.sleep(.5)
    gameDisplay.blit(randMonster.monsterBackground,[250,0])
    gameDisplay.blit(randMonster.monsterPic,[250,0])
    redrawBorders()
    audio.shatterArmor.play()
    while rotateL < 25:
        clock.tick(50)
        rotateL += .4
        rotateR -= .4
        x1 -= 1
        x2 += .5
        y += .3
        swordAni1 = pygame.transform.rotate(swordRight,(rotateR))
        swordAni2 = pygame.transform.rotate(swordLeft,(rotateL))
        gameDisplay.blit(swordAni1,[x1,y])
        gameDisplay.blit(swordAni2,[x2,y])
        pygame.display.update()
        gameDisplay.blit(randMonster.monsterBackground,[250,0])
        gameDisplay.blit(randMonster.monsterPic,[250,0])
        redrawBorders()
    
    
def iceAnimation():
    icebolt = pygame.image.load("pictures/weapons/icicle.png")
    ascend,ascend1,ascend2,ascend3,ascend4,ascend5,ascend6,\
    ascend7,ascend8 = 500,500,500,500,500,500,500,500,500
    bolt1,bolt2,bolt3,bolt4,bolt5,bolt6,bolt7,bolt8 = \
    575,575,575,575,575,575,575,575
    while ascend > -650:
        clock.tick(50)
        leftIce = pygame.transform.rotate(icebolt,(35))
        leftMidIce = pygame.transform.rotate(icebolt,(15))
        rightCenterIce = pygame.transform.rotate(icebolt,(-10))
        leftCenterIce = pygame.transform.rotate(icebolt,(10))
        rightMidIce = pygame.transform.rotate(icebolt,(-15))
        rightIce = pygame.transform.rotate(icebolt,(-35))
        if ascend < 0:
            gameDisplay.blit(leftIce,[bolt1,ascend1])
            bolt1 -= 30
            ascend1 -= 50
        if ascend < 200:
            gameDisplay.blit(leftMidIce,[bolt2,ascend2])
            bolt2 -= 20
            ascend2 -= 50
        if ascend < 400:
            gameDisplay.blit(leftCenterIce,[bolt7,ascend7])
            bolt7 -= 10
            ascend7 -= 50

        gameDisplay.blit(icebolt,[bolt3,ascend3])
        ascend3 -= 50 # Center bolt
        if ascend < 100:
            gameDisplay.blit(icebolt,[bolt8,ascend8])
            ascend8 -= 50 # Center bolt2

        if ascend < 300:
            gameDisplay.blit(rightCenterIce,[bolt6,ascend6])
            bolt6 += 10
            ascend6 -= 50
        if ascend < 100:
            gameDisplay.blit(rightMidIce,[bolt4,ascend4])
            bolt4 += 20
            ascend4 -= 50
        if ascend < -100:
            gameDisplay.blit(rightIce,[bolt5,ascend5])
            bolt5 += 30
            ascend5 -= 50
        DialogBox.displayText("Razor shards of ice spray forth!",yellow,
        "",yellow,"",yellow,"",yellow,False)
        redrawBorders()
        pygame.display.update()
        gameDisplay.blit(randMonster.monsterBackground,[250,0])
        gameDisplay.blit(randMonster.monsterPic,[250,0])
        ascend -= 50
    
def staff():
    global skillBar,weaponAnimations,damage1
    X = combat.damageReducer*combat.damageEnhancer
    savables.staffTick -= 2
    savables.staffTick = -56 if savables.staffTick <= -56 else savables.staffTick
    skillBar = savables.staffTick
    min,max = savables.staffMin,savables.staffMax
    damage1,damage2,damage3,damage4,damage5 = random.randint(min,max),\
    random.randint(min,max),random.randint(min,max),random.randint(min,max),\
    random.randint(min,max)
    damage1,damage2,damage3,damage4,damage5 = int(damage1*X),int(damage2*X),\
    int(damage3*X),int(damage4*X),int(damage5*X)
    multiStrike = random.randint(-10,38) #34,27,18 = chance combos
    multiStrike = 1 if finalBattle.punishBattle else multiStrike
    if multiStrike >= 34 and savables.staffSkill >= 3:
        DialogBox.displayText("You unleash a devestating flurry of blows!",yellow,
            "",yellow,"",yellow,"",yellow,False)
        DialogBox.displayText("You unleash a devestating flurry of blows!",yellow,
            "",yellow,"             S U P E R  C O M B O ! ! !",orange,"",yellow,False)
        audio.weaponSwoosh.play()
        staffMultiAni(585)
        weaponAnimations = True
        audio.monsterHit.play()
        combat.monsterHealth -= damage1
        combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
        DialogBox.displayText("You unleash a devestating flurry of blows!",yellow,
            "   You do %d damage!"%damage1,yellow,"",yellow,"",yellow,False)
        monsterTakeDamage()
        audio.monsterHit.play()
        combat.monsterHealth -= damage2
        combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
        DialogBox.displayText("You unleash a devestating flurry of blows!",yellow,
            "   You do %d damage!  You do %d damage!"%(damage1,damage2),
            yellow,"",yellow,"",yellow,False)
        monsterTakeDamage()
        audio.monsterHit.play()
        combat.monsterHealth -= damage3
        combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
        DialogBox.displayText("You unleash a devestating flurry of blows!",yellow,
            "   You do %d damage!  You do %d damage!"%(damage1,damage2),yellow,
            "   You do %d damage!"%damage3,orange,"",yellow,False)
        monsterTakeDamage()
        audio.monsterHit.play()
        combat.monsterHealth -= damage4
        combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
        DialogBox.displayText("You unleash a devestating flurry of blows!",yellow,
            "   You do %d damage!  You do %d damage!"%(damage1,damage2),yellow,
            "   You do %d damage!  You do %d damage!"%(damage3,damage4),orange,"",yellow,False)
        monsterTakeDamage()
        audio.monsterHit.play()
        combat.monsterHealth -= damage5
        combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
        DialogBox.displayText("You unleash a devestating flurry of blows!",yellow,
            "   You do %d damage!  You do %d damage!"%(damage1,damage2),yellow,
            "   You do %d damage!  You do %d damage!"%(damage3,damage4),orange,
            "                You do %d damage!"%damage5,red,False)
        monsterTakeDamage()
        weaponAnimations = False
        DialogBox.displayText("You unleash a devestating flurry of blows!",yellow,
            "   You do %d damage!  You do %d damage!"%(damage1,damage2),yellow,
            "   You do %d damage!  You do %d damage!"%(damage3,damage4),orange,
            "                You do %d damage!"%damage5,red,False)
    elif multiStrike >= 27 and savables.staffSkill >= 2:
        DialogBox.displayText("               T r i p l e  S t r i k e !",yellow,
            "",yellow,"",yellow,"",yellow,False)
        audio.weaponSwoosh.play()
        staffMultiAni(345)
        weaponAnimations = True
        audio.monsterHit.play()
        combat.monsterHealth -= damage1
        combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
        DialogBox.displayText("               T r i p l e  S t r i k e !",yellow,
            "The %s takes %d damage!"%(randMonster.monster,damage1),orange,
            "",yellow,"",yellow,False)
        monsterTakeDamage()
        audio.monsterHit.play()
        combat.monsterHealth -= damage2
        combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
        DialogBox.displayText("               T r i p l e  S t r i k e !",yellow,
            "The %s takes %d damage!"%(randMonster.monster,damage1),orange,
            "The %s takes %d damage!"%(randMonster.monster,damage2),red,
            "",yellow,False)
        monsterTakeDamage()
        audio.monsterHit.play()
        combat.monsterHealth -= damage3
        combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
        DialogBox.displayText("               T r i p l e  S t r i k e !",yellow,
            "The %s takes %d damage!"%(randMonster.monster,damage1),orange,
            "The %s takes %d damage!"%(randMonster.monster,damage2),red,
            "The %s takes %d damage!"%(randMonster.monster,damage3),yellow,False)
        monsterTakeDamage()
        weaponAnimations = False
        DialogBox.displayText("               T r i p l e  S t r i k e !",yellow,
            "The %s takes %d damage!"%(randMonster.monster,damage1),orange,
            "The %s takes %d damage!"%(randMonster.monster,damage2),red,
            "The %s takes %d damage!"%(randMonster.monster,damage3),yellow,False)
    elif multiStrike >= 18 and savables.staffSkill >= 1:
        weaponAnimations = True
        DialogBox.displayText("                     Double Strike!",yellow,
        "",yellow,"",yellow,"",yellow,False)
        audio.weaponSwoosh.play()
        staffAnimationRight()
        audio.weaponSwoosh.play()
        staffAnimationLeft()
        combat.monsterHealth -= damage1
        combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
        audio.monsterHit.play()
        DialogBox.displayText("                     Double Strike!",yellow,
            "The %s takes %d damage!"%(randMonster.monster,damage1),orange,
            "",red,"",yellow,False)
        monsterTakeDamage()
        combat.monsterHealth -= damage2
        combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
        audio.monsterHit.play()
        DialogBox.displayText("                     Double Strike!",yellow,
            "The %s takes %d damage!"%(randMonster.monster,damage1),orange,
            "The %s takes %d damage!"%(randMonster.monster,damage2),red,"",yellow,False)
        monsterTakeDamage()
        weaponAnimations = False
        DialogBox.displayText("                     Double Strike!",yellow,
            "The %s takes %d damage!"%(randMonster.monster,damage1),orange,
            "The %s takes %d damage!"%(randMonster.monster,damage2),red,"",yellow,False)
    else:
        roll = random.randint(1,2)
        weaponAnimations = True
        DialogBox.displayText("You strike the %s with"%randMonster.monster,yellow,
            "your staff!",yellow,"",yellow,"",yellow,False)
        audio.weaponSwoosh.play()
        staffAnimationLeft() if roll == 1 else staffAnimationRight()        
        if not finalBattle.punishBattle:
            audio.monsterHit.play()
            combat.monsterHealth -= damage1
            combat.monsterBar = (((combat.monsterHealth*100)/combat.totalMhealth)*2)
            DialogBox.displayText("You strike the %s with"%randMonster.monster,yellow,
            "your staff!",yellow,"The %s takes %d damage!"%(randMonster.monster,damage1),
            orange,"",yellow,False)
            monsterTakeDamage()
            weaponAnimations = False
            DialogBox.displayText("You strike the %s with"%randMonster.monster,yellow,
            "your staff!",yellow,"The %s takes %d damage!"%(randMonster.monster,damage1),
            orange,"",yellow,False)
        #time.sleep(.3)
        
def staffStrikeText():
    DialogBox.displayText("You strike the %s with"%randMonster.monster,yellow,
    "your staff!",yellow,"",yellow,"",yellow,False)
    
def staffDamageText():
    DialogBox.displayText("You strike the %s with"%randMonster.monster,yellow,
    "your staff!",yellow,"The %s takes %d damage!"%(randMonster.monster,damage1),
    orange,"",yellow,False)
        
def swooshCombo(number):
    hits = 0
    while hits < number:
        audio.weaponSwoosh.play()
        time.sleep(.15)
        hits += 1

def staffAnimationRight():
    global weaponAnimations
    staffPic = pygame.image.load('pictures/weapons/staffAni.png')
    stX,stY,turn = 750,-350,-36
    while stY < 175 :
        weaponAnimations = True
        clock.tick(75)
        stX += -30
        stY += 66
        turn += 9
        spin = pygame.transform.rotate(staffPic,(turn))
        gameDisplay.blit(spin,[stX,stY])
        redrawBorders()
        staffStrikeText()
        pygame.display.update()
        gameDisplay.blit(randMonster.monsterBackground,[250,0])
        gameDisplay.blit(randMonster.monsterPic,[250,0]) 

def staffAnimationLeft():
    global weaponAnimations
    staffPic = pygame.image.load('pictures/weapons/staffAni2.png')
    stX,stY,turn = -25,-350,36
    while stY < 175 :
        weaponAnimations = True
        clock.tick(75)
        stX += 25
        stY += 55
        turn += -8
        spin = pygame.transform.rotate(staffPic,(turn))
        gameDisplay.blit(spin,[stX,stY])
        redrawBorders()
        staffStrikeText()
        pygame.display.update()
        gameDisplay.blit(randMonster.monsterBackground,[250,0])
        gameDisplay.blit(randMonster.monsterPic,[250,0])
    
def staffMultiAni(hits):
    global weaponAnimations
    staffPic = pygame.image.load('pictures/weapons/staffMulti.png')
    turn = 0
    while turn < hits:
        weaponAnimations = True
        clock.tick(75)
        turn += 15
        spin = pygame.transform.rotate(staffPic,(turn))
        gameDisplay.blit(spin,[200,175])
        audio.weaponSwoosh.play() if turn%120 == 0 else ""
        redrawBorders()
        staffStrikeText()
        pygame.display.update()
        gameDisplay.blit(randMonster.monsterBackground,[250,0])
        gameDisplay.blit(randMonster.monsterPic,[250,0])
    weaponAnimations = False
    
    
miniGun = pygame.image.load('pictures/weapons/miniGun3.png')    
def deadMiniGun():
    global weaponAnimations
    weaponAnimations = True
    miniGunRaise()
    weaponAnimations = False
    if savables.miniGunFirstFire:
        savables.miniGunFirstFire = False
        line1 = "You pull the trigger expecting to see"
        line2 = "fireworks."
        line3 = ""
        line4 = ""    
        DialogBox.displayText(line1,yellow,line2,yellow,line3,\
        yellow,line4,yellow,False)
        audio.dryMiniGun.play()
        time.sleep(1.0)
        line1 = "You pull the trigger expecting to see"
        line2 = "fireworks."
        line3 = "Um..."
        line4 = ""    
        DialogBox.displayText(line1,yellow,line2,yellow,line3,\
        yellow,line4,yellow,False)
        line1 = "You pull the trigger expecting to see"
        line2 = "fireworks."
        line3 = "Um..."
        line4 = "Apparently this thing dosent have ammo."    
        DialogBox.displayText(line1,yellow,line2,yellow,line3,\
        yellow,line4,yellow,False)
    else:
        audio.dryMiniGun.play()
        time.sleep(1.2)
        line1 = "No ammo. Try a different weapon."
        line2 = ""
        line3 = ""
        line4 = ""    
        DialogBox.displayText(line1,yellow,line2,yellow,line3,\
        yellow,line4,yellow,False)
    weaponAnimations = True
    miniGunLower()
    weaponAnimations = False
    combat.NoWeaponSelected = True
    
def miniGunRaise():
    x,y = 640,360
    while y > 200:
        gameDisplay.blit(randMonster.monsterBackground,[250,0])
        if not finalBattle.dragonBattle:
            gameDisplay.blit(randMonster.monsterPic,[250,0])
        gameDisplay.blit(miniGun,[x,y])
        line1 = ""
        line2 = ""
        line3 = ""
        line4 = ""    
        DialogBox.displayText(line1,yellow,line2,yellow,line3,\
        yellow,line4,yellow,False)
        x -= 2
        y -= 8
        redrawBorders()
        pygame.display.update()
        
def miniGunLower():
    x,y = 600,200
    while y < 360:
        gameDisplay.blit(randMonster.monsterBackground,[250,0])
        if not finalBattle.dragonBattle:
            gameDisplay.blit(randMonster.monsterPic,[250,0])
        gameDisplay.blit(miniGun,[x,y])
        line1 = ""
        line2 = ""
        line3 = ""
        line4 = ""    
        DialogBox.displayText(line1,yellow,line2,yellow,line3,\
        yellow,line4,yellow,False)
        redrawBorders()
        x += 2
        y += 8
        pygame.display.update()
