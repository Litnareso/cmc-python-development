import tkinter as tk
import tkinter.font as tkFont


class InputLabel(tk.Label):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, takefocus=True, highlightthickness=1,
                         anchor='w', *args, **kwargs)

        self.fontConf = tkFont.Font(font=self['font'])
        self.fontConf.configure(family='Courier')
        self['font'] = self.fontConf

        self.cursor = tk.Frame(self, width=1)
        self.bind('<Button-1>', self.placeCursor)

    def placeCursor(self, *args, **kwargs):
        self.pad = self.winfo_height() // 10
        self.focus_set()
        self.cursor.configure(background=self['fg'],
                              height=self.winfo_height() - 3 * self.pad)
        if len(self['text']):
            self.wid = self.fontConf.measure(self['text']) / len(self['text'])
        else:
            self.wid = 2
        self.coord = min(round((args[0].x - self.wid / 4) / self.wid),
                         len(self['text']))
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
        self.str.set('testtesttest')
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
