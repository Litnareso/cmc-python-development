import tkinter as tk
import tkinter.font as tkFont


class InputLabel(tk.Label):
    def __init__(self, master=None, text=None, textvariable=None,
                 *args, **kwargs):
        if textvariable is None:
            textvariable = tk.StringVar()
            textvariable.set(text)
        super().__init__(master, takefocus=True, highlightthickness=1,
                         anchor='w', textvariable=textvariable,
                         *args, **kwargs)

        self.textvariable = textvariable

        self.fontConf = tkFont.Font(font=self['font'])
        self.fontConf.configure(family='Courier')
        self['font'] = self.fontConf

        self.cursor = tk.Frame(self, width=1)
        self.bind('<Button-1>', self.placeCursor)
        self.bind('<KeyPress>', self.handler)

    def move(self, shift):
        self.coord = min(len(self['text']), max(0, self.coord + shift))
        self.cursor.place(x=round(self.wid * self.coord), y=self.pad)

    def handler(self, *args, **kwargs):
        if args[0].keysym == "BackSpace":
            self.removeChar()
        elif args[0].keysym == "Up" or args[0].keysym == "End":
            self.move(len(self['text']))
        elif args[0].keysym == "Down" or args[0].keysym == "Home":
            self.move(-len(self['text']))
        elif args[0].keysym == "Left":
            self.move(-1)
        elif args[0].keysym == "Right":
            self.move(1)
        else:
            if len(args[0].keysym) == 1 and args[0].keysym.isprintable():
                self.insert(args[0].keysym)
            elif args[0].keysym == "space":
                self.insert(" ")

    def placeCursor(self, *args, **kwargs):
        self.pad = self.winfo_height() // 10
        self.focus_set()
        self.cursor.configure(background=self['fg'],
                              height=self.winfo_height() - 3 * self.pad)
        if len(self['text']):
            self.wid = self.fontConf.measure(self['text']) / len(self['text'])
        else:
            self.wid = self.fontConf.measure('a')
        self.coord = min(round((args[0].x - self.wid / 4) / self.wid),
                         len(self['text']))
        self.cursor.place(x=round(self.wid * self.coord), y=self.pad)

    def insert(self, sym):
        str = self['text']
        self.textvariable.set(str[:self.coord] + sym + str[self.coord:])
        self.coord += 1
        self.cursor.place(x=round(self.wid * self.coord), y=self.pad)

    def removeChar(self):
        if len(self['text']) and self.coord > 0:
            str = self['text']
            self.textvariable.set(str[:self.coord - 1] + str[self.coord:])
            self.coord -= 1
            self.cursor.place(x=round(self.wid * self.coord), y=self.pad)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.createWidgets()

    def createWidgets(self):
        self.font = ("Calibri", 20)
        self.str = tk.StringVar()
        self.label = InputLabel(self, textvariable=self.str, font=self.font)
        self.quit = tk.Button(self, text='Quit', command=self.quit,
                              font=self.font)
        self.label.grid(sticky="WE")
        self.quit.grid()


def main():
    app = Application()
    app.master.title('Label Edit')
    app.mainloop()


if __name__ == "__main__":
    main()
