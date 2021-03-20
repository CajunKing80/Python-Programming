# =================================================================================================
# EASY ============================================================================================
# =================================================================================================


# #Import datetime CLASS from time datetime MODULE

# # Now METHOD from within the datetime MODULE to retrieve a datetime OBJECT
# now = datetime.now()

# # Format current time using string formatting
# currentTime = now.strftime("%H:%M:%S")

# print (currentTime.timezone)


from time import localtime, strftime
    
currentTime = strftime("%H:%M:%S", localtime())

def timeLoop(currentTime):

    for everySecond in currentTime:
        print(currentTime)
        currentTime = currentTime + localtime

timeLoop(currentTime)