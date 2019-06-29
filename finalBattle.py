import DialogBox,audio,pygame,sys,weapons,random,\
randMonster,combat,miscellaneous,time,savables
from pygame.locals import *
gameDisplay = pygame.display.set_mode((900,600))
clock = pygame.time.Clock()
    
red,orange,green,yellow,blue = (255,0,0),(255,155,0),(0,255,0),(240,240,0),(28,209,255)
color1,color2,color3,color4 = yellow,yellow,yellow,yellow
line1,line2,line3,line4 = "","","",""
text = "DialogBox.displayText(line1,color1,line2,color2,line3,\
color3,line4,color4,False)"

wyvern = pygame.image.load('pictures/monsters/wyvern.jpg')
wyvern2 = pygame.image.load('pictures/monsters/wyvern2.jpg')
deadDragon = pygame.image.load('pictures/rooms/deadDragon.jpg')
punishBattle = False
finalBattle = False
dragonBattle = False
def slayDragon():
    global dragonBattle
    dragonBattle = True
    randMonster.monsterBackground = wyvern
    audio.pygame.mixer.music.load('Audio/bossBattle.ogg')
    audio.pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.4)
    audio.dragonRoar.play()
    gameDisplay.blit(wyvern,[250,0])
    line1 = "The dragon stands guarding the exit to"
    line2 = "the labyrinth alert and ready to attack!"
    line3 = ""
    line4 = ""
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    weapons.weaponAnimations = True
    weapons.miniGunRaise()
    weapons.weaponAnimations = False
    gameDisplay.blit(miniGun,[600,200])
    line1 = "With your minigun primed and ready to"
    line2 = "spill blood, you take aim and prepare to"
    line3 = "pump that ugly sucker full of lead."
    line4 = ""
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    line1 = "With your minigun primed and ready to"
    line2 = "spill blood, you take aim and prepare to"
    line3 = "pump that ugly sucker full of lead."
    line4 = "                Hasta la vista, baby!"
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    miniGunAnimation()
    gameDisplay.blit(wyvern,[250,0])
    gameDisplay.blit(miniGun,[600,200])
    line1 = "The dragon takes 999,999,999,999,999"
    line2 = "999,999,999,999,999,999,999,999,999"
    line3 = "999,999,999,999,999,999,999,999,999"
    line4 = "999,999,999,999,999,999,999 damage!!!"
    DialogBox.displayText(line1,orange,line2,orange,line3,\
    orange,line4,orange,False)
    weapons.weaponAnimations = True
    weapons.miniGunLower()
    weapons.weaponAnimations = False
    audio.dragonMoan.play()
    gameDisplay.blit(deadDragon,[250,0])
    line1 = "Your ammo runs dry and the blood-covered"
    line2 = "beast hits the ground with and tremorous."
    line3 = "*thump*!"
    line4 = ""
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    audio.pygame.mixer.music.fadeout(3000)
    line1 = "You did it! You cleared the way for escape!"
    line2 = "Finally you can get out of this cursed"
    line3 = "maze and go..."
    line4 = ""
    audio.leprechaunLaugh.play()
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    line1 = "You did it! You cleared the way for escape!"
    line2 = "Finally you can get out of this cursed"
    line3 = "maze and go..."
    line4 = "What is that sound? Laughing?"
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    leprechaunDialog()
    
miniGun = pygame.image.load('pictures/weapons/miniGun3.png')
def miniGunAnimation():
    miniGun2 = pygame.image.load('pictures/weapons/miniGun4.png')
    splats = pygame.image.load('pictures/weapons/splat.png')
    frames = 0
    audio.miniGunAttack.play()
    while frames < 320:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit() 
        
        frames += 1 
        
        x,y = random.randint(500,650),random.randint(150,250)
        clock.tick(35)        
        gameDisplay.blit(wyvern2,[250,0])
        gameDisplay.blit(miniGun2,[600,203])
        gameDisplay.blit(splats,[x,y])
        weapons.redrawBorders()
        pygame.display.update()

        x,y = random.randint(500,650),random.randint(150,250)
        gameDisplay.blit(wyvern,[250,0])
        gameDisplay.blit(miniGun,[600,196])
        gameDisplay.blit(splats,[x,y])
        weapons.redrawBorders()
        pygame.display.update()
        
