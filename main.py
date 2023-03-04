from tkinter import *
from tkinter import simpledialog
import Hanoi_tower_solver as solver
import time



class Graph(Frame):
    def __init__(self, master=None, layer=10, manualMode = True):
        super().__init__(master, height=350, width=600)
        self.master = master
        self.pack(side='bottom')
        self.manualMode = manualMode
        if not manualMode:
            solution = solver.solver(layer, sequence=[])
            self.solution = solution
            print(self.solution)

        self.move_input = []
        self.createWidget()
        self.createPosition(layer)

    def createPosition(self, layer):
        if layer < 3:
            layer = 3
        r = [60 - i * (30/(layer-1)) for i in range(layer)]
        self.plate_height = 180/layer
        if self.plate_height > 30:
            self.plate_height = 30
        self.plate = []
        for i in range(len(r)):
            i = len(r) - i - 1
            self.plate.append(self.cnv.create_rectangle(125-r[i], 250-(i+1)*self.plate_height, 125+r[i], 250-i*self.plate_height))
        self.left = [layer - i - 1 for i in range(layer)]
        self.middle = []
        self.right = []

    def createWidget(self):
        self.cnv = Canvas(self, height=300, width=600)
        self.cnv.place(x = 0, y = 0)
        self.cnv.create_line(300, 50, 300, 250)
        self.cnv.create_line(125, 50, 125, 250)
        self.cnv.create_line(475, 50, 475, 250)
        self.cnv.create_line(50, 250, 550, 250)
        self.cnv.create_line(0, 300, 600, 300)
        if self.manualMode:
            self.btn1 = Button(self, text = "1", command=self.btn1_click)
            self.btn2 = Button(self, text = "2", command=self.btn2_click)
            self.btn3 = Button(self, text = "3", command=self.btn3_click)
            self.btn1.place(x = 125, y = 335, anchor='s')
            self.btn2.place(x = 300, y = 335, anchor='s')
            self.btn3.place(x = 475, y = 335, anchor='s')
        else:
            self.btn4 = Button(self, text = "run", command=self.run)
            self.btn4.place(x = 300, y = 335, anchor='s')

    def btn1_click(self):
        self.move_input.append('left')
        if len(self.move_input) == 2:
            self.move(self.move_input)
            self.move_input = []

    def btn2_click(self):
        self.move_input.append('middle')
        if len(self.move_input) == 2:
            self.move(self.move_input)
            self.move_input = []

    def btn3_click(self):
        self.move_input.append('right')
        if len(self.move_input) == 2:
            self.move(self.move_input)
            self.move_input = []

    def isValid(self, moves):
        if moves[0] == 'left':
            if len(self.left) > 0:
                plate = self.left[-1]
            else:
                plate = float('inf')
        elif moves[0] == 'middle':
            if len(self.middle) > 0:
                plate = self.middle[-1]
            else:
                plate = float('inf')
        elif moves[0] == 'right':
            if len(self.right) > 0:
                plate = self.right[-1]
            else:
                plate = float('inf')
        else:
            plate = float('inf')
        if moves[1] == 'left':
            if len(self.left) > 0:
                dest = self.left[-1]
            else:
                dest = float('inf')
        elif moves[1] == 'middle':
            if len(self.middle) > 0:
                dest = self.middle[-1]
            else:
                dest = float('inf')
        elif moves[1] == 'right':
            if len(self.right) > 0:
                dest = self.right[-1]
            else:
                dest = float('inf')
        else:
            plate = float('inf')
        return plate < dest

    def move(self, moves):
        print(moves)
        if self.isValid(moves):
            if moves[0] == "left":
                if moves[1] == "middle":
                    self.left, self.middle = self.move_2(self.left, self.middle, 175)
                elif moves[1] == "right":
                    self.left, self.right = self.move_2(self.left, self.right, 350)
            elif moves[0] == "middle":
                if moves[1] == "left":
                    self.middle, self.left = self.move_2(self.middle, self.left, -175)
                elif moves[1] == "right":
                    self.middle, self.right = self.move_2(self.middle, self.right, 175)
            elif moves[0] == "right":
                if moves[1] == "left":
                    self.right, self.left = self.move_2(self.right, self.left, -350)
                elif moves[1] == "middle":
                    self.right, self.middle = self.move_2(self.right, self.middle, -175)

    def move_2(self, stat, dest, distance):
        self.cnv.move(self.plate[stat[-1]], distance, self.plate_height * (len(stat)-len(dest)-1))
        dest.append(stat[-1])
        stat = stat[:-1]
        return stat, dest
    
    def run(self):
        for i in self.solution:
            self.move(i)
            self.cnv.update()
            time.sleep(0.1)

class Option(Frame):
    def __init__(self, master=None, layer=3):
        super().__init__(master, height=50, width=600)
        self.master = master
        self.pack(side='bottom')
        self.game = Graph(master=root)

        self.createWidget()

    def createWidget(self):
        self.btn1 = Button(self, text='Manual', command=self.manual)
        self.btn2 = Button(self, text='Auto', command=self.auto)
        self.btn1.place(x = 200, y = 35, anchor='s')
        self.btn2.place(x = 400, y = 35, anchor='s')

    def manual(self):
        layer = simpledialog.askinteger(title = 'Manual Play',prompt='Layers：',initialvalue = '3')
        if layer is not None:
            self.game.destroy()
            self.game = Graph(master=root, layer=layer)

    def auto(self):
        layer = simpledialog.askinteger(title = 'Manual Play',prompt='Layers：',initialvalue = '3')
        if layer is not None:
            self.game.destroy()
            self.game = Graph(master=root, layer=layer, manualMode=False)


if __name__ == "__main__":
    root = Tk()
    root.geometry('600x400+200+300')
    root.title('Hanoi tower')

    opt = Option(master=root)
    #graph = Graph(master=root, layer=10)

    root.mainloop()
