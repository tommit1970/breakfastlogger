import bcrypt
import datetime
from pymongo import MongoClient

now = datetime.datetime.now()

print('What is the userName?')
userName = input()

print('What is your new password?')
password = input().encode()
hashedPW = bcrypt.hashpw(password, bcrypt.gensalt())

print('What is your userID?')
userID = int(input())


client = MongoClient('mongodb://localhost:27017/')
db = client['breakfastPW']
collection = db['pw']

ok = collection.insert_one({'_id':userID,'userName':userName,'userPW':hashedPW, 'created':now})
client.close()

if ok:
	print('collection created')
