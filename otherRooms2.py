import pygame,DialogBox,audio,combat,savables,random,randMonster,time,corridor1,weapons
gameDisplay = pygame.display.set_mode((900,600))
yellow,green,orange,red = (240,240,0),(0,255,0),(255,155,0),(255,0,0)
from pygame.locals import *
'''
Module Contents:
    Fossil
    Hillary
    flood potions
    spider cave / chainmail
    Increase dungeon level door
    safe - sprint shoes
'''    

def selectionResults(priorMenu):
    choiceNum = (DialogBox.selectionx*DialogBox.selectiony)
    if choiceNum == 3:
        levelDoorFeel() if priorMenu == levelDoorOptions else ""
        pullLever() if priorMenu == yes else ""
        getRedPotions() if priorMenu == floodRun else ""
        safe2() if priorMenu == safeOptions else ""
    elif choiceNum == 4:
        kickDoor() if priorMenu == levelDoorOptions else ""
        getWhitePotion() if priorMenu == floodRun else ""
    elif choiceNum == 5:
        levelDoorLeave() if priorMenu == levelDoorOptions else ""
        drown() if priorMenu == floodRun else ""
    elif choiceNum == 6:
        pass
    elif choiceNum == 8:
        pass
    elif choiceNum == 10:
        pass
    
darkFossil = pygame.image.load('pictures/rooms/fossilDark.jpg')
lightFossil = pygame.image.load('pictures/rooms/fossil.jpg')
matches = pygame.image.load('pictures/items/matches.png')
def fossil():
    gameDisplay.blit(darkFossil,[250,0])
    DialogBox.displayText("You continue on your way down the tunnel",yellow,
    "then see something inscribed on the wall.",yellow,
    "You feel that this is important somehow.",yellow,
    "Unfortunately you cant tell what it is.",yellow,False)
    DialogBox.displayText("You run your hand over it trying to guess",yellow,
    "what is could be. Writing? A picture?",yellow,
    "It is too dark and hard to make out.",yellow,
    "You pull out a match and light it.",yellow,False)
    audio.match.play()    
    gameDisplay.blit(lightFossil,[250,0])
    DialogBox.displayText("WOW! That is incredible! You had no",yellow,
    "idea! This is too good to be true!",yellow,
    "If only you knew about this before",yellow,
    "It could have been a total game changer!",yellow,False)
    gameDisplay.blit(matches,[460,90])
    DialogBox.displayText("This whole time, you had matches?! You",yellow,
    "could have been lighting things on fire!",yellow,
    "",yellow,
    "Oh, and there is a fossil on the wall. Neat.",yellow,False)
    DialogBox.displayText("Hey the the fire ring on your finger",yellow,
    "is drawing the flame to it. You move it",yellow,
    "closer and the fire from the match gets",yellow,
    "completely sucked up by the ring.",yellow,False)
    gameDisplay.blit(darkFossil,[250,0])
    audio.getItem1.play()
    audio.getItem2.play()
    DialogBox.displayText("                         New Boost:",yellow,
    "                     Fire + 15 damage",green,
    "                       Now available!",yellow,"",yellow,False)
    savables.fireMax += 15
    audio.match.play()
    gameDisplay.blit(lightFossil,[250,0])
    DialogBox.displayText("You light another match hoping to get",yellow,
    "the same effect. Nope, the ring's thirst",yellow,
    "appears to have been quenched. Time to",yellow,
    "move on. You continue down the corridor.",yellow,False)
    
HillaryPic = pygame.image.load('pictures/rooms/hillary.jpg')    
def Hillary():
    audio.doorSound.play()
    DialogBox.displayText("An ominous chant can be heard on the",yellow,
    "other side of this door...",yellow,"",yellow,"",yellow,False)
    gameDisplay.blit(HillaryPic,[250,0])
    audio.hillaryLaugh.play()
    DialogBox.displayText("Hmm, it looks like this room is occupied",yellow,
    "by somone communing with Satan. You",yellow,
    "decide not to interrupt and leave the",yellow,
    "she-deamon to her human sacrificing.",yellow,False)
    
# Flood potions #################
def flood():
    DialogBox.displayText("You come to a level on the wall. It appears",yellow,
    "to be in netrual position and can be moved",yellow,
    "up or down. Will you pull it?",yellow,"",yellow,False)
    leverOptions()
    
