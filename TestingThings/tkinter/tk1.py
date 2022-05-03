from tkinter import Tk
from tkinter import ttk
import multiprocessing
import os

print(os.getpid())
print('Hello')

def windowStarter():
	print(os.getpid())
	root = Tk()
	frm = ttk.Frame(root, padding=150)
	frm.grid()
	ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
	ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
	root.mainloop()


def ask():
	val = input()
	print(val)


if __name__ == '__main__':
	p = multiprocessing.Process(target=windowStarter)
	p2 = multiprocessing.Process(target=ask)
	p.start()
	p.join()
	p2.start()
	p2.join()