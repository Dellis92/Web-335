load (houses.js)

//list houses in document
db.houses.find()

//get a list of students in document
db.students.find()

//add a document to student collection 
db.students.insertOne({ firstName: 'Dwayne', lastName: 'Johnson', studentId: 's1019', houseId: 'h1007'})

//delete student query
db.students.deleteOne({ studentId: 's1019'})

//query by house
db.students.aggregate([
    {
        $lookup: {
            from: "houses",
            localField: "houseId",
            foreignField: "houseId",
            as: "house_info"
        }
    }
])

//query by house Gryffindor
db.students.aggregate([
    {
        $lookup: {
            from: "houses",
            localField: "houseId",
            foreignField: "houseId",
            as: "house_info"
        }
    },
    {
        $match: { "house_info.houseId": "h1002"}
    }
])

//query students by Eagle mascot
db.students.aggregate([
    {
        $lookup: {
            from: "houses",
            localField: "houseId",
            foreignField: "houseId"
            as: "house_info"
        }
    },
    {
        $match: { "house_info.mascot": "Eagle"}
    }
])
