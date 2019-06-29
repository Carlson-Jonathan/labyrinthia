import DialogBox

green,yellow,orange,red = (0,225,0),\
(240,240,0),(255,155,0),(255,0,0)
line1,line2,line3,line4 = 0,0,0,0

def ladder():
    line1 = "You climb the ladder to a sealed hatch at"
    line2 = "at the top. You try to bash it open but it"
    line3 = "is securely fastened. There is nowhere"
    line4 = "else to go but back down the ladder."
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    corridor1.start()
    
def grandRoom():
    line1 = "You come to a grand junction room. There"
    line2 = "are many doors and corridors branching"
    line3 = "off of this room. There is no way of"
    line4 = "telling where they might lead to."
    DialogBox.displayText(line1,yellow,line2,yellow,line3,\
    yellow,line4,yellow,False)
    
def grandRoomOptions():
    line1 = "What will you do?"     
    line2 = "Open door                  Drink a potion"
    line3 = "Random Corridor"
    line4 = "Yell for Help"
    DialogBox.displayText(line1,yellow,line2,green,line3,\
    green,line4,green,False)
        
    
    