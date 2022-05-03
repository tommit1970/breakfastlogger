import threading
import time

total = 4

def create_items():
	global total
	for i in range(5):
		time.sleep(1)
		print('added item')
		total += 1
	print('creation done')

def create_items2():
	global total
	for i in range(3):
		time.sleep(0.5)
		print('added item')
		total += 1
	print('creation done')

def limit_items():
	global total
	while True:
		if total > 5:
			total -= 3
			print('subtracted 3')
		else:
			time.sleep(0.5)
			print('waiting')


creator1 = threading.Thread(target = create_items)
creator2 = threading.Thread(target = create_items2)

# daemon = Trye will make this process die when main process reaches the end
limitor = threading.Thread(target = limit_items, daemon = True)

creator1.start()
creator2.start()
limitor.start()

creator1.join()
creator2.join()
# limitor.join()

print('our ending value of total is: ', total)
