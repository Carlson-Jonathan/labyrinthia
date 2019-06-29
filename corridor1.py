import random,DialogBox,pygame,randMonster,combat,\
door,grate,yell,audio,savables,weapons,miscellaneous,\
otherRooms2,corridor2,otherRooms3
green,yellow = (0,225,0),(240,240,0)
gameDisplay = pygame.display.set_mode((900,600))
orange = (255,155,0)
red = (255,0,0)
healthPotion = pygame.image.load('pictures/items/health_potion.png')
grandRoomPic = pygame.image.load('pictures/rooms/grandRoom.jpg')

'''
Module Contents:
    Bats, ice bridge, 
    dragon encounter, 
    snake event
    regeneration pool, 
    grate to sewer, 
    hallway potion
'''

# User selection interpreter function
def travelOptions(travelType):
    choiceNum = (DialogBox.selectionx*DialogBox.selectiony)
    if choiceNum == 3:
        corridorFork() if travelType == emptySnakePit else ""
        crossIceBridge() if travelType == iceBridge else ""
        dragonSneak() if travelType == dragon else ""
        poolDrink() if travelType == pool else ""
        door.door() if travelType == start or travelType == grandRoomOptions else ""
        otherRooms2.levelDoor() if travelType == fork else ""
        batActionSneak() if travelType == bats else ""
        snakePitJump() if travelType == snakePitOptions else ""
        iceAnswerIncorrect() if travelType == iceQuestionAnswers1 or travelType == iceQuestionAnswers2 or travelType == iceQuestionAnswers3 else ""
    elif choiceNum == 4:
        random.choice([fallInPit,snakePitJump])() if travelType == emptySnakePit else "" 
        randCorridor() if travelType == grandRoomOptions else ""
        rockPool() if travelType == pool else ""
        iceLookDown() if travelType == iceBridge else ""
        corridor2.ladder() if travelType == start and savables.dungeonSection == 1 else ""
        iceAnswerIncorrect() if travelType == iceQuestionAnswers2 or travelType == iceQuestionAnswers3 else ""
        iceAnswerCorrect(1) if travelType == iceQuestionAnswers1 else ""
        snakePit() if travelType == fork else ""
        grate.grate() if travelType == tunnelGrateOptions else ""
        batActionRun() if travelType == bats else "" 
        snakePitTurn() if travelType == snakePitOptions else ""
    elif choiceNum == 5:
        yell.yell() if travelType == grandRoomOptions else ""
        randCorridor() if travelType == start else ""
        poolLeave() if travelType == pool else ""
        iceLeave() if  travelType == iceBridge else ""
        iceDoorOpen() if travelType == iceQuestionAnswers3 else ""
        iceAnswerIncorrect() if travelType == iceQuestionAnswers1 or travelType == iceQuestionAnswers2 else ""
        batActionNoise() if travelType == bats else ""
        if travelType == snakePitOptions:
            snakePitPlay() if savables.snakePlaytime == False else snakePitPlay2() 
        yell.yell() if travelType == tunnelGrateOptions or travelType == fork else ""
    elif choiceNum == 6:
        if travelType == grandRoomOptions:
            miscellaneous.useItem()
            grandRoomOptions() 
        refillBottle() if travelType == pool else ""
        iceAnswerCorrect(2) if travelType == iceQuestionAnswers2 else ""
        iceAnswerIncorrect() if travelType == iceQuestionAnswers1 or travelType == iceQuestionAnswers3 else "" 
        yell.yell() if travelType == start else ""
    elif choiceNum == 8:
        notCute() if travelType == iceQuestionAnswers3 else ""
        iceAnswerIncorrect() if travelType == iceQuestionAnswers1 or travelType == iceQuestionAnswers2 or travelType == iceQuestionAnswers3 else ""
        randMonster.randMonster("strong",4) if travelType == start else "" 
        #if travelType in threeChoiceMenu or travelType in fourChoiceMenu:
            #invalid()
            #travelType()
    elif choiceNum == 10:
        iceAnswerIncorrect() if travelType == iceQuestionAnswers1 or travelType == iceQuestionAnswers2 or travelType == iceQuestionAnswers3 else ""
        if travelType == start:
            miscellaneous.potionsMenu()
            start() 
        #elif travelType in threeChoiceMenu or travelType in fourChoiceMenu or travelType in fiveChoiceMenu:
            #invalid()
            #travelType()