def leverOptions():
    DialogBox.menuType = "threeChoiceMenu"
    DialogBox.displayText("What will you do?",yellow,
    "     Pull down",green,
    "     Pull up",green,
    "     Leave it alone",green,True)
    
def leverSelection():
    DialogBox.displayText("The lever moves with a rusty 'twang'. You",yellow,
    "see two pannels open at both ends of the",yellow,
    "tunnel. In one there is an empty white",yellow,
    "potion bottle. The other has 5 red potions.",yellow,False)
    DialogBox.displayText("A hatch opens above you and water begins,",yellow,
    "pouring into the tunnel. Soon it will be",yellow,
    "flooded and you must run one way or the",yellow,
    "other or you will drown.",yellow,False)
    floodRun()
   
def floodRun():
    DialogBox.displayText("Which potions way will you run for?",yellow,
    "     White potion",green,
    "     Red potions",green,
    "     Stay and drown",green,True)
    selectionResults(floodRun)
    
def getRedPotions():
    DialogBox.displayText("You bolt toward the pannel containing the",yellow,
    "red potions hoping that they are the same",yellow,
    "flavor as the others you have already",yellow,
    "drank. This should keep you stocked up.",yellow,False)
    savables.healthPotions += 5
    
def getWhitePotion():
    DialogBox.displayText("Even though it is an empty bottle you",yellow,
    "see a long-term advantage in having it.",yellow,
    "You rush for the white potion bottle and",yellow,
    "escape the imminent flood.",yellow,False)
    savables.regenPotions += 1
    
def drown():
    DialogBox.displayText("Uh, no. If you are not going to pick,",yellow,
    "then I will pick for you...",yellow,"",yellow,"",yellow,False)
    roll = random.randint(1,2)
    getRedPotions() if roll == 1 else getWhitePotion()
    
###########################
Frodo = pygame.image.load('pictures/rooms/Frodo.jpg')
chainmail = pygame.image.load('pictures/items/chainmail.png')
spiderLair = pygame.image.load("pictures/rooms/spiderWeb.jpg")
def spiderCave():
    DialogBox.displayText("Stickly little spider webs keep getting",yellow,
    "stuck in your eyes the farther down this",yellow,
    "corridor you travel. They dont taste",yellow,
    "wonderful etiher.",yellow,False)
    gameDisplay.blit(spiderLair,[250,0])
    DialogBox.displayText("Well now, it looks like something big made",yellow,
    "that. Big and probably very hungry. There",yellow,
    "is no sense in being an arachnaphob if this",yellow,
    "is the way out. Whats a few little spiders?",yellow,False)
    DialogBox.displayText("At least that is what you think until you",yellow,
    "feel a long hairy leg stroke the back of",yellow,
    "your neck...",yellow,"",yellow,False)
    randMonster.randMonster("weak",2)
    if combat.victory == True:
        DialogBox.displayText("You didnt really think yo were going to get",yellow,
        "out of this that easily did you? There are",yellow,
        "more to kill!",yellow,"",yellow,False)
        if combat.victory == True:
            randMonster.randMonster("weak",2)
            DialogBox.displayText("One more to go!",yellow,"",yellow,
            "",yellow,"",yellow,False)
            randMonster.randMonster("weak",2)
            gameDisplay.blit(Frodo,[250,0])
            DialogBox.displayText("After clearing the spider's lair a corpse",yellow,
            "of a short hairy person with giagantic feet",yellow,
            "falls from a web on the ceiling. On the",yellow,
            "corspe is a very nice suite of chainmail!",yellow,False)
            gameDisplay.blit(chainmail,[425,30])
            DialogBox.displayText("Well, it's not good to him now. Better",yellow,
            "you take it that let it go to waste.",yellow,"",yellow,"",yellow,
            False)
            audio.getItem1.play()
            audio.getItem2.play()
            DialogBox.displayText("                         New Armor:",yellow,
            "                           Chainmail",green,
            "                       Now Available!",yellow,"",yellow,False)
            savables.armor.append("chainmail")
    else:
        corridor1.randCorridor()
    
# Advance to next section of dungeon
levelDoorPic = pygame.image.load('pictures/rooms/levelDoor.jpg')
def levelDoor():
    gameDisplay.blit(levelDoorPic,[250,0])
    DialogBox.displayText("You come to a door alot like the other",yellow,
    "ones you have seen. Beside it is a sign",yellow,
    "with markings that are mostly rubbed off",yellow,
    "and unreadable. You are able to make out...",yellow,False)
    DialogBox.displayText("'...will remain sealed...'",green,
    "'...price that must be paid...'",green,
    "'...reach into the darkness...'",green,
    "'...to drink a gross in drops of blood...'",green,False)
    DialogBox.displayText("Surely these are instructions about how",yellow,
    "to open this door. You dont see anything",yellow,
    "in the hole. Perhaps there is some kind,",yellow,
    "of button or switch inside that opens it.",yellow,False)
    levelDoorOptions()
    
