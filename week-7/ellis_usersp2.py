from pymongo import MongoClient

client = MongoClient(
    "mongo"
)

db = client['web335db']

new_comp = {
    "firstName": "Michael",
    "lastName": "Jordan",
    "employeeID": "1014",
    "email": "mjordan23@gmail.com"
}

new_user = db.users.insert_one(new_user)

new_user = db.users.find_one({"employeeID": "1014"})
print("Created user: ")
print(created_user)

#update email address
db.users.update_one({"employeeId": "1014"}, {"$set": {"email: mjordad23@gmail.com"}})

#display update
updated_user = db.users.find_one({"employeeId": "1014"})
print("Updated user:")
print(updated_user)

#delete document
db.users.delete_one({"employeeId": "1014"})

#show user was deleted
deleted_user = db.users.find_one({"employeeId": "1014"})