randomTunnel = pygame.image.load('pictures/rooms/anotherTunnel.jpg')
def randCorridor():
    gameDisplay.blit(randomTunnel,[250,0])
    DialogBox.displayText("You head down the nearest corridor",yellow,
    "you see hoping that it will lead you",yellow,
    "to something useful.",yellow,"",yellow,False)
    random.choice(randomCorridor)()
    
def monsterEncounter():
    DialogBox.displayText("A monster jumps out of the darkness and",yellow,
    "attacks you!",yellow,"",yellow,"",yellow,False)
    if savables.dungeonSection == 3:
        monsterStrength = "medium"
    else:
        monsterStrength = (random.choice(["weak","medium"]))\
            if savables.dungeonSection == 2 else "weak"
    randMonster.randMonster(monsterStrength,"random")
          
corridor1 = pygame.image.load('pictures/rooms/tunnel1.jpg')
def startText():
    gameDisplay.blit(corridor1,(250,0))
    DialogBox.displayText("You see a long corridor in front of you.",yellow,
        "There is a door on the left wall and a",yellow,
        "ladder going up on the right wall behind",yellow,
        "you. What would you like to do?",yellow,False)
    start()
    
def start():
    DialogBox.displayText("What will you do? Make your selection:",yellow,
        "     Open the door           Yell for help",green,
        "     Climb the ladder        Monster",green,
        "     Go down corridor       Drink a Potion",green,True)
    travelOptions(start)    

'''
def invalid():
    DialogBox.displayText("Invalid selection. Try again.",red,
        "",yellow,"",yellow,"",yellow,False)
'''
        
def corridorFork():
    fork1 = pygame.image.load('pictures/rooms/tunnelFork.jpg')
    gameDisplay.blit(fork1,[250,0])
    DialogBox.displayText("The tunnel comes to a fork. To the",yellow,
    "left you can feel a warm breeze and see",yellow,
    "a faint light. The right tunnel looks",yellow,
    "dark and emits and strange odor.",yellow,False)
    fork()

def fork():
    DialogBox.menuType = "threeChoiceMenu"
    DialogBox.displayText("What will you do?",yellow,
    "     Go left",green,
    "     Go right",green,
    "     Yell for help",green,True)
    travelOptions(fork)    

def dragonEnding():
    lightTunnel = pygame.image.load('pictures/rooms/lighttunnel.jpg')
    gameDisplay.blit(lightTunnel,[250,0])
    DialogBox.displayText("The light grows brighter and the air",yellow,
        "gets warmer the farther down the cooridor",yellow,
        "you get. Something just dosen't feel right.",yellow,"",yellow,False)
    dragon1 = pygame.image.load('pictures/rooms/sleepingdragon.jpg')
    gameDisplay.blit(dragon1,[250,0])
    DialogBox.displayText("You found the way out! But there is a",yellow,
        "sleeping dragon blocking the exit. If you",yellow,
        "are extremely careful, you might be able",yellow,
        "to sneak past it. It looks very risky!",yellow,False)
    dragon()

def hallwayPotion():
    gameDisplay.blit(healthPotion,[440,80])    
    DialogBox.displayText("                       *Ooof!*",orange,
    "You trip over something and fall.",yellow,
    "Whats this? It seems you have tripped",yellow,
    "over a magic potion!",yellow,False)
    savables.healthPotions += 1
    DialogBox.displayText("Since there is nowhere else to go",yellow,
    "you continue walking down the corridor.",yellow,"",yellow,""
    ,yellow,False)
    grandRoom()
    
