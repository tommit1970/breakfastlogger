# Filehandling simple

def readFile(fileName):
	logfileOne = open(fileName, 'r')
	content = logfileOne.read().splitlines() # from lines in a file to list

	logfileOne.close()
	return content

def writeFile(content):
	logfileOne = open('log.txt','w')
	logfileOne.writelines(content)
	logfileOne.close()