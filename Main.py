import pygame,sys,DialogBox,corridor1,\
combat,yell,door,startCavern,leprechaun,\
otherRooms2,randMonster,miscellaneous,corridor2,\
otherRooms3,finalBattle


from pygame.locals import *

# basic variable definitions

white = (255,255,255)
red = (255,0,0)
green = (0,225,0)
darkgreen = (0,125,0)
black = (0,0,0)
blue = (0,0,75)
yellow = (240,240,0)
brown = (200,200,150)

# pygame initialization
pygame.init()
screen=pygame.display.set_mode((900,600),0,32)
pygame.display.set_caption('Labyrinthia')
gameDisplay = pygame.display.set_mode((900,600))
clock = pygame.time.Clock()
clock.tick(35)

pygame.font.get_init()
font = pygame.font.SysFont("comicsansms",30)
combat.battle = False
logo = pygame.image.load('pictures/logo.png')
keyControls = pygame.image.load('pictures/arrowKeys.jpg')

# main game loop
def game_loop():
    startScreen = True
    fade = True
    while True:
        clock.tick(5)
        for event in pygame.event.get():
            
            # 'Quit' function
            def XQuit():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            XQuit()
            
            # Title Screen
            while startScreen == True:
                XQuit()
                TitleScreen = pygame.image.load('pictures/TitleScreen.jpg')
                TitleScreenFade = pygame.image.load('pictures/TitleScreen.png')
                if fade:
                    for i in range(30):
                        clock.tick(40)
                        #Title screen fade-in. Reactivate later.
                        ''' 
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        gameDisplay.blit(TitleScreenFade,(0,0))
                        pygame.display.update()
                        '''
                fade = False
                gameDisplay.blit(TitleScreen,(0,0))
                openCaption3 = font.render("Press [ENTER] to continue",True,brown,)
                gameDisplay.blit(openCaption3,[270,395])
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:# or pygame.K_KP_ENTER:
                            #TitleScreen Fade-out. Reactivate later.
                            '''
                            fadeOut = pygame.image.load('pictures/fadeOut.png')
                            for i in range(40):
                                clock.tick(30)
                                gameDisplay.blit(fadeOut,[0,0])
                                pygame.display.update()
                            '''    
                            gameDisplay.fill(black)
                            startScreen = False
                pygame.display.update()
            
            # opening text
            gameDisplay.blit(logo,[300,150])
            DialogBox.displayText("              Welcome to Labyrinthia!",yellow,
            "                  by Jonathan Carlson",green,"",yellow,"",yellow,False)
            gameDisplay.fill(black)            
            gameDisplay.blit(keyControls,[300,100])
            DialogBox.displayText("          Use the ARROW keys and the",yellow,
                                "                 [ENTER] key to play.",yellow,"",yellow,"",yellow,False)
            DialogBox.displayText("This is a story about someone being",yellow,
                                   "lost in some kind of labyrinth dungeon.",yellow,
                                  "Your character must find a way out of the",yellow,
                                    "labyrinth without dying.",yellow,False)
            DialogBox.displayText("You will control the character using",yellow,
                        "the arrow keys and ENTER key.",yellow,
                        "Fight monsters, explore around, find clues,",yellow,
                        "& aquire weapons and special items to win.",yellow,False)
            
            import otherRooms,grate
            #corridor1.poolRoom()
            #corridor1.snakePit()
            corridor1.startText()
            #corridor1.grandRoom()
            #corridor1.findIceBridge()
            #corridor1.randCorridor()
            #corridor1.batTunnel()
            #corridor1.emptySnakePit()
            #corridor2.ladder()
            
            #otherRooms.gunRoom()
            #otherRooms.shrine()
            #otherRooms.bathroom()
            #otherRooms.potionsRoulette()
            #otherRooms.barney()
            #otherRooms.alchemyRoom()
            
            #otherRooms2.fossil()
            #otherRooms2.Hillary()
            #otherRooms2.spiderCave()
            #otherRooms2.safe()
            #otherRooms3.moneyGame()
            #otherRooms3.mineCraftRoom()
            
            #yell.yell2() #<-- get you to leprechaun
            #startCavern.startingCavern()
            #randMonster.randMonster("strong",1)
            #miscellaneous.armorMenu()
            #grate.grate()
            
            #finalBattle.slayDragon()
            #finalBattle.fadeOutAni()
            #finalBattle.exitFadeIn()
            #finalBattle.leprechaunPunishOptions()
            #finalBattle.weaponsMerge()
            #finalBattle.runeFeatherAppear()

#start trigger
game_loop()


  