# --------------- Bats Events ----------------
def batActionRun():
    roll = random.randint(1,2)
    DialogBox.displayText("You dash forward hoping to pass",yellow,
        "through the danger before any of those",yellow,
        "flying rodents can respond...",yellow,"",yellow,False)
    if roll == 1:
        damage = random.randint(7,12)
        DialogBox.displayText("After only a few steps you slip on",yellow,
        "bat guano and fall hard hitting your",yellow,
        "head on a rock.",yellow, 
        "You take %d damage!"%damage,orange,False)
        savables.health -= damage
        roll = random.randint(1,2)
        if roll == 1:
            DialogBox.displayText("As you get up you find the bats",yellow,
            "are still undisturbed. You make it safely",yellow,
            "through the danger.",yellow,"",yellow,False)
        if roll == 2:
            DialogBox.displayText("You stand up in the middle of a bat swarm!",yellow,
            "They have been whipped up into a frenzy",yellow,
            "by the disturbance you caused!",yellow,"",yellow,False)
            randMonster.randMonster("weak",4)
            batVictory() if combat.victory == True else randCorridor()
    
    elif roll == 2:
        DialogBox.displayText("The bats suddenly drop from the ceiling",yellow,
        "and begin to swarm around you. A moment",yellow,
        "later, the cloud breaks and you see a",yellow,
        "a giagantic bat dive straight at you.",yellow,False)
        randMonster.randMonster("weak",4)
        batVictory() if combat.victory == True else randCorridor()
        
def batActionSneak():
    DialogBox.displayText("You keep low and creep as quietly",yellow,
    "as you can passed the hanging flock.",yellow,"",yellow,"",yellow,False)
    DialogBox.displayText("You keep low and creep as quietly",yellow,
    "as you can passed the hanging flock.",yellow,
    "None of them have appeared to have",yellow,"been disturbed.",yellow,False)
    grandRoom()

def batActionNoise():
    DialogBox.displayText("It will be just like running",yellow,
    "through a flock of birds",yellow,
    "on the ground...",yellow,"",yellow,False)
    DialogBox.displayText("It will be just like running",yellow,
    "through a flock of birds",yellow,
    "on the ground...",yellow,"...right?",yellow,False)
    DialogBox.displayText("The bats suddenly drop from the ceiling",yellow,
    "and begin to swarm around you. A moment",yellow,
    "later, the cloud breaks and you see a",yellow,
    "a giagantic bat dive straight at you.",yellow,False)
    randMonster.randMonster("weak",4)
    batVictory() if combat.victory == True else randCorridor()

def batTunnel():
    batCave = pygame.image.load('pictures/rooms/bats.jpg')
    gameDisplay.blit(batCave,[250,0])
    DialogBox.displayText("You make your way down the corridor",yellow,
    "only to discover a tunnel full of bats.",yellow,"",yellow,"",yellow,False)
    bats()
    
def bats():
    DialogBox.menuType = "threeChoiceMenu"
    DialogBox.displayText("What will you do?",yellow,
    "     Sneak past",green,
    "     Run past",green,
    "     Make noise",green,True)
    travelOptions(bats)
    
def batVictory():
    import leprechaun
    DialogBox.displayText("With their leader defeated the rest of",yellow,
    "the bat swarm disapates.",yellow,"",yellow,"",yellow,False) 
    if "staff" not in savables.weaponInventory:
        DialogBox.displayText("Before continuing, you look up and",yellow,
        "notice many bats were hanging on a",yellow,
        "sturdy wooden staff stuck to the ceiling.",yellow,
        "",yellow,False)
        staffObtain = pygame.image.load('pictures/weapons/boStaff.png')
        gameDisplay.blit(staffObtain,[425,30])
        DialogBox.displayText("This looks like it would be a great weapon!",yellow,
        "You decide to grab it and free it from",yellow,
        "where it was lodged between the rocks.",yellow,"",yellow,False)
        audio.getItem1.play()
        audio.getItem2.play()
        DialogBox.displayText("                       New Weapon:",yellow,
        "                      Quarter Staff",green,
        "                       Now available!",yellow,"",yellow,False)
        savables.weaponInventory.append("staff")
    tunnelGrate()
# ---------------------------------    
    
def dragon():
    DialogBox.menuType = "threeChoiceMenu"
    DialogBox.displayText("What will you attempt?",yellow,
    "     Sneak past",green,
    "     Make noise",green,
    "     Turn back",green,True)
    travelOptions(dragon)

