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
            self.y +=self.vy
            self.vy += GRAVITY
    
    def start(self):
        self.is_started = True
    
    def jump(self):
        self.vy = JUMP_VELOCITY

class FlappyGame(GameApp):
    def create_sprites(self):
        self.dot = Dot(self, 'images/dot.png', CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
        self.elements.append(self.dot)
        self.create_pillar() # call method that will create pillar

    def create_pillar(self):
        pillar_size = random.randint(150,350) # random which pillar will take more space
        self.pillar_pair = Pillarpair(self, 'images/pillar-pair.png', CANVAS_WIDTH, CANVAS_HEIGHT-pillar_size)
        self.elements.append(self.pillar_pair)

        
    def init_game(self):
        self.create_sprites()

    def pre_update(self):
        pass

    def post_update(self):
        pass

    def on_key_pressed(self, event):
        pass

class Pillarpair(Sprite):
    def update(self):
        self.x -= 5


    def is_out_of_screen(self): #method that check pillar position
        return self.x , self.y

    def reset_position(self): #method that delete pillar that out of screen
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Banana Game")
 
    # do not allow window resizing
    root.resizable(False, False)
    app = FlappyGame(root, CANVAS_WIDTH, CANVAS_HEIGHT, UPDATE_DELAY)
    app.start()
    root.mainloop()
