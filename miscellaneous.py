import DialogBox,corridor1,savables,combat,audio,pygame,weapons,randMonster,random,time,finalBattle
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((900,600))

'''
Module Contents:
    Potions/Potions Menu
    Combat flee amination/game
    Use item menu

'''

line1 = "     Red Potion                 Back"
line2 = "     White Potion"
line3 = "     Blue Potion"
blankRowBack = "     ?                                Back"
blankRow = "     ?"
green = (0,240,0)
yellow = (240,240,0)
red = (255,0,0)
blue = (0,0,150)
orange = (255,155,0)
equippedArmor = ""

def potionsMenu():
    DialogBox.menuType = "fourChoiceMenu"
    row1 = line1 if savables.healthPotions > 0 else blankRowBack
    row2 = line2 if savables.regenPotions > 0 else blankRow
    row3 = line3 if savables.megaPotions > 0 else blankRow
    DialogBox.displayText("Available potions:",yellow,
    row1,green,row2,green,row3,green,True)
    selectionMenu(potionsMenu)
    
def selectionMenu(priorMenu):
    global equippedArmor
    choiceNum = (DialogBox.selectionx*DialogBox.selectiony)
    if choiceNum == 3:
        if priorMenu == potionsMenu and savables.healthPotions == 0:          
            unavailable(priorMenu)
        elif priorMenu == potionsMenu:
            drinkRedPotion()
        equippedArmor = "chainmail" if priorMenu == armorMenu else equippedArmor
    elif choiceNum == 4:
        if priorMenu == potionsMenu and savables.regenPotions == 0:          
            unavailable(priorMenu)
        elif priorMenu == potionsMenu:
            if combat.battle == True:
                audio.potionDrink.play()
                DialogBox.displayText("You gulp down the white potion as",yellow,
                "fast as you can...",yellow,"",yellow,"",yellow,False)
                DialogBox.displayText("You gulp down the white potion as",yellow,
                "fast as you can...",yellow,"...your wounds begin to close.",yellow,"",yellow,False)
                combat.regeneration = True
                savables.regenPotions -=1
                savables.emptyBottles += 1
                combat.monsterAttack(False) if not finalBattle.punishBattle else ""
            else:
                audio.potionDrink.play()
                DialogBox.displayText("You pop the cork and gulp down the white",yellow,
                "potion. You feel the regenerative effects",yellow,
                "heal your wounds.",yellow,"",yellow,False)
                DialogBox.displayText("You pop the cork and gulp down the white",yellow,
                "potion. You feel the regenerative effects",yellow,
                "heal your wounds.",yellow,"You regain 80 health (after like an hour).",green,False)
                savables.health += 80
                savables.regenPotions -= 1
                savables.emptyBottles += 1
        equippedArmor = "breastPlate" if priorMenu == armorMenu else equippedArmor
    elif choiceNum == 5:
        drinkBluePotion() if priorMenu == potionsMenu else ""
        if priorMenu == potionsMenu and savables.megaPotions == 0:          
            unavailable(priorMenu)
        elif priorMenu == potionsMenu:
            pass
        equippedArmor = "battleSuite" if priorMenu == armorMenu else equippedArmor  
    elif choiceNum == 6:
        pass
    elif choiceNum == 8:
        pass
    elif choiceNum == 10:
        pass
        
def unavailable(priorMenu):
    DialogBox.displayText("That potion is not available. Try again.",red,
    "",yellow,"",yellow,"",yellow,False)
    priorMenu()
    
def drinkRedPotion():
    audio.potionDrink.play()
    DialogBox.displayText("You pop the cork on a red potion and",yellow,
    "gulp it down.",yellow,"",yellow,"",yellow,False)
    DialogBox.displayText("You pop the cork on a red potion and",yellow,
    "gulp it down.",yellow,"You regain 35 health!",yellow,
    "",yellow,False)
    savables.health += 35
    savables.healthPotions -= 1
    combat.monsterAttack(False) if combat.battle == True and not finalBattle.punishBattle else ""

def drinkBluePotion():
    if savables.megaPotions > 0:
        audio.potionDrink.play()
        DialogBox.displayText("You pol the cork on the blue potion and",yellow,
        "gulp it down.",yellow,"",yellow,"",yellow,False)
        DialogBox.displayText("You pop the cork on the blue potion and",yellow,
        "gulp it down.",yellow,"Your health fully recovers!",green,"",yellow,False)
        savables.health += DialogBox.maxHealth
        savables.megaPotions -= 1
        combat.monsterAttack(False) if combat.battle == True and not finalBattle.punishBattle else ""
    else:
        unavailable(potionsMenu)
    
