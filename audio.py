import pygame

pygame.mixer.pre_init(44100, -16, 1, 512) #<-- fixes sound lag delay :D
pygame.init()

''''
music = ('Audio/battle.ogg')
bossBattleMusic = ('Audio/bossBattle.ogg')
finalBattleMusic = ('Audio/finalBattle.ogg')
pygame.mixer.music.set_volume(.2)
'''

drawSword = pygame.mixer.Sound('Audio/swordDraw.ogg')
drawSword.set_volume(.3)

inferno = pygame.mixer.Sound('Audio/fireDoorExplosion.ogg')
inferno.set_volume(.15)

fireBurn = pygame.mixer.Sound('Audio/fire.ogg')
fireBurn.set_volume(.2)

getItem1 = pygame.mixer.Sound('Audio/getItem1.ogg')
getItem1.set_volume(.2)
getItem2 = pygame.mixer.Sound('Audio/getItem2.ogg')
getItem2.set_volume(.2)

splash = pygame.mixer.Sound('Audio/splash.ogg')
splash.set_volume(.2)

weaponSwoosh = pygame.mixer.Sound('Audio/weaponSwoosh.ogg')
weaponSwoosh.set_volume(.3)

punch = pygame.mixer.Sound('Audio/punch.ogg')
punch.set_volume(.2)

monsterHit = pygame.mixer.Sound('Audio/strike2.ogg')
monsterHit.set_volume(.2)

parryAttack = pygame.mixer.Sound('Audio/swordecho.ogg')
parryAttack.set_volume(.1)

gunRoomLaugh = pygame.mixer.Sound('Audio/gunRoomLaugh.ogg')
gunRoomLaugh.set_volume(.2)

metriodAcquire = pygame.mixer.Sound('Audio/itemAcquasition.ogg')
metriodAcquire.set_volume(.6)

levelUp = pygame.mixer.Sound('Audio/levelup.ogg')
levelUp.set_volume(.2)

doorSound = pygame.mixer.Sound('Audio/door_2.ogg')
doorSound.set_volume(.2)

arrowTick = pygame.mixer.Sound("Audio/tick.ogg")
arrowTick.set_volume(.2)

selectTick = pygame.mixer.Sound("Audio/select.ogg")
selectTick.set_volume(.2)

textForward = pygame.mixer.Sound('Audio/textForward.ogg')
textForward.set_volume(.2)

heartBeat = pygame.mixer.Sound('Audio/Hearbeat.ogg')
heartBeat.set_volume(.7)

scream = pygame.mixer.Sound('Audio/scream.ogg')
scream.set_volume(.5)

match = pygame.mixer.Sound('Audio/match.ogg')
match.set_volume(.4)

hillaryLaugh = pygame.mixer.Sound('Audio/Hillary2.ogg')
hillaryLaugh.set_volume(.2)

growling = pygame.mixer.Sound('Audio/monsters/growling.ogg')
growling.set_volume(.5)

whipSound = pygame.mixer.Sound('Audio/monsters/whipAttack.ogg')
whipSound.set_volume(.5)

monsterAttackSound = pygame.mixer.Sound('Audio/monsters/whipAttack.ogg')
monsterRoar = pygame.mixer.Sound('Audio/monsters/roar.ogg')

ouch = pygame.mixer.Sound('Audio/whack.ogg')
ouch.set_volume(.2)

iceAttackSound = pygame.mixer.Sound('Audio/iceAttack.ogg')
iceAttackSound.set_volume(.2)

freezing = pygame.mixer.Sound('Audio/freeze.ogg')
freezing.set_volume(.3)

shatterArmor = pygame.mixer.Sound('Audio/shatterArmor.ogg')
shatterArmor.set_volume(.3)

bleed = pygame.mixer.Sound('Audio/bleed.ogg')
bleed.set_volume(.5)

iceWind = pygame.mixer.Sound('Audio/iceWind.ogg')
iceWind.set_volume(.3)

gunLoad = pygame.mixer.Sound('Audio/gunLoad.ogg')
gunLoad.set_volume(.3)

potionDrink = pygame.mixer.Sound('Audio/potion2.ogg')
potionDrink.set_volume(.4)

bluePotion = pygame.mixer.Sound('Audio/potion.ogg')
bluePotion.set_volume(.4)

metalGleam = pygame.mixer.Sound('Audio/metalGleam.ogg')
metalGleam.set_volume(.4)

miniSwoosh = pygame.mixer.Sound('Audio/monsters/goblinAttack.ogg')
miniSwoosh.set_volume(.5)

saveGame = pygame.mixer.Sound('Audio/saveGame.ogg')
loadGame = pygame.mixer.Sound('Audio/gameLoad.ogg')

alchemy = pygame.mixer.Sound('Audio/alchemy.ogg')
alchemy.set_volume(.4)

chaChing = pygame.mixer.Sound('Audio/chaChing.ogg')
chaChing.set_volume(.4)

toilet = pygame.mixer.Sound('Audio/toiletFlush.ogg')
toilet.set_volume(.4)

miniGunAttack = pygame.mixer.Sound('Audio/miniGunAttack.ogg')
miniGunAttack.set_volume(.4)

leprechaunLaugh = pygame.mixer.Sound('Audio/monsters/leprechaunLaugh.ogg')
leprechaunLaugh.set_volume(.7)

dryMiniGun = pygame.mixer.Sound('Audio/dryMiniGun.ogg')
dryMiniGun.set_volume(.4)

dragonMoan = pygame.mixer.Sound('Audio/monsters/dragonMoan.ogg')
dragonMoan.set_volume(.4)

dragonRoar = pygame.mixer.Sound('Audio/monsters/dragon.ogg')
dragonRoar.set_volume(.4)

lepDissapear = pygame.mixer.Sound('Audio/lepreMagic.ogg')
lepDissapear.set_volume(.4)

slowSwoosh = pygame.mixer.Sound('Audio/slowSwoosh.ogg')
slowSwoosh.set_volume(.3)
