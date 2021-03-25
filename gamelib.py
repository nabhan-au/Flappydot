import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

class GameCanvasElement():
    def __init__(self, game_app, x=0, y=0):
        self.x = x
        self.y = y
        self.canvas = game_app.canvas

        self.is_visible = True

        self.init_canvas_object()
        self.init_element()

    def show(self):
        self.is_visible = True
        self.canvas.itemconfigure(self.canvas_object_id, state="normal")

    def hide(self):
        self.is_visible = False
        self.canvas.itemconfigure(self.canvas_object_id, state="hidden")

    def render(self):
        if self.is_visible:
            self.canvas.coords(self.canvas_object_id, self.x, self.y)

    def init_canvas_object(self):
        pass

    def init_element(self):
        pass

    def update(self):
        pass

class Text(GameCanvasElement):
    def __init__(self, game_app, text, x=0, y=0):
        self.text = text
        super().__init__(game_app, x, y)

    def init_canvas_object(self):
        self.canvas_object_id = self.canvas.create_text(
            self.x, 
            self.y,
            text=self.text)

    def set_text(self, text):
        self.text = text
        self.canvas.itemconfigure(self.canvas_object_id, text=text)
        

class Sprite(GameCanvasElement):
    def __init__(self, game_app, image_filename, x=0, y=0):
        self.image_filename = image_filename
        super().__init__(game_app, x, y)

    def init_canvas_object(self):
        self.photo_image = tk.PhotoImage(file=self.image_filename)
        self.canvas_object_id = self.canvas.create_image(
            self.x, 
            self.y,
            image=self.photo_image)


class GameApp(ttk.Frame): 
    def __init__(self, parent, canvas_width=800, canvas_height=500, update_delay=33):
        super().__init__(parent)
        self.parent = parent
        
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        
        self.update_delay = update_delay

        self.grid(sticky="news")
        self.create_canvas()

        self.elements = []
        self.init_game()

        self.parent.bind('<KeyPress>', self.on_key_pressed)
        self.parent.bind('<KeyRelease>', self.on_key_released)
        
    def create_canvas(self):
        self.canvas = tk.Canvas(self, borderwidth=0,
            width=self.canvas_width, height=self.canvas_height, 
            highlightthickness=0)
        self.canvas.grid(sticky="news")

    def animate(self):
        self.pre_update()

        for element in self.elements:
            element.update()
            element.render()

        self.post_update()

        self.after(self.update_delay, self.animate)

    def start(self):
        self.after(0, self.animate)

    def init_game(self):
        pass

    def pre_update(self):
        pass

    def post_update(self):
        a = ''
        for i in self.elements:
            if i == self.elements[1]:
                x ,y = i.is_out_of_screen()
                if x > 0:
                    if x % 300 == 0:
                        a = self.random_height()
                elif x == 0:
                    i.reset_position()
            elif i == self.elements[0]:
                x,y = i.is_out_of_screen()
                if y > 500:
                    messagebox.showinfo(title='Popup',
                    message="You lose")
                    self.destroy()
                elif y < 0:
                    messagebox.showinfo(title='Popup',
                    message="You lose")
                    self.destroy()
                for i in range(1, len(self.elements)):
                    x1 , y1  = self.elements[i].is_out_of_screen()
                    if x >= x1 - 40 and x <= x1 + 40:
                        if y > y1 + 100 or y < y1 - 100:
                            messagebox.showinfo(title='Popup',
                            message="You lose")
                            self.destroy()
            elif i != self.elements[0] and i != self.elements[1]:
                x,y = i.is_out_of_screen()
                if x < 0 :
                    self.elements.remove(i)
        if a != '':
            self.elements.append(a)
            if self.elements[1].is_started == True:
                self.elements[-1].is_started = True

    def on_key_pressed(self, event):
        pass

    def on_key_released(self, event):
        pass