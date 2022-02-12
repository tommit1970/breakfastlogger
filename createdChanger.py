import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['breakfastPW']
collection = db['pw']

randomDay = datetime.datetime(2022,1,31,20,15)

collection.update_one({'_id':4},{'$set':{'created':randomDay}})
client.close()