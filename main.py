import eel
import os

eel.init("www")
@eel.expose
def opt1():
    os.system("python3 opt1.py")
    
@eel.expose
def opt2():
    os.system("python3 opt2.py")

eel.start('index.html', size=(945, 700))
