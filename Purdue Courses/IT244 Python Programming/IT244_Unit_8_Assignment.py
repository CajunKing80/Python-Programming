
#UNIT 8 ASSIGNMENT

# 1. In the Python shell, forst import the sys, os, and subprocess modules
import sys 
import os
import subprocess

# 2. Execute os.getlogin()
user = os.getlogin()

# 3. Execute os.get_exec_path()
execPath = os.get_exec_path()

print (user)
print (execPath)

# 4. Take a screenshot

# 5. Execute sys.path
path = sys.path

# 6. Execute sys.byteorder
byteOrder = sys.byteorder

print (path)
print (byteOrder)

# 7. Take a screenshot

# 8. Execute os.listdir on your C: drive
dirPath = "C:\\"

# 9. Use os.mkdir to make a new folder on your C: drive name tempPython
dir_list = os.listdir (dirPath)

path = ("C:\\tempPython")
#os.mkdir (path)

print (dirPath)

# 10. Take a screenshot

# 11. Use subprocess.Popen to execute the Windows dir command and have its output placed in a text file named pythonOut.txt
subprocess.Popen ('C:\\windows\\system32\\cmd.exe "/c dir C:\\ >> C:\\temp\pythonOut.txt"')

# 12. Open pythonOut.txt in Notepad and position that window next to the Python shell window where both can be seen

# 13. Take a screenshot

# 14. Use subprocess.Popen to open Windows calc.exe utility
subprocess.Popen ('calc.exe')

#END OF UNIT 8 ASSIGNMENT