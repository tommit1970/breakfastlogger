import pymongo
from pymongo import MongoClient
import datetime


# 'mongodb+srv://user:<password>@cluster0.itadr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
# replace <password> with actuall password from cloud mongodb
# replacde myFirstDatabase with the name of the database you want to access

now = datetime.datetime.now()
# mongodb+srv://user:<password>@cluster0.itadr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
# cloud


# if it does not work check your IP address, my was changed to 89.10.125.18

client = MongoClient('mongodb+srv://user:user@cluster0.itadr.mongodb.net/breakfast?retryWrites=true&w=majority')
db = client['breakfast']
collection = db['pw']

post = {'userName':'orange','userPW':'cloak','created':now}
collection.insert_one(post)


# post1 = {'_id':1,'userName':'green','userPW':'grass'}
# post2 = {'_id':2,'userName':'white','userPW':'stripes'}
# collection.insert_many([post1,post2])


# local

# client = MongoClient('mongodb://localhost:27017/')
# db = client['breakfastPW']
# collection = db['pw']


# post4 = {'_id':4, 'userName':'black','userPW':'berry'} 
# collection.insert_one(post4)

# result = collection.find({'userName':'black'})
# for item in result:
# 	print(item['userPW'])


# result = collection.find_one({})
# result = collection.find({})
# result = collection.delete_one({})
# result = collection.delete_many({})
# operators
# $set, $inc, $max, $min,
# result = collection.update_one({'_id':4},{'$set':{'joy':14}})
# result = collection.update_one({'_id':4},{'$set':{'userName':'blue'}})
# result = collection.update_many({})
