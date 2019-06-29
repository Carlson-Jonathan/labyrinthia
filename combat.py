import DialogBox,pygame,random,corridor1,randMonster,\
weapons,door,audio,savables,time,miscellaneous,finalBattle
gameDisplay = pygame.display.set_mode((900,600))
green,yellow,orange = (0,225,0),(240,240,0),(255,155,0)
monsterHealth,attackDamage,monsterBar = 20,0,200
equip,battle = "none",False
NoWeaponSelected = True
red = (255,0,0)
clock = pygame.time.Clock()
dodgeFactor = 0

def combat():
    global battle,monsterBar
    monsterBar = 200
    battle = True
    global monsterHealth,totalMhealth
    from randMonster import monsterStrength
    if monsterStrength == "weak":
        monsterHealth = random.randint(50,70)
    elif monsterStrength == "medium":
        monsterHealth = random.randint (150,250)
    elif monsterStrength == "strong":
        monsterHealth = random.randint (500,600)
    elif monsterStrength == "boss":
        monsterHealth = 1000
    totalMhealth = monsterHealth        
    fight()   
        
def combatOptions():        
    DialogBox.displayText("Your action?",yellow,
        "     Attack                       Drink Potion",green,
        "     Defend                      Change Weapon",green,
        "     Flee                           Change Armor",green,
        True)
    combatOptionSelection("newRound")

# defines which menu will apply to the selections choice
def combatOptionSelection(optionType):
    global equip,NoWeaponSelected
    choiceNum = (DialogBox.selectionx*DialogBox.selectiony)
    if choiceNum == 3:
        if NoWeaponSelected == True:
            weaponSelect() 
        elif optionType == "selectWeapon":
            equip = "fists"
            weapons.skillBar = 0
            combatOptions()
        elif optionType == "newRound":
            attack(equip)
    elif choiceNum == 4:
        if optionType == "newRound":
            monsterAttack(True) if not finalBattle.punishBattle else finalBattle.defendPunish()
        elif optionType == "selectWeapon":
            if "sword" in savables.weaponInventory:
                weapons.skillBar = savables.swordTick
                equip = "sword"
                audio.drawSword.play()
            else:
                DialogBox.displayText("That weapon is not available.",red,
                    "",yellow,"",yellow,"",yellow,False)
                weaponSelect()
            combatOptions()
    elif choiceNum == 5:
        if optionType == "newRound":
            miscellaneous.flee() if not finalBattle.punishBattle else finalBattle.fleePunish()
            monsterAttack(False)
        elif optionType == "selectWeapon":
            if "staff" in savables.weaponInventory:
                weapons.skillBar = savables.staffTick
                equip = "staff"
                weapons.swooshCombo(3)
            else:
                DialogBox.displayText("That weapon is not available.",red,
                    "",yellow,"",yellow,"",yellow,False)
                weaponSelect()
            combatOptions()
    elif choiceNum == 6:
        if optionType == "newRound":
            miscellaneous.potionsMenu()
            combatOptions()
        elif optionType == "selectWeapon":
            if "fire" in savables.weaponInventory:
                weapons.skillBar = savables.fireTick
                equip = "fire"
                audio.inferno.play()
            else:
                DialogBox.displayText("That weapon is not available.",red,
                    "",yellow,"",yellow,"",yellow,False)
                weaponSelect()
            combatOptions()
    elif choiceNum == 8:
        if optionType == "newRound":
            weaponSelect()
        elif optionType == "selectWeapon":
            if "ice" in savables.weaponInventory:
                weapons.skillBar = savables.iceTick
                audio.iceWind.play()
                equip = "ice"
            else:
                DialogBox.displayText("That weapon is not available.",red,
                    "",yellow,"",yellow,"",yellow,False)
                weaponSelect()
            combatOptions()
    elif choiceNum == 10:
        if optionType == "newRound":
            miscellaneous.armorMenu()
            combatOptions()
        elif optionType == "selectWeapon":
            if "gun" in savables.weaponInventory:
                weapons.skillBar = 0
                audio.gunLoad.play()
                equip = "gun"
            else:
                DialogBox.displayText("That weapon is not available.",red,
                    "",yellow,"",yellow,"",yellow,False)
                weaponSelect()
            combatOptions()

