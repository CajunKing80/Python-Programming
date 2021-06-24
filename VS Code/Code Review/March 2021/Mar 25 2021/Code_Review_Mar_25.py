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


# import requests
# import json
# import time
# from datetime import datetime 
 

# def get_data():
    
#     timer = 1
#     while timer:

#         url = 'http://api.open-notify.org/iss-now.json'
#         req = requests.request('GET',url,)
#         json_data = req.json()
    
#         print(f"time - {json_data['timestamp']} lat - {json_data['iss_position']['latitude']} long - {json_data['iss_position']['longitude']}")
#         time.sleep(1)

# get_data()


# =================================================================================================
# HARD ============================================================================================
# =================================================================================================


import requests
import json
import time
from datetime import datetime 


def get_iss_data(counter, interval):
    
    iss_position_1 = {}
    
    while counter >= 1:

        json_data = requests.get('http://api.open-notify.org/iss-now.json').json()
        converted = str(datetime.fromtimestamp(json_data['timestamp']))
            
        iss_position_1[converted] = {"Latitude": json_data['iss_position']['latitude'],
            "Longitude": json_data['iss_position']['longitude']}
        print(f"Time - {json_data['timestamp']} Lat - {json_data['iss_position']['latitude']} Long - {json_data['iss_position']['longitude']}")
        counter -= 1
        time.sleep(interval)
    
    iss_position = {'ISS_Postition': iss_position_1}
    with open ('Code_Review_Mar_25.json', 'w') as json_data:
        json.dump(iss_position, json_data, indent = 2)

get_iss_data(10, 1)