dragonFace = pygame.image.load('pictures/rooms/dragonFace.jpg')
solidBlack = pygame.image.load('pictures/rooms/solidBlack.jpg')
def dragonSneak():
    DialogBox.displayText("The dragon is snoring flames from its",yellow,
    "snout. It is all you can do you remain quiet",yellow,
    "and creep around the beast without",yellow,
    "getting singed by its firey breath.",yellow,False)
    DialogBox.displayText("You made it! You can see the light",yellow,
    "of day within your reach! Then a burning",yellow,
    "wind can be felt from behind you. You",yellow,
    "turn around to see firey yellow eyes...",yellow,False)
    gameDisplay.blit(solidBlack,[250,0])
    audio.growling.play()
    clock = pygame.time.Clock()
    x = 550
    while x > 230:
        gameDisplay.blit(dragonFace,[x,0])
        weapons.redrawBorders()
        clock.tick(50)
        x -= 2
        pygame.display.update()
    DialogBox.displayText("The tunnel entrance is at least 200 feet",yellow,
    "away. There is nothing to hide behind and",yellow,
    "no way back. Oddly, a calm feeling sweeps ",yellow,
    "over with assurance that this is the end.",yellow,False)

def findIceBridge():
    iceBridge1 = pygame.image.load('pictures/rooms/iceBridge.jpg')
    gameDisplay.blit(iceBridge1,[250,0])
    DialogBox.displayText("The temperature drops the longer you",yellow,
    "walk. You eventually come to a frozen",yellow,
    "tunnel with a bridge made entirely of ice!",yellow,
    "Crossing looks rather dangerous.",yellow,False)
    iceBridge()
    
def iceBridge():
    DialogBox.menuType = "threeChoiceMenu"
    DialogBox.displayText("What will you do?",yellow,
    "     Try to cross",green,
    "     Look Down",green,
    "     Turn Back",green,True)
    travelOptions(iceBridge)
    
def crossIceBridge():
    DialogBox.displayText("What you wouldnt give for a nice pair",yellow,
    "of golf shoes right now! The bridge is",yellow,
    "as slick as can be and one stumble could",yellow,
    "spell doom. You carefully tread across.",yellow,False)
    random.choice([iceDoorRiddles,iceBridgeSlip])()

def iceLookDown():
    DialogBox.displayText("It is a looooooong way down! It looks like",yellow,
    "there is more ice and snow at the bottom",yellow,
    "but it is too dark to see if the revene",yellow,
    "leads anywhere. No way up or down.",yellow,False)
    iceBridge()

def iceLeave():
    DialogBox.displayText("You decide not to risk it and go",yellow,
    "back the way you came. (chicken!)",yellow,"",yellow,"",yellow,False)
    gameDisplay.blit(corridor1,(250,0))
    grandRoom()
        
def iceBridgeSlip():
    DialogBox.displayText("You make it to the center of the bridge",yellow,
    "but find it impossible to keep your footing.",yellow,
    "There is too much slope! You slide to the",yellow,
    "edge and tumble down into the abyss...",yellow,False)
    
def iceDoorRiddles():
    iceDoor = pygame.image.load('pictures/rooms/iceDoor.jpg')
    gameDisplay.blit(iceDoor,[250,0])
    DialogBox.displayText("You made it safely to the other side!",yellow,
    "Standing before you is a door encompassed",yellow,
    "in a glowing wall of ice. There is",yellow,
    "something inscribed in the ice...",yellow,False)
    DialogBox.displayText("As you read the engraving you hear",yellow,
    "a voice in your head as if the words",yellow,
    "are being spoken aloud. It says,",yellow,"",yellow,False)
    DialogBox.displayText("'This door shall remain sealed until", green,
    "three questions are answered correctly.",green,
    "An incorrect answer will expell you from",green,
    "this place. The first question is...'",green,False)
    DialogBox.displayText("'You are participating in a race.",green,
    "You overtake the second person. What",green,
    "position are you in? Give me your answer.'",green,"",yellow,False)
    iceQuestionAnswers1() 

def iceQuestion2():
    DialogBox.displayText("'What is the sum of the following:",green,
    "Take 1000 and add 40 to it.",green,
    "Add another 1000.",green,
    "Add 30.'",green,False)
    DialogBox.displayText("'Add another 1000.",green,
    "Now add 20.",green,
    "Add another 1000.",green,
    "Now add 10.'",green,False)
    iceQuestionAnswers2()  
    
