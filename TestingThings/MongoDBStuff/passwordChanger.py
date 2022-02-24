import bcrypt
from pymongo import MongoClient

print('What is your new password?')
password = input().encode()
hashedPW = bcrypt.hashpw(password, bcrypt.gensalt())

print('What is your userID?')
userID = int(input())


client = MongoClient('mongodb://localhost:27017/')
db = client['breakfastPW']
collection = db['pw']

collection.update_one({'_id':userID},{'$set':{'userPW':hashedPW}})
client.close()