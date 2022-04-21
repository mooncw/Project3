import json

data = None

with open('cardio.json','r') as json_file:
    data = json.load(json_file)


from pymongo import MongoClient

URI = "mongodb+srv://s3pro:nvQrIob89ExsJ35V@edadata.wjdcv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient(URI)

DATABASE = "myFirstDatabase"

database = client[DATABASE]

COLLECTION = "cardio"

collection = database[COLLECTION]

collection.insert_many(data)