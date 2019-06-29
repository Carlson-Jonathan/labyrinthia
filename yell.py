import random,DialogBox,pygame,randMonster,combat,door,grate,corridor1,leprechaun,savables
gameDisplay = pygame.display.set_mode((900,600))
green,yellow = (0,225,0),(240,240,0)
orange = (255,155,0)
red = (255,0,0)

def yell():
    roll = random.randint(1,4)
    DialogBox.displayText("You yell at the top of your lungs hoping",yellow,
    "that somehow, help will arrive.", yellow,"",yellow,
    "",yellow,False)
    if roll == 1:
        roll = random.randint(1,2)
        yell1() if roll == 1 else yell2()
    elif roll == 2:
        DialogBox.displayText("Your voice reverberates through the halls",yellow,
        "A tremor starts and the ground shakes!",yellow,
        "",yellow,"",yellow,False)
        roll = random.randint (1,2)
        tremor1() if roll == 1 else tremor2()
    elif roll == 3:
        monsterAttack()
    elif roll == 4:
        shutup()
       
def shutup():
    DialogBox.displayText("You shout as loudly as you can,",yellow,
    "'Help me! Is anyone there?!'",orange,
    "",yellow,"",yellow,False)
    DialogBox.displayText("You shout as loudly as you can,",yellow,
    "'Help me! Is anyone there?!'",orange,
    "You hear your voice echo back to you,",yellow,
    "'No! Now shut up and stop yelling!'",orange,False)
    corridor1.tunnelGrateOptions()
    
def monsterAttack():
    DialogBox.displayText("Your voice echoes down the corridor",yellow,
    "for several moments. Then you hear",yellow,
    "a low roar approaching behind you...",yellow,"",yellow,False)
    DialogBox.displayText("Your voice echoes down the corridor",yellow,
    "for several moments. Then you hear",yellow,
    "a low roar approaching behind you...",yellow,
    "A monster jumps out of the darkness!",orange,False)
    randMonster.randMonster("weak","random")

def yell1():            
    damage = random.randint(7,12)
    DialogBox.displayText("You yell at the top of your lungs hoping",yellow,
    "that somehow, help will arrive.", yellow,
    "Nope. No help arrived. In fact, now your",yellow,
    "throat hurts. You take %d damage. (Idiot!)"%damage,yellow,False)
    savables.health -= damage
    corridor1.tunnelGrateOptions()
    
def yell2():
    leprechaunAppear = pygame.image.load('pictures/rooms/leprechaun.jpg')
    gameDisplay.blit(leprechaunAppear,[250,0])    
    DialogBox.displayText("You yell at the top of your lungs hoping",yellow,
    "that somehow, help will arrive.", yellow,
    "A door magically appears on the wall and",yellow,
    "a curious leprechaun pokes its head out.",yellow,False)
    leprechaun.leprechaunOptions()    

def tremor1():
    DialogBox.displayText("Your voice reverberates through the halls",yellow,
    "A tremor starts and the ground shakes!",yellow,
    "Something falls and hits you on the head!",yellow,
    "",green,False)
    gameDisplay.blit(corridor1.healthPotion,[440,80])
    DialogBox.displayText("Your voice reverberates through the halls",yellow,
    "A tremor starts and the ground shakes!",yellow,
    "Something falls and hits you on the head!",yellow,
    "You found a potion!",green,False)
    savables.healthPotions += 1
    
    
def tremor2():
    damage = random.randint(7,12)
    DialogBox.displayText("Your voice reverberates through the halls",yellow,
    "A tremor starts and the ground shakes!",yellow,
    "Something falls and hits you on the head!",yellow, 
    "It was a big rock. You take %d damage!"%damage,orange,False)
    savables.health -= damage
