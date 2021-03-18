import tkinter as tk


class InputLabel(tk.Label):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, takefocus=True, highlightthickness=1, *args,
                         **kwargs)
        self.pad = 3
        self.cursor = tk.Frame(self, width=1)
        self.bind('<Button-1>', self.placeCursor)

    def placeCursor(self, *args, **kwargs):
        self.focus_set()
        self.cursor.configure(background=self['fg'],
                              height=self.winfo_height() - 3 * self.pad)
        self.cursor.place(x=10)


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
