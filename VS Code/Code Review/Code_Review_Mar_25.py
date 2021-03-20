# =================================================================================================
# EASY ============================================================================================
# =================================================================================================


# Import datetime CLASS from time datetime MODULE
# Now METHOD from within the datetime MODULE to retrieve a datetime OBJECT
# Format current time using string formatting
# currentTime = now.strftime("%H:%M:%S")
# currentTime = strftime("%H:%M:%S", localtime())


from time import localtime, strftime
from datetime import datetime, timezone


now = datetime.now()

# def timeLoop(currentTime):

#     for everySecond in currentTime:
#         print(currentTime)
#         currentTime = currentTime + localtime

# timeLoop(currentTime)


print(now.strftime("%m-%d-%Y %H:%M:%S"))