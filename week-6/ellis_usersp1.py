from pymongo import MongoClient

client = MongoClient()

db = client["web335db"]

#find all users
users = (db.users.find({}))

for doc in users:
    print(doc)

#separate with empty line to help readability
    print(" ")

#find users by employeeId
print(db.users.find_one({"employeeId": '1011'}))

#find user(s) by last name
print(db.users.find_one({'lastName': 'Mozart'}))


