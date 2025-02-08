from tkinter import *
import random
import time

tk = Tk()


# class Ball
class Ball:
    def __init__(self, canvas, paddle, score_label, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

        self.score_label = score_label
        self.score = 0

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        self.pos = pos
        # print(self.pos)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[3] >= self.canvas_height:
            self.y = -3
        if self.hit_paddle(pos) == True:
            self.y = -3
            self.score += 1
            self.canvas.itemconfig(self.score_label, text=str(self.score))
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


# class Paddle
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-a>", self.turn_left)
        self.canvas.bind_all("<KeyPress-d>", self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -2.5

    def turn_right(self, evt):
        self.x = 2.5


# make Window
tk.title("PINGBALL")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=400, height=400, bd=0, highlightthickness=0)

score_label = canvas.create_text(
    70, 15, text="0", fill="black", font=("Helvetica", 15, "bold")
)
canvas.create_text(30, 15, text="Score", fill="black", font=("Helvetica 15 bold"))

canvas.pack()
tk.update()

# define Classes
paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, score_label, "red")

# main loop
while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    else:
        canvas.create_text(ball.pos[0], ball.pos[1] - 10, text="GAME OVER", fill="red")
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
