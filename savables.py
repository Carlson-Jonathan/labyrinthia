import DialogBox,audio
yellow,red,green = (240,240,0),(255,0,0),(0,255,0)

dungeonSection = 2

healthPotions = 12
regenPotions = 4
emptyBottles = 10
megaPotions = 3
healthTanks = 4
armor = []

# Potential items: 
    # leprecaller
    # save orb

health = 100 

weaponInventory = ["fire","ice","staff","sword","gun"]

sprintShoes = True
leprecaller = True
saveOrb = True
magicRocks = True

swordMin,swordMax = 15,25
fireMin,fireMax = 1,50
iceMin,iceMax = 20,20
staffMin,staffMax = 15,20

fistSkill = 3
swordSkill = 3
staffSkill = 3
fireSkill = 3
iceSkill = 3
gunSkill = 3

chainmailSkill = 3 
breastPlateSkill = 3
battleSuiteSkill = 3

swordTick = 0
staffTick = 0
fireTick = 0
iceTick = 0

chainmailTick = 0
breastPlateTick = 0
battleSuiteTick = 0

# Menu and event non-repeatables:
# Leprechaun menu:
allMenuItemsComplete = False
opt1 = False
opt6 = False
# Regeneration Pool:
drankFromPool = False
snakePlaytime = False
#One-time Rooms:
grandRoomFirstVisit = True
miniGunFirstFire = True

# Save/Load Game Functions
def orb():
    DialogBox.displayText("Make your selection:",yellow,
    "     Save Game",green,
    "     Load Game",green,
    "     Cancel",green,True)
    choiceNum = (DialogBox.selectionx*DialogBox.selectiony)
    if choiceNum == 3:
        saveGame() 
    elif choiceNum == 4:
        loadGame() 
    elif choiceNum == 5:
        pass
    else:
        DialogBox.displayText("Invalid selection. Try again.",red,
        "",yellow,"",yellow,"",yellow,False)

def loadGame():
    DialogBox.displayText("Abandon current progress and load game?",yellow,
    "     Continue",green,
    "     Cancel",green,"",yellow,True)
    choiceNum = (DialogBox.selectionx*DialogBox.selectiony)
    if choiceNum == 4:
        pass
    elif choiceNum == 3:
        DialogBox.displayText("You feel the memories of some former",yellow,
        "life rush into you...",yellow,"",yellow,"",yellow,False)
        audio.loadGame.play()
        DialogBox.displayText("You feel the memories of some former",yellow,
        "life rush into you...",yellow,"                      Game Loaded!",green,
        "",yellow,False)
        import savedGame
        reload(savedGame)
        savedGame.loadGame()
    else:
        DialogBox.displayText("Invalid selection. Try again.",red,
        "",yellow,"",yellow,"",yellow,False)
        loadGame()

def saveGame():
    DialogBox.displayText("Overwite your previously saved game?",yellow,
    "     Continue",green,
    "     Cancel",green,"",yellow,True)
    choiceNum = (DialogBox.selectionx*DialogBox.selectiony)
    if choiceNum == 4:
        pass
    elif choiceNum == 3:
        with open('savedGame.py','w') as open_file:
            open_file.write('''
def loadGame():
    import savables
    savables.dungeonSection = %d
    savables.healthPotions = %d
    savables.regenPotions = %d
    savables.emptyBottles = %d
    savables.megaPotions = %d
    savables.healthTanks = %d
    savables.armor = %s
    savables.health = %d
    savables.weaponInventory = %s
    savables.sprintShoes = %s
    savables.leprecaller = %s
    savables.saveOrb = %s
    savables.swordMin = %d
    savables.swordMax = %d
    savables.fireMin = %d
    savables.fireMax = %d
    savables.iceMin = %d
    savables.iceMax = %d
    savables.staffmin = %d
    savables.staffMax = %d
    savables.fistSkill = %d
    savables.swordSkill = %d
    savables.staffSkill = %d
    savables.fireSkill = %d
    savables.iceSkill = %d
    savables.gunSkill = %d
    savables.chainmailSkill = %d
    savables.breastPlateSkill = %d
    savables.battleSuiteSkill = %d
    savables.allMenuItemsComplete = %s
    savables.opt1 = %s
    savables.opt6 = %s
    savables.drankFromPool = %s
    savables.snakePlaytime = %s
    savables.grandRoomFirstVisit = %s
    savables.miniGunFirstFire = %s
    savables.magicRocks %s
'''
%(dungeonSection,healthPotions,regenPotions,\
emptyBottles,megaPotions,healthTanks,armor,health,\
weaponInventory,sprintShoes,leprecaller,saveOrb,swordMin,\
swordMax,fireMin,fireMax,iceMin,iceMax,staffMin,\
staffMax,fistSkill,swordSkill,staffSkill,fireSkill,\
iceSkill,gunSkill,chainmailSkill,breastPlateSkill,\
battleSuiteSkill,allMenuItemsComplete,opt1,opt6,\
drankFromPool,snakePlaytime,grandRoomFirstVisit,\
miniGunFirstFire,magicRocks))
        DialogBox.displayText("You place your hand on the orb and see",yellow,
        "a vision of yourself right where you are.",yellow,"",yellow,"",yellow,False)
        audio.saveGame.play()
        DialogBox.displayText("You place your hand on the orb and see",yellow,
        "a vision of yourself right where you are.",yellow,"                       Game Saved!",green,
        "",yellow,False)
    else:
        DialogBox.displayText("Invalid selection. Try again.",red,
        "",yellow,"",yellow,"",yellow,False)
        saveGame()