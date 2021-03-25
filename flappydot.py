import tkinter as tk
import random 
from gamelib import Sprite, GameApp, Text

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

UPDATE_DELAY = 33
STARTING_VELOCITY = -30 
GRAVITY = 2.5
JUMP_VELOCITY = -20

class Dot(Sprite):
    def init_element(self):
        self.vy = STARTING_VELOCITY
        self.is_started = False 

    def update(self):
        if self.is_started:
            self.y += self.vy
            self.vy += GRAVITY
    
    def start(self):
        self.is_started = True
    
    def jump(self):
        self.vy = JUMP_VELOCITY
    
    def is_out_of_screen(self):
        return self.x, self.y

class FlappyGame(GameApp):
    def create_sprites(self):
        self.dot = Dot(self, 'images/dot.png', CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
        self.elements.append(self.dot)
        self.create_pillar()
         # self.pillar_pair = Pillarpair(self, 'images/pillar-pair.png', CANVAS_WIDTH, CANVAS_HEIGHT//1)
         # self.elements.append(self.pillar_pair)
    def create_pillar(self):
        random_pillar_height = self.random_height() # random size of pillar
        random_pillar_side = random.randint(1, 2) 
        # random pillar side where random number is 1 pillar will top will take more space.
        # if random number is 2 pillar bottom will take more space
        if random_pillar_side == 1 :
            self.pillar_top = Pillarpair(self, 'images/pillar-top.png', CANVAS_WIDTH, CANVAS_HEIGHT-650+random_pillar_height)
            self.elements.append(self.pillar_top)
            self.pillar_bottom = Pillarpair(self, 'images/pillar-bottom.png', CANVAS_WIDTH, CANVAS_HEIGHT+150+random_pillar_height)
            self.elements.append(self.pillar_bottom)
        elif random_pillar_side == 2 :
            self.pillar_top = Pillarpair(self, 'images/pillar-top.png', CANVAS_WIDTH, CANVAS_HEIGHT-650-random_pillar_height)
            self.elements.append(self.pillar_top)
            self.pillar_bottom = Pillarpair(self, 'images/pillar-bottom.png', CANVAS_WIDTH, CANVAS_HEIGHT+150-random_pillar_height)
            self.elements.append(self.pillar_bottom)


    def random_height(self): # method that random pillar height
        h = random.randint(0, 150)
        return h

    def init_game(self):
        self.create_sprites()

    def pre_update(self):
        pass

    def post_update(self):
        super().post_update()
    
    def on_key_pressed(self, event):
        self.elements[0].start()
        self.elements[0].jump()

        self.elements[1].is_started = True
        self.elements[2].is_started = True

class Pillarpair(Sprite):
    def init_element(self):
        self.is_started = False

    def update(self):
        if self.is_started:
            self.x -= 5

    def is_out_of_screen(self): #method that check pillar position
        return self.x, self.y

    def reset_position(self): # method that move pillar that out of screen to right side 
        self.x = CANVAS_WIDTH


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Monkey Banana Game")
 
    # do not allow window resizing
    root.resizable(False, False)
    app = FlappyGame(root, CANVAS_WIDTH, CANVAS_HEIGHT, UPDATE_DELAY)
    app.start()
    root.mainloop()