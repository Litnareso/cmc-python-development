import tkinter as tk
import random


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.boardSize = 4
        self.nums = list(range(1, self.boardSize ** 2))
        self.tiles = list()

        self.frameMenu = tk.Frame(self.master)
        self.frameBoard = tk.Frame(self.master)
        self.menuFont = ("Calibri", 20, "italic")
        self.boardFont = ("Calibri", 20)

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.frameMenu.pack(fill=tk.X, side=tk.TOP)
        self.frameBoard.pack(fill=tk.BOTH, expand=1)

        self.frameMenu.columnconfigure(0, weight=1)
        self.frameMenu.columnconfigure(1, weight=1)

        for i in range(self.boardSize):
            self.frameBoard.columnconfigure(i, weight=1)
            self.frameBoard.rowconfigure(i, weight=1)

        self.createBoard(self.frameBoard)
        self.createMenubar(self.frameMenu)

    def new(self):
        pass

    def moveTile(self):
        pass

    def createMenubar(self, parent):
        self.newButton = tk.Button(parent, text='New', command=self.new,
                                   font=self.menuFont)
        self.quitButton = tk.Button(parent, text='Quit', command=self.quit,
                                    font=self.menuFont)
        self.newButton.grid(row=0, column=0)
        self.quitButton.grid(row=0, column=1)

    def createBoard(self, parent):
        self.nums = list(range(1, self.boardSize ** 2))
        random.shuffle(self.nums)
        self.tiles.clear()
        for i in range(len(self.nums)):
            self.tiles.append(tk.Button(parent, text=str(self.nums[i]),
                                        command=self.moveTile,
                                        font=self.boardFont))
            self.tiles[i].grid(row=i // self.boardSize,
                               column=i % self.boardSize, sticky="NSWE")


def main():
    app = Application()
    app.master.title('15')
    app.mainloop()


if __name__ == "__main__":
    main()
