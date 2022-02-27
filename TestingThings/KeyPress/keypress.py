import keyboard
import time

print(keyboard.version)
print('Press Space to continue')
keyboard.wait('space', suppress = True)
print('space was pressed, continuing...')
print(keyboard.KEY_UP)
# print('I dont know')

for i in range(10):
	print(i, end='', flush=True)
	time.sleep(0.2)

value = input()
print('---'+value+'---') # a space value is at input even if there is a time delay
