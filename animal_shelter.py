from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://localhost:44773')
        #self.client = MongoClient('mongodb://%s:%s@localhost:xxxxx' % (username, password))
        # where xxxx is your unique port number
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD. 
    def read_all(self, data):
        cursor = self.database.animals.find(data, {'_id':False}) #return a cursor which points to a list of document results
        return cursor
    def read(self, data):
        return self.database.animals.find_one(data,{"_id":False}) #returns only one document as a python dictionary