import sys


for line in sys.stdin:
	if 'E' == line.rstrip():
		break
	print(f"Message : {line}")
print("End")


# sys.stderr.write("This is error msg")