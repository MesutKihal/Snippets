from tkinter import *
import pickle
from tkinter.scrolledtext import ScrolledText

class App:
	def __init__(self, master = Tk()):
		self.master = master

	def settings(self):
		self.master.geometry('320x240')
		self.master.configure(bg = 'grey85')

	def widgets(self):
		self.var1 = StringVar()
		self.var2 = StringVar()
		self.var3 = StringVar()
		self.var1.set('4165')
		self.var2.set('1501')
		vars_ = [self.var1,self.var2,self.var3]
		data = [str(var.get()) for var in vars_]
		pickle.dump(data, open("file.tl", "wb"))
		def get():
			data = pickle.load(open("file.tl", "rb"))
			print(data)

		self.btn = Button(text='get',bg='red',command=get).place(x = 150, y = 50)
		i = 0
		labels = [Label(textvariable=self.var1,bg='white',width=20),
				  Label(textvariable=self.var2,bg='white',width=20),
				  Label(textvariable=self.var3,bg='white',width=20),]
		for l in labels:
			l.place(x = 0,y = i*50)
			i += 1
tdl = App()
tdl.settings()
tdl.widgets()
mainloop()
