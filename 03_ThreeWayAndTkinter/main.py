import tkinter as tk
import tkinter.messagebox as tkm
import random


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.boardSize = 4
        self.nums = list(range(1, self.boardSize ** 2 + 1))
        self.target = list(range(1, self.boardSize ** 2 + 1))
        self.idxHidden = self.boardSize ** 2 - 1
        self.tiles = list()

        self.menuPad = 4
        self.boardPad = 1

        self.menuColor = '#f1d18a'
        self.menuColorActv = '#e2c275'
        self.boardColor = '#f1d18a'
        self.boardColorActv = '#e2c275'
        self.backColor = '#eadca6'
        self.textColor = '#222831'
        self.textColorActv = '#222831'

        self.frameMenu = tk.Frame(self.master)
        self.frameBoard = tk.Frame(self.master)
        self.menuFont = ("Calibri", 20, "italic")
        self.boardFont = ("Calibri", 20)

        self.master['background'] = self.backColor
        self.frameMenu['background'] = self.backColor
        self.frameBoard['background'] = self.backColor

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.frameMenu.pack(fill=tk.X, side=tk.TOP, pady=self.menuPad)
        self.frameBoard.pack(fill=tk.BOTH, expand=1, padx=self.boardPad)

        self.frameMenu.columnconfigure(0, weight=1)
        self.frameMenu.columnconfigure(1, weight=1)

        for i in range(self.boardSize):
            self.frameBoard.columnconfigure(i, weight=1)
            self.frameBoard.rowconfigure(i, weight=1)

        self.createBoard(self.frameBoard)
        self.createMenubar(self.frameMenu)

    def new(self):
        self.createBoard(self.frameBoard)

    def showTile(self, idx):
        self.tiles[idx].grid(row=idx // self.boardSize,
                             column=idx % self.boardSize, sticky="NSWE",
                             padx=self.boardPad, pady=self.boardPad)

    def swap(self, idx1, idx2):
        self.nums[idx1], self.nums[idx2] = self.nums[idx2], self.nums[idx1]
        self.tiles[idx1]['text'] = self.nums[idx1]
        self.tiles[idx2]['text'] = self.nums[idx2]

    def moveTile(self, idx):
        dist = abs(idx - self.idxHidden)
        if (dist == self.boardSize or dist == 1 and
                idx // self.boardSize == self.idxHidden // self.boardSize):
            self.swap(idx, self.idxHidden)
            self.showTile(self.idxHidden)
            self.tiles[idx].grid_forget()
            self.idxHidden = idx
            if self.nums == self.target:
                self.win()

    def win(self):
        tkm.showinfo("Win", "You win!")
        self.new()

    def isSolvable(self):
        empty = 0
        self.nums.append(empty)
        sum = 0
        for i in range(len(self.nums)):
            tileA = self.nums[i]
            for j in range(i + 1, len(self.nums)):
                tileB = self.nums[j]
                if tileA != empty and tileB != empty and tileB < tileA:
                    sum += 1
        self.nums.remove(empty)
        return (sum % 2 == 0) == (self.idxHidden // self.boardSize % 2 == 1)

    def createMenubar(self, parent):
        self.newButton = tk.Button(parent, text='New', command=self.new,
                                   font=self.menuFont,
                                   background=self.menuColor,
                                   activebackground=self.menuColorActv,
                                   foreground=self.textColor,
                                   activeforeground=self.textColorActv)
        self.quitButton = tk.Button(parent, text='Quit', command=self.quit,
                                    font=self.menuFont,
                                    background=self.menuColor,
                                    activebackground=self.menuColorActv,
                                    foreground=self.textColor,
                                    activeforeground=self.textColorActv)
        self.newButton.grid(row=0, column=0)
        self.quitButton.grid(row=0, column=1)

    def createBoard(self, parent):
        self.nums = list(range(1, self.boardSize ** 2))
        while self.nums == self.target[:-1] or not self.isSolvable():
            random.shuffle(self.nums)
        self.nums.append(self.boardSize ** 2)
        if not self.tiles:
            for i in range(len(self.nums)):
                tile = tk.Button(parent, text=self.nums[i],
                                 command=lambda idx=i: self.moveTile(idx),
                                 font=self.boardFont, width=3,
                                 background=self.boardColor,
                                 activebackground=self.boardColorActv,
                                 foreground=self.textColor,
                                 activeforeground=self.textColorActv)
                self.tiles.append(tile)
                self.showTile(i)
        else:
            for i in range(len(self.nums)):
                self.tiles[i]['text'] = self.nums[i]
            self.showTile(self.idxHidden)
        self.idxHidden = self.boardSize ** 2 - 1
        self.tiles[-1].grid_forget()


def main():
    app = Application()
    app.master.title('15')
    app.mainloop()


if __name__ == "__main__":
    main()
