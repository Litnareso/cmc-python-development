import tkinter as tk
import random


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.frameMenu = tk.Frame(self.master)
        self.frameBoard = tk.Frame(self.master)
        self.nums = list(range(1, 16))
        self.tiles = list()
        self.grid()
        self.createMenubar(self.frameMenu)
        self.createBoard(self.frameBoard)

    def new(self):
        pass

    def moveTile(self):
        pass

    def createMenubar(self, parent):
        parent.grid()
        self.newButton = tk.Button(parent, text='New', command=self.new)
        self.quitButton = tk.Button(parent, text='Quit', command=self.quit)
        self.newButton.grid()
        self.quitButton.grid(row=0, column=1)

    def createBoard(self, parent):
        random.shuffle(self.nums)
        self.tiles.clear()
        parent.grid()
        for i in range(len(self.nums)):
            self.tiles.append(tk.Button(parent, text=str(self.nums[i]),
                                        command=self.moveTile))
            self.tiles[i].grid(row=i // 4, column=i % 4)


def main():
    app = Application()
    app.master.title('15')
    app.mainloop()


if __name__ == "__main__":
    main()
