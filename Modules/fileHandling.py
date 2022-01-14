import __main__ as main
# Filehandling simple

def readFile(fileName):
	logfileOne = open(fileName, 'r')
	content = logfileOne.read().splitlines() # from lines in a file to list

	logfileOne.close()
	return content

def writeFile():
	logfileOne = open('log.txt','w')
	# print(main.breakfastList)
	textCollection = ""
	for item in main.breakfastList:
		textCollection = textCollection + item + '\n'
	# print(textCollection)
	logfileOne.write(textCollection)
	logfileOne.close()