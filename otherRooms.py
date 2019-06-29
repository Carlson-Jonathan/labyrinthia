import pygame,DialogBox,audio,combat,savables,random,corridor1
gameDisplay = pygame.display.set_mode((900,600))
yellow,green,orange,red = (240,240,0),(0,255,0),(255,155,0),(255,0,0)

'''
Module Contents:
    Armory  
    Shrine
    Bathroon
    Potion Roulette
    Barney
    Alchemy lab (make mega potions)
'''

# Armory - obtain minigun
armory = pygame.image.load('pictures/rooms/armory.jpg')
minigun = pygame.image.load('pictures/weapons/minigun.png')
def gunRoom():
    gameDisplay.blit(armory,[250,0])    
    DialogBox.displayText("Oh...",yellow,"",yellow,"",yellow,
    "",yellow,False)
    DialogBox.displayText("Oh...",yellow,"my...",yellow,"",yellow,
    "",yellow,False)
    audio.gunRoomLaugh.play()
    DialogBox.displayText("Oh...",yellow,"my...",yellow,
    "G O O D N E S S ! ! ! ! ! ! ! !",yellow,
    "",yellow,False)
    DialogBox.displayText("Words can't even begin to describe...",yellow,
    "You drooooool over all the goodies in",yellow,
    "this room. This is just tooooo good",yellow,
    "to be true!!!",yellow,False)
    DialogBox.displayText("Of all the options, all the ways",yellow,
    "to kill... If only you had some of this stuff",yellow,
    "earlier. You think your decision is going",yellow,
    "to be a tough one- but then you see it.",yellow,False)
    gameDisplay.blit(minigun,[410,50])
    DialogBox.displayText("Ooooooooohhh Yeeeeeeessssssss!!!",yellow,
    "",yellow,"",yellow,"",yellow,False)
    audio.getItem1.play()
    audio.getItem2.play()
    DialogBox.displayText("                        New Weapon:",yellow,
    "                        Widow Maker",green,
    "                        Now available!",yellow,"",yellow,False)
    savables.weaponInventory.append("gun")
    
# Shrine - obtain save orb
saveOrb = pygame.image.load('pictures/items/orb.png')
shrineRoom = pygame.image.load('pictures/rooms/shrine.jpg')
def shrine():
    gameDisplay.blit(shrineRoom,[250,0])
    DialogBox.displayText("What is this? A shrine of some sort. It",yellow,
    "looks like this was used at one point for",yellow,
    "ceremonial rituals. Looking around you ",yellow,
    "dont see anything that seems useful.",yellow,False)
    if savables.saveOrb == False:
        gameDisplay.blit(saveOrb,[470,70])    
        DialogBox.displayText("There, on the alter- what is that? You",yellow,
        "feel strangely drawn to it. As you reach",yellow,
        "out for the glowing object you feel that",yellow,
        "some sort of divinity is watching over you.",yellow,False)
        audio.getItem1.play()
        audio.getItem2.play()
        DialogBox.displayText("                         New Item:",yellow,
        "                          Save Orb",green,
        "                       Now available!",yellow,"",yellow,False)
        savables.saveOrb = True
    DialogBox.displayText("With nothing more to do here, you leave",yellow,
    "the room the same way you came in.",yellow,"",yellow,"",yellow,False)
    corridor1.grandRoom()