def iceQuestion3():
    DialogBox.displayText("'Mary's father has five daughters...'",green,
    "",yellow,"",yellow,"",yellow,False)
    DialogBox.displayText("1. Nana",green,
    "2. Nene",green,
    "3. Nini",green,
    "4. Nono",green,False)
    DialogBox.displayText("'What is the name of the fifth daughter?'",green,
    "",yellow,"",yellow,"",yellow,False)
    iceQuestionAnswers3()
    
def iceAnswerCorrect(question):
    DialogBox.displayText("'That is correct.",green,
    "Here is your next question...'",green,
    "",yellow,"",yellow,False)
    iceQuestion2() if question == 1 else ""
    iceQuestion3() if question == 2 else ""
     
def iceAnswerIncorrect():
    DialogBox.displayText("'INCORRECT!'",red,
    "",yellow,"",yellow,"",yellow,False)
    DialogBox.displayText("'INCORRECT!'",red,
    "You suddenly feel a tremedous gush of",yellow,
    "wind push you back. You slide across the",yellow,
    "ice and fall into the gulf at the bridge.",yellow,False)
        
def iceQuestionAnswers1():
    DialogBox.displayText("How will you respond?",yellow,
    "     First Place                 Raspberry Jam",green,
    "     Second Place              I hate running",green,
    "     Third Place                Open the Door!!!",green,True)
    travelOptions(iceQuestionAnswers1)
    
def iceQuestionAnswers2():
    DialogBox.displayText("How will you resond?",yellow,
    "     5000                          4100",green,           
    "     4000                          I can't count",green,    
    "     5100                          Open Sesame?",green,True)
    travelOptions(iceQuestionAnswers2)
    
def iceQuestionAnswers3():
    DialogBox.displayText("How will you respond?",yellow,
    "     Nummy                      Nunu",green,
    "     Jane                          Is she cute?",green, 
    "     Mary                         I hate you!",green,True)
    travelOptions(iceQuestionAnswers3)
    
def notCute():
    DialogBox.displayText("No. Now what is your answer?",green,
    "",yellow,"",yellow,"",yellow,False)
    iceQuestionAnswers3()

iceWall = pygame.image.load('pictures/rooms/iceWall.jpg')
iceAmulet = pygame.image.load('pictures/weapons/iceAmulet.png')

def iceDoorOpen():
    audio.doorSound.play()
    DialogBox.displayText("'That is correct.'",green,
    "The giagantic door in the ice creeks open...",yellow,
    "",yellow,"",yellow,False)
    gameDisplay.blit(iceWall,[250,0])
    gameDisplay.blit(iceAmulet,[500,50])
    DialogBox.displayText("You expected to see another tunnel",yellow,
    "but the doors were actually a vault. There",yellow,
    "is a shining amulet hanging on the wall",yellow,
    "in the back of the vault.",yellow,False)
    DialogBox.displayText("You remove it and place it around your",yellow,
    "neck. It emits a soft blue glow. You are",yellow,
    "now able to shoot bolts of ice from your",yellow,
    "finger tips! Hooray for ice powers!",yellow,False)
    audio.getItem1.play()
    audio.getItem2.play()
    DialogBox.displayText("                       New Weapon:",yellow,
    "                         Ice Amulet",green,
    "                       Now available!",yellow,
    "",yellow,False)
    savables.weaponInventory.append("ice")

# Pool Room ------------------------
pool1 = pygame.image.load('pictures/rooms/cavePool.jpg')
drankWater = False
def poolRoom():
    global drankWater
    drankWater = False
    gameDisplay.blit(pool1,[250,0])
    DialogBox.displayText("The corridor ends at a glowing pool of",yellow,
    "water. The water looks clear and clean.",yellow,
    "You feel like you could use a drink.",yellow,"",yellow,False)
    pool()
    
def refillBottle():
    if savables.emptyBottles == 0:
        DialogBox.displayText("You dont have any empty bottles to",yellow,
        "refill. If you use a regeneration potion",yellow,
        "it can be refilled at this pool.",yellow,"",yellow,False)
    else:
        DialogBox.displayText("The red vials were too small to be of",yellow,
        "any use so you smashed them after you",yellow,
        "emptied them. You do, however, have some",yellow,
        "of the larger white bottles to refill.",yellow,False)
        for i in range(savables.emptyBottles):
            savables.regenPotions += 1
            savables.emptyBottles = 0
    pool()
    
