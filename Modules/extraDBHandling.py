import Modules.colors as colors
from pymongo import MongoClient
import datetime
import __main__ as main
import Modules.smallFunctions as smallFuncs

##############################################################
# if it does not work check your IP address, my was changed to 89.10.125.18
##############################################################

# 'mongodb+srv://user:<password>@cluster0.itadr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
# replace <password> with actuall password from cloud mongodb
# replacde myFirstDatabase with the name of the database you want to access

# mongodb+srv://user:<password>@cluster0.itadr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
# cloud

def findUser(dbAddress, userName):
	client = MongoClient(dbAddress)
	db = client['breakfastPW']
	collection = db['pw']

	result = collection.find({'userName':userName})
	oneUser = []
	counter = 0
	if result:
		for item in result:
			counter += 1
			oneUser.append({'userName':item['userName'],'userPW':item['userPW'],'created':item['created']})
	
	client.close()

	if counter != 0:
		return oneUser
	return False

def loadDBtoArray(collection):

	result = collection.find()
	pwArray = []
	counter = 0
	if result:
		for item in result:
			counter += 1
			# print('Found user data')
			pwArray.append({'userName':item['userName'],'userPW':item['userPW'],'created':item['created']})
	
	if counter != 0:
		return pwArray
	return False


def createDBUser(dbAddress, userName, userPW, created):
	client = MongoClient(dbAddress)
	db = client['breakfastPW']
	collection = db['pw']

	collection.insert_one({'userName':userName, 'userPW':userPW, 'created':created})
	client.close()


def syncHandling(fromDB, toDB):

	client = MongoClient(fromDB)
	db = client['breakfastPW']
	collection = db['pw']
	allLocalDBArray = loadDBtoArray(collection)


	for item in allLocalDBArray:
		if not findUser(toDB, item['userName']):
			createDBUser(toDB, item['userName'], item['userPW'], item['created'])
			print('User ' + item['userName'] + ' created')
		else:
			print('.',end="")
	
	client.close()
	print()


def syncDBs():
	print('On the way.......this may take some time!')
	dbLocal = main.globals['dbAddressLocal']
	dbCloud = main.globals['dbAddressCloud']

	# dbFrom - first, dbTo - last
	syncHandling(dbLocal,dbCloud)
	syncHandling(dbCloud,dbLocal)



def whichDB():
	while True:
		print('\nChoose ({}l{})ocal or ({}c{})loud DB! (x to abort)'.format(colors.brightRed,colors.white,colors.brightRed,colors.white))
		userChoice = input()
		if userChoice == 'x':
			smallFuncs.abortedFeedback()
			break
		elif userChoice == 'l':
			main.globals['dbTypeActive'] = 'local'
			main.globals['dbAddressActive'] = 'mongodb://localhost:27017'
			break
		elif userChoice == 'c':
			main.globals['dbTypeActive'] = 'cloud'
			main.globals['dbAddressActive'] = 'mongodb+srv://user:user@cluster0.itadr.mongodb.net/breakfast?retryWrites=true&w=majority'
			break


def dbActionMenu():
	while True:
		print('DB - Now: {}{}{}'.format(colors.brightRed,main.globals['dbTypeActive'],colors.white))
		print('Set ({}m{})ongeDB or ({}s{})ync local + cloud DB (x to abort)'.format(colors.brightRed,colors.white,colors.brightRed,colors.white))
		userChoice = input()
		if userChoice == 'x':
			smallFuncs.abortedFeedback()
			break
		elif userChoice == 'm':
			whichDB()
			break
		elif userChoice == 's':
			syncDBs()
			break
		else:
			print('\n{}Not an option!{}\n'.format(colors.brightRed,colors.white))