healthTank = pygame.image.load('pictures/items/healthTank.png')
bathroomPic = pygame.image.load('pictures/rooms/bathroom.jpg')   
def bathroom():
    audio.doorSound.play()
    DialogBox.displayText("The door opens with a creak. What",yellow,
    "unspeakable horror could be waiting for",yellow,
    "you on the other side of this door?",yellow,"",yellow,False)
    gameDisplay.blit(bathroomPic,[250,0])
    DialogBox.displayText("Yes! Finally! After drinking all those",yellow,
    "potions you seriously need to pee!!! You",yellow,
    "rush over to the toilet and let loose.",yellow,
    "                        Health +10!",green,False)
    savables.health += 10
    audio.toilet.play()
    if savables.healthTanks < 2:
        line1 = "Oh yea, you feel soooo much better! You"
        line2 = "wash your hands in the sink and open" 
        line3 = "the medicine cabinet. What this?"
        line4 = "" 
        DialogBox.displayText(line1,yellow,line2,yellow,line3,\
        yellow,line4,yellow,False)
        gameDisplay.blit(healthTank,[410,70])
        DialogBox.displayText("Oh, you couldnt have found this at a",yellow,
        "better time! The monsters are getting.",yellow,
        "tough! Time for a powerup!",yellow,
        "",yellow,False) 
        audio.metriodAcquire.play()
        DialogBox.displayText("                         New Boost:",yellow,
        "                        Health Tank",green,
        "                          Acquired!",yellow,"",yellow,False)
        savables.healthTanks += 1
        savables.health += 100
    line1 = "After washing up you gather your thing"
    line2 = "and head back out into the dungeon." 
    line3 = "Your glad that whoever built this place"
    line4 = "made such accomodating facilities!" 
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    
# Potion Roulette ----------------------------
rouletteRoom = pygame.image.load('pictures/rooms/rouletteRoom.jpg')
def potionsRoulette():
    gameDisplay.blit(rouletteRoom,[250,0])
    DialogBox.displayText("You wander into a room that is empty",yellow,
    "except for a table in the middle with 6",yellow,
    "potions sitting on it. On the wall is a",yellow,
    "plack that reads,",yellow,False)
    roulettePlack()
    
def roulettePlack():
    DialogBox.displayText("'To those who enter in this room,",orange,
    "Drinking a mixture may cause doom,",orange,
    "Strength and health and wisdom await,",orange,
    "Adventurers who tempt their fate.'",orange,False)
    DialogBox.displayText("'Four give power, one gives breath,",orange,
    "Lastly, one will bring swift death,",orange,
    "For them who curb, there is no shame,",orange,
    "In fleeing from this deadly game.'",orange,False)
    DialogBox.displayText("Well, this is pretty self-explanatory.",yellow,
    "What do you say? Care to play a game",yellow,
    "of potion roulette?",yellow,"",yellow,False)
    rouletteOptions()

def rouletteOptions():
    DialogBox.menuType = "threeChoiceMenu"
    DialogBox.displayText("What will you do?",yellow,
    "     Drink a potion",green,
    "     Read plack again",green,
    "     Leave room",green,True)
    actionSelection(rouletteOptions)
    
def actionSelection(priorMenu):
    choiceNum = (DialogBox.selectionx*DialogBox.selectiony)
    if choiceNum == 3:
        createBluePotion() if priorMenu == labOptions else ""
        drinkPotion() if priorMenu == rouletteOptions else ""
    elif choiceNum == 4:
        roulettePlack() if priorMenu == rouletteOptions else ""
    elif choiceNum == 5:
        corridor1.randCorridor() if priorMenu == rouletteOptions else ""
    elif choiceNum == 6:
        pass
    elif choiceNum == 8:
        pass
    elif choiceNum == 10:
        openBarneyDoor() if priorMenu == barneyOptions1 else ""
        barneyAttack() if priorMenu == barneyOptions2 else ""
    
def invalid(priorMenu):
    DialogBox.displayText("That is not a valid option. Try again.",red,
    "",yellow,"",yellow,"",yellow,False)
    priorMenu()
    
def drinkPotion():
    DialogBox.displayText("Which potion will you drink?",yellow,
    "     Red Potion                  Orange Potion",green,
    "     Yellow Potion              Green Potion",green,
    "     Blue Potion                 Purple Potion",green,True)
    downTheHatch()

