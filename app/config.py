from pymongo import MongoClient

def get_con():
    con = MongoClient('mongodb://localhost:27017')
    return con['aplication']


def create_collection():
    db = get_con()
    db.create_collection('address')
    db.create_collection('user')
    db.create_collection('tools')
    db.create_collection('musician')
    db.create_collection('orchestra')
    return True
