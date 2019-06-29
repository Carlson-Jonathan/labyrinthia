import random,DialogBox,pygame,corridor1,audio,savables
gameDisplay = pygame.display.set_mode((900,600))
green,yellow,orange,red = (0,225,0),(240,240,0),(255,155,0),(255,0,0)
opt2,opt3,opt4,opt5 = False,False,False,False

def leprechaunOptionsComplete():
    DialogBox.menuType = "fourChoiceMenu"
    DialogBox.displayText("What will you do?",yellow,
        "     Train Skills                Leave",green,
        "     Ask about quest          ",green,
        "     Ask about...             ",green,True)
    leprechaunSelection(leprechaunOptionsComplete)

def leprechaunOptions():
    if opt2 == True and opt3 == True and opt4 == True and opt5 == True and savables.opt6 == True:
        savables.allMenuItemsComplete = True 
    leprechaunOptionsComplete() if savables.allMenuItemsComplete == True else ""
    DialogBox.displayText("What will you do?",yellow,
        "     Approach him            Walk away",green,
        "     Attack him                Threaten him",green,
        "     Do nothing                 Make fun of him",green,True)
    leprechaunSelection(leprechaunOptions)

stickAround = True
def leprechaunSelection(priorMenu):
    global stickAround
    choiceNum = (DialogBox.selectionx*DialogBox.selectiony)
    if choiceNum == 3:
        if priorMenu == leprechaunOptions and savables.opt1 == False: 
            leprechaunApproach() 
        elif priorMenu == leprechaunOptions and savables.opt1 == True: 
            leprechaunApproach2()
        swordSkills() if priorMenu == leprechaunTraining else ""
        leprechaunTraining() if priorMenu == leprechaunOptionsComplete else ""
    elif choiceNum == 4:
        leprechaunAttack() if priorMenu == leprechaunOptions else ""
        staffSkills() if priorMenu == leprechaunTraining else ""
        leprechaunQuest() if priorMenu == leprechaunOptionsComplete else ""
    elif choiceNum == 5:
        leprechaunNothing() if priorMenu == leprechaunOptions else ""
        otherSkills() if priorMenu == leprechaunTraining else ""
        askAbout() if priorMenu == leprechaunOptionsComplete else ""    
    elif choiceNum == 6:
        leprechaunLeave() if priorMenu == leprechaunOptions else ""
        stickAround = False if priorMenu == leprechaunOptionsComplete else ""
    elif choiceNum == 8:
        leprechaunThreaten()
    elif choiceNum == 10:
        leprechaunMock() if savables.opt6 == False else leprechaunMock2()
    leprechaunOptions() if stickAround else ""
    corridor1.grandRoom()
    
def leprechaunApproach():
    savables.opt1 = True
    DialogBox.displayText("You step forward toward the freakish",yellow,
    "little freak hoping to get a better look at",yellow,
    "how freakish he is. As you get closer, he",yellow,
    "cringes away and startles.",yellow,False)
    DialogBox.displayText("The leprechaun then bolts toward you with",yellow,
    "a tiny dagger and pokes you in the knee.",yellow,
    "",yellow,"",yellow,False)
    damage = random.randint(20,30)
    DialogBox.displayText("You take %d damage!"%damage,orange,
    "The leprechaun then dissapears behind",yellow,
    "the door which vanishes as quickly as",yellow,
    "it appeared.",yellow,False)
    savables.health -= damage
    
def leprechaunApproach2():
    DialogBox.displayText("That didnt turn out to well the last time",yellow,
    "you tried it. This guy is obviously paranoid.",yellow, 
    "Better try something else instead.",yellow,
    "",yellow,False)

