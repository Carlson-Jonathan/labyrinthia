import random,pygame,DialogBox,combat,audio,finalBattle
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((900,600))
green,yellow = (0,225,0),(240,240,0)

monsterDamage, defaultMonsterPic,monsterPic,monsterRoar,\
monster,attackSound,monsterStrength,monsterBackground\
= 0,0,0,0,"",0,0,0

keyBattle = False
def randMonster(strength,dice):
    global monsterStrength,monsterPic
    monsterStrength = strength
    if dice == "random":
        roll = random.randint(1,5)
    else:
        roll = dice
    if strength == "weak":
        weakMonsters(roll)
    elif strength == "medium":
        mediumMonsters(roll)
    elif strength == "strong":
        strongMonsters(roll)
    elif strength == "boss":
        setLeprechaunPunish()
    if strength == "weak" or strength == "medium":
        if not keyBattle:
            audio.pygame.mixer.music.load('Audio/battle.ogg')
        else:
            audio.pygame.mixer.music.load('Audio/bossBattle.ogg') 
    elif strength == "strong":
        audio.pygame.mixer.music.load('Audio/bossBattle.ogg')
    monsterPic = defaultMonsterPic
    if not finalBattle.punishBattle:
        audio.monsterRoar.play() 
        audio.pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(.4)
        encounterAnimation()
        DialogBox.displayText("A %s suddenly attacks!"%monster,yellow,
                "",yellow,"",yellow,"",yellow,False)
    combat.combat()
    
zoomX,zoomY = 0,0
blitX,blitY = 575,200
def encounterAnimation():
    global zoomX,zoomY,blitX,blitY
    while zoomX < 640:
        clock.tick(80)
        zoomX += 34
        zoomY += 20
        blitX -= 17
        blitY -= 10
        zoom = pygame.transform.scale(defaultMonsterPic,[zoomX,zoomY])
        zoom2 = pygame.transform.scale(monsterBackground,[zoomX,zoomY])
        gameDisplay.blit(zoom2,(blitX,blitY))
        gameDisplay.blit(zoom,(blitX,blitY))
        pygame.display.update()
    gameDisplay.blit(monsterBackground,[250,0])
    gameDisplay.blit(defaultMonsterPic,[250,0])
    zoomX,zoomY = 0,0
    blitX,blitY = 575,200
    
def weakMonsters(roll):
    global monster,defaultMonsterPic,monsterBackground,monsterFrozenPic,monsterDamage
    if roll == 1:
        defaultMonsterPic = pygame.image.load('pictures/monsters/moleRat.png')
        monsterFrozenPic = pygame.image.load('pictures/monsters/modifiedMonsters/moleRatFrozen.png')
        monsterBackground = pygame.image.load('pictures/monsters/ratTunnel.jpg')
        monster = "Gnaked Gnawer"
        #monsterDamage = random.randint(5,15)
        audio.monsterRoar = pygame.mixer.Sound('Audio/monsters/rat.ogg')
        audio.monsterRoar.set_volume(.15)
        audio.monsterAttackSound = pygame.mixer.Sound('Audio/monsters/bite.ogg')
        audio.monsterAttackSound.set_volume(.15)
    elif roll == 2:
        defaultMonsterPic = pygame.image.load('pictures/monsters/terantula.png')
        monsterFrozenPic = pygame.image.load('pictures/monsters/modifiedMonsters/terantulaFrozen.png')
        monsterBackground = pygame.image.load('pictures/monsters/scorpionTunnel.jpg')
        monster = "Acromantula"
        #monsterDamage = random.randint(5,15)
        audio.monsterRoar = pygame.mixer.Sound('Audio/monsters/spiderRoar.ogg')
        audio.monsterRoar.set_volume(.3)
        audio.monsterAttackSound = pygame.mixer.Sound('Audio/monsters/spiderAttack.ogg')
        audio.monsterAttackSound.set_volume(.4)
    elif roll == 3:
        defaultMonsterPic = pygame.image.load('pictures/monsters/slime.png')
        monsterFrozenPic = pygame.image.load('pictures/monsters/modifiedMonsters/slimeFrozen.png')
        monsterBackground = pygame.image.load('pictures/monsters/slimeTunnel.jpg')
        monster = "Demon Slime" 
        #monsterDamage = random.randint(5,15)
        audio.monsterRoar = pygame.mixer.Sound('Audio/monsters/slimeRoar.ogg')
        audio.monsterRoar.set_volume(.4)
        audio.monsterAttackSound = pygame.mixer.Sound('Audio/monsters/slimeAttack.ogg')
        audio.monsterAttackSound.set_volume(.30)
    elif roll == 4:
        defaultMonsterPic = pygame.image.load('pictures/monsters/batKing.png')
        monsterFrozenPic = pygame.image.load('pictures/monsters/modifiedMonsters/batKingFrozen.png')
        monsterBackground = pygame.image.load('pictures/monsters/batRoom.jpg')
        monster = "Bat King"
        monsterDamage = random.randint(5,15)
        audio.monsterRoar = pygame.mixer.Sound('Audio/monsters/bats.ogg')
        audio.monsterRoar.set_volume(.15)
        audio.monsterAttackSound = pygame.mixer.Sound('Audio/monsters/batAttack.ogg')
        audio.monsterAttackSound.set_volume(.5)
    elif roll == 5:
        defaultMonsterPic = pygame.image.load('pictures/monsters/mantis.png')
        monsterFrozenPic = pygame.image.load('pictures/monsters/modifiedMonsters/mantisFrozen.png')
        monsterBackground = pygame.image.load('pictures/monsters/mantisTunnel.jpg')
        monster = "Killer Mantis"
        monsterDamage = random.randint(5,15)
        audio.monsterRoar = pygame.mixer.Sound('Audio/monsters/mantisRoar.ogg')
        audio.monsterRoar.set_volume(.3)
        audio.monsterAttackSound = pygame.mixer.Sound('Audio/monsters/goblinAttack.ogg')
        audio.monsterAttackSound.set_volume(.5)
        