row1 = "     Chainmail" if "chainmail" in savables.armor else "     ?"
row2 = "     Breast Plate" if "breastPlate" in savables.armor else "     ?"
row3 = "     Battle Suite" if "battleSuite" in savables.armor else "     ?"
def armorMenu():
    DialogBox.menuType = "threeChoiceMenu"
    DialogBox.displayText("Select your armor:",yellow,
    row1,green,row2,green,row3,green,True)
    selectionMenu(armorMenu)

def flee():
    pointer = pygame.image.load('pictures/cursor2.png')    
    shield = pygame.image.load('pictures/weapons/shield1.png')
    bootPrints = pygame.image.load('pictures/bootPrints.jpg')
    xAxis = 260
    xAxis2 = random.randint(775,1350)
    xAxis3 = xAxis2
    weapons.weaponAnimations = True
    time.sleep(.5)
    DialogBox.displayText("Strike the shield with [ENTER] to escape!",orange,
    "",yellow,"",yellow,"               (Press ENTER to begin)",orange,False)
    DialogBox.displayText("Strike the shield with [ENTER] to escape!",orange,
    "",yellow,"                                Go!",green,"",yellow,False)
    
    while xAxis3 > 260:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    xAxis3 = 0
                    if (xAxis+10) > (xAxis2) and (xAxis+10) < (xAxis2 + 50):
                        audio.metalGleam.play()
                        weapons.weaponAnimations = False
                        DialogBox.displayText("You sucessfully escaped!",green,
                        "",red,"",red,"",red,False)
                        combat.battleEnder()
                        combat.escape = True
                        '''
                        DialogBox.displayText("You flee down the corridor.",yellow,
                        "",yellow,"",yellow,"",yellow,False)
                        corridor1.startText()
                        '''
                    else:
                        audio.miniSwoosh.play()
                        weapons.weaponAnimations = False
                        DialogBox.displayText("You failed to escape!",orange,
                        "",yellow,"",yellow,"",yellow,False)
        gameDisplay.blit(randMonster.monsterBackground,[250,0])
        gameDisplay.blit(randMonster.defaultMonsterPic,[250,0])
        weapons.redrawBorders()
        if xAxis3 < 1:
            continue
        if savables.sprintShoes:
            xAxis += 4
            xAxis2 -= 6
        else:
            xAxis += 8
            xAxis2 -= 10
        
        xAxis3 = xAxis2
        gameDisplay.blit(bootPrints,[250,315])
        gameDisplay.blit(shield,[xAxis2,300])
        gameDisplay.blit(pointer,[xAxis,325])
        pygame.display.update()
    weapons.weaponAnimations = False

def useLeprecaller():
    import leprechaun
    line1 = "You find a nice flat section of wall and"
    line2 = "press the knocker onto it until it sticks."
    line3 = "After three taps, a magical door appears"
    line4 = "and slowly opens." 
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    leprechaunAppear = pygame.image.load('pictures/rooms/leprechaun.jpg')
    gameDisplay.blit(leprechaunAppear,[250,0])
    line1 = "What is it ya pulled me from the bath"
    line2 = "that is so important? Do ya need some"
    line3 = "pointers in how to use yer weapons or"
    line4 = "are ya just lost and need advice?" 
    DialogBox.displayText(line1,green,line2,green,line3,\
    green,line4,green,False)
    leprechaun.leprechaunOptionsComplete()

def useItem():
    DialogBox.menuType = "fourChoiceMenu"
    line1 = "Make your selection:"
    line2 = "     Drink Potion               Back"
    line3 = "     Leprecaller"
    line4 = "     Use Orb"
    DialogBox.displayText(line1,yellow,line2,green,line3,\
    green,line4,green,True)
    choiceNum = (DialogBox.selectionx*DialogBox.selectiony)
    if choiceNum == 3:
        potionsMenu()
    elif choiceNum == 4:
        useLeprecaller()
        corridor1.grandRoomOptions()
    elif choiceNum == 5:
        savables.orb()
    elif choiceNum == 6:
        pass
        