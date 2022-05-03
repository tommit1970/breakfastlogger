import Modules.colors as colors
import Modules.smallFunctions as smallFuncs
from pymongo import MongoClient
import datetime
import bcrypt
import __main__ as main
import getpass


def viewUsers():
	client = MongoClient(main.globals['dbAddressActive'])

	db = client['breakfastPW']
	collection = db['pw']

	result = collection.find()

	userArray = []

	print('DB-Users:')
	print('UserID\t\t\t\tUserName')

	for item in result:
		item['_id'] = str(item['_id'])
		data = [item['_id'], item['userName']]
		userArray.append(data)

	for i,u in userArray:
		textJunction = '{}{}{}{}{}'.format(colors.green,i,'\t',colors.magenta,u)
		print(textJunction)
	print('{}---------------------------------------'.format(colors.white))
	smallFuncs.printLines(2)
	client.close()


def deleteHandling(dbAddress, userName):
		client = MongoClient(dbAddress)

		db = client['breakfastPW']
		collection = db['pw']

		result = collection.find({'userName':userName})

		counter = 0
		for item in result:
			# print(item)
			counter = counter + 1

		if counter >= 1:
			collection.delete_one({'userName':userName})

		client.close()
		
		if counter >= 1:
			return True
		return False
	

def deleteUser():
	viewUsers()

	print('Who do you want to delete? (x to abort)')
	userName = input()

	if userName == 'x':
		smallFuncs.abortedFeedback()
		return

	else:
		localDel = deleteHandling(main.globals['dbAddressLocal'], userName)
		if localDel:
			cloudDel = deleteHandling(main.globals['dbAddressCloud'], userName)
		
			if cloudDel:
				smallFuncs.userDeletedFeedback(userName)
			else:
				smallFuncs.userNotFoundFeedback()




def dbSave(dbAddress, userName, userPW):
	client = MongoClient(dbAddress)

	db = client['breakfastPW']
	collection = db['pw']

	now = datetime.datetime.now()
	collection.insert_one({'userName':userName, 'userPW':userPW, 'created':now})
	client.close()



def createUser():
	while True:
		print('UserName: (x to abort)')
		userName = input()
		if userName == 'x':
			smallFuncs.abortedFeedback()
			break

		if len(userName) >=3:
			if indentifyUser(userName):
				smallFuncs.userExistsFeedback(userName)
			else:
				userPW = getpass.getpass('Password: (x to abort)')
				if userPW == 'x':
					smallFuncs.abortedFeedback()
					break
				userPW = bcrypt.hashpw(userPW.encode(), bcrypt.gensalt())
				dbSave(main.globals['dbAddressLocal'], userName, userPW)
				dbSave(main.globals['dbAddressCloud'], userName, userPW)

				smallFuncs.userCreatedFeedback(userName)
				break
		else:
			print('{}\nUsername is too short!\n{}'.format(colors.brightRed, colors.white))


def indentifyUser(userName):
	client = MongoClient(main.globals['dbAddressActive'])

	db = client['breakfastPW']
	collection = db['pw']

	result = collection.find({'userName':userName})

	for item in result:
		if item:
			return True # User exists

	return False # No user


def checkPassword(userName, userPW):
	client = MongoClient(main.globals['dbAddressActive'])

	db = client['breakfastPW']
	collection = db['pw']

	result = collection.find({'userName':userName})

	for item in result:
		if bcrypt.checkpw(userPW.encode(), item['userPW']):
			print('{}Passport is the same!{}'.format(colors.brightRed,colors.white))
			return False
		else:
			print('{}Password changed!{}'.format(colors.green, colors.white))
			return True


def modifyInnDB(dbAddress, userName, value):
	newCreated = datetime.datetime.now()

	client = MongoClient(dbAddress)
	db = client['breakfastPW']
	collection = db['pw']
	collection.update_one({'userName':userName},{'$set':{'userPW':value,'created':newCreated}})

	client.close()


def modifyHandler(userName):
	passCheckOK = False
	while True:
		textJunction = '\nWhat is the new value? (x to abort)'
		value = getpass.getpass(textJunction + '\n')
		if value == 'x':
			smallFuncs.abortedFeedback()
			return
		if checkPassword(userName, value):
				passCheckOK = True
				value = value.encode()
				value = bcrypt.hashpw(value, bcrypt.gensalt())
				modifyInnDB(main.globals['dbAddressLocal'], userName, value)
				modifyInnDB(main.globals['dbAddressCloud'], userName, value)
				smallFuncs.userDataModifiedFeedback('UserPW') # feedback
				return



def modifyUser():
	viewUsers()
	print('Which user do you want to modify? (x to abort)')
	userName = input()

	if userName == 'x':
		smallFuncs.abortedFeedback()
		return

	if indentifyUser(userName):

		while True:
			print('Do you want to modify the ({}p{})assword? ({}x to abort{})'.format(colors.brightRed,colors.white,colors.brightRed,colors.white))
			userChoice = input()

			if userChoice == 'x':
				smallFuncs.abortedFeedback()
				break
			elif userChoice == 'p':
				# modify password
				modifyHandler(userName)
				break
	else:
		smallFuncs.userNotFoundFeedback()
	return False


def usersMenu():
	while True:
		print('Do you want to (c)reate a user, (v)iew all users, (d)elete users or (m)odify users? (x to abort)')
		userChoice = input()
		if userChoice == 'v':
			viewUsers()
			break
		elif userChoice == 'c':
			createUser()
			break
		elif userChoice == 'd':
			deleteUser()
			break
		elif userChoice == 'm':
			modifyUser()
			break
		elif userChoice == 'x':
			smallFuncs.abortedFeedback()
			break