
# LoggyDoggy   

Python script with UI to automatically join Microsoft Teams meetings.  
Automatically turns off your microphone and camera before joining. Automatic login and blacklist can be set.
   
## Configuration options  
  
- **email/password:**  
The email/password of your Microsoft account (can be left empty if you don't want to automatically login)  

- **start_automatically:**  
If true, skips the `Start [s], Reload teams [r], Quit [q]` dialog and starts on it's own. Useful if you schedule the script to start at a specific time.  

- **random_delay:**  
If true, adds a random delay (10s-30s) before joining a meeting. Can be useful so the bot seems more "human like".  

- **auto_leave_after_min:**  
If set to a value greater than zero, the bot leaves every meeting after the specified time (in minutes). Useful if you know the length of your meeting, if this is left a the default the bot will stay in the meeting until a new one is available.

- **leave_if_last:**  
If true, leaves the meeting if you are the last person in it.

- **mute_audio:**     
If true, mutes all the sounds.

- **chrome_type:**     
Valid options: `google-chrome`, `chromium`, `msedge`. By default, google chrome is used, but the script can also be used with Chromium or Microsoft Edge.

- **blacklist:**  
A list of Teams and their channels to ignore. Meetings ocurring in these channels will not be joined.  
If you have a Team called "Test1" and, within that, two channels called "General" and "Channel1" and you don't want to join meetings in the "General" Channel: 
```json
"blacklist": [  
  {  
    "team_name": "Test1",  
    "channel_names": [  
      "General"
    ]  
  }
]
```