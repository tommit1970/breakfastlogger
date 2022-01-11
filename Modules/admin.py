from Modules.fileHandling import readFile
import __main__ as main

# Here you ask for admin access


def askForCredentials():
	print('Username: ',end='')
	userName = input()
	print('Password: ', end='')
	userPWD = input()
	return {'u':userName,'p':userPWD}

def toggleAdminMode():
	if main.adminModeOn:
		main.adminModeOn = False
	else:
		idData = readFile('admin.txt')
		# print(idData)
		userID = askForCredentials()
		if userID['u'] == idData[0] and userID['p'] == idData[1]:
			print('Access granted!')
			main.adminModeOn = True
		else:
			print('Access denied!')

