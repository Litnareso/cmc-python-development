import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.frameText = tk.Frame(self.master)
        self.framePaint = tk.Frame(self.master)

        self.paintStyle = {'width': 2, 'fill': "white"}

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.frameText.pack(fill=tk.BOTH, side=tk.LEFT, expand=1)
        self.framePaint.pack(fill=tk.BOTH, side=tk.RIGHT, expand=1)

        self.frameText.columnconfigure(0, weight=1)
        self.frameText.rowconfigure(0, weight=1)

        self.framePaint.columnconfigure(0, weight=1)
        self.framePaint.rowconfigure(0, weight=1)

        self.createPaint(self.framePaint)
        self.createText(self.frameText)

    def createText(self, parent):
        self.descr = tk.Text(parent)
        self.descr.grid(sticky="NSWE")

    def createPaint(self, parent):
        self.canv = tk.Canvas(parent)
        coord = 10, 50, 240, 210
        id = self.canv.create_oval(coord, self.paintStyle)
        self.canv.grid(sticky="NSWE")


def main():
    app = Application()
    app.master.title('Painter')
    app.mainloop()


if __name__ == "__main__":
    main()
