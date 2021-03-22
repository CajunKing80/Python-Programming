# =================================================================================================
# EASY ============================================================================================
# =================================================================================================


# from datetime import datetime
# import time


# def get_time():

#     while True:
        
#         current_time = datetime.now()
#         print(current_time.strftime("%m-%d-%Y %H:%M:%S"))
#         time.sleep(1)

# get_time()


# import tkinter as tk
# import time as tm


# def display_time():

#     current_time = tm.strftime('%H:%M:%S') 
#     clock_label['text'] = current_time
#     my_window.after (1000,display_time)

# # Format Windows window to display the current time
# my_window = tk.Tk() #Create an instance of a window
# my_window.title('Current Time') # Set title of window
# clock_label = tk.Label(my_window, font = 'ariel 100', bg = 'black', fg = 'red') # Format the window's font, size, background and foreground
# clock_label.grid (row = 0, column = 0) # Sets label to label position 
# display_time()
# my_window.mainloop() # Event loop


# =================================================================================================
# MEDIUM ==========================================================================================
# =================================================================================================


import requests
import json
import time
from datetime import datetime 

    
url = 'http://api.open-notify.org/iss-now.json'
req = requests.request('GET',url,)
json_data = req.json()

iss_data = {
    "Timestamp": [],
    "Latitude": [],
    "Longitude": []
}

# print(iss_data)

def get_data():
    
    while True:

        for key in json_data:
            if key == 'timestamp':
                iss_data["Timestamp"].append(json_data["timestamp"])
            if key == "iss_position":
                iss_data["Latitude"].append(json_data["iss_position"]["latitude"])
            if key == "iss_position":
                iss_data["Longitude"].append(json_data["iss_position"]["longitude"])
               
        print(iss_data)
        time.sleep(1)

get_data()
