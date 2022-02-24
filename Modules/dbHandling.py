import Modules.colors as colors
import Modules.smallFunctions as smallFuncs
from pymongo import MongoClient
import datetime
import bcrypt


def viewUsers():
	client = MongoClient('mongodb://localhost:27017')

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
	smallFuncs.printLines(2)
	client.close()

	return False # done, break loop

def deleteUser():
	viewUsers()

	print('Who do you want to delete? (x to abort)')
	userName = input()

	if userName == 'x':
		smallFuncs.abortedFeedback()
		return False
	client = MongoClient('mongodb://localhost:27017')

	db = client['breakfastPW']
	collection = db['pw']

	result = collection.find({'userName':userName})

	counter = 0
	for item in result:
		# print(item)
		counter = counter + 1

	if counter == 1:
		collection.delete_one({'userName':userName})
		smallFuncs.userDeletedFeedback(userName, counter)

	client.close()
	return False


def createUser():
	loop = True
	while loop:
		print('UserName:')
		userName = input()
		if indentifyUser(userName):
			smallFuncs.userExistsFeedback(userName)
		else:
			print('Password:')
			userPW = input()
			userPW = bcrypt.hashpw(userPW.encode(), bcrypt.gensalt())


			client = MongoClient('mongodb://localhost:27017')

			db = client['breakfastPW']
			collection = db['pw']

			now = datetime.datetime.now()
			collection.insert_one({'userName':userName, 'userPW':userPW, 'created':now})
			client.close()
			smallFuncs.userCreatedFeedback(userName, now)
			loop = False
	return False


def indentifyUser(userName):
	client = MongoClient('mongodb://localhost:27017')

	db = client['breakfastPW']
	collection = db['pw']

	result = collection.find({'userName':userName})

	for item in result:
		if item:
			return True # User exists

	return False # No user


def modifyHandler(userName, willBeModified):

	print('What is the new value? (x to abort)')
	value = input()

	if value == 'x':
		smallFuncs.abortedFeedback()
		return False
	elif willBeModified == 'userPW':
		value = value.encode()
		value = bcrypt.hashpw(value, bcrypt.gensalt())

	client = MongoClient('mongodb://localhost:27017')

	db = client['breakfastPW']
	collection = db['pw']

	collection.update_one({'userName':userName},{'$set':{willBeModified:value}})

	client.close()

	smallFuncs.userDataModifiedFeedback(willBeModified) # feedback
	return False


def modifyUser():
	viewUsers()
	print('Which user do you want to modify? (x to abort)')
	userName = input()

	if userName == 'x':
		smallFuncs.abortedFeedback()
		return False

	if indentifyUser(userName):

		loop = True
		while loop:
			print('Do you want to modify (u)sername or (p)assword? (x to abort)')
			userChoice = input()

			if userChoice == 'x':
				smallFuncs.abortedFeedback()
				return False
			elif userChoice == 'u':
				# modify username
				loop = modifyHandler(userName,'userName')
			elif userChoice == 'p':
				# modify password
				loop = modifyHandler(userName,'userPW')
	else:
		smallFuncs.userNotFoundFeedback()
	return False


def usersMenu():

	loop = True
	while loop:

		print('Do you want to (c)reate a user, (v)iew all users, (d)elete users or (m)odify users? (x to abort)')
		userChoice = input()
		if userChoice == 'v':
			loop = viewUsers()
		elif userChoice == 'c':
			loop = createUser()
		elif userChoice == 'd':
			loop = deleteUser()
		elif userChoice == 'm':
			loop = modifyUser()
		elif userChoice == 'x':
			smallFuncs.abortedFeedback()
			loop = False
