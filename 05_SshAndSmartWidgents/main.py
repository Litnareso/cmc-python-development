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
        self.canv.grid(sticky="NSWE")
        self.drawn = None
        self.start = None
        self.canv.bind('<ButtonPress-1>', self.onStart)
        self.canv.bind('<B1-Motion>', self.onGrow)
        self.canv.bind('<ButtonPress-3>', self.onMove)

    def onStart(self, event):
        self.start = event
        self.drawn = None

    def onGrow(self, event):
        if self.drawn:
            self.canv.delete(self.drawn)
        id = self.canv.create_oval(self.start.x, self.start.y,
                                   event.x, event.y, self.paintStyle)
        self.drawn = id

    def onClear(self, event):
        self.canv.delete('all')

    def onMove(self, event):
        if self.drawn:
            diffX, diffY = event.x - self.start.x, event.y - self.start.y
            self.canv.move(self.drawn, diffX, diffY)
            self.start = event


def main():
    app = Application()
    app.master.title('Painter')
    app.mainloop()


if __name__ == "__main__":
    main()