def poolLeave():
    DialogBox.displayText("Your business is concluded here so you",yellow,
    "gather your things and head back out into",yellow,
    "the maze.",yellow,"",yellow,False)
    grandRoom()
    
def pool():
    DialogBox.menuType = "fourChoiceMenu"
    DialogBox.displayText("What will you do?",yellow,
    "     Drink from pool         Fill a bottle",green,
    "     Throw a rock in",green,
    "     Leave",green,True)
    travelOptions(pool)
    
def rockPool():
    DialogBox.displayText("You throw a stone into the glowing pool",yellow,
    "half expecting something to jump out and",yellow,
    "strike at it. The water is crystal clear",yellow,
    "and you can see it sink to the bottom.",yellow,False)
    DialogBox.displayText("The stone comes to a rest and begins",yellow,
    "to transform in the a shiney smooth",yellow,
    "pebble. There is definately something odd",yellow,
    "about this water. Maybe have a taste?",yellow,False)
    pool()

regenPotion = pygame.image.load('pictures/items/whitePotion.png')    
def poolDrink():
    global drankWater
    if savables.drankFromPool and not drankWater: 
        DialogBox.displayText("You suck down the glowing crystal water",yellow,
        "and slowly recover 80 health.",yellow,
        "",yellow,"",yellow,False)
        savables.health += 80
        drankWater = True
    elif not savables.drankFromPool:    
        DialogBox.displayText("You gracefully stroll up to the shimmering",yellow,
        "crystal water so as not to offend whatever",yellow,
        "generous spirits placed it here for you...",yellow,
        "",yellow,False)
        audio.splash.play()
        DialogBox.displayText("You gracefully stroll up to the shimmering",yellow,
        "crystal water so as not to offend whatever",yellow,
        "generous spirits placed it here for you...",yellow,
        "...and awkwardly plunk your head in.",yellow,False)
        DialogBox.displayText("The water tastes unbelievable! You have",yellow,
        "never tasted anything like it! This will",yellow,
        "surely give you a massive health boost!",yellow,
        "Let's see what it does...",yellow,False)
        savables.health += 5
        DialogBox.displayText("Um ok, +5 health is not a massive",yellow,
        "boost but per say but...",yellow,"",yellow,"",yellow,False)
        savables.health += 7 
        DialogBox.displayText("...and there is another +7 health.",yellow,
        "What in the world is this water...",yellow,"",yellow,"",yellow,False)
        savables.health += 4
        DialogBox.displayText("...+4 more health. Hmm, this water",yellow,
        "appears to have regenerative properties.",yellow,
        "After some time you recover 80 health",yellow,
        "before the effects wear off.",yellow,False)
        savables.health += 80
        drankWater = True
        DialogBox.displayText("You have got to get a bottle of this stuff",yellow,
        "to go! Unfortunately you couldn't resist",yellow,
        "the overwhelming urge to smash every",yellow,
        "potion bottle you drank from.",yellow,False)
        gameDisplay.blit(regenPotion,[500,90])
        DialogBox.displayText("Hey look! There is a perfectly good",yellow,
        "bottle sitting over there in the corner!",yellow,
        "After filling it, you decide that this",yellow,
        "stuff should be saved for a fight.",yellow,False)
        savables.regenPotions += 1
        savables.drankFromPool = True
    else:
        DialogBox.displayText("A monster randomly wanders into the room.",yellow,
        "The amount of time you have spent in here",yellow,
        "must have allowed it to catch your scent!",yellow,
        "It would be a good idea to move on.",yellow,False)
        monsterEncounter()
        gameDisplay.blit(pool1,[250,0])
    pool()
    
def tunnelGrate():
    tunnelGratePic = pygame.image.load('pictures/rooms/tunnelGrate.jpg')
    gameDisplay.blit(tunnelGratePic,[250,0])
    DialogBox.displayText("You arrive at another corridor",yellow,
    "this one having a metal grate in the",yellow,
    "floor that easily comes off. There is",yellow,
    "a ladder going down the opening.",yellow,False)
    tunnelGrateOptions()
    
