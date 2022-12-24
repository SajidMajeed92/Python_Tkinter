from tkinter import *
import random, time


class Snake(Tk):
    def __init__(self, *arge, **kwargs):
        Tk.__init__(self, *arge, **kwargs)
        self.initialSetup()

    def initialSetup(self):
        self.base = Canvas(self, width=500, height=500)
        self.base.pack(padx=10, pady=10)
        self.snake = self.base.create_rectangle(1, 1, 21, 21, fill="DodgerBlue2")
        self.score = 0
        self.scoreDisplay = Label(self, text="Score:{}".format(self.score), font=('arial', 20, 'bold'))
        self.scoreDisplay.pack(anchor='n')
        self.length = 3
        self.target = None
        self.gameStatus = 1
        self.x = 20
        self.y = 0
        self.bodycoords = [(0, 0)]
        self.bind('<Any-KeyPress>', self.linkKeys)
        return

    def check_snake_coords(self):
        self.base.move(self.snake, self.x, self.y)
        i, j, ii, jj = self.base.coords(self.snake)
        if i <= 0 or j <= 0 or ii >= 500 or jj >= 500:
            self.x = 0
            self.y = 0
            # gameover
            self.base.create_text(220, 220, text="GAME OVER", font=('arial', 40, 'bold'), fill='red')
            self.gameStatus = 0
        return

    def move_snake(self):
        i, j, ii, jj = self.base.coords(self.snake)
        ii = (ii - ((ii - i) / 2))
        jj = (jj - ((jj - j) / 2))
        self.bodycoords.append((ii, jj))
        self.base.delete('snakebody')
        if len(self.bodycoords) >= self.length:
            self.bodycoords = self.bodycoords[-self.length:]
        self.base.create_line(tuple(self.bodycoords), tag='snakebody', width=20, fill="DodgerBlue2")
        return

    def food(self):
        if self.target == None:
            a = random.randint(20, 480)
            b = random.randint(20, 480)
            self.target = self.base.create_oval(a, b, a + 20, b + 20, fill='red', tag='food')
            # print(self.base.coords(self.target))
        if self.target:
            # print(self.base.coords(self.target))
            i, j, ii, jj = self.base.coords(self.target)
            # time.sleep(0.1)
            if len(self.base.find_overlapping(i, j, ii, jj)) != 1:
                self.base.delete("food")
                self.target = None
                self.updateScore()
                self.length += 1
            return

    def updateScore(self):
        self.score += 1
        self.scoreDisplay['text'] = "Score : {}".format(self.score)
        return

    def linkKeys(self, event=None):
        pressedkey = event.keysym
        if pressedkey == 'Left':
            self.x = -20
            self.y = 0

        elif pressedkey == 'Up':
            self.x = 0
            self.y = -20

        elif pressedkey == 'Right':
            self.x = 20
            self.y = 0

        elif pressedkey == 'Down':
            self.x = 0
            self.y = 20

        else:
            pass
        return

    def manage(self):
        if (self.gameStatus == 0):
            return
        self.check_snake_coords()
        self.move_snake()
        self.food()

        return


snakeobj = Snake(className="Snake Game")
while True:
    snakeobj.update()
    snakeobj.update_idletasks()
    snakeobj.manage()
    time.sleep(0.4)
