import tkinter
import datetime
from PIL import Image, ImageTk, ImageSequence

class App:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tkinter.Canvas(parent, width=400, height=400)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(r'static/dog.gif'))]
        self.image = self.canvas.create_image(200,200, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(50, lambda: self.animate((counter+1) % len(self.sequence)))

# root = tkinter.Tk()
# app = App(root)
# root.mainloop()

date_time_obj = datetime.datetime.now()
print( int(date_time_obj.strftime("%m")) )