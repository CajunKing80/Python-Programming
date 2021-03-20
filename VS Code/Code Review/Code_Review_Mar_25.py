# =================================================================================================
# EASY ============================================================================================
# =================================================================================================


# Import datetime CLASS from time datetime MODULE
# Now METHOD from within the datetime MODULE to retrieve a datetime OBJECT
# Format current time using string formatting
# currentTime = now.strftime("%H:%M:%S")
# currentTime = strftime("%H:%M:%S", localtime())
# from time import localtime, strftime
# from datetime import datetime, timezone
# now = datetime.now()

import tkinter as tk
import time as tm


def display_time():

    current_time = tm.strftime('%H:%M:%S') 
    clock_label['text'] = current_time
    my_window.after (1000,display_time)

# Format Windows window to display the current time
my_window = tk.Tk() #Create an instance of a window
my_window.title('Current Time') # Set title of window
clock_label = tk.Label(my_window, font = 'ariel 100', bg = 'black', fg = 'red') # Format the window's font, size, background and foreground
clock_label.grid (row = 0, column = 0) # Sets label to label position 
display_time()
my_window.mainloop() # Event loop