def attack(weapon):
    global monsterHealth,attackDamage,monsterBar
    armorModifiers()
    weapons.staff() if weapon == "staff" else ""
    weapons.fists() if weapon == "fists" else ""
    weapons.sword() if weapon == "sword" else ""
    weapons.fire() if weapon == "fire" else ""
    weapons.ice() if weapon == "ice" else ""
    weapons.deadMiniGun() if weapon == "gun" else ""
    weapons.weaponAnimations = False if finalBattle.punishBattle else ""
    monsterBar = (((monsterHealth*100)/totalMhealth)*2)
    monsterAttack(False) if not finalBattle.punishBattle else finalBattle.leprechaunTaunt() 

escape = False
deepFreeze = 0
def monsterAttack(defend):
    from randMonster import monsterStrength
    global battle,monsterHealth,regeneration,regenH,equip,deepFreeze
    if monsterHealth <= 0 or escape:
        battleEnder()
    else:
        par = random.randint(1,3)
        if monsterStrength == "weak":
            monsterDamage = random.randint(5,15)
        elif monsterStrength == "medium":
            monsterDamage = random.randint(15,25)
        elif monsterStrength == "strong":
            monsterDamage = random.randint(25,50)
        monsterDamage = int(monsterDamage*reductionFactor)
        monsterDamage = (monsterDamage/2) if defend == True else monsterDamage
        additionalRoar()
        if deepFreeze > 0:
            deepFreeze -= 1
            if deepFreeze == 0:
                DialogBox.displayText("The %s thaws!"%randMonster.monster,yellow,"",yellow,
                "",yellow,"",yellow,False)
                gameDisplay.blit(randMonster.defaultMonsterPic,[250,0])
                randMonster.monsterPic = randMonster.defaultMonsterPic
            else:
                DialogBox.displayText("The %s is frozen"%randMonster.monster,yellow,
                "and cannot move!",yellow,"",yellow,"",yellow,False)
        elif equip == "sword" and par == 3 and savables.swordSkill >= 1:
            weapons.parry()
            rip = random.randint(1,3)
            if rip > 1 and savables.swordSkill >= 2:
                weapons.riposte()
            if weapons.bleed > 0:
                bleedDamage()
        elif miscellaneous.equippedArmor == "battleSuite" and dodgeFactor <= 10:
            weapons.weaponAnimations = True
            audio.monsterAttackSound.play()
            DialogBox.displayText("The %s attacks!"%randMonster.monster,yellow,
            "",green,"",yellow,"",green,False)
            time.sleep(.3)
            DialogBox.displayText("The %s attacks!"%randMonster.monster,yellow,
            "          You quickly dodge the attack!",green,"",yellow,"",green,False)
            weapons.weaponAnimations = False
            DialogBox.displayText("The %s attacks!"%randMonster.monster,yellow,
            "          You quickly dodge the attack!",green,"",yellow,"",green,False)
            time.sleep(.3)
            if weapons.bleed > 0:
                bleedDamage()
        else:
            weapons.weaponAnimations = True
            if miscellaneous.equippedArmor == "chainmail":
                savables.chainmailTick -= 2 
            elif miscellaneous.equippedArmor == "breastPlate":
                savables.breastPlateTick -= 2 
            elif miscellaneous.equippedArmor == "battleSuite":
                savables.breastPlateTick -= 2 
            audio.monsterAttackSound.play() 
            DialogBox.displayText("The %s attacks!"%randMonster.monster,yellow,
                "",orange,"",yellow,"",yellow,False)
            time.sleep(.3)#add sleep delays in randMonster to sync attack sound and shake
            takeDamageAnimation()
            weapons.weaponAnimations = False
            savables.health -= monsterDamage
            DialogBox.displayText("The %s attacks!"%randMonster.monster,yellow,
                "You take %d damage!"%monsterDamage,orange,"",yellow,"",yellow,False)
            time.sleep(.3)
            if weapons.bleed > 0:
                bleedDamage()
        whitePotion()
        defend = False
        
