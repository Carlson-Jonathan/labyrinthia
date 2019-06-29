import DialogBox,pygame,sys,audio,weapons,savables
from pygame import *
gameDisplay = pygame.display.set_mode((900,600))
red,yellow,green = (255,0,0),(240,240,0),(0,225,0)

'''
Module contents:
    money guessing game
'''    

def moneyGame():
    moneyDoor = pygame.image.load('pictures/rooms/cashQuiz.jpg')
    gameDisplay.blit(moneyDoor,[250,0])
    line1 = "This door has an odd sign above it and a"
    line2 = "dollar sign. The sing hanging above reads:" 
    line3 = "'Every bill value + Every coin value = Entry''"
    line4 = "Look, a keypad! Who makes these doors?"
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    green,line4,yellow,False)
    cashOptions()
    
def cashOptions():
    DialogBox.menuType = "twoChoiceMenu"
    line1 = "What will you do?"
    line2 = "     Enter Guess"
    line3 = "     Leave"
    line4 = ""
    DialogBox.displayText(line1,yellow,line2,green,line3,\
    green,line4,yellow,True)
    choiceNum = (DialogBox.selectionx*DialogBox.selectiony)
    cashGuess() if choiceNum == 3 else ""
    
def cashGuess():
    weapons.weaponAnimations = True
    DialogBox.menuType = "twoChoiceMenu"
    line1 = "Enter your guess using the number keys:"
    line2 = ""
    line3 = ""
    line4 = ""
    DialogBox.displayText(line1,yellow,line2,green,line3,\
    green,line4,yellow,False)
    guessing = True
    keys = {pygame.K_0:0,pygame.K_1:1,pygame.K_2:2,pygame.K_3:3,
    pygame.K_4:4,pygame.K_5:5,pygame.K_6:6,pygame.K_7:7,
    pygame.K_8:8,pygame.K_9:9,pygame.K_PERIOD:"."}
    x = 500
    guess = []
    keyStroke = 0
    while guessing:
        font = pygame.font.SysFont("comicsansms",50)
        dollarSign = font.render("$",True,green)
        gameDisplay.blit(dollarSign,[465,475])
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                for key in keys:
                    if event.key == key:
                        keyStroke += 1
                        number = keys[key]
                        digit = font.render(str(number),True,green)
                        audio.arrowTick.play()    
                        gameDisplay.blit(digit,[x,475])
                        x += 33
                        guess.append(number)
                        if keyStroke == 6:
                            audio.selectTick.play()
                            guess = float(''.join(map(str,guess)))
                            weapons.weaponAnimations = False
                            moneyCorrect() if float('%.2f'%guess) == float(189.91) else moneyIncorrect()
                            guessing = False
        pygame.display.update()
    
def moneyCorrect():
    audio.chaChing.play()
    line1 = "The door slowly opens..."
    line2 = ""
    line3 = ""
    line4 = ""
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    green,line4,yellow,False)
    audio.doorSound.play()
    
def moneyIncorrect():
    line1 = "The keypad goes blank, then resets." 
    line2 = "Apparently that answer was not correct."
    line3 = "Maybe you should try again?"
    line4 = ""
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    cashOptions()
    
    
    
def mineCraftRoom():
    line1 = "You start to feel ill as the corridor"
    line2 = "continues. The walls and rocks seem to"
    line3 = "transform developing sharp edges. Things" 
    line4 = "are starting to get really weird."
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    mineCraft = pygame.image.load('pictures/rooms/mineCraftCave.jpg')
    gameDisplay.blit(mineCraft,[250,0])
    line1 = "It seems you have wandered into some kind"
    line2 = "of parallel dimension. You arms, legs and "
    line3 = "head feel like they are transforming into" 
    line4 = "cubes. Better not stay too long."
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    sandPaper = pygame.image.load('pictures/items/sand.png')
    gameDisplay.blit(sandPaper,[480,80])
    line1 = "On the floor you notice a peice of sand"
    line2 = "paper. Did somone shape this place using"
    line3 = "pick axes and then smooth it down? You" 
    line4 = "know just what to do with sandpaper."
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    line1 = "You smooth down the shaft of your staff"
    line2 = "removing splinters and making it more"
    line3 = "arrowdynamic. You can now swing harder" 
    line4 = "and do more damage to monsters."
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    audio.getItem1.play()
    audio.getItem2.play()
    DialogBox.displayText("                         New Boost:",yellow,
    "                    Staff + 5 damage",green,
    "                       Now available!",yellow,"",yellow,False)
    savables.staffMin += 5
    savables.staffMax += 5
    line1 = "You turn around and head back out."
    line2 = ""
    line3 = "" 
    line4 = ""
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)