redDrank,yellowDrank,greenDrank,orangeDrank,blueDrank,purpleDrank=False,False,False,False,False,False
def downTheHatch():
    global redDrank,yellowDrank,greenDrank,orangeDrank,blueDrank,purpleDrank
    choiceNum = (DialogBox.selectionx*DialogBox.selectiony)
    if choiceNum == 3 and redDrank == False:
        redDrank = True
        DialogBox.displayText("Ahhh red! Can't go wrong with the color",yellow,
        "of blood and guts. You pop the cork and",yellow,
        "gulp it down...",yellow,"",yellow,False)
        potionResultGenerator()
    elif choiceNum == 4 and yellowDrank == False:
        yellowDrank = True
        DialogBox.displayText("Lemony yellow! Nothing poisonous has ever",yellow,
        "been colored yellow! This is a win for sure!",yellow,
        "You pop the cork and gulp it down...",yellow,
        "",yellow,False)
        potionResultGenerator()
    elif choiceNum == 5 and blueDrank == False:
        blueDrank = True
        DialogBox.displayText("Of course! Everyone's favorite color! The",yellow,
        "logic is infallable! You pop the cork and",yellow,
        "gulp it down...",yellow,"",yellow,False)
        potionResultGenerator()
    elif choiceNum == 6 and orangeDrank == False:
        orangeDrank = True
        DialogBox.displayText("Citrusy orange. If nothing else, this one",yellow,
        "should at least be loaded with vitamin C!",yellow, 
        "You pop the cork and gulp it down...",yellow,
        "",yellow,False)
        potionResultGenerator()
    elif choiceNum == 8 and greenDrank == False:
        greenDrank = True
        DialogBox.displayText("The color of money! This one looks like a",yellow,
        "payout! You pop the cork and gulp it down.",yellow,
        "",yellow,"",yellow,False)
        potionResultGenerator()
    elif choiceNum == 10 and purpleDrank == False:
        purpleDrank = True
        DialogBox.displayText("Thick and inky life-giving purple. Reminds,",yellow,
        "you of unicorns and fairies and...stuff.",yellow,
        "You pop the cork and gulp it down...",yellow,"",yellow,False)
        potionResultGenerator()
    else:
        DialogBox.displayText("You already drank that potion. Drink",yellow,
        "a different color.",yellow,"",yellow,"",yellow,False)
        drinkPotion()
    if redDrank and blueDrank and greenDrank and orangeDrank\
        and yellowDrank and purpleDrank:
        door.level3Doors.pop(otherRooms.potionsRoulette)

effects = range(6)
potionEffects = [i for i in effects]
def potionResultGenerator():
    global potionEffects
    random.shuffle(potionEffects)
    poison() if potionEffects[0] == 0 else ""
    healthRestore() if potionEffects[0] == 2 else ""
    swordDamageUp() if potionEffects[0] == 3 else ""
    staffDamageUp() if potionEffects[0] == 4 else ""
    fireDamageUp() if potionEffects[0] == 5 else ""
    iceDamageUp() if potionEffects[0] == 1 else ""
    potionEffects.pop(0)
    rouletteOptions()
    
def poison():
    audio.potionDrink.play()
    DialogBox.displayText("This is the most delicious deadly",yellow,
    "poison you have ever tasted!",yellow,"You are dead.",red,"",yellow,False)
    
def healthRestore():
    audio.potionDrink.play()    
    DialogBox.displayText("Eww, it tastes like cough syrup. It",yellow,
    "makes you feel a lot better though.",yellow,"Your health is restored!",
    green,"",yellow,False)
    savables.health += DialogBox.maxHealth
    
def swordDamageUp():
    audio.potionDrink.play()
    DialogBox.displayText("Mmm! This one tastes like cold metal! You",yellow,
    "feel like you can hit harder with a sword!",yellow,"",yellow,"",yellow,False)
    audio.getItem1.play()
    audio.getItem2.play()
    DialogBox.displayText("                         New Boost:",yellow,
    "                    Sword + 5 damage",green,
    "                       Now available!",yellow,"",yellow,False)
    savables.swordMin += 5
    savables.swordMax += 5
    
