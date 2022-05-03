from multiprocessing import Process
import os
import time
from tkinter import *


def gorm(anything):
	print('Water is '+anything)
	print(os.getpid())
	name = input('What is your name?')
	return 'Your name is: ' + name




class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

    def exitProgram(self):
        exit()


def make_a_window(windowName):
	root = Tk()
	app = Window(root)
	root.wm_title(windowName)
	root.mainloop()



# p1 = Process(target=make_a_window, args=['TKinter window'])
p2 = Process(target=gorm, args=['wide'])

if __name__ == '__main__':
	# p1.start()
	p2.start()
	# p1.join()
	p2.join()


finished = time.perf_counter()
print('Seconds to finish: {}'.format(finished))
