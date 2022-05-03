# Testing map function

def myfunc(f):
	return f*10


c = [1,2,3]

a = map(myfunc, [1,2,3]) # a will change if you look at it

print('Address')
print(a)

b = list(a)

print('Each item')

for item in b:
	print(item)
	# break

print('List')
print(b)

print('Address?')
print(a)

print('Anything')