def tunnelGrateOptions():
    DialogBox.menuType = "threeChoiceMenu"
    DialogBox.displayText("What will you do?",yellow,
    "     Go down corridor",green,
    "     Go down grate",green,
    "     Yell for help",green,True)
    travelOptions(tunnelGrateOptions)
    
# Snake Pit --------------------------
snakePitPic = pygame.image.load('pictures/rooms/snakePit.jpg')
hole = pygame.image.load('pictures/rooms/emptyPit.jpg')

def emptySnakePit():
    gameDisplay.blit(hole,[250,0])
    DialogBox.displayText("Whoaa! You almost fell into a pit in",yellow,
    "the middle of the path! It looks like you",yellow,
    "can make it over if you jump. Care to try?",yellow,"",yellow,False)
    DialogBox.menuType = "twoChoiceMenu"
    DialogBox.displayText("What will you do?",yellow,
    "     Turn back",green,
    "     Jump over pit",green,"",yellow,True)
    travelOptions(emptySnakePit)
    
def fallInPit():
    DialogBox.displayText("You get a running start and sprint towards",yellow,
    "the pit. Oops! There is a puddle of slime",yellow,
    "on the floor which causes you to slip and",yellow,
    "fall. You plundge into the pit!",yellow,False)
    damage = random.randint(10,15)
    savables.health -= damage
    DialogBox.displayText("You hit the bottom hard!",yellow,
    "You take %d damage!"%damage,orange,"",yellow,"",yellow,False)
    DialogBox.displayText("Eww, it looks like there was something,",yellow,
    "living in here at some point. Is that a",yellow,
    "snake's skin in the corner? Fortunately it",yellow,
    "is not a deep pit and easy to climb out.",yellow,False)
    randCorridor()

def snakePit():
    if len(savables.weaponInventory) == 4:
        DialogBox.displayText("The corridor continues but there is",yellow,
        "something blocking your path- sort of.",yellow,"",yellow,"",yellow,
        False)
        gameDisplay.blit(snakePitPic,[250,0])
        DialogBox.displayText("You look down and see a pit full of",yellow,
        "poisonous serpents. They look mean and!",yellow, 
        "very dangerous! The other side is not far.",yellow, 
        "in fact, you think you can jump across.",yellow,False)
        snakePitOptions()
    else:   
        emptySnakePit()

def snakePitOptions(): 
    DialogBox.menuType = "threeChoiceMenu"
    DialogBox.displayText("What will you do?",yellow,
    "     Jump over pit",green,
    "     Turn back",green,
    "     Play with snakes",green,True)
    travelOptions(snakePitOptions)
    
def snakePitJump():
    DialogBox.displayText("You back up and get a running start then",yellow,
    "leap over the snake pit. That was easy.",yellow,
    "There isn't anywhere else to go but down",yellow,
    "the corridor. You continue walking.",yellow,False)
    randCorridor()
    
def snakePitTurn():
    DialogBox.displayText("You have seen the movies. As soon as you",yellow,
    "try to leap over the pit you would slip",yellow,
    "and fall in or something else stupid",yellow,
    "would happen. You decide to turn back...",yellow,False)
    DialogBox.displayText("...only to find that mommy has returned",yellow,
    "to the nest!",yellow,"Oh crap.",yellow,"",yellow,False)
    randMonster.keyBattle = True if savables.healthTanks < 1 else False
    randMonster.randMonster("medium",4)
    randMonster.keyBattle = False
    if savables.healthTanks < 1 and combat.victory == True:
        snakePitVictory()
    else:
        randCorridor()
    
healthTank = pygame.image.load('pictures/items/healthTank.png')
def snakePitVictory():
    DialogBox.displayText("The giant anaconda hits the ground with a",yellow,
    "'thump'. Booya! Take that snakey boy!",yellow,
    "You notice a large lump rising up its.",yellow,
    "belly. It must have eaten something.",yellow,False)
    gameDisplay.blit(healthTank,[410,70])    
    DialogBox.displayText("The anaconda regurgitates a large tank",yellow,
    "of some sort. Slimey or not, you find it a",yellow,
    "good idea to take it along with you. Hmm,",yellow,
    "this odd tank makes you feel stronger!",yellow,False)
    audio.metriodAcquire.play()
    DialogBox.displayText("                         New Boost:",yellow,
    "                        Health Tank",green,
    "                          Acquired!",yellow,"",yellow,False)
    savables.healthTanks += 1
    savables.health += 100

