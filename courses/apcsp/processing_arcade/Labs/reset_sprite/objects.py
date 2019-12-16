"""
Simple Game Lab
We will be writing our first simple game in this lab!
We will write a simple game where the objective of the player is to evade the boss. 

Do the following:

1) Create a player and boss Sprite using "tank.png" and "boss.png". Initialize player on the left 
side of the screen and boss on the right side of the screen. If you are using Processing, use 
set_left(new_left) or set_right(new_right) methods. 
If you're using the original Arcade library, you can use 
self.player.left = new_left or self.player.right = new_right.

2) Move the player with arrow keys and move the boss with the mouse. 
3) If boss catch the player, player resets to the left side of the screen.
If you are using Processing, use set_left(new_left) method. 
If you're using the original Arcade library, you can use self.player.lives = new_left.
Use arcade.check_for_collision function which returns whether two sprites are colliding. 

4) Add a lives variable that keep track of the number of lives of the player, initialize it to 3.
5) Each time the player gets caught, decrease his lives by 1.
6) If the player's lives is 0, display "Game Over" and "Press r to restart" screen.
7) If user presses "r", call setup() to restart the game.


"""

from __future__ import division, print_function
import arcade
from constants import *

class Window:    
    def __init__(self):
        """ Declare the variables, set them to None. """
        self.player = None
        self.boss = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.player = arcade.Sprite("tank.png", 0.5)
        self.boss = arcade.Sprite("boss.png", 0.5)

        

    def on_draw(self):
        """ Called automatically 60 times a second to draw objects."""
        self.player.draw()

    def on_update(self):
        """ Called to update our objects. Happens approximately 60 times per second."""
        
        self.player.update()


    def on_mouse_motion(self, x, y, dx, dy):        
        """ Called whenever the mouse moves. """
        # if x is within width of rectangle and y within height of rectangle
        # return True otherwise return False.
        pass    
    
    def on_mouse_press(self, x, y, button):
        """ Called whenever the mouse is pressed. """

        pass
        
    def on_mouse_release(self, x, y, button):
        """ Called whenever the mouse is released. """
        pass
                  
    def on_key_press(self, key):
        """ Called automatically whenever a key is pressed. """
        if key == LEFT:
            self.player.change_x = -5
        elif key == RIGHT:
            self.player.change_x = 5
        elif key == UP:
            self.player.change_y = -5 
        elif key == DOWN:
            self.player.change_y = 5


    def on_key_release(self, key):
        """ Called automatically whenever a key is released. """
        if key == LEFT:
            self.player.change_x = 0
        elif key == RIGHT:
            self.player.change_x = 0
        elif key == UP:
            self.player.change_y = 0
        elif key == DOWN:
            self.player.change_y = 0
            
            
        
        
    
