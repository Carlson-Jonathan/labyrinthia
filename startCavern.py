import DialogBox,pygame,randMonster,combat,corridor1,audio,savables
gameDisplay = pygame.display.set_mode((900,600))
green,yellow,orange = (0,225,0),(240,240,0),(255,155,0)

openCavern = pygame.image.load('pictures/rooms/bigRoom.jpg')
startDoor = pygame.image.load('pictures/rooms/tunnelDoor3.jpg')

def startingCavern():
    gameDisplay.blit(openCavern,[250,0])
    DialogBox.displayText("You get up and find yourself in a large",yellow,
    "spaceous cavern. As you look around you",yellow,
    "see no flames or other sources of light but",yellow,
    "the surrounding area is well lit. Weird.",yellow,False)
    DialogBox.displayText("A low growling can be heard from",yellow,
    "a dark corner of the cave. Before you",yellow,
    "even have time to decide whether or not",yellow,
    "to investigate, a creature springs out!",yellow,False)
    randMonster.randMonster("weak","random")
    gameDisplay.blit(openCavern,[250,0])
    DialogBox.displayText("You are badly injured. Clearly this place",yellow,
    "is dangerous! You must find a way out as",yellow,
    "quickly as you can! There is no way back",yellow,
    "the way you came, but you see a door.",yellow,False)
    gameDisplay.blit(startDoor,[250,0])
    DialogBox.displayText("This appears to be your only option unless",yellow,
    "you would rather stay here and wait for",yellow,
    "something else to pounce on you from",yellow,
    "the darkness.",yellow,False)
    healthPotion = pygame.image.load('pictures/items/health_potion.png')
    gameDisplay.blit(healthPotion,[440,80])
    DialogBox.displayText("On the door knob you see a vial of red",yellow,
    "liquid hanging from a chain. You think",yellow,
    "this might make you feel better if you",yellow,
    "drink it. Are there more of these around?",yellow,False)
    savables.healthPotions +=1 
    gameDisplay.blit(startDoor,[250,0])
    audio.doorSound.play()
    DialogBox.displayText("You approach the door and it opens with",yellow,
    "a creek. You slowly walk through not",yellow,
    "having any idea what to expect on the",yellow,
    "other side...",yellow,False)
    corridor1.startText()