def snakePitPlay():
    savables.snakePlaytime = True
    DialogBox.displayText("You are way higher than they can reach.",yellow,
    "Why not have a little fun? What could",yellow,
    "possibly go wrong?",yellow,"",yellow,False)
    DialogBox.displayText("You pick up a few rocks and throw them",yellow,
    "down at the snakes. The snakes hiss loudly",yellow,
    "and stir around. What great fun! You grab",yellow,
    "another rock but realize, it's not a rock...",yellow,False)
    gameDisplay.blit(healthPotion,[440,80])
    DialogBox.displayText("It's a potion! Sweet! Well things are just",yellow,
    "as you thought. There is no harm at all in",yellow,
    "playing with deadly, poisonous creatures",yellow,
    "in dark, scary dungeons.",yellow,False)
    savables.healthPotions += 1
    gameDisplay.blit(snakePitPic,[250,0])
    snakePitOptions()
    
def snakePitPlay2():
    DialogBox.displayText("Meh, you have already had your fun with",yellow,
    "these things. Besides, there dosent seem",yellow,
    "to be any more potions laying around.",yellow,
    "Do something else.",yellow,False)
    snakePitOptions()
# -----------------------------------

def grandRoom():
    gameDisplay.blit(grandRoomPic,[250,0])
    if savables.grandRoomFirstVisit == True:
        line1 = "You come to a grand junction room. There"
        line2 = "are many doors and corridors branching"
        line3 = "off of this room. There is no way of"
        line4 = "telling where they might lead to."
        DialogBox.displayText(line1,yellow,line2,yellow,line3,\
        yellow,line4,yellow,False)
        line1 = "In the center of the room you see an"
        line2 = "alter that looks designed to display small"
        line3 = "yellow statues... of dragons... holding"
        line4 = "orbs between their wings. (hint, hint)"
        DialogBox.displayText(line1,yellow,line2,yellow,line3,\
        yellow,line4,yellow,False)
        line1 = "There is also a broad, straight clean wall"
        line2 = "perfect for hanging door knockers that"
        line3 = "you may or may not have found laying"
        line4 = "around or been given by a leprechaun."
        DialogBox.displayText(line1,yellow,line2,yellow,line3,\
        yellow,line4,yellow,False)
        line1 = "Junction rooms like this would be good"
        line2 = "to revisit every now and then to do"
        line3 = "things like, oh, say, use special items?"
        line4 = ""
        DialogBox.displayText(line1,yellow,line2,yellow,line3,\
        yellow,line4,yellow,False)
        savables.grandRoomFirstVisit = False
    else:
        line1 = "You re-enter the grand junction room."
        line2 = "Several doors and passages leading from"
        line3 = "this place are locked and sealed off. It"
        line4 = "would be beneficial to find a way through."
        DialogBox.displayText(line1,yellow,line2,yellow,line3,\
        yellow,line4,yellow,False)
    grandRoomOptions()
    
def grandRoomOptions():
    DialogBox.menuType = "fourChoiceMenu"
    gameDisplay.blit(grandRoomPic,[250,0])
    line1 = "What will you do?"     
    line2 = "     Open a door              Use an Item"
    line3 = "     Random Corridor"
    line4 = "     Yell for Help"
    DialogBox.displayText(line1,yellow,line2,green,line3,\
    green,line4,green,True)
    travelOptions(grandRoomOptions)

randomCorridor = [hallwayPotion,batTunnel,findIceBridge,
corridorFork,monsterEncounter]

level2Corridors = [otherRooms3.mineCraftRoom,poolRoom,otherRooms2.fossil,\
otherRooms2.spiderCave]

level3Corridors = [otherRooms2.safe]

if savables.dungeonSection >= 2:
    randomCorridor = randomCorridor + level2Corridors
    if savables.dungeonSection >= 3:
        randomCorridor = randomCorridor + level3Corridors