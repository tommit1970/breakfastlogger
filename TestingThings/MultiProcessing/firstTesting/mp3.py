import time
import os
# from multiprocessing import Process
import concurrent.futures


start = time.time()

def print_square(number):
	print('The process id is {}'.format(os.getpid()))
	time.sleep(1)
	print('The square of {} is {}'.format(number, number**2))
	return "Done {}".format(os.getpid())

# with concurrent.futures.ProcessPoolExecutor() as executor:
if __name__ == '__main__':
		# p1 = executor.submit(print_square, 2)
		# p2 = executor.submit(print_square, 3)
	p1 = concurrent.futures.ProcessPoolExecutor().submit(print_square, 2)
	p2 = concurrent.futures.ProcessPoolExecutor().submit(print_square, 3)
	print(p1.result()) # return value
	print(p2.result()) # return value



# print_square(2)
# print_square(3)

end = time.time()

print('It took {} seconds'.format(end-start))