def staffDamageUp():
    audio.potionDrink.play()
    line1 = "Ick! This one tastes like bark! As gross"
    line2 = "as it is, it makes you feel like you can"
    line3 = "relate to wood better- or at least swing" 
    line4 = "a staff harder."
    DialogBox.displayText(line1,yellow,line2,yellow,line3,
    yellow,line4,yellow,False)
    audio.getItem1.play()
    audio.getItem2.play()
    DialogBox.displayText("                         New Boost:",yellow,
    "                    Staff + 5 damage",green,
    "                       Now available!",yellow,"",yellow,False)
    savables.staffMin += 5
    savables.staffMax += 5
    
def fireDamageUp():
    audio.potionDrink.play()
    line1 = "SPICY! SPICY! HOT! HOT!"
    line2 = "You run around the room with your tongue"
    line3 = "hanging out trying to relieve the pain." 
    line4 = "Afterwards, you feel stronger with fire!"
    DialogBox.displayText(line1,orange,line2,yellow,line3,
    yellow,line4,yellow,False)
    audio.getItem1.play()
    audio.getItem2.play()
    DialogBox.displayText("                         New Boost:",yellow,
    "                     Fire + 15 damage",green,
    "                       Now available!",yellow,"",yellow,False)
    savables.fireMax += 15
    
def iceDamageUp():
    audio.potionDrink.play()
    line1 = "Cool mint? No, COLD MINT! Wow!"
    line2 = "This stuff is chilly! And GOOOOD!"
    line3 = "You finish the last drop and ice swirls" 
    line4 = "around you. Your ice attacks are stronger!"
    DialogBox.displayText(line1,yellow,line2,yellow,line3,
    yellow,line4,yellow,False)
    audio.getItem1.play()
    audio.getItem2.play()
    DialogBox.displayText("                         New Boost:",yellow,
    "                      Ice + 5 damage",green,
    "                       Now available!",yellow,"",yellow,False)
    savables.iceMin += 5
    savables.iceMax += 5

# -------------------------------------------

barneyDoor = pygame.image.load('pictures/rooms/door.jpg')
def barney():
    gameDisplay.blit(barneyDoor,[250,0])
    DialogBox.displayText("You come to the end of the tunnel.",yellow,
    "Whatever is behind this door seems to be",yellow,
    "attacking your very soul. There is a",yellow,
    "hideously evil feeling lurking in the air.",yellow,False)
    audio.heartBeat.play()
    DialogBox.displayText("You reach for the door and your hand",yellow,
    "unexpectingly begins to bleed. You feel",yellow,
    "sick to your stomach. It's not too late",yellow,
    "to turn back...",yellow,False)
    barneyOptions1()
    
def barneyOptions1():
    DialogBox.displayText("What will you do?",yellow,
    "     Turn back                  Flee",green,
    "     Run Away                   Retreat",green,
    "     Escape                       Open door?",green,True)
    actionSelection(barneyOptions1)    
    
def openBarneyDoor():
    DialogBox.displayText("That is not a valid option. Try again.",red,
    "",yellow,"",yellow,"",yellow,False)
    DialogBox.displayText("That is not a valid option. Try again.",red,
    "Ok, I am lying, it is a valid option",yellow,
    "but are you sure you want to do this?",yellow,
    "",yellow,False)
    barneyOptions2()
    
def barneyOptions2():
    DialogBox.displayText("Open the door? Really?",yellow,
    "     No                             No",green,
    "     No                             No",green,
    "     No                             Not no",green,True)
    actionSelection(barneyOptions2)

