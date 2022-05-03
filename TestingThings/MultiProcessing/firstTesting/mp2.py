import time
import os
from multiprocessing import Process


start = time.time()

def print_square(number):
	print('The process id is {}'.format(os.getpid()))
	time.sleep(1)
	print('The square of {} is {}'.format(number, number**2))


processes = []
for i in range(1,11):
	p = Process(target = print_square, args = [i])
	if __name__ == '__main__':
		p.start()
	processes.append(p)
for process in processes:
	if __name__ == '__main__':
		process.join()


# print_square(2)
# print_square(3)

end = time.time()

print('It took {} seconds'.format(end-start))