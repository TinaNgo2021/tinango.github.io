# DO NOT MODIFY THIS FILE!!!!!!!!
# DO NOT MODIFY THIS FILE!!!!!!!!


from __future__ import division, print_function

import game
window = None

def setup():
    global window
    size(game.WIDTH, game.HEIGHT)
    imageMode(CENTER)
    window = game.Window()
    

def draw():
    background(game.BACKGROUND_COLOR)
    window.on_draw()
