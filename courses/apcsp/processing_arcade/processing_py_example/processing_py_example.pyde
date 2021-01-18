# DO NOT MODIFY THIS FILE!!!!!!!!
# DO NOT MODIFY THIS FILE!!!!!!!!


from __future__ import division, print_function

import game

window = None

def setup():
    global window
    size(game.WIDTH, game.HEIGHT)
    rectMode(CENTER)
    imageMode(CENTER)
    window = game.Window()
    

def draw():
    background(game.BACKGROUND_COLOR)
    window.on_draw()
    window.on_update()

def keyPressed():
    if key == CODED:
        window.on_key_press(keyCode)
    else:
        window.on_key_press(key)
    
def keyReleased():
    if key == CODED:
        window.on_key_release(keyCode)
    else:
        window.on_key_release(key)

def mouseMoved():
    window.on_mouse_motion(mouseX, mouseY)

def mousePressed():
    window.on_mouse_press(mouseX, mouseY, mouseButton)

def mouseReleased():
    window.on_mouse_release(mouseX, mouseY, mouseButton)
