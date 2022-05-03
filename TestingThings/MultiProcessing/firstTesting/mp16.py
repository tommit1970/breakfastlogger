from multiprocessing import Process, Queue
import time
import keyboard

def f(q):
	q.put({'navn':'Tommy','alder':51})
	time.sleep(1)
	q.put(55)
	keyboard.wait('space', suppress=False)
	q.put('Tommy er best')
	print('\u001b[1A----All done\u001b[1B',end="")


if __name__ == '__main__':
	q = Queue()
	p = Process(target=f, args=[q])
	p.start()
	a = q.get()
	print(type(a))
	print(a)
	b = q.get()
	print(type(b))
	print(b)
	userInput = input()
	print(userInput)
	print(q.get())
	p.join()