barneyPic = pygame.image.load('pictures/rooms/barney.jpg')
def barneyAttack():
    audio.doorSound.play()
    DialogBox.displayText("The door creeks open...",yellow,
    "",yellow,"",yellow,"",yellow,False)
    gameDisplay.blit(barneyPic,[250,0])
    audio.scream.play()
    DialogBox.displayText("No. NOOOOOOOOOOOOOOOOOOO!!!",yellow,
    "AAAAAAAAAAAAAAAAAAAAAHHHH!!!",orange,
    "HELP ME HELP ME HELP ME HELP ME!",red,
    "      RUUUUUUUUUUUUUUN!!!!!!!!!!!!",yellow,False)
    DialogBox.displayText("'I love you, you love me...'",green,
    "",yellow,"",yellow,"",yellow,False)
    DialogBox.displayText("'I love you, you love me...'",green,
    "           20 damage!",orange,
    "",yellow,"",yellow,False)
    savables.health -= 20
    DialogBox.displayText("'I love you, you love me...'",green,
    "           20 damage!",orange,
    "                  32 damage!",orange,"",yellow,False)
    savables.health -= 32
    DialogBox.displayText("'I love you, you love me...'",green,
    "           20 damage!",orange,
    "                  32 damage!",orange,
    "                         44 damage!",orange,False)
    savables.health -= 44
    DialogBox.displayText("GET OUT NOW! RUN!!! RUUUUUN!!!",red,
    "",yellow,"",yellow,"",yellow,False)
    DialogBox.displayText("You bolt out the door in such a haste",yellow,
    "that you drop several items durring your",yellow,
    "retreat.",yellow,"",yellow,False)
    savables.healthPotions.pop(0)
    savables.healthPotions.pop(0)
    savables.healthPotions.pop(0)
    savables.regenPotions.pop(0)
    gameDisplay.blit(barneyDoor,[250,0])
    DialogBox.displayText("The door slams itself behind you and the",yellow,
    "door handle melts. Blood oozes from the",yellow,
    "cracks in and and around the door. It",yellow,
    "must never be opened again!",yellow,False)
    
def alchemyRoom():
    audio.alchemy.play()
    alchemyLab = pygame.image.load('pictures/rooms/alchemyLab.jpg')
    gameDisplay.blit(alchemyLab,[250,0])
    line1 = "Well this room looks like a lot of fun!"
    line2 = "Things are bubbling and things are"
    line3 = "zapping. It looks like someone nearly"
    line4 = "succeeded in bringing something to life!"
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    line1 = "On the table you see a chemistry... err,"
    line2 = "'alchemy' set. There is a note that looks"
    line3 = "like a recipie of some sort. The note"
    line4 = "is easy to read and says,"
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    line1 = "                 Mega Potion recipie:"
    line2 = "Mix 1 flask of regeneration potion with" 
    line3 = "3 vials of health potions..."
    line4 = ""
    DialogBox.displayText(line1,green,line2,green,line3,\
    green,line4,yellow,False)
    line1 = "The recipie continues with other things"
    line2 = "to add like bat wings and troll brains," 
    line3 = "most of which are already lying around"
    line4 = "in the lab. Wanna make a mega potion?"
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    labOptions()
    
def labOptions():
    DialogBox.menuType = "twoChoiceMenu"
    line1 = "What action will you take?"
    line2 = "     Make potion"
    line3 = "     Leave lab"
    line4 = ""
    DialogBox.displayText(line1,yellow,line2,green,line3,\
    green,line4,yellow,True)
    actionSelection(labOptions)
    
def createBluePotion():
    if (savables.healthPotions >= 3) and (savables.regenPotions >= 1):
        savables.healthPotions -= 3
        savables.regenPotions -= 1
        savables.megaPotions += 1
        savables.emptyBottles += 1
        audio.bluePotion.play()
    else:
        line1 = "You dont have have the required potions"
        line2 = "to create a mega potion."
        line3 = ""
        line4 = ""
        DialogBox.displayText(line1,red,line2,red,line3,\
        yellow,line4,yellow,False)
    labOptions()
    