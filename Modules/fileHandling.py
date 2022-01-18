import __main__ as main
# Filehandling simple

def readFile(fileName):
	logfileOne = open(fileName, 'r')
	content = logfileOne.read().splitlines() # from lines in a file to list

	logfileOne.close()
	return content

def writeFile():
	logfileOne = open('log.txt','w')
	breakfastListLength = len(main.breakfastList)
	textCollection = ""
	for i in range(0,breakfastListLength):
		if i < breakfastListLength-1:
			textCollection = textCollection + main.breakfastList[i] + '\n'
		else:
			textCollection = textCollection + main.breakfastList[i]

	# print(textCollection)

	logfileOne.write(textCollection)
	logfileOne.close()