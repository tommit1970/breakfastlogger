from pymongo import MongoClient
from pymongo.errors import CollectionInvalid
from collections import OrderedDict

db = MongoClient("mongodb://localhost:27017/")['mydatabase']

user_schema = {
    'firstName': {
        'type': 'string',
        'minlength': 1,
        'required': True,
    },
    'lastName': {
        'type': 'string',
        'minlength': 1,
        'required': True,
    },
    'email': {
        'type': 'string',
        "required": False,
    },
    'phoneNo': {
        'type': 'int',
        'required': True,
    },
    'userId': {
        'type': 'int',
        'required': True,
    },
    'patientId': {
        'type': 'int',
        'required': True,
    },
    'age': {
        'type': 'int'
    },
    "userStatus": {
        "type": "int"
    }
}

collection = 'Userinformation'
validator = {'$jsonSchema': {'bsonType': 'object', 'properties': {}}}
required = []

for field_key in user_schema:
    field = user_schema[field_key]
    properties = {'bsonType': field['type']}
    minimum = field.get('minlength')

    if type(minimum) == int:
        properties['minimum'] = minimum

    if field.get('required') is True: required.append(field_key)

    validator['$jsonSchema']['properties'][field_key] = properties

if len(required) > 0:
    validator['$jsonSchema']['required'] = required

query = [('collMod', collection),
         ('validator', validator)]

try:
    db.create_collection(collection)
except CollectionInvalid:
    pass

command_result = db.command(OrderedDict(query))