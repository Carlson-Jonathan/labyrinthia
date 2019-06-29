import random,DialogBox,pygame,randMonster,combat,corridor1,grate,yell,savables,miscellaneous
green,yellow = (0,225,0),(240,240,0)
gameDisplay = pygame.display.set_mode((900,600))
orange = (255,155,0)
red = (255,0,0)

def grate():
    sewer = pygame.image.load('pictures/rooms/sewer.jpg')
    gameDisplay.blit(sewer,(250,0))
    random.choice([rungBreak,ladderPotion,monsterEncounter])()
        
def sewerSelection(fromOption):
    choiceNum = (DialogBox.selectionx*DialogBox.selectiony)
    if choiceNum == 3:
        ninjaTurtles() if fromOption == sewerTravelOptions else "" 
    elif choiceNum == 4:
        yell.yell() if fromOption == sewerTravelOptions else ""
    elif choiceNum == 5:
        if fromOption == sewerTravelOptions: 
            miscellaneous.potionsMenu()
            sewerTravelOptions() 
    elif choiceNum == 6:
        pass
    elif choiceNum == 8:
        pass
    elif choiceNum == 10:
        pass

def ninjaTurtles():
    DialogBox.displayText("You slosh down the sewer hoping to find",yellow,
    "a ladder up to a manhole or anything that",yellow,
    "might lead back the surface. You hear",yellow,
    "voices and the sound of something approaching.",yellow,False)
    turtles = pygame.image.load('pictures/rooms/ninjaTurtles.jpg')
    gameDisplay.blit(turtles,[250,0])
    DialogBox.displayText("                             ???,",yellow,
    "Who the heak are these... guys?",yellow,"",yellow,"",yellow,False)

def monsterEncounter():
    DialogBox.displayText("You reach the bottom with a splash and",yellow,
    "notice a pair of sinister yellow eyes slowly",yellow,
    "approaching you in the darkness.",yellow,"",yellow,False)
    randMonster.randMonster("weak","random")
    sewerTravelOptions()

def rungBreak():        
    trpDmg = random.randint (10,20)
    DialogBox.displayText("As you climb down the ladder one of the",yellow,
    "rungs breaks causing you to fall landing",yellow,
    "hard at bottom. You take %d damage to"%trpDmg,yellow,
    "your health.",yellow,False)
    savables.health -= trpDmg
    DialogBox.displayText("As you get back up you find yourself",yellow,
    "in a damp, wet sewer deep underground.",yellow,"",yellow,"",yellow,False)
    sewerTravelOptions()
    
def ladderPotion():
    DialogBox.displayText("On your way down the ladder you find",yellow,
    "a small bottle of red liquid strung over",yellow,
    "one of the center rungs. How convenient!",yellow,
    "",yellow,False)
    savables.healthPotions += 1
    DialogBox.displayText("Yyou are in a discusting looking sewer.",yellow,
    "Best not to drink anything else that might",yellow,
    "be randomly laying around down here.",yellow,"",yellow,False)
    sewerTravelOptions()
    
def sewerTravelOptions():
    DialogBox.menuType = "fourChoiceMenu"
    DialogBox.displayText("What will you do?",yellow,
    "     Go down passage        Save Game",orange,
    "     Yell for help",orange,
    "     Drink Potion",orange,True)
    sewerSelection(sewerTravelOptions)
    
def subwayLocked():
    DialogBox.displayText("You come to a junction section of",yellow,
    "the sewer. There are several doors that are",yellow,
    "are all locked from the other side. The only",yellow,
    "way out appears to be the staircase.",yellow,False)
    
            