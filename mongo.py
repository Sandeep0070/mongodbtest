import pymongo

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://sandeepwaghmare9834:Sandeew@cluster0.v4la18y.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
print(client)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

d= {
    "name":"sandeep",
    "Email":"sandeep@gmail.com"
}

db=client['mongotes   t']
coll=db['test']
coll.insert_one(d)