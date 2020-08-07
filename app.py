import os
import sys
import json
import datetime
import auto_joiner
from tkinter import *
from PIL import Image, ImageTk, ImageSequence

root = Tk()
bg_col = '#000000'
fg_col = '#FFFFFF'
hl_col = '#FF0000'
last_date = -1
days_left = 31
email = StringVar()
pwd = StringVar()
refresh_rate = IntVar()
mute_audio = BooleanVar()
random_delay = BooleanVar()
auto_start = BooleanVar()
config_path = os.path.join(os.path.expanduser('~'), 'config.json')
config = None

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

def main_screen():
   global auto_start, bg_col, fg_col
   root.geometry("300x600")
   root.configure(background=bg_col)
   root.title("DoggyLoggy")
   # root.iconbitmap('static/icon.ico')
   Label(text = "", bg = bg_col).pack()
   Label(text = "LoggyDoggy", bg = bg_col, fg = fg_col, font = ("Comfortaa", 20)).pack()
   Label(text = "", bg = bg_col).pack()
   Label(text = "Days Left", font = ("Comfortaa", 12), bg = bg_col, fg = fg_col).pack()
   Label(text = str(days_left), font = ("Comfortaa", 10), bg = bg_col, fg = hl_col).pack()
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
   if(days_left > 0):
      Button(root, text = "Start", width=10, command=get_started).pack()
      Label(text = "", bg = bg_col).pack()
      Button(root, text = "Stop", width=10, command=get_stopped).pack()
      Label(text = "", bg = bg_col).pack()
   else:
      Button(root, text = "Renew Subscription", width=15, command=get_started).pack()
      Label(text = "", bg = bg_col).pack()
   # if auto_start.get() is True:
   #    get_started()
   # image = Image.open("static/shiba.png")
   # image = image.resize((300, 300), Image.ANTIALIAS)
   # image_tk = ImageTk.PhotoImage(image)
   # image_lbl = Label(image=image_tk, bg = bg_col).pack()
   root.mainloop()

def get_stopped():
   sys.exit("Error message")

def get_started():
   global config, config_path, start_month
   if not os.path.isfile(config_path):
      print('Config file missing. Creating new...')
      create_config()
   else:
      print('Config file exists. Loading...')
      save_config()
   load_config()
   auto_joiner.mainu(config)

def create_config():
   global config_path, email, pwd, refresh_rate, mute_audio, random_delay, auto_start, days_left, last_date
   dictionary = {"email": email.get(), "password": pwd.get(), "delay": refresh_rate.get(), "start_automatically": auto_start.get(), 
      "random_delay": random_delay.get(),  "auto_leave_after_min": -1, "leave_if_last": True, "mute_audio": mute_audio.get(), 
         "chrome_type": "google-chrome", "blacklist": [{"team_name": "Group ISTE-NITK", "channel_names": []}], 
               "days_left": days_left, "last_date": last_date}
   with open(config_path, "w") as outfile: 
      json.dump(dictionary, outfile)

def save_config():
   global config_path, email, pwd, refresh_rate, mute_audio, random_delay, auto_start, days_left, last_date
   load_config()
   config['email'] = email.get()
   config['password'] = pwd.get()
   config['delay'] = refresh_rate.get()
   config['mute_audio'] = mute_audio.get()
   config['random_delay'] = random_delay.get()
   config['start_automatically'] = auto_start.get()
   config['days_left'] = days_left
   config['last_date'] = last_date
   with open(config_path, 'w') as f:
      json.dump(config, f)

def pre_load_config():
   global config_path, config, email, pwd, refresh_rate, mute_audio, random_delay, auto_start, days_left, last_date
   if os.path.isfile(config_path):
      print('Config file exists. Pre-Loading...')
      with open(config_path) as json_data_file:
         config = json.load(json_data_file)
      email.set(config['email'])
      pwd.set(config['password'])
      refresh_rate.set(config['delay'])
      mute_audio.set(config['mute_audio'])
      random_delay.set(config['random_delay'])
      auto_start.set(config['start_automatically'])
      if(last_date != config['last_date']):
         print('New day since last opened...')
         days_left = config['days_left']-(last_date-config['last_date'])
      else:
         print('Same day as last opened...')
         days_left = config['days_left']
      last_date = config['last_date']

def load_config():
   global config_path, config
   with open(config_path) as json_data_file:
      config = json.load(json_data_file)


if __name__ == '__main__':
   date_time_obj = datetime.datetime.now()
   last_date = int(date_time_obj.strftime("%d"))
   print(f'Start date is {last_date}')

   # app = App(root)
   pre_load_config()
   main_screen()