def leprechaunAttack():
    global opt2
    opt2 = True 
    DialogBox.displayText("First rule of video games:",yellow,
    "Attack EVERYTHING!",red,
    "...and if it dies, it was bad.",yellow,"",yellow,False)
    DialogBox.displayText("You draw your weapon and swing at",yellow,
    "the ugly little freak. Your swing hits",yellow,
    "nothing but air and the leprechaun",yellow,
    "is gone. You hear a voice from behind you,",yellow, False)
    DialogBox.displayText("'What do ya think yer doin flailing around",green,
    "so clumsily like that? You call that an",green,
    "attack? Surely you need some training",green,
    "there or you'll never win in a fight!'",green,False)
    DialogBox.displayText("'I can teach ya a thing'er two about using",green,
    "a sword or even a staff. Down here you'll",green,
    "need skills or you'll never survive!'",green,
    "",yellow,False)
    leprechaunTraining()
    
def leprechaunTraining():
    DialogBox.displayText("'Keep in mind that I can't teach you to use",green,
    "a weapon that you have never so much as",green,
    "held before. When you find a weapons and",green,
    "have had a bit of practice with it, see me.'",green,False)
    DialogBox.menuType = "threeChoiceMenu"
    DialogBox.displayText("'What is it you would like to learn?'",green,
    "     Sword Skills",green,
    "     Staff Skills",green,
    "     Other Skills",green,True)
    leprechaunSelection(leprechaunTraining)

def swordSkills():
    if savables.swordSkill == 0 and savables.swordTick <= -56:
        savables.swordTick = 0
        parrySkill() 
    elif savables.swordSkill == 1 and savables.swordTick <= -56:
        savables.swordTick = 0
        riposteSkill()
    elif savables.swordSkill == 2:
        DialogBox.displayText("'I have taught you all I can about using",yellow,
        "swords. You must learn additional skills",green,
        "elsewhere. I have heard that there are",green,
        "weapons masters in the sewers somewhere.'",green,False)
    else:
        DialogBox.displayText("'You need to bloody up a sword before",green,
        "I can teach you any advanced techniques!",green,
        "Go kill some monsters with a sword. When",green,
        "your sword skillbar fills, come see me.'",green,False)

def parrySkill():
    DialogBox.displayText("'So ya wish to be a swordsman eh?",green,
    "A valuable skill to have! It looks like",green,
    "have a nice blade there with plenty of",green,
    "monster blood already on it to boot!'",green,False)
    DialogBox.displayText("'Let me show you a trick you can do with",green,
    "the sword when a fat ugly beast throws",green,
    "its claws at you. This will help protect",green,
    "you in a fight by blocking attacks.'",green,False)
    DialogBox.displayText("...",yellow,"practice...practice...",yellow,
    "...",yellow,"still practicing...",yellow,False)
    DialogBox.displayText("'There ya go, you got it!  In fact,",green,
    "you get a gold star for proficiency!'",green,"",green,"",green,False)
    audio.levelUp.play()
    DialogBox.displayText("                      New Sword Skill:",yellow,
    "                              Parry",green,
    "                        Now available!",yellow,"",yellow,False)
    savables.swordSkill = 1
    
def riposteSkill():
    DialogBox.displayText("'Your skills with the sword have increased",green,
    "quite a bit! You might even be a challenge",green,
    "for me someday! You have more to learn.",green,
    "Your next lesson is quite useful.'",green,False)
    DialogBox.displayText("'Once you have mastered the parry ability,",green,
    "you can land a hard counterattack on your",green,
    "foe called a 'riposte'. You are essentially",green,
    "turning their own attack against them.'",green,False)
    DialogBox.displayText("...",yellow,"practice...practice...",yellow,
    "...",yellow,"still practicing...",yellow,False)
    DialogBox.displayText("'There ya go, you got it!  In fact,",green,
    "you get a gold star for proficiency!'",green,"",green,"",green,False)
    audio.levelUp.play()
    DialogBox.displayText("                      New Sword Skill:",yellow,
    "                             Riposte",green,
    "                        Now available!",yellow,"",yellow,False)
    savables.swordSkill = 2
        