def levelDoorOptions():    
    DialogBox.displayText("What will you do?",yellow,
    "     Feel in hole",green,
    "     Kick door in",green,
    "     Leave",green,True)
    selectionResults(levelDoorOptions)
    
def levelDoorFeel():
    DialogBox.displayText("You reach into the hole hoping to find",yellow,
    "whatever mechanism is keeping this door",yellow,
    "sealed. The hole is deep and you extend",yellow,
    "your whole arm in not feeling an end.",yellow,False)
    DialogBox.displayText("A cold metal cuff abruptly grabs you by",yellow,
    "the wrist. You feel metal rods stab into",yellow,
    "your arm and begin to siphon your blood.",yellow,
    "The pain is almost unbearable!",yellow,False)
    audio.bleed.play()
    savables.health -= 36
    DialogBox.displayText("     36 damage!",orange,
    "",orange,
    "",orange,
    "",orange,False)
    audio.bleed.play()
    savables.health -= 36
    DialogBox.displayText("     36 damage!",orange,
    "          36 damage!",orange,
    "",orange,
    "",orange,False)
    audio.bleed.play()
    savables.health -= 36
    DialogBox.displayText("     36 damage!",orange,
    "          36 damage!",orange,
    "               36 damage!",orange,
    "",orange,False)
    audio.bleed.play()
    savables.health -= 36
    DialogBox.displayText("     36 damage!",orange,
    "          36 damage!",orange,
    "               36 damage!",orange,
    "                    36 damage!",orange,False)
    levelDoorResults()
    
lever = pygame.image.load('pictures/rooms/lever.jpg')
def levelDoorResults():
    if savables.health <= 0:
        DialogBox.displayText("You are dead.",yellow,
        "",yellow,"",yellow,"",yellow,False)
    else:
        DialogBox.displayText("You feel very faint. That healthtank",yellow,
        "you picked up saved your life! You arm",yellow,
        "is released from the cuff in the hole",yellow,
        "and you fall to the ground.",yellow,False)
        audio.doorSound.play()
        DialogBox.displayText("The door creeks open...",yellow,
        "",yellow,"",yellow,"",yellow,False)
        gameDisplay.blit(lever,[250,0])
        DialogBox.displayText("This room is enclosed with nothing",yellow,
        "more than a large lever in the middle of it.",yellow,
        "There dosent seem to be anything else",yellow,
        "to do in here. Will you pull it?",yellow,False)
        yes()
        
def yes():
    DialogBox.displayText("What will you do?",yellow,
    "     Pull lever",green,"",yellow,"",yellow,True)
    selectionResults(yes)
        
def pullLever():
    DialogBox.displayText("There are so many choices here you had",yellow,
    "to think long and hard about which one",yellow,
    "you would do. Finally, you decided it would",yellow,
    "be best just to go ahead and pull the lever.",yellow,False)
    DialogBox.displayText("The walls begin to groan and you hear stone",yellow,
    "grinding against stone both near and far",yellow,
    "away. Other sounds like growls and hissing",yellow,
    "can be heard. Something is different...",yellow,False)
    DialogBox.displayText("Well, nothing left to do here. You head",yellow,
    "back out the way you came in.",yellow,"",yellow,"",yellow,False)
    savables.dungeonSection = 2
    corridor1.corridorFork()
    
kick = pygame.mixer.Sound('Audio/monsters/elementalAttack.ogg')
def kickDoor():
    kick.play()
    time.sleep(.5)
    kick.play()
    time.sleep(.5)
    kick.play()
    DialogBox.displayText("You start doing your best Bruce Lee",yellow,
    "impressions and begin awkwardly kicking at",yellow,
    "the door. Several loud thumps echo down",yellow,
    "the corridor. You then hear a roar...",yellow,False)
    randMonster.randMonster("weak","random")
    gameDisplay.blit(levelDoorPic,[250,0])
    DialogBox.displayText("Well that was fun! Now we are back",yellow,
    "to where we started.",yellow,"",yellow,"",yellow,False)
    levelDoorOptions()
    
