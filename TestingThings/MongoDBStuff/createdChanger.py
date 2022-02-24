import datetime
from pymongo import MongoClient

print('What is your userName?')
userName = input()

client = MongoClient('mongodb://localhost:27017/')
db = client['breakfastPW']
collection = db['pw']

randomDay = datetime.datetime(2022,1,31,20,15)

collection.update_one({'userName':userName},{'$set':{'created':randomDay}})
client.close()