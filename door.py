import random,DialogBox,pygame,randMonster,combat,corridor1,grate,yell,weapons,audio,savables,otherRooms,otherRooms2
green,yellow = (0,225,0),(240,240,0)
gameDisplay = pygame.display.set_mode((900,600))
orange = (255,155,0)
red = (255,0,0)

'''
Module contents:
    Treasure Room (obtain sword)
    Fire Door (obtain fire ring)
    Empty Room to sewer

'''
def door():
    random.choice(randomDoor)()
    
# Event Functions--------------------------------
treasureRoom = pygame.image.load('pictures/rooms/treasureRoom2.jpg')
healthPotion = pygame.image.load('pictures/items/health_potion.png')
def treasureDoorPotion():
    gameDisplay.blit(treasureRoom,(250,0))
    DialogBox.displayText("Look at all that swag! How you wish",yellow,
    "you wernt lost in a dungeon struggling",yellow,
    "to stay alive. Taking any of this would",yellow,
    "just slow you down and get you killed...",yellow,False)
    gameDisplay.blit(healthPotion,[440,80])
    DialogBox.displayText("...except for that potion over there.",yellow,
    "",yellow,"",yellow,"",yellow,False)
    savables.healthPotions += 1
    DialogBox.displayText("After gathering your loot you exit",yellow,
    "through the door at the back of the room.",yellow,"",
    yellow,"",yellow,False)
    exitOptions()

def treasureDoor():
    DialogBox.displayText("You open the door apprehensively.",yellow,
        "A dim light can be seen within...",yellow,"",yellow,
        "",yellow,False)
    gameDisplay.blit(treasureRoom,(250,0))       
    DialogBox.displayText("You have found a room full of treasure!",
        yellow,"",yellow,"",yellow,"",yellow,False)
    DialogBox.displayText("Unfortunately you forgot to bring your",yellow,
        "pants with the bottomless pockets. Gold,",yellow,
        "and gems wont do you any good if you are",yellow,
        "dead anyway. You decide to travel light.",yellow,False)
    DialogBox.displayText("You notice a wicked looking sword",yellow,
        "gleaming in the light at the top of a",yellow,
        "treasure pile. Right next to it is a",yellow,
        "stiring monster about to awaken.",yellow,False)
    treasureDoorOptions()
        
def treasureDoorOptions():
    DialogBox.menuType = "threeChoiceMenu"
    DialogBox.displayText("What will you do?",yellow,
    "     Go for sword",green,
    "     Leave room",green,
    "     Throw object",green,True)
    travelOptions(treasureDoorOptions)

swordObtain = pygame.image.load('pictures/weapons/sword3.png')
def treasureRoomSword():
    DialogBox.displayText("You make a dash for the sword hoping to",yellow,
    "get ahold of it before the monster wakes",yellow,
    "up.",yellow,"",yellow,False)
    DialogBox.displayText("Too late! The monster woke up!",orange,
    "",yellow,"",yellow,"",yellow,False)
    randMonster.randMonster("weak","random")
    gameDisplay.blit(treasureRoom,[250,0])
    DialogBox.displayText("With the monster dead you return to",yellow,
    "the treasure hoard to claim your prize.",yellow,"",yellow,"",yellow,False)
    gameDisplay.blit(swordObtain,[440,40])
    audio.getItem1.play()
    audio.getItem2.play()
    DialogBox.displayText("                       New Weapon:",yellow,
    "                            Sword",green,"                       Now available!",yellow,"",yellow,False)
    savables.weaponInventory.append("sword")
    exitOptions()
    
def exitOptions():
    DialogBox.displayText("There is nothing left to do here. There",yellow,
    "is another door leading out the back of",yellow,
    "the room, or you can exit the way you",yellow,
    "came in.",yellow,False,)
    exitChoices()
    
def exitChoices():
    DialogBox.menuType = "twoChoiceMenu"
    DialogBox.displayText("What will you do?",yellow,
    "     Exit rear door",green,
    "     Go back",green,"",yellow,True)
    travelOptions(exitChoices)