def levelDoorLeave():
    DialogBox.displayText("Well, nothing left to do here. You head",yellow,
    "back out the way you came in.",yellow,"",yellow,"",yellow,False)
    corridor1.corridorFork()

safeTunnel = pygame.image.load('pictures/rooms/safeTunnel.jpg')   
safeDialPic = pygame.image.load('pictures/rooms/safeDial.jpg')
def safe():
    gameDisplay.blit(safeTunnel,[250,0])
    DialogBox.displayText("There is a safe randomly sitting in the",yellow,
    "middle of the tunnel. How did it get there?",yellow,
    "And what could be in it???",yellow,"",yellow,False)
    gameDisplay.blit(safeDialPic,[325,63])    
    DialogBox.displayText("This is one of the Department of Homeland",yellow,
    "Security's finest lockdown protective",yellow,
    "devices, the Acme 1-digit combo safe! Do",yellow,
    "you want to see if you can get it open?",yellow,False)
    safeOptions()
    
def safeOptions():
    DialogBox.displayText("Try to open it?",yellow,
    "     Of course!",green,
    "     No. Leave.",green,"",yellow,True)
    selectionResults(safeOptions)
    
def safe2():
    DialogBox.displayText("Great! I knew you couldnt resist a",yellow,
    "challange! This should be easy enough. All",yellow,
    "you need to do is guess every number,",yellow,"right?",yellow,False)
    safeDial()
    
def safeDial():
    DialogBox.displayText("What number would you like to guess?",yellow,
    "",yellow,"",yellow,"",yellow,False)
    comboGuess = safeGuess()
    DialogBox.displayText("You set the dial to %d and turn the handle."%comboGuess,yellow,
    "",yellow,"",yellow,"",yellow,False)
    if comboGuess != 30:
        DialogBox.displayText("Arrows suddenly shoot from unseen",yellow,
        "nitches in the walls and stab you!",yellow,
        "You take %d damage!"%comboGuess,orange,
        "That wasnt the right number. Try again?",yellow,False)
        savables.health -= comboGuess
        safeOptions()
    else:
        rightNumber()
    
def wrongNumber():
    DialogBox.displayText("Arrows suddenly shoot from unseen nitches",yellow,
    "in the walls and stab you!",yellow,
    "You take %d damage!"%comboGuess,orange,
    "That wasnt the right number. Try again?",yellow,False)
    safeOptions()

sprintShoes = pygame.image.load('pictures/items/wingBoots.png')    
def rightNumber():
    DialogBox.displayText("You hear a *click* as you turn the wheel",yellow,
    "and the safe door slowly opens...",yellow,"",yellow,"",yellow,False)
    gameDisplay.blit(sprintShoes,[400,40])
    DialogBox.displayText("Inside are the coolest pair of shoes you",yellow,
    "have ever seen! They are a perfect fit!",yellow,
    "They also allow you to run faster. It ",yellow,
    "should be easier to flee from monsters!",yellow,False)
    audio.getItem1.play()
    audio.getItem2.play()
    DialogBox.displayText("                         New Boost:",yellow,
    "                        Sprint Shoes",green,
    "                       Now Available!",yellow,"",yellow,False)
    savables.sprintShoes = True

def safeGuess():
    currentNumber = 0
    guessing = True
    clock = pygame.time.Clock()
    weapons.weaponAnimations = True
    while guessing:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    audio.selectTick.play()
                    guessing = False
                if event.key == pygame.K_UP:
                    currentNumber += 1
                    audio.arrowTick.play()
                    currentNumber = 0 if currentNumber > 99 else currentNumber
                if event.key == pygame.K_LEFT:
                    audio.arrowTick.play()
                    if currentNumber < 10: 
                        currentNumber += 90 
                    else: 
                        currentNumber -= 10
                if event.key == pygame.K_RIGHT:
                    if currentNumber >= 90: 
                        currentNumber -= 90 
                    else: 
                        currentNumber += 10
                    audio.arrowTick.play()
                if event.key == pygame.K_DOWN:
                    currentNumber -= 1
                    audio.arrowTick.play()
                    currentNumber = 99 if currentNumber < 0 else currentNumber
        DialogBox.displayText("",yellow,"                                %d"%currentNumber,green,
        "",yellow,"",yellow,False)
        pygame.display.update()
    weapons.weaponAnimations = False
    return currentNumber
                
    
    
    
    