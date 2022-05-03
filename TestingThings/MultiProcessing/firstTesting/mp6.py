from multiprocessing import Process
import os

# This is run twice
print('Main Process: '+str(os.getpid()))
print('My friends want to play')


def gorm():
	print("I'm Gorm")
	value = input('Your name:')
	return value + " - Only in America"

def display():
	print('Hello!!!!')
	print('Sub Process: '+str(os.getpid()))
	return "Nothing really"

if __name__ == '__main__':
	p1 = Process(target = display)
	p2 = Process(target = gorm)
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	# print()