def exitRear():
    DialogBox.displayText("After gathering your loot you exit",yellow,
    "through the door at the back of the room.",yellow,"",
    yellow,"",yellow,False)
    corridor1.tunnelGrate()
    
def exitFront():
    DialogBox.displayText("You go back the way you came to be",yellow,
    "sure you didnt miss anything comming in.",yellow,
    "",yellow,"",yellow,False)
    gameDisplay.blit(corridor1.corridor1,(250,0))
    corridor1.start()
    
def treasureRoomLeave():
    DialogBox.displayText("Like a big chicken, you decide to",yellow,
    "abandon the room and all its goodies",yellow,
    "in fear of getting your butt whipped.",yellow,"",yellow,False)
    corridor1.startText()
    
def treasureRoomThrow():
    DialogBox.displayText("You grab a nearby pot and toss it through",yellow,
    "the entry door. The monster awakens",yellow,
    "at the loud crash and bolts out after it.",yellow,
    "You quickly rush to claim your prize.",yellow,False)
    gameDisplay.blit(swordObtain,[440,40])
    audio.getItem1.play()
    audio.getItem2.play()
    DialogBox.displayText("                       New Weapon:",yellow,
    "                            Sword",green,
    "                       Now available!",yellow,
    "",yellow,False)
    savables.weaponInventory.append("sword")
    DialogBox.displayText("The monster returns into the room",yellow,
    "after realizing it had been fooled. Looks",yellow,
    "like you have a fight on your hands, but",yellow,
    "at least you are armed with cold steel!",yellow,False)
    randMonster.randMonster("weak","random")
    gameDisplay.blit(treasureRoom,[250,0])
    exitOptions()

# Fire room -------------------------------        
smokeRoom = pygame.image.load('pictures/rooms/smokeRoom.jpg')
flameTrap = pygame.image.load('pictures/rooms/flames.jpg')

def fireDoor():
    if "fire" in savables.weaponInventory:
        emptyRoom() 
    else:
        trapDmg = random.randint(10,20)
        gameDisplay.blit(flameTrap,(250,0))
        audio.inferno.play()
        audio.fireBurn.play()
        DialogBox.displayText("The door suddenly bursts open! Hot blue",yellow,
            "and yellow flames spew out at you!",yellow,
            "",yellow,"",yellow,False)
        roll = random.randint(1,2)
        if roll == 1:
            DialogBox.displayText("Your clothes catch fire! You suffer burns",yellow,
            "on your upper body and take %d damage"%trapDmg,yellow,
            "before you manage to extinguishing the",yellow,
            "flames.",yellow,False)
            savables.health -= trapDmg
        elif roll == 2:
            DialogBox.displayText("You jump out of the way just in time!",yellow,
            "Phew! That was close! You wait for a",yellow,
            "and the flames eventually die down.",yellow,""
            ,yellow,False) 
        DialogBox.displayText("You think there may be something in",yellow,
            "that room but are not sure if it is safe.",yellow,
            "Maybe you should have another look?",yellow,"",yellow,False )
        fireDoorOptions()
   
def fireDoorOptions():
    DialogBox.menuType = "threeChoiceMenu"
    audio.fireBurn.fadeout(2500)
    DialogBox.displayText("What will you do?",yellow,
    "     Go back in",green,
    "     Steer clear",green,
    "     Use Item",green,True)
    travelOptions(fireDoorOptions)
    
def fireDoorFail():
    gameDisplay.blit(smokeRoom,[250,0])
    DialogBox.displayText("You look around the corner only to see",yellow,
    "smoke pooring out of the room. You",yellow,
    "courageously walk into the room to have",yellow, 
    "a look around.",yellow,False)
    damage = random.randint (15,25)
    gameDisplay.blit(flameTrap,(250,0))
    audio.inferno.play()
    audio.fireBurn.play()
    gameDisplay.blit(flameTrap,(250,0))
    DialogBox.displayText("                        B O O M ! ! !",orange,
    "Another inferno! You are blasted out of",yellow,
    "the room back at where you entered.",yellow,
    "You take %d points of damage!"%damage,orange,False)
    savables.health -= damage
    DialogBox.displayText("This dosent seem to be going your way.",yellow,
    "However, you are SURE there is something",yellow,
    "good in that room. What do you say?",yellow,
    "Are you feeling persistant?",yellow,False)
    fireDoorOptions()

