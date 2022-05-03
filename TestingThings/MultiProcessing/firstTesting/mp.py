import time
import multiprocessing

def sleep_for_a_bit(seconds):
	print('Seconds sleeping: {}'.format(seconds))
	time.sleep(seconds)
	print('Done sleeping!!')


p1 = multiprocessing.Process(target=sleep_for_a_bit, args=[1])
p2 = multiprocessing.Process(target=sleep_for_a_bit, args=[1])

if __name__ == '__main__':
	p1.start()
	p2.start()
	p1.join()
	p2.join()


finished = time.perf_counter()
print('Seconds to finish: {}'.format(finished))