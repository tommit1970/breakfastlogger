from pymongo import MongoClient
import datetime
import bcrypt
from Modules.fileHandling import readFile
import __main__ as main
import Modules.colors as colors
import getpass
import logindata



def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

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
	for item in result: # result is a list/an array
		findings = item
		# print(item)
		counter = counter + 1
	# print('Length of finds are '+ str(counter))
	client.close() # close connection

	if counter != 0:
		# print(findings['userPW'])
		return [findings['userPW'],findings['created']]
	return False



def askForCredentials():
	userName = getpass.getpass('Username: ')
	userPWD = getpass.getpass('Password: ').encode() # encode() for hash_compare
	DBresult = mongoDB_handling(userName)
	# print(DBresult)
	if DBresult:
		return {'p':userPWD, 'dbp':DBresult[0].encode(), 'created':DBresult[1]}
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
			today = datetime.datetime.now()
			dayDiff = (today - userID['created']).days
			# print(days_between(today, userID['created']))
			if bcrypt.checkpw(userID['p'], userID['dbp']):
				print('\n{}Access granted!{}\n'.format(colors.green,colors.white))
				# password freshness check
				if dayDiff > 3:
					print('Password Creation Date was:')
					print(userID['created'])
					print('That is {} days ago!'.format(dayDiff))
					print('You got to change your password!')
					if newPassword(): # returns True if Acceptable
						main.globals['adminModeOn'] = True
				else:
					print('Password is fresh enough')
			else:
				print('\n{}Access denied 1 - wrong pass!\n'.format(colors.brightRed))
		else:
			print('\n{}Access denied 2 - no user!\n'.format(colors.brightRed))

def newPassword():
	# ask for old password
	userID = askForCredentials()
	if userID:

		# password must be 5 characters long
		loop = True
		while loop:
			newPW = getpass.getpass('New Password: (x to abort) ')
			if newPW == 'x':
				print('Aborted!')
				loop = False
				return False
			else:
				if len(newPW) >= 5:
					# creation date
					now = datetime.datetime.now()
					# now = date.today().strftime('%Y-%m-%d')
					print(now.date())
					# connect to db
					client = MongoClient('mongodb://localhost:27017/')
					db = client['breakfastPW']
					collection = db['pw']
					hashedNewPW = bcrypt.hashpw(newPW.encode(), bcrypt.gensalt()).decode()
					collection.update_one({'_id':4},{'$set':{'userPW':hashedNewPW, 'created':now}})
					loop = False
					print('Password Changed!')
					client.close()
					return True
				else:
					print('Password must be at least 5 characters long.'.format(colors.brightRed))
	else:
		print('\n{}Rejected!\n'.format(colors.brightRed))
