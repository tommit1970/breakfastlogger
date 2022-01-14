from Modules.fileHandling import readFile
import __main__ as main
import Modules.colors as colors


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
		print('\n{}Admin logged out!{}\n'.format(colors.brightRed, colors.white))
	else:
		idData = readFile('admin.txt')
		# print(idData)
		userID = askForCredentials()
		if userID['u'] == idData[0] and userID['p'] == idData[1]:
			print('\n{}Access granted!{}\n'.format(colors.green,colors.white))
			main.adminModeOn = True
		else:
			print('\n{}Access denied!\n'.format(colors.brightRed))

