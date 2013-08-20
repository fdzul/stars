
import Tkinter as tk

class CanvasFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("CanvasView")
        self.pack(fill=tk.BOTH, expand = 1)
        height = self.parent.winfo_screenheight() / 2.
        width = self.parent.winfo_screenwidth() /2.
        self.canvas = tk.Canvas(self, bg='white', width=width, height=height)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.canvas.grid(row=0, column=0, sticky='nesw')
        self.canvas.create_line(0, 0, width, height, width = 5.0)
        self.canvas.create_line(0, height, width, 0, width = 5.0)
        self.config_events = 0

        # Event bindings
        self.canvas.bind('<Configure>', self.onConfigure)

    def onConfigure(self, event):
        print '(%d, %d)' %(event.width, event.height)
        print 'config_events: ', self.config_events
        #self.canvas.delete(tk.ALL)
        #self.canvas.create_line(0,0, event.width, event.height, width=5.0)
        self.width = event.width
        self.height = event.height
        self.redraw()
        self.config_events += 1

    def redraw(self):
        self.canvas.delete(tk.ALL)
        # start with assumption width of screen > height of screen
        dim = self.height
        width_screen = self.height 
        height_screen = self.height
        self.x0 = self.width - width_screen
        self.x0 /= 2.0
        self.x1 = self.x0 + width_screen
        self.y0 = 0
        self.y1 = self.height
        if self.height > self.width:
            height_screen = self.width
            self.y0 = self.height - self.width
            self.y0 /= 2.
            self.y1 = self.y0 + height_screen
            self.x0 = 0
            self.x1 = self.width

        # world coords for line
        wc_line = [ (100,100), (2000,2000) ]
        wc_line1 = [ (100,2000), (2000, 100) ]

        width_world = wc_line[1][0] - wc_line[0][0]
        height_world = wc_line[1][1] - wc_line[0][0]
        sy = height_screen * 1. / height_world
        sx = width_screen * 1. / width_world

        x0 = (100 - 100) * sx + self.x0
        y0 = self.y0 + (2000 - 100) * sy 
        x1 = (2000 - 100) * sx + self.x0
        y1 = self.y0 + (2000 - 2000) * sy
        print x0,y0,x1,y1
        self.canvas.create_line(x0, y0, x1, y1, width=5.0)

        # second line
        x0 = (100 - 100) * sx + self.x0
        y0 = self.y0 + (2000 - 2000) * sy 
        x1 = (2000 - 100) * sx + self.x0
        y1 = self.y0 + (2000 - 100) * sy
        print x0,y0,x1,y1
        self.canvas.create_line(x0, y0, x1, y1, width=5.0)




if __name__ == '__main__':
    root = tk.Tk()
    view = CanvasFrame(root)
    root.mainloop()

