import pygame,sys,time,savables,audio,miscellaneous
from pygame.locals import *
pygame.mixer.pre_init(44100, -16, 1, 512) #<-- fixes sound lag delay :D

# basic variable definitions
white = (255,255,255)
red = (255,0,0)
darkred = (125,0,0)
green = (0,225,0)
darkgreen = (0,100,0)
black = (0,0,0)
blue = (0,0,75)
yellow = (240,240,0)
orange = (255,155,0)
darkyellow = (210,210,0)
selectionx,selectiony = 1,1
weaponSkill = 0
HBwarning = False

# pygame initialization
pygame.init()
gameDisplay = pygame.display.set_mode((900,600))
swordIcon = pygame.image.load('pictures/weapons/sword2.jpg')
fist = pygame.image.load('pictures/weapons/fist.png')
staff = pygame.image.load('pictures/weapons/staff3.jpg')
fire = pygame.image.load('pictures/weapons/fire.jpg')
gun = pygame.image.load('pictures/weapons/minigun2.jpg')
chainmail = pygame.image.load('pictures/items/chainmail.jpg')
brestPlate = pygame.image.load('pictures/items/breastPlate2.jpg')
battleSuite = pygame.image.load('pictures/items/battleSuite.jpg')
star1 = pygame.image.load('pictures/star2.png')
star2 = pygame.image.load('pictures/star.png')
ice = pygame.image.load('pictures/weapons/ice.png')
Background1 = pygame.image.load('pictures/background1.jpg').convert_alpha()
Background2 = pygame.image.load('pictures/background2.jpg')
arrowCover1 = pygame.image.load('pictures/arrowCover3.bmp')
arrowCover2 = pygame.image.load('pictures/arrowCover4.bmp')
leftBorder = pygame.image.load('pictures/leftBorder.png')
bottomBorder = pygame.image.load('pictures/bottomBorder.png')
rightBorder = pygame.image.load('pictures/rightBorder.png')
topBorder = pygame.image.load('pictures/topBorder.png')
hPotion = pygame.image.load('pictures/items/health_potion.gif')
rPotion = pygame.image.load('pictures/items/whitePotion.jpg')
mPotion = pygame.image.load('pictures/items/bluePotion.jpg')
cursor = pygame.image.load('pictures/cursor.png')
smallBox = pygame.image.load('pictures/smallBorder.png')

font = pygame.font.SysFont("comicsansms",44) #30
font2 = pygame.font.SysFont("comicsansms",20) #16
font3 = pygame.font.SysFont("comicsansms",25) #22
clock = pygame.time.Clock()
undefined = font.render("?",True,yellow)
maxHealth = 100
menuType = 0

def skillDisplayChange(equip):
    global weaponSkill
    if equip == "fists":
        weaponSkill = savables.fistSkill
    elif equip == "sword":
        weaponSkill = savables.swordSkill
    elif equip == "staff":
        weaponSkill = savables.staffSkill
    elif equip == "fire":
        weaponSkill = savables.fireSkill
    elif equip == "ice":
        weaponSkill = savables.iceSkill
    elif equip == "gun":
        weaponSkill = savables.gunSkill

armorBar = 0    
def armorSkillChange():
    global armorBar
    if miscellaneous.equippedArmor == "chainmail":
        armorBar = savables.chainmailTick
        armorSkill = savables.chainmailSkill
    elif miscellaneous.equippedArmor == "breastPlate":
        armorBar = savables.breastPlateTick
        armorSkill = savables.breastPlateSkill
    elif miscellaneous.equippedArmor == "battleSuite":
        armorBar = savables.battleSuiteTick
        armorSkill = savables.battleSuiteSkill
    else:
        armorSkill = 0
    armorBar = -60 if armorBar <= -60 else armorBar
    return armorSkill
        
