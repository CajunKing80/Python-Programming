import webbrowser, sys, pyperclip 

sys.argv # ['mapit.py', '870', 'Valencia', 'St']

# webbrowser.open("http://192.168.99.210/api/dcim/devices/?name=B-KL001-H-R")

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else: 
    address = pyperclip.paste

webbrowser.open('https://www.google.com/maps/places/' + address)