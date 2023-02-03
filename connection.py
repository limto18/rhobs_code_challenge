import json
from pymongo import MongoClient

def get_database():
 
   # mongodb atlas url 
   CONNECTION_STRING = "mongodb+srv://rhobs:123456lamine@rhobscluster.biytn8p.mongodb.net/?retryWrites=true&w=majority"
 
   # connection using MongoClient. 
   client = MongoClient(CONNECTION_STRING)
 
   return client['rhobsData']

def collection():
    database = get_database()
    collection = database["people"]
    return collection

def load(datapath):
    coll = collection()
    with open(datapath,"r") as fp:
        data = json.load(fp)

        for person in data:
            coll.insert_one(person)




if __name__ == "__main__": 
    db = get_database()  
#load data
file_path = "./data.json.codechallenge.janv22.RHOBS.json"
#load(file_path)


