import pgzrun
import time

WIDTH=800
HEIGHT=600

TITLE="recycle game"

START_SPEED = 10
ITEMS=["bag","battery","bottle","chips"]

FINAL_LEVEL = 6
current_level = 1
#lose the game
game_over=False
#win the game
game_complete = False

items=[]
animations=[]

def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit("bground", (0,0))
    if game_over:
        display_message("GAME OVER", "try again")
    if game_complete:
        display_message("GAME completed","you've won!")
    else:
        #using forloop drawing each of the item in items list
        for item in items:
            item.draw()

def display_message(heading,subheading):
    screen.draw.text(heading, fontsize=60, center=(400,300), color="black")
    screen.draw.text(subheading, fontsize=30, center=(400,330), color="black")

def update():
    global items
    #checking if the list is empty
    if len(items)== 0:
        items = make_items(current_level)

#make items
#1 get the options from items list - random
#2 create actors and add it to items list
#3 layout items - display them with equal spacing
#4 animations - move the objects down

def make_items(number_of_extra_items):
    item_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(item_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items


def get_option_to_create(number_of_extra_items):
    pass

def create_items(item_to_create):
    pass

def layout_items(new_items):
    pass

def animate_items(new_items):
    pass

    














pgzrun.go()