# basic text/dialog display - if arrowX and arrowY == TRUE, selections apply 
def displayText(msg1,color1,msg2,color2,msg3,color3,msg4,color4,arrowX):
    import randMonster,combat,weapons
    global selectionx,selectiony,maxHealth,HBwarning,menuType
    combat.damageDisplay()
    script = True
    tick = 1
    selectionx,selectiony = 3,1    
    while script == True:
        clock.tick(35)
        if weapons.weaponAnimations == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:# or pygame.K_KP_ENTER:
                        audio.textForward.play()
                        script = False
                        
                # must include 'X' click game quit function for every 
                # 'while' loop or 'X' Windows button wont work while in loop
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
        else:
            script = False
        
        # blue rectangle menu background and yellow outlines
        gameDisplay.blit(Background2,[0,0])
        gameDisplay.blit(Background1,(250,400))
        pygame.draw.rect(gameDisplay,yellow,(255,410,635,180),2)
        pygame.draw.rect(gameDisplay,yellow,(10,10,230,580),2)
        
        # Scene decorative borders
        gameDisplay.blit(bottomBorder,[243,388])
        gameDisplay.blit(topBorder,[243,-3])
        gameDisplay.blit(leftBorder,[230,5])
        gameDisplay.blit(rightBorder,[880,5])
        
        # menu titles and content
        weptitle = font3.render("Weapon",True,green)
        armor = font3.render("Armor",True,green)
        item = font3.render("Item",True,green)
        hlthtitle = font3.render("Health",True,green)
        gameDisplay.blit(weptitle,[85,17])
        gameDisplay.blit(armor,[93,140])
        gameDisplay.blit(item,[100,263])
        gameDisplay.blit(hlthtitle,[90,400])
        
        # Skill Bars
        import weapons
        armorSkill = armorSkillChange()
        if weapons.skillBar <= -56: 
            skillColor = darkyellow 
        else: 
            skillColor = green
        pygame.draw.rect(gameDisplay,skillColor,(90,113,15,(weapons.skillBar)))
        
        if armorBar <= -56: 
            skillColor2 = darkyellow 
        else: 
            skillColor2 = green
        pygame.draw.rect(gameDisplay,skillColor2,(90,233,15,(armorBar)))
        
        # Potion Item Boxes (keep behind borders)
        gameDisplay.blit(hPotion,[27,302]) if savables.healthPotions > 0 else gameDisplay.blit(undefined,[49,307])
        gameDisplay.blit(rPotion,[97,302]) if savables.regenPotions > 0 else gameDisplay.blit(undefined,[119,307])
        gameDisplay.blit(mPotion,[167,302]) if savables.megaPotions > 0 else gameDisplay.blit(undefined,[189,307])
        
        # weapon equipped pictures
        if combat.equip == "sword":
            gameDisplay.blit(swordIcon,(26,56,))
        elif combat.equip == "fists":
            gameDisplay.blit(fist,(26,56))
        elif combat.equip == "staff":
            gameDisplay.blit(staff,(26,56))
        elif combat.equip == "fire":
            gameDisplay.blit(fire,(26,56))
        elif combat.equip == "gun":
            gameDisplay.blit(gun,(26,56))
        elif combat.equip == "ice":
            gameDisplay.blit(ice,(26,56))
        else: 
            gameDisplay.blit(undefined,[49,62])
            
        # armor equipped pictures
        if miscellaneous.equippedArmor == "chainmail":
            gameDisplay.blit(chainmail,[27,177])
        elif miscellaneous.equippedArmor == "breastPlate":
            gameDisplay.blit(brestPlate,[27,177])
        elif miscellaneous.equippedArmor == "battleSuite":
            gameDisplay.blit(battleSuite,[27,177])
        else:
            gameDisplay.blit(undefined,[49,182])
        
        # Number of potions display
        numHpotions = str(savables.healthPotions)
        numHpotionsDisp = font3.render(numHpotions,True,green)
        gameDisplay.blit(numHpotionsDisp,[68,328]) if savables.healthPotions > 0 else ""
        
        numRpotions = str(savables.regenPotions)
        numRpotionsDisp = font3.render(numRpotions,True,green)
        gameDisplay.blit(numRpotionsDisp,[138,328]) if savables.regenPotions > 0 else ""
        
        numMpotions = str(savables.megaPotions)
        numMpotionsDisp = font3.render(numMpotions,True,green)
        gameDisplay.blit(numMpotionsDisp,[208,328]) if savables.megaPotions > 0 else ""
        
        #Weapon and Armor outlines
        gameDisplay.blit(smallBox,[25,55])
        gameDisplay.blit(smallBox,[25,175])
        
        # Potions Outlines
        gameDisplay.blit(smallBox,[25,300])
        gameDisplay.blit(smallBox,[95,300])
        gameDisplay.blit(smallBox,[165,300])
        
        skillDisplayChange(combat.equip)
        gameDisplay.blit(star2,(115,50)) if weaponSkill >= 1 else gameDisplay.blit(star1,(115,50))
        gameDisplay.blit(star2,(155,50)) if weaponSkill >= 2 else gameDisplay.blit(star1,(155,50))
        gameDisplay.blit(star2,(195,50)) if weaponSkill >= 3 else gameDisplay.blit(star1,(195,50))
        
        gameDisplay.blit(star2,(115,175)) if armorSkill >= 1 else gameDisplay.blit(star1,(115,175))
        gameDisplay.blit(star2,(155,175)) if armorSkill >= 2 else gameDisplay.blit(star1,(155,175))
        gameDisplay.blit(star2,(195,175)) if armorSkill >= 3 else gameDisplay.blit(star1,(195,175))
        
        wDamage = font2.render("Damage:",True,orange)
        gameDisplay.blit(wDamage,[135,77])
        wDamage = font2.render(combat.dispDamage,True,orange)
        gameDisplay.blit(wDamage,[138,97])
  
        # Hero health amount display
        maxHealth = 100+(savables.healthTanks*100)
        savables.health = maxHealth if savables.health > maxHealth else savables.health
        savables.health = 0 if savables.health < 0 else savables.health
        health = savables.health
        pygame.draw.rect(gameDisplay,darkred,(25,435,((float(health)/maxHealth)*200.0),45))
        hlthamt = font.render(("%s"%health),True,yellow) 
        pygame.draw.rect(gameDisplay,yellow,(25,435,200,45),2)
        gameDisplay.blit(hlthamt,[100,435])
        
        # Low health audio warning
        if savables.health <= 20 and HBwarning == False:
            HBwarning = True
            audio.heartBeat.play()
        elif savables.health > 20:
            HBwarning = False 
        
        # Monster health amount display
        if combat.battle == True:
            import combat
            mhlthtitle = font3.render(randMonster.monster,True,green)
            gameDisplay.blit(mhlthtitle,[25,495])
            combat.monsterBar = 0 if combat.monsterBar <= 0 else combat.monsterBar
            pygame.draw.rect(gameDisplay,darkred,(25,530,(combat.monsterBar),45))
            pygame.draw.rect(gameDisplay,yellow,(25,530,200,45),2)
        
        # dialog/text box engine
        textLine1 = font.render(msg1,True,color1)
        textLine2 = font.render(msg2,True,color2)
        textLine3 = font.render(msg3,True,color3)
        textLine4 = font.render(msg4,True,color4)
        gameDisplay.blit(textLine1,[275,415])
        gameDisplay.blit(textLine2,[275,455])
        gameDisplay.blit(textLine3,[275,495])
        gameDisplay.blit(textLine4,[275,535])
        pygame.display.update()
        
        # double column arrow selection menu
        while arrowX:# == True and arrowY == True:
            clock.tick(35)
            threeChoiceMenus = ["oneChoiceMenu","twoChoiceMenu","threeChoiceMenu"]
            fourChoiceMenus = threeChoiceMenus + ["fourChoiceMenu"]
            fiveChoiceMenus = fourChoiceMenus + ["fiveChoiceMenu"]
            pygame.draw.rect(gameDisplay,yellow,(255,410,635,180),2)
            gameDisplay.blit(arrowCover1,[257,469])
            gameDisplay.blit(arrowCover2,[557,469])
            if selectionx <= 3 and selectiony <= 1:
                selectionx = 3
                selectiony = 1
                gameDisplay.blit(cursor,[265,470])
            elif selectionx == 4 and selectiony <= 1:
                if menuType == "oneChoiceMenu":
                    selectionx = 3
                    selectiony = 1
                else:
                    selectiony = 1
                    gameDisplay.blit(cursor,[265,510])
            elif selectionx >= 5 and selectiony <= 1:
                if menuType == "twoChoiceMenu":
                    selectionx = 4
                    selectiony = 1
                else:
                    selectionx = 5
                    selectiony = 1
                    gameDisplay.blit(cursor,[265,550])
            elif selectionx <= 3 and selectiony >= 2:
                if menuType in threeChoiceMenus:
                    selectiony = 1
                    selectionx -= 1
                else:
                    selectionx = 3
                    selectiony = 2
                    gameDisplay.blit(cursor,[565,470])
            elif selectionx == 4 and selectiony >= 2:
                if menuType in fourChoiceMenus:
                    selectionx = 3
                    selectiony = 2
                else:
                    selectiony = 2
                    gameDisplay.blit(cursor,[565,510])
            elif selectionx >= 5 and selectiony >= 2:
                if menuType in fiveChoiceMenus:
                    selectionx = 4
                    selectiony = 2
                else:
                    selectionx = 5
                    selectiony = 2
                    gameDisplay.blit(cursor,[565,550])
            for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        audio.selectTick.play()
                        arrowX = False
                        arrowY = False
                        script = False
                    elif event.key == pygame.K_DOWN:
                        audio.arrowTick.play()
                        selectionx += 1
                    elif event.key == pygame.K_UP:
                        audio.arrowTick.play()
                        selectionx -= 1
                    elif event.key == pygame.K_RIGHT:
                        audio.arrowTick.play()
                        selectiony += 1
                    elif event.key == pygame.K_LEFT: 
                        audio.arrowTick.play()
                        selectiony -= 1
            pygame.display.update()
        menuType = 0