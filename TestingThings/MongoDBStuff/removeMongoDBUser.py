from pymongo import MongoClient

print('What is your userName?')
userName = input()

client = MongoClient('mongodb://localhost:27017')
db = client['breakfastPW']
collection = db['pw']


result = collection.find({'userName':userName})

for item in result:
	print(item)


print('Which ID do you want to delete? (x to abort)')
id = input()

if id == 'x':
	print('Aborted')
else:
	collection.delete_one({'_id':int(id)})

client.close()