lepCloseUp = pygame.image.load('pictures/monsters/evilLeprechaun3.jpg')
lepStandBack = pygame.image.load('pictures/monsters/leprechaun.png')
def leprechaunDialog():
    line1 = "'You have done well! VERY well! It has"
    line2 = "been a long time since I was able to pull"
    line3 = "anyone into this realm. I was starting to"
    line4 = "lose hope.''"
    DialogBox.displayText(line1,green,line2,green,line3,\
    green,line4,green,False)       
    line1 = "You recognize that voice. You have heard"
    line2 = "it down here before. The air begins to "
    line3 = "grow heavy with an evil presense." 
    line4 = ""
    audio.pygame.mixer.music.load('Audio/sephiroth.ogg')
    audio.pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.4)
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    line1 = "'Most would just die by traps or get lost"
    line2 = "and slowly starve to death. I even tried"
    line3 = "to free myself by creating armies but" 
    line4 = "none were any match for that dragon!''"
    DialogBox.displayText(line1,green,line2,green,line3,\
    green,line4,green,False)
    line1 = "'Too long. Too long have I wasted away"
    line2 = "in these depths, deceived into searching"
    line3 = "for some non-existing artifact. But now," 
    line4 = "now I am free, thanks to your stupidity!''"
    DialogBox.displayText(line1,green,line2,green,line3,\
    green,line4,green,False)
    line1 = "You turn rapidly in every direction trying"
    line2 = "to find the source of that voice."
    line3 = "" 
    line4 = ""
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)  
    line1 = "You turn rapidly in every direction trying"
    line2 = "to find the source of that voice."
    line3 = "Then you see him..." 
    line4 = ""
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    gameDisplay.blit(lepCloseUp,[250,0])
    line1 = "                              'BOO!''"
    line2 = ""
    line3 = "" 
    line4 = ""
    DialogBox.displayText(line1,green,line2,green,line3,\
    green,line4,green,False)
    line1 = "                              'BOO!''"
    line2 = "'Bwaaa hahahahahahahahaha!"
    line3 = "Whats the matter? Didnt recognize me" 
    line4 = "without that stupid fake nose and hat?''"
    DialogBox.displayText(line1,green,line2,green,line3,\
    green,line4,green,False)
    line1 = "'Would you have trusted me had I looked"
    line2 = "like any of my other minions creeping"
    line3 = "around down here?'" 
    line4 = ""
    DialogBox.displayText(line1,green,line2,green,line3,\
    green,line4,green,False)
    line1 = "'Thats right, all the enormous mutations"
    line2 = "lurking about were merely my prior failed"
    line3 = "attempts of escape. Eventually they all" 
    line4 = "went rogue and I lost control over them.'"
    DialogBox.displayText(line1,green,line2,green,line3,\
    green,line4,green,False)
    line1 = "'But none of that matters now. I have you"
    line2 = "to thank for slaying my jailor. At last"
    line3 = "I am free to return to the world of men." 
    line4 = "I have been locked away for so long.'"
    DialogBox.displayText(line1,green,line2,green,line3,\
    green,line4,green,False)
    line1 = "'Oh how I miss the days of pludering and"
    line2 = "destroying. Once my full strength is"
    line3 = "restored it will be just like old times." 
    line4 = "I will once again be known and feared!'"
    DialogBox.displayText(line1,green,line2,green,line3,\
    green,line4,green,False)
    line1 = "'Oh, but dont worry, I wont make you"
    line2 = "whitness the terror that will spread."
    line3 = "I will reward you for giving me my" 
    line4 = "freedom by granting you a swift death!'"
    DialogBox.displayText(line1,green,line2,green,line3,\
    green,line4,green,False)
    fadeOutAni(25,None)
    exitFadeIn()
    
fadeOut = pygame.image.load('pictures/rooms/fadeOut.png')
def fadeOutAni(speed,priorMenu):
    for i in range(70):
        clock.tick(speed)
        gameDisplay.blit(fadeOut,[250,0])
        if i == 20 and priorMenu == blackOut:
            line1 = "Everything is going dark..."
            line2,line3,line4 = "","",""
            weapons.weaponAnimations = True
            eval(text)
            weapons.weaponAnimations = False
        weapons.redrawBorders()
        pygame.display.update()

lepSitting = pygame.image.load('pictures/monsters/leprechaunSitting1.png')        
exitCavern = pygame.image.load('pictures/rooms/caveExit.jpg')
exitCavern2 = pygame.image.load('pictures/rooms/caveExit2.png')        