def staffSkills():
    if savables.staffSkill == 0 and savables.staffTick <= -56:
        savables.staffTick = 0
        doubleStrikeSkill() 
    elif savables.staffSkill == 1 and savables.staffTick <= -56:
        savables.staffTick = 0
        tripleStrikeSkill()
    elif savables.staffSkill == 2:
        DialogBox.displayText("'I have taught you all I can about using",green,
        "staffs. You must learn additional skills",green,
        "elsewhere. I have heard that there are",green,
        "weapons masters in the sewers somewhere.'",green,False)
    else:
        DialogBox.displayText("'You need to bloody up a staff before",green,
        "I can teach you any advanced techniques!",green,
        "Go kill some monsters with a staff. When",green,
        "your staff skillbar fills, come see me.'",green,False)

def doubleStrikeSkill():
    DialogBox.displayText("'Ahh the staff, a great weapon that can",green,
    "be forged from any stick or pole laying",green,
    "around. Looks like you found a nice sturdy",green,
    "white one too! Let me show you a trick...'",green,False)
    DialogBox.displayText("The leprechaun pulls out a pinyata.",yellow,
    "'If you hold it in the middle you can strike",green,
    "using both ends of the staff. This will let",green,
    "you land multiple blows on monster heads!'",green,False)
    DialogBox.displayText("...",yellow,"practice...practice...",yellow,
    "...",yellow,"still practicing...",yellow,False)
    DialogBox.displayText("'Very nice! You are doing well! I'd hate",green,
    "to be the poor fool who got in the way of",green,
    "those swings! I'll give you a gold star",green,
    "for your efficiency in staff fighting.'",green,False)
    audio.levelUp.play()
    DialogBox.displayText("                      New Staff Skill:",yellow,
    "                        Double Strike",green,
    "                        Now available!",yellow,"",yellow,False)
    savables.staffSkill = 1
    
def tripleStrikeSkill():
    DialogBox.displayText("'So you think yer gettin pretty adept with",green,
    "the staff eh? Well you can always get",green,
    "better. The 'double strike' technique is",green,
    "usefull but I'll show ya something better!",green,False)
    DialogBox.displayText("...",yellow,"practice...practice...",yellow,
    "...",yellow,"still practicing...",yellow,False)
    DialogBox.displayText("'Very nice! You are doing well! I'd hate",green,
    "to be the poor fool who got in the way of",green,
    "those swings! I'll give you a gold star",green,
    "for your efficiency in staff fighting.'",green,False)
    audio.levelUp.play()
    DialogBox.displayText("                      New Staff Skill:",yellow,
    "                        Triple Strike",green,
    "                        Now available!",yellow,"",yellow,False)
    savables.staffSkill = 2
        
def otherSkills():
    DialogBox.displayText("'There are other weapons besides just",green,
    "sticks and blades around. There are magic",green,
    "weapons that allow you to shoot fire and",green,
    "ice from your hands with only a thought!'",green,False)
    DialogBox.displayText("'They, like physical weapons, require",green,
    "practice in order to master. Unfortunately",green,
    "I am unskilled with such weapons and can",green,
    "teach you nothing if you aquire one.'",green,False)
        
def leprechaunNothing():
    global opt3
    opt3 = True 
    DialogBox.displayText("You sit and stare at the lreprechaun with",yellow,
    "wide eyes and a slack-jaw expression.",yellow,
    "You start to drool like a braindead video",yellow,
    "game player. The leprechaun then speaks,",yellow,False)
    DialogBox.displayText("'Poor thing. Poor pathetic thing. You have",green,
    "no idea where you are or what you",green,
    "should do, isnt that right? well I'll",green,
    "take pitty on ya and explain things.'",green,False)
    leprechaunQuest()
    
def leprechaunQuest():
    DialogBox.displayText("'This is Labyrinthia, a magical place of",green,
    "magical things and magical stuff. It",green,
    "is quite magical you came to be here",green,
    "and magic is needed to survivie.'",green,False)
    DialogBox.displayText("'Over the years I've accumulated quite",green,
    "a colleciton of magical artifacts including",green,
    "pink hearts, yellow moons, orange stars,",green,
    "purple horeshoes, green clovers and red...'",green,False)
    DialogBox.displayText("'Well, you get the picture.'",green,
    "",green,"",green,"",green,False)
    DialogBox.displayText("'In Labyrinthia rests the most powerful",green,
    "artifact, the 'Runefeather'! Help me find",green,
    "this artifact and I will make sure you get",green,
    "out of here alive and in once peice.'",green,False)
    DialogBox.displayText("'You can start by finding my partner from",green,
    "whom I was seperated after being",green,
    "ambushed by monsters. Surely he will have",green,
    "found some useful clues by now.'",green,False)
    