sewer = pygame.image.load('pictures/rooms/sewer.jpg')
def getFireRing():
    gameDisplay.blit(smokeRoom,[250,0])
    DialogBox.displayText("You carefully poke your head back into",yellow,
    "the room expecting the worst. The walls",yellow,
    "are blackened and charred and clouds",yellow,
    "of smoke create a screen of darkness.",yellow,False)
    fireRing = pygame.image.load('pictures/weapons/fireRing.png')
    gameDisplay.blit(fireRing,[420,60])        
    DialogBox.displayText("Through the smoke and soot you see",yellow,
    "a flickering light. Whats this? A magical",yellow,
    "artifact! So that is what was causing all",yellow,
    "the flame spirts in here?!",yellow,False)
    DialogBox.displayText("You approach and feel the ring. It is",yellow,
    "cool to the touch and fits perfectly on",yellow,
    "your finger. Furthermore you can use it",yellow,
    "to shoot fire from your hands! Awesome!",yellow,False)
    audio.getItem1.play()
    audio.getItem2.play()
    DialogBox.displayText("                       New Weapon:",yellow,
    "                           Fire Ring",green,
    "                       Now available!",yellow,
    "",yellow,False)
    savables.weaponInventory.append("fire")
    gameDisplay.blit(smokeRoom,[250,0])
    DialogBox.displayText("You turn around to leave the room but...",yellow,
    "",yellow,"",yellow,"",yellow,False)
    DialogBox.displayText("The floor suddenly opens under you!",yellow,
    "Oh no! A trap door! And it is trapping you!",yellow,
    "",yellow,"",yellow,False)
    gameDisplay.blit(sewer,[250,0])
    audio.splash.play()
    DialogBox.displayText("With a 'SPLASH' you land in a smelly",yellow,
    "dark sewer.",yellow,"Smells like New Jersey down here.",yellow,
    "",yellow,False)
    
def emptyRoom():
    MTroom = pygame.image.load('pictures/rooms/MTroom.jpg')
    gameDisplay.blit(MTroom,(250,0))
    DialogBox.displayText("You walk through the door only to find an",yellow, 
        "empty room.",yellow,"",yellow,"",yellow,False)
    DialogBox.displayText("Soon after you enter the room the door",yellow, 
        "behind you slams shut and wont open.",yellow,"The only way out of the room seems to be",yellow,
        "through a grate in the corner floor.",yellow,False)
    grate.grate()
    
def monsterDoor():
    DialogBox.displayText("A monster was lurking behind the door!",yellow,
    "",yellow,"",yellow,"",yellow,False)
    corridor1.monsterEncounter()
    
# Door module selection definitions
def travelOptions(travelType):
    choiceNum = (DialogBox.selectionx*DialogBox.selectiony)
    if choiceNum == 3:
        exitRear() if travelType == exitChoices else "" 
        roll = random.randint(1,3)
        getFireRing() if roll == 3 else fireDoorFail()
    elif choiceNum == 4:
        exitFront() if travelType == exitChoices else ""
        treasureRoomLeave() if travelType == treasureDoorOptions else ""
    elif choiceNum == 5:
        pass 
        treasureRoomThrow() if travelType == treasureDoorOptions else "" 
    elif choiceNum == 6:
        pass
    elif choiceNum == 8:
        pass
    elif choiceNum == 10:
        pass

randomDoor = [treasureDoor,monsterDoor,fireDoor,emptyRoom,\
otherRooms.shrine]

level2Doors = [otherRooms.alchemyRoom]

level3Doors = [otherRooms.gunRoom,\
otherRooms.potionsRoulette]

sewerRooms = [otherRooms.bathroom]
hellRooms = [otherRooms2.Hillary,otherRooms.barney]

if savables.dungeonSection >= 2:
    randomDoor = randomDoor + level2Doors
    if savables.dungeonSection >= 3:
        randomDoor = randomDoor + level3Doors