def exitFadeIn():
    global punishBattle
    x = 70 
    for i in range(70):
        clock.tick(40)
        gameDisplay.blit(exitCavern2,[250,0])
        gameDisplay.blit(lepSitting,[250,0])
        weapons.redrawBorders()
        pygame.display.update()
    gameDisplay.blit(exitCavern,[250,0])
    gameDisplay.blit(lepSitting,[250,0])
    line1 = "'Never let it be said that I am not a"
    line2 = "good sport. I know how hard you have"
    line3 = "worked to build your fighting skills." 
    line4 = "Go ahead and take your best shot.'"
    DialogBox.displayText(line1,green,line2,green,line3,\
    green,line4,green,False)
    randMonster.monsterPic = lepSitting
    randMonster.monsterBackground = exitCavern
    randMonster.monsterRoar = audio.leprechaunLaugh
    combat.battle = True
    punishBattle = True
    combat.monsterHealth = 3000
    combat.totalMhealth = 3000
    randMonster.randMonster('boss','random')
    #combat.combatOptions()

def fleePunish():
    line1 = "There is nowhere to run!"
    line2,line3,line4 = "","",""
    DialogBox.displayText(line1,yellow,line2,green,line3,\
    green,line4,green,False)
    combat.combatOptions()
    
def defendPunish():
    line1 = "He is waiting for you to attack."
    line2,line3,line4 = "","",""
    DialogBox.displayText(line1,yellow,line2,green,line3,\
    green,line4,green,False)
    combat.combatOptions()
    
taunt = 0
def leprechaunTaunt():
    global taunt
    if taunt == 0:
        line1 = "Your attack passes through open air. How"
        line2 = "could you completely miss him? He was"
        line3 = "holding absolutely still!" 
        line4 = ""
        DialogBox.displayText(line1,yellow,line2,yellow,line3,\
        yellow,line4,green,False)
        line1 = "'Nice swing, but blows that dont land"
        line2 = "dont hurt. Why dont you try again.'"
        line3 = "" 
        line4 = ""
        DialogBox.displayText(line1,green,line2,green,line3,\
        green,line4,green,False)
    elif taunt == 1:
        audio.parryAttack.play()
        line1 = "'Hahahaha! Very noble of you but you are"
        line2 = "predictable and your blows are easy to"
        line3 = "block.'" 
        line4 = ""
        DialogBox.displayText(line1,green,line2,green,line3,\
        green,line4,green,False)
        gameDisplay.blit(lepCloseUp,[250,0])
        line1 = "'I tell you what, I am going to stand here"
        line2 = "completely still. I want you to hit me as"
        line3 = "hard as you can!'" 
        line4 = ""
        DialogBox.displayText(line1,green,line2,green,line3,\
        green,line4,green,False)
        gameDisplay.blit(exitCavern,[250,0])
        gameDisplay.blit(lepSitting,[250,0])
    elif taunt == 2:
        audio.monsterHit.play()
        line1 = "You strike with all your strength."
        line2 = "The leprechaun takes 0 damage!"
        line3 = "" 
        line4 = ""
        DialogBox.displayText(line1,yellow,line2,orange,line3,\
        green,line4,green,False)
        line1 = "'Pathetic! Your useless flailing reminds"
        line2 = "me of a squirming worm on a hook."
        line3 = "I have seen enough of your puniness. Now" 
        line4 = "witness real power!'"
        DialogBox.displayText(line1,green,line2,green,line3,\
        green,line4,green,False)
        combat.escape == True
        leprePunishAttack() 
    taunt += 1
    
def leprePunishAttack():
    weapons.monsterTakeDamage()
    audio.lepDissapear.play()
    weapons.monsterTakeDamage()
    gameDisplay.blit(exitCavern,[250,0])
    line1 = "What the-"
    line2 = ""
    line3 = "" 
    line4 = ""
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    audio.leprechaunLaugh.play()
    line1 = "What the-"
    line2 = "Where did he go? He couldnt have just..."
    line3 = "" 
    line4 = ""
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    
    # Double slash ownage
    weapons.weaponAnimations = True
    currentHealth = savables.health
    
    audio.whipSound.play()
    time.sleep(.4)
    savables.health -= ((currentHealth/2)-1)
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    punishDamageAnimation1()
    
    audio.whipSound.play()
    time.sleep(.4)
    savables.health = 1
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    punishDamageAnimation2()
    
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    time.sleep(2)
    line1,line2 = "You take...",""
    DialogBox.displayText(line1,orange,line2,yellow,line3,\
    yellow,line4,yellow,False)
    time.sleep(2)
    line2 = "          ...a lot of damage..."
    DialogBox.displayText(line1,orange,line2,orange,line3,\
    yellow,line4,yellow,False)
    weapons.weaponAnimations = False
    time.sleep(1.5)
    blackOut()
    