def leprechaunLeave():
    global opt4
    opt4 = True 
    DialogBox.displayText("This isnt the weirdest thing you have seen",yellow,
    "since you got here. You decide to leave.",yellow,
    "You turn around and scarcely take a step",yellow,
    "when the leprechaun speaks to you...",yellow,False)
    DialogBox.displayText("'Just where do ya think yer going in your",green,
    "condition? You wouldnt last 10 minutes in a",green,
    "place like this! Surely you need to know",green,
    "what yer doin to even stand a chance!'",green,False)
    DialogBox.displayText("'I could really care less if you end up a",green,
    "corpse but I'd be willing to give ya a few",green,
    "pointers. I'm just very a charitable",green,
    "person. What would you like to discuss?'",green,False)
    askAbout()
    
def askAbout():
    DialogBox.menuType = "fiveChoiceMenu"
    DialogBox.displayText("Ask about:",yellow,
    "     The Labyrinth            Items",green,
    "     Weapons                    Combat",green,
    "     Armor",green,True)
    leprechaunOptionsComplete()

def leprechaunThreaten():
    global opt5
    opt5 = True 
    DialogBox.displayText("What is it that leprechauns give people?",yellow,
    "Gold? Wishes? Luck? Chocolaty nugget?",yellow,
    "You demand the surrender of whatever",yellow,
    "the little green stuff-giver has- OR ELSE!",yellow,False)
    DialogBox.displayText("The leprechaun stares at you for a moment",yellow,
    "then begins to laugh uncontrollably.",yellow,
    "",yellow,"",yellow,False)
    DialogBox.displayText("'Just what exactly are ya ta'think yer",green,
    "any threat to me? I've encountered and",green,
    "survived far more dangerous things than",green,
    "you. Let me tell ya about monsters.'",green,False)
    askMonsters()
    
def askMonsters():
    DialogBox.displayText("'There are weak monsters, strong ones,",green,
    "and even stronger ones down here. The",green,
    "monsters of similar strength live together.",green,
    "Beware where you venture!'",green,False)
    DialogBox.displayText("'I wouldnt go down too many ladders or",green,
    "or you'll encounter some of the biggest",green,
    "beasts you've ever dreamed of, but if yer",green,
    "feeling lucky (or suicidal), go right ahead.'",green,False)

lepricaller = pygame.image.load('pictures/items/lepricaller.png') 
def leprechaunMock():
    savables.opt6 = True 
    DialogBox.displayText("You point and laugh at the little green",yellow,
    "goober with the big nose and funny hat.",yellow,
    "Then you start throwing as many short",yellow,
    "and ugly jokes at him as you can think of.",yellow,False)
    DialogBox.displayText("'Well yer not very nice are ya! I",green,
    "understand that overwhelming fear can",green,
    "make one irrational. Tell ya what, take a",green,
    "moment to regain your sanity, then call me.'",green,False)
    DialogBox.displayText("The leprechaun throws something to you",yellow,
    "then slams the door. The door then",yellow,
    "vanishes as quickly as it appeared.",yellow,"",yellow,False)
    audio.getItem1.play()
    audio.getItem2.play()
    gameDisplay.blit(lepricaller,[490,60])
    DialogBox.displayText("                          New Item:",yellow,
    "                          Leprecaller",green,
    "                        Now available!",yellow,"",yellow,False)
    leprechaunAppear = pygame.image.load('pictures/rooms/leprechaun.jpg')
    gameDisplay.blit(leprechaunAppear,[250,0])
    savables.leprecaller = True
    
def leprechaunMock2():
    DialogBox.displayText("It probably wouldnt do you any more good",yellow,
    "than it already has to make fun of the",yellow,
    "little freak. Try something else.",yellow,"",yellow,False)
    