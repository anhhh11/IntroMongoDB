__author__ = 'anhhh11'
"""
Your task is to sucessfully run the exercise to see how pymongo works
and how easy it is to start using it.
You don't actually have to change anything in this exercise,
but you can change the city name in the add_city function if you like.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB (see Instructor comments for link to installation information)
and uncomment the get_db function.
"""
"Regrex"
"http://regexpal.com/"
import datetime
def get_db():
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017')
    # 'examples' here is the database name. It will be created if it does not exist.
    db = client.examples
    return db

def command(db):
    db.autos.insert({"name" : "Car"})
    db.autos.find({'manufacturer_label':'Porsche'}).count()
    db.autos.find({"productionEndYear":{"$gte":datetime.datetime(1800,1,1,0,0,0)}}).count()
    db.autos.find({"class_label":{"$regex":"sport"}})
    db.autos.find({"class_label":{"$in":["sport","car"]}})


if __name__ == "__main__":

    db = get_db() # uncomment this line if you want to run this locally
    command(db)