blood1 = pygame.image.load('pictures/rooms/final/bloodStreak1.png')
blood2 = pygame.image.load('pictures/rooms/final/bloodStreak2.png')
def punishDamageAnimation1():
    shakes,x,y = 0,250,0
    monsterLair = randMonster.monsterBackground
    monsterPic = randMonster.monsterPic        
    def compress():
        gameDisplay.blit(monsterLair,[x,y])
        weapons.redrawBorders()
        gameDisplay.blit(blood1,[450,-50])
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
        
def punishDamageAnimation2():
    shakes,x,y = 0,250,0
    monsterLair = randMonster.monsterBackground
    monsterPic = randMonster.monsterPic        
    def compress():
        gameDisplay.blit(monsterLair,[x,y])
        weapons.redrawBorders()
        gameDisplay.blit(blood1,[450,-50])
        gameDisplay.blit(blood2,[300,100])
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
        
def blackOut():
    fadeOutAni(10,blackOut)
    line1 = "Everything is going dark..."
    eval(text)
    line2 = "You can't continue."
    eval(text)
    line3 = "But you know you must."
    audio.pygame.mixer.music.fadeout(5000)
    eval(text)
    line1,color1,line2,line3 = "'You must!'",blue,"",""
    eval(text)
    line2,color2 = "'You must continue!'",blue
    eval(text)
    line1,color1,line2 = "Who's there?",yellow,""
    eval(text)
    line1,color1,line2,color2 = "'This is YOUR realm, not his.'",blue,"",blue
    eval(text)
    line2 = "'You control what is and what will be.'"
    eval(text)
    line3, color3 = "'You are more powerful. Don't give up!'",blue
    eval(text)
    line4,color4 = "'It is time for me to help you.'",blue
    eval(text)
    weaponsMerge()
    
staff = pygame.image.load('pictures/weapons/boStaff.png')
sword = pygame.image.load('pictures/weapons/sword3.png')
fireRing = pygame.image.load('pictures/weapons/fireRingSmall.png')
iceAmulet = pygame.image.load('pictures/weapons/iceAmuletSmall.png')
black = pygame.image.load('pictures/blackBackground.jpg')
    
def weaponsMerge():
    weapons.weaponAnimations = True    
    angle1,angle2 = 0,0
    swordEntry = -25
    staffEntry = 1175
    iceY,fireY = 575,610
    
    while iceY > 135:
        clock.tick(40)
        eval(text)
        pygame.display.update()
        gameDisplay.blit(black,[250,0])
        audio.slowSwoosh.play() if (angle1+0) % 190 == 0 else "" 
        
        if swordEntry < 575:
            swordEntry += 5
            staffEntry -= 5
        
        oldRect = sword.get_rect(center = (swordEntry,200))
        oldRect2 = sword.get_rect(center = (staffEntry,200))         
        
        if iceY > 135:
            angle1 += 5
            angle2 -= 5
        
        swordSpin, newRect = rot_center(sword,oldRect,angle1)
        gameDisplay.blit(swordSpin,newRect)
        
        staffSpin, newRect = rot_center(staff,oldRect2,angle2)
        gameDisplay.blit(staffSpin,newRect)
        
        weapons.redrawBorders()
        
        if swordEntry >= 575:
            if iceY > 135:
                iceY -= 5       
                fireY -= 5
            gameDisplay.blit(fireRing,[330,fireY])
            gameDisplay.blit(iceAmulet,[770,iceY])
    runeFeatherAppear()
    
def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect

def runeFeatherAppear():
    audio.parryAttack.play()
    whiteOut = pygame.image.load('pictures/whiteOut.png')
    featherFade = pygame.image.load('pictures/weapons/runeFeatherFadeIn.png')
    for i in range(25):
        clock.tick(30)
        gameDisplay.blit(whiteOut,[250,0])
        weapons.redrawBorders()
        pygame.display.update()
    for i in range(30):
        clock.tick(10)
        gameDisplay.blit(featherFade,[250,0])
        weapons.redrawBorders()
        pygame.display.update()
    weapons.weaponAnimations = False
    line1 = "Runefeather appears!"
    eval(text)
    savables.health += DialogBox.maxHealth
    line1 = "Your health is restored!"
    eval(text)
    line1 = "You feel stronger."
    eval(text)
    line2 = "        You feel faster."
    eval(text)
    line3 = "                You feel more alert."
    eval(text)
    line4 = "You feel ready to fight!"
    eval(text)