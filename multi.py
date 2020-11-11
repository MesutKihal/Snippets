from tkinter import *
import datetime
import random

class App:
    def __init__(self, master = Tk()):
        self.master = master

    def settings(self):
        self.master.minsize(340,420)
        self.master.maxsize(340,420)
        self.master.title("Multiplication")

    def widgets(self):
        self.timeCount = StringVar()
        later = datetime.datetime.now() + datetime.timedelta(minutes=1)
        def timer():
            seconds =  (later - datetime.datetime.now()).seconds
            minutes = seconds // 60
            seconds %= 60
            return "%02d:%02d" % (minutes, seconds)
        def OperationGenerator():
            yield str(random.randint(0,9)) + '*' + str(random.randint(0,9))
        self.time_board = Label(textvariable=self.timeCount,font="verdana 12 bold").place(x=20,y=20)
        self.timeCount.set(timer())
        
multi = App()
multi.settings()
multi.widgets()
mainloop()
