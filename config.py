import pymongo

mongo_url = "mongodb+srv://class:qybMHYNyqWj3INLr@cluster0.dy4zs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_url)
db = client.get_database('Fanatika')