def bleedDamage():  
    global monsterHealth,monsterBar  
    weapons.weaponAnimations = True
    DialogBox.displayText("The %s bleeds from"%randMonster.monster,yellow,
    "its wounds!",yellow,"",yellow,"",yellow,False)
    weapons.bleed -= 3
    monsterHealth -= weapons.bleed
    audio.bleed.play()
    time.sleep(.3)
    audio.bleed.play()
    monsterBar = (((monsterHealth*100)/totalMhealth)*2)
    weapons.monsterTakeDamage()
    weapons.weaponAnimations = False
    DialogBox.displayText("The %s bleeds from"%randMonster.monster,yellow,
    "its wounds!",yellow,"The %s takes %d damage!"%(randMonster.monster,weapons.bleed),
    orange,"",yellow,False)
    time.sleep(.3)
    if monsterHealth <= 0:
        battleEnder()
    weapons.bleed = 0 if weapons.bleed < 4 else weapons.bleed 
    
def takeDamageAnimation():
    shakes,x,y = 0,250,0
    monsterLair = randMonster.monsterBackground
    monsterPic = randMonster.monsterPic        
    def compress():
        gameDisplay.blit(monsterLair,[x,y])
        weapons.redrawBorders()
        gameDisplay.blit(monsterPic,(250,0))
        pygame.display.update()
    while shakes < 6:
        clock.tick(50)
        x -= 5
        y -= 5   
        compress()
        x += 10
        y += 10
        compress()
        x -= 10
        compress()
        x += 10
        y -= 10
        compress()
        x -= 5
        y += 5
        compress()
        shakes += 1

roarRepitition = 1
def additionalRoar():
    global roarRepitition
    if roarRepitition%5 == 0:
        audio.monsterRoar.play()
    roarRepitition += 1
            
def weaponSelect():
    global NoWeaponSelected,equip

    fistFire = ("     Fists                          Fire")
    swordIce = ("     Sword                        Ice")
    staffGun = ("     Staff                         Mini Gun")
    fistOnly = ("     Fists                          ?")
    swordOnly = ("     Sword                        ?")
    staffOnly = ("     Staff                         ?")
    iceOnly = ("     ?                                Ice")
    gunOnly = ("     ?                                Mini Gun")
    noneRow2 = ("     ?                                ?")
    noneRow3 = ("     ?                                ?")
    
    # options row 1    
    if "fire" in savables.weaponInventory:
        row1 = fistFire
    else:
        row1 = fistOnly
    # options row 2
    if "sword" in savables.weaponInventory and "ice" in savables.weaponInventory:
        row2 = swordIce
    elif "sword" in savables.weaponInventory and "ice" not in savables.weaponInventory:
        row2 = swordOnly
    elif "sword" not in savables.weaponInventory and "ice" in savables.weaponInventory:
        row2 = iceOnly
    else:
        row2 = noneRow2
    # options row 3
    if "staff" in savables.weaponInventory and "gun" in savables.weaponInventory:
        row3 = staffGun
    elif "staff" in savables.weaponInventory and "gun" not in savables.weaponInventory:
        row3 = staffOnly
    elif "staff" not in savables.weaponInventory and "gun" in savables.weaponInventory:
        row3 = gunOnly
    else:
        row3 = noneRow3
        
    DialogBox.displayText("Select your weapon:",yellow,row1,orange,row2,orange,row3,orange,True)
    NoWeaponSelected = False      
    combatOptionSelection("selectWeapon")   

