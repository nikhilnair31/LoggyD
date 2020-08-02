import sys
import json
import auto_joiner
from tkinter import *

def get_stopped():
   sys.exit("Error message")

def get_started():
   auto_joiner.mainu(email.get(), pwd.get(), refresh_rate.get(), mute_audio.get(), random_delay.get(), auto_start.get() )

def main_screen():
   root.geometry("300x500")
   root.configure(background=bg_col)
   root.title("GUI")

   Label(text = "", bg = bg_col).pack()
   Label(text = "LoggyDoggy", bg = bg_col, fg = fg_col, font = ("Comfortaa", 20)).pack()
   Label(text = "", bg = bg_col).pack()

   Label(text = "Email ID", font = ("Comfortaa", 12), bg = bg_col, fg = fg_col).pack()
   email_entry = Entry(root, textvariable=email, width=25).pack()

   Label(text = "Password", font = ("Comfortaa", 12), bg = bg_col, fg = fg_col).pack()
   pwd_entry = Entry(root, textvariable=pwd, width=25).pack()

   Label(text = "Refresh Rate", font = ("Comfortaa", 12), bg = bg_col, fg = fg_col).pack()
   rate_entry = Entry(root, textvariable=refresh_rate, width=25).pack()

   Label(text = "", bg = bg_col).pack()
   mute_check = Checkbutton(root, text = 'Mute Audio', variable = mute_audio).pack()

   Label(text = "", bg = bg_col).pack()
   delay_check = Checkbutton(root, text = 'Random Delay', variable = random_delay).pack()

   Label(text = "", bg = bg_col).pack()
   auto_star = Checkbutton(root, text = 'Auto Start', variable = auto_start).pack()

   Label(text = "", bg = bg_col).pack()
   Button(root, text = "Start", width=10, command=get_started).pack()

   Label(text = "", bg = bg_col).pack()
   Button(root, text = "Stop", width=10, command=get_stopped).pack()

   root.mainloop()

if __name__ == '__main__':
   bg_col = '#000000'
   fg_col = '#FFFFFF'

   with open('config.json') as json_data_file:
      config = json.load(json_data_file)

   root = Tk()
   email = StringVar()
   email.set(config['email'])
   pwd = StringVar()
   email.set(config['password'])
   refresh_rate = IntVar()
   email.set(config['delay'])
   mute_audio = BooleanVar()
   email.set(config['mute_audio'])
   random_delay = BooleanVar()
   email.set(config['random_delay'])
   auto_start = BooleanVar()
   email.set(config['start_automatically'])

   main_screen()