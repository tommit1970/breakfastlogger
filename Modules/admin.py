from Modules.fileHandling import readFile
import __main__ as main
import Modules.colors as colors
import getpass
import logindata

print()
# Here you ask for admin access


def askForCredentials():
	userName = getpass.getpass('Username: ')
	userPWD = getpass.getpass('Password: ')
	return {'u':userName,'p':userPWD}

def toggleAdminMode():
	if main.globals['adminModeOn']:
		main.globals['adminModeOn'] = False
		print('\n{}Admin logged out!{}\n'.format(colors.brightRed, colors.white))
	else:
		# idData = readFile('admin.txt')
		# print(idData)
		userID = askForCredentials()
		# if userID['u'] == idData[0] and userID['p'] == idData[1]:
		if userID['u'] == logindata.secret['username'] and userID['p'] == logindata.secret['password']:
			print('\n{}Access granted!{}\n'.format(colors.green,colors.white))
			main.globals['adminModeOn'] = True
		else:
			print('\n{}Access denied!\n'.format(colors.brightRed))