dispDamage = "0"
def damageDisplay():
    fistDamage = "4 - 12"
    swordDamage = "%d - %d"%(savables.swordMin,savables.swordMax)
    staffDamage = "%d - %d"%(savables.staffMin,savables.staffMax)
    fireDamage = "%d - %d"%(savables.fireMin,savables.fireMax)
    iceDamage = "%d - %d"%(savables.iceMin,savables.iceMax)
    gunDamage = "???"    
    global dispDamage
    if equip == "fists":
        dispDamage = fistDamage
    elif equip == "sword":
        dispDamage = swordDamage
    elif equip == "staff":
        dispDamage = staffDamage
    elif equip == "fire":
        dispDamage = fireDamage
    elif equip == "ice":
        dispDamage = iceDamage
    elif equip == "gun":
        dispDamage = gunDamage    

regeneration = False
regenH = 0
def whitePotion():
    global regeneration,regenH,weaponAnimations
    if regeneration == True and regenH <= 100:
        regen = random.randint(5,10)
        regenH += regen
        weaponAnimations = True
        DialogBox.displayText("You feel the healing effects of the",yellow,
        "regeneration potion.",yellow,"",yellow,"",yellow,False)
        DialogBox.displayText("You feel the healing effects of the",yellow,
        "regeneration potion.",yellow,"You regain %d health!"%regen,green,"",yellow,False)
        weaponAnimations = True
        DialogBox.displayText("You feel the healing effects of the",yellow,
        "regeneration potion.",yellow,"You regain %d health!"%regen,green,"",yellow,False)
        savables.health += regen
    elif (regeneration == True and regenH >= 100):
        DialogBox.displayText("The effects of the regeneration potion",yellow,
        "have worn off.",yellow,"",yellow,"",yellow,False)
        regeneration,regenH = False,0
    else:
        regeneration,regenH = False,0

reductionFactor = 1
damageReducer = 1
damageEnhancer = 1
def armorModifiers():
    global damageReducer,reductionFactor,dodgeFactor
    reductionFactor = 1
    damageReducer = 1
    dodgeFactor = 0
    if miscellaneous.equippedArmor == "chainmail":
        if savables.chainmailSkill == 0:
            reductionFactor = .80 
        elif savables.chainmailSkill == 1:
            reductionFactor = .75 
        elif savables.chainmailSkill == 2:
            reductionFactor = .70 
        elif savables.chainmailSkill == 3:
            reductionFactor = .65 
    elif miscellaneous.equippedArmor == "breastPlate":
        damageReducer = .66    
        if savables.breastPlateSkill == 0:
            reductionFactor = .65 
        elif savables.breastPlateSkill == 1:    
            reductionFactor = .55 
        elif savables.breastPlateSkill == 2:    
            reductionFactor = .45 
        elif savables.breastPlateSkill == 3:
            reductionFactor = .35 
    elif miscellaneous.equippedArmor == "battleSuite":
        if savables.battleSuiteSkill == 0:
            dodgeFactor = random.randint(1,50) 
        elif savables.battleSuiteSkill == 1:
            dodgeFactor = random.randint(1,40) 
        elif savables.battleSuiteSkill == 2:
            dodgeFactor = random.randint(1,25) 
        elif savables.battleSuiteSkill == 3:
            dodgeFactor = random.randint(1,20) 
    reductionFactor -= float(weapons.monsterAttackBreak)

victory = False
def battleEnder():
    global battle,regeneration,regenH,damageEnhancer,deepFreeze,escape,victory
    gameDisplay.blit(randMonster.monsterBackground,[250,0])
    if monsterHealth <= 0:
        DialogBox.displayText("The %s drops to the"%randMonster.monster,yellow,
        "ground writhing and squealing!",yellow,"You are victorious!",yellow,
        "",yellow,False)  
        victory = True    
    else:
        victory = False
    battle = False
    regeneration,regenH = False,0
    weapons.bleed = 0
    damageEnhancer = 1
    deepFreeze = 0
    weapons.monsterAttackBreak = 0
    escape = False
    audio.pygame.mixer.music.fadeout(3000)
    
def fight():
    while battle == True:
        clock.tick(35)
        combatOptions()
        