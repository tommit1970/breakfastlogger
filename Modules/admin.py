from pymongo import MongoClient
import bcrypt
from Modules.fileHandling import readFile
import __main__ as main
import Modules.colors as colors
import getpass
import logindata

print()
# Here you ask for admin access


def mongoDB_handling(userName):
	client = MongoClient('mongodb://localhost:27017/')
	db = client['breakfastPW']
	collection = db['pw']
	result = collection.find({'userName':userName})
	# print(type(result))
	# print(result) #result is a list of finds
	findings = ""
	counter = 0
	for item in result:
		findings = item
		# print(item)
		counter = counter + 1
	# print('Length of finds are '+ str(counter))
	client.close() # close connection

	if counter != 0:
		# print(findings['userPW'])
		return findings['userPW']
	return False



def askForCredentials():
	userName = getpass.getpass('Username: ')
	userPWD = getpass.getpass('Password: ').encode() # encode() for hash_compare
	DBresult = mongoDB_handling(userName).encode() # encode for hash_compare
	# print(DBresult)
	if DBresult:
		return {'p':userPWD, 'dbp':DBresult}
	return False

def toggleAdminMode():
	if main.globals['adminModeOn']:
		main.globals['adminModeOn'] = False
		print('\n{}Admin logged out!{}\n'.format(colors.brightRed, colors.white))
	else:
		# idData = readFile('admin.txt')
		# print(idData)
		
		userID = askForCredentials()
		if userID:
			# if userID['u'] == idData[0] and userID['p'] == idData[1]:
			# if userID['u'] == logindata.secret['username'] and userID['p'] == logindata.secret['password']:
			# if userID['u'] == logindata.secret['username'] and userID['p'] == logindata.secret['password']:

			# if userID['p'] == userID['dbp']:
			# 	print("It matches")
			# 	# return redirect(url_for('user_profile'))
			# else:
			# 	print("Din't match")
			# 	# flash("Invalid credetials", "warning")

			# print(userID['p'])
			if bcrypt.checkpw(userID['p'], userID['dbp']):
				print('\n{}Access granted!{}\n'.format(colors.green,colors.white))
				main.globals['adminModeOn'] = True
			else:
				print('\n{}Access denied 1 - wrong pass!\n'.format(colors.brightRed))
		else:
			print('\n{}Access denied 2 - no user!\n'.format(colors.brightRed))

