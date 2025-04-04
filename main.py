import pgzrun
import time
import random 

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
    items_to_create = ["paper"]
    for i in range(0, number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(item_to_create):
    newitems=[]
    for i in item_to_create:
        items=Actor(i+"img")
        newitems.append(items)
    return newitems

def layout_items(items_to_layout):
    gaps=len(items_to_layout)+1
    gap_size=WIDTH/gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout):
        new_x_pos = (index + 1) * gap_size
        item.x = new_x_pos

def animate_items(items_to_animate):
    global animations
    for i in items_to_animate:
        duration=START_SPEED-current_level
        animation=animate(i,duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over=True
    
def on_mouse_down(pos):
    global items
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global current_level,items,animations,game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete=True
    else:
        current_level=current_level+1
        items=[]
        animations=[]

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()









pgzrun.go()