def mediumMonsters(roll):
    global monster,defaultMonsterPic,monsterBackground,monsterFrozenPic,monsterDamage        
    if roll == 1: 
        defaultMonsterPic = pygame.image.load('pictures/monsters/minitaur.png')
        monsterFrozenPic = pygame.image.load('pictures/monsters/modifiedMonsters/minitaurFrozen.png')
        monsterBackground = pygame.image.load('pictures/monsters/minitaurArena.jpg')
        monster = "Minotaur"
        monsterDamage = random.randint(15,25)
        audio.monsterRoar = pygame.mixer.Sound('Audio/monsters/minataurRoar.ogg')
        audio.monsterRoar.set_volume(.3)
        audio.monsterAttackSound = pygame.mixer.Sound('Audio/monsters/minitaurAttack.ogg')
        audio.monsterAttackSound.set_volume(.6)
    elif roll == 2:
        defaultMonsterPic = pygame.image.load('pictures/monsters/goblin.png')
        monsterFrozenPic = pygame.image.load('pictures/monsters/modifiedMonsters/goblinFrozen.png')
        monsterBackground = pygame.image.load('pictures/monsters/goblinTunnel.jpg')
        monster = "Sinister Goblin"
        monsterDamage = random.randint(15,25)
        audio.monsterRoar = pygame.mixer.Sound('Audio/monsters/goblinRoar.ogg')
        audio.monsterRoar.set_volume(.3)
        audio.monsterAttackSound = pygame.mixer.Sound('Audio/monsters/goblinAttack.ogg')
        audio.monsterAttackSound.set_volume(.5)
    elif roll == 3:
        defaultMonsterPic = pygame.image.load('pictures/monsters/scorpion.png')
        monsterFrozenPic = pygame.image.load('pictures/monsters/modifiedMonsters/scorpionFrozen.png')
        monsterBackground = pygame.image.load('pictures/monsters/scorpionTunnel.jpg')
        monster = "Seismic Scorpion"
        monsterDamage = random.randint(15,25)
        audio.monsterRoar = pygame.mixer.Sound('Audio/monsters/scorpionRoar.ogg')
        audio.monsterRoar.set_volume(.15)
        audio.monsterAttackSound = pygame.mixer.Sound('Audio/monsters/scorpionAttack.ogg')
        audio.monsterAttackSound.set_volume(.2)
    elif roll == 4:
        defaultMonsterPic = pygame.image.load('pictures/monsters/snake.png')
        monsterFrozenPic = pygame.image.load('pictures/monsters/modifiedMonsters/snakeFrozen.png')
        monsterBackground = pygame.image.load('pictures/monsters/snakeTunnel.jpg')
        monster = "Venomous Anaconda"
        monsterDamage = random.randint(15,25)
        audio.monsterRoar = pygame.mixer.Sound('Audio/monsters/snakeRoar.ogg')
        audio.monsterRoar.set_volume(.3)
        audio.monsterAttackSound = pygame.mixer.Sound('Audio/monsters/snakehit.ogg')
        audio.monsterAttackSound.set_volume(.2)
    elif roll == 5:
        defaultMonsterPic = pygame.image.load('pictures/monsters/trog.png')
        monsterFrozenPic = pygame.image.load('pictures/monsters/modifiedMonsters/trogFrozen.png')
        monsterBackground = pygame.image.load('pictures/monsters/trogTunnel.jpg')
        monster = "Troglodtye Sentry"
        monsterDamage = random.randint(15,25)
        audio.monsterRoar = pygame.mixer.Sound('Audio/monsters/creatureLaugh.ogg')
        audio.monsterRoar.set_volume(.3)
        audio.monsterAttackSound = pygame.mixer.Sound('Audio/monsters/trogAttack.ogg')
        audio.monsterAttackSound.set_volume(.2)
        
def strongMonsters(roll):
    global monster,defaultMonsterPic,monsterBackground,monsterFrozenPic,monsterDamage
    if roll == 1:
        defaultMonsterPic = pygame.image.load('pictures/monsters/dementor.png')
        monsterFrozenPic = pygame.image.load('pictures/monsters/modifiedMonsters/dementorFrozen.png')
        monsterBackground = pygame.image.load('pictures/monsters/ratWay.jpg')
        monster = "Guardian Shade"
        monsterDamage = random.randint(25,50)
        audio.monsterRoar = pygame.mixer.Sound('Audio/monsters/ghostRoar.ogg')
        audio.monsterRoar.set_volume(.3)
        audio.monsterAttackSound = pygame.mixer.Sound('Audio/monsters/ghostAttack.ogg')
        audio.monsterAttackSound.set_volume(.2)
    elif roll == 2:
        defaultMonsterPic = pygame.image.load('pictures/monsters/troll.png')
        monsterFrozenPic = pygame.image.load('pictures/monsters/modifiedMonsters/trollFrozen.png')
        monsterBackground = pygame.image.load('pictures/monsters/trollCave.jpg')
        monster = "Collosal Troll"
        monsterDamage = random.randint(25,50)
        audio.monsterRoar = pygame.mixer.Sound('Audio/monsters/trollRoar.ogg')
        audio.monsterRoar.set_volume(.1)
        audio.monsterAttackSound = pygame.mixer.Sound('Audio/monsters/minitaurAttack.ogg')
        audio.monsterAttackSound.set_volume(.6)
    elif roll == 3:
        defaultMonsterPic = pygame.image.load('pictures/monsters/dog.png')
        monsterFrozenPic = pygame.image.load('pictures/monsters/modifiedMonsters/dogFrozen.png')
        monsterBackground = pygame.image.load('pictures/monsters/dogTunnel.jpg')
        monster = "Cerberus"
        monsterDamage = random.randint(25,50)
        audio.monsterRoar = pygame.mixer.Sound('Audio/monsters/dogRoar.ogg')
        audio.monsterRoar.set_volume(.4)
        audio.monsterAttackSound = pygame.mixer.Sound('Audio/monsters/dogAttack.ogg')
        audio.monsterAttackSound.set_volume(.2)
    elif roll == 4:
        defaultMonsterPic = pygame.image.load('pictures/monsters/balrog.png')
        monsterFrozenPic = pygame.image.load('pictures/monsters/modifiedMonsters/balrogFrozen.png')
        monsterBackground = pygame.image.load('pictures/monsters/balrogBackground.jpg')
        monster = "Giga-Demon"
        monsterDamage = random.randint(25,50)
        audio.monsterRoar = pygame.mixer.Sound('Audio/monsters/roar.ogg')
        audio.monsterRoar.set_volume(.3)
        audio.monsterAttackSound = pygame.mixer.Sound('Audio/monsters/whipAttack.ogg')
        audio.monsterAttackSound.set_volume(.3)
    elif roll == 5:
        defaultMonsterPic = pygame.image.load('pictures/monsters/earthElemental.png')
        monsterFrozenPic = pygame.image.load('pictures/monsters/modifiedMonsters/elementalFrozen.png')
        monsterBackground = pygame.image.load('pictures/monsters/elementalRoom.jpg')
        monster = "Earth Elemental"
        monsterDamage = random.randint(25,50)
        audio.monsterRoar = pygame.mixer.Sound('Audio/monsters/elemental.ogg')
        audio.monsterRoar.set_volume(.4)
        audio.monsterAttackSound = pygame.mixer.Sound('Audio/monsters/elementalAttack.ogg')
        audio.monsterAttackSound.set_volume(.7)
        
def setLeprechaunPunish():
    global monster,defaultMonsterPic,monsterBackground,\
    monsterFrozenPic,monsterDamage
    defaultMonsterPic = pygame.image.load('pictures/monsters/leprechaunSitting1.png')
    monsterFrozenPic = pygame.image.load('pictures/monsters/leprechaunSitting1.png')
    monsterBackground = pygame.image.load('pictures/rooms/caveExit.jpg')
    monster = "Leprechaun"
    monsterDamage = random.randint(100,200)
    audio.monsterRoar = pygame.mixer.Sound('Audio/monsters/elemental.ogg')
    audio.monsterRoar.set_volume(.4)
    audio.monsterAttackSound = pygame.mixer.Sound('Audio/monsters/trogAttack.ogg')
    audio.monsterAttackSound.set_volume(.2)
        