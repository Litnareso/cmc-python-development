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
        self.canv = tk.Canvas(parent, takefocus=True)
        self.canv.grid(sticky="NSWE")
        self.drawn = None
        self.start = None
        self.rad = 2
        self.canv.bind('<ButtonPress-1>', self.onStart)
        self.canv.bind('<B1-Motion>', self.onGrow)
        self.canv.bind('<Double-1>', self.onRaise)
        self.canv.bind('<Control-Return>', self.updateText)

    def onStart(self, event):
        self.canv.focus_set()
        self.start = event
        self.drawn = None
        rad = self.rad
        ids = self.canv.find_overlapping(event.x - rad, event.y - rad,
                                         event.x + rad, event.y + rad)
        if ids:
            self.redrawn = ids[-1]
            return
        self.redrawn = None

    def onGrow(self, event):
        if self.redrawn:
            diffX, diffY = event.x - self.start.x, event.y - self.start.y
            self.canv.move(self.redrawn, diffX, diffY)
            self.canv.tag_raise(self.redrawn)
            self.start = event
            return
        if self.drawn:
            self.canv.delete(self.drawn)
        self.drawn = self.canv.create_oval(self.start.x, self.start.y,
                                           event.x, event.y,
                                           self.paintStyle)

    def onRaise(self, event):
        self.canv.focus_set()
        rad = self.rad
        ids = self.canv.find_overlapping(event.x - rad, event.y - rad,
                                         event.x + rad, event.y + rad)
        if ids:
            self.canv.tag_raise(ids[-1])

    def onClear(self, event):
        self.canv.delete('all')

    def updateText(self, event):
        self.descr.delete("1.0", "end")
        for id in self.canv.find_all():
            colorFill = self.canv.itemcget(id, "fill")
            colorOutline = self.canv.itemcget(id, "outline")
            outline = self.canv.itemcget(id, "offset").replace(",", ".")
            coords = self.canv.coords(id)
            self.descr.insert("end", "oval <" +
                              "{:.1f} {:.1f} {:.1f} {:.1f}> ".format(*coords) +
                              "{:.1f}".format(float(outline)) + " " +
                              colorOutline + " " + colorFill + "\n")


def main():
    app = Application()
    app.master.title('Painter')
    app.mainloop()


if __name__ == "__main__":
    main()
