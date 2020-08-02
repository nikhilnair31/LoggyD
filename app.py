import os
import sys
import json
import auto_joiner
from tkinter import *
from PIL import Image, ImageTk, ImageSequence

class App:
   def __init__(self, parent):
      self.parent = parent
      self.canvas = Canvas(parent, width=300, height=150)
      self.canvas.pack()
      self.sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(r'static/dog.gif'))]
      self.image = self.canvas.create_image(150,75, image=self.sequence[0])
      self.animate(1)
   def animate(self, counter):
      self.canvas.itemconfig(self.image, image=self.sequence[counter])
      self.parent.after(50, lambda: self.animate((counter+1) % len(self.sequence)))

def get_stopped():
   sys.exit("Error message")

def get_started():
   auto_joiner.mainu(email.get(), pwd.get(), refresh_rate.get(), mute_audio.get(), random_delay.get(), auto_start.get() )

def main_screen():
   root.geometry("300x700")
   root.configure(background=bg_col)
   root.title("DoggyLoggy")
   # root.iconbitmap('static/icon.ico')

   Label(text = "", bg = bg_col).pack()
   Label(text = "LoggyDoggy", bg = bg_col, fg = fg_col, font = ("Comfortaa", 20)).pack()
   Label(text = "", bg = bg_col).pack()

   Label(text = "Email ID", font = ("Comfortaa", 12), bg = bg_col, fg = fg_col).pack()
   email_entry = Entry(root, textvariable=email, width=35, justify='center').pack()

   Label(text = "Password", font = ("Comfortaa", 12), bg = bg_col, fg = fg_col).pack()
   pwd_entry = Entry(root, textvariable=pwd, width=35, justify='center').pack()

   Label(text = "Refresh Rate", font = ("Comfortaa", 12), bg = bg_col, fg = fg_col).pack()
   rate_entry = Entry(root, textvariable=refresh_rate, width=35, justify='center').pack()

   Label(text = "", bg = bg_col).pack()
   mute_check = Checkbutton(root, text = 'Mute Audio', variable = mute_audio, width=10).pack()

   Label(text = "", bg = bg_col).pack()
   delay_check = Checkbutton(root, text = 'Rand Delay', variable = random_delay, width=10).pack()

   Label(text = "", bg = bg_col).pack()
   auto_star = Checkbutton(root, text = 'Auto Start', variable = auto_start, width=10).pack()

   Label(text = "", bg = bg_col).pack()
   Button(root, text = "Start", width=10, command=get_started).pack()

   Label(text = "", bg = bg_col).pack()
   Button(root, text = "Stop", width=10, command=get_stopped).pack()
   Label(text = "", bg = bg_col).pack()

   # image = Image.open("static/shiba.png")
   # image = image.resize((300, 300), Image.ANTIALIAS)
   # image_tk = ImageTk.PhotoImage(image)
   # image_lbl = Label(image=image_tk, bg = bg_col).pack()

   root.mainloop()

if __name__ == '__main__':
   bg_col = '#000000'
   fg_col = '#FFFFFF'

   root = Tk()
   # app = App(root)
   email = StringVar()
   pwd = StringVar()
   refresh_rate = IntVar()
   mute_audio = BooleanVar()
   random_delay = BooleanVar()
   auto_start = BooleanVar()

   path = os.path.join(os.path.expanduser('~'), 'Documents', 'config.json')
   if os.path.exists(path):
      with open(path) as json_data_file:
         config = json.load(json_data_file)
      email.set(config['email'])
      pwd.set(config['password'])
      refresh_rate.set(config['delay'])
      mute_audio.set(config['mute_audio'])
      random_delay.set(config['random_delay'])
      auto_start.set(config['start_automatically'])

   main_screen()