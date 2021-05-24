import os
import shutil # shell utilities removes a folder and all of its content

os.getcwd()

os.unlink('filename')

os.rmdir() # delet entire directory. Directory must be empty to remove

os.chdir('C:\\Users\\Jeremy\\Desktop')
for filename in os.listdir():
    if filename.endswith('.txt'):
        # os.unlink(filename)
        print (filename)

import send2trash
send2trash.send2trash('path/to/file.filename')

os.mkdir('C:\\Users\\jerem\\repositories')