# Filehandling simple

def readFile():
	logfileOne = open('log.txt', 'r')
	content = logfileOne.readlines() # from lines in a file to list
	logfileOne.close()
	return content

def writeFile(content):
	logfileOne = open('log.txt','w')
	logfileOne.writelines(content)
	logfileOne.close()