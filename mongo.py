# creating connection string
CONNECTION = 'mongodb+srv://andreDB:Jackie287@cluster0.cidwu.mongodb.net/?retryWrites=true&w=majority'

# setting up MongoDB
# importing python connector
import pymongo as pm

# connecting to DB
client = pm.MongoClient(CONNECTION)
db = client['andreDB']
mycol = db['first-table']

# inserting first row
data = {'name': 'Andre', 'state': 'Texas', 'age': 22}
first_insert = mycol.insert_one(data)

data = {'name': 'Jackie', 'state': 'Germany', 'age': 22}
second_insert = mycol.insert_one(data)

# get collection_names
print(db.list_collection_names())

mycol.delete_many({'age': 22})

for x in mycol.find():
    print(x)