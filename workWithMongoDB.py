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
"RoboMongo"
import datetime
def get_db():
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017')
    # 'examples' here is the database name. It will be created if it does not exist.
    #import data
# mongoimport --host localhost --port 27017--type csv --headerline --collection autos < ~/Desktop/autos.csv --db examples
    db = client.examples
    return db

def command(db):
    #Inserw
    db.autos.insert({"name" : "Car"})
    #Equal condition == where ..=...
    db.autos.find({'manufacturer_label':'Porsche'}).count()
    #Comparastion == where ... >= ...
    db.autos.find({"productionEndYear":{"$gte":datetime.datetime(1800,1,1,0,0,0)}}).count()
    #Pattern == like ...
    db.autos.find({"class_label":{"$regex":"sport"}})
    #Range == in (.... , ... )
    db.autos.find({"class_label":{"$in":["sport","car"]}})
    #All == all ( ..... )
    db.autos.find({"class_label":{"$all":[1891,1895,1990]}})
    #Dot == join + where
    db.autos.find({"dimensions.width":{"$gt":2.5}})
    #Save == insert into
    a = db.autos.find_one({"class_label":"Sports car"})
    a["designer"] = "MODIFIED DESIGNER"
    db.autos.save(a)
    #Update == update .. set .. where
    condition = {"rdf-schema#label" : "Mazda MX-5"}
    set = {"$set":{"width":300},"$unset":{"height":""}}
    db.autos.update(condition,set)
    #Multiple update
    condition = {"class_label" : {"$regex":"sport"}}
    set = {"$set":{"width":150},"$unset":{"height":""}}
    db.autos.update(condition,set,multi=True)
    #Delete == delete from ... where ...
    condition = {"class_label" : {"$regex":"sport"}}
    db.autos.remove(condition)
    #Find document not have `super car` tag
    condition = {"super car" : {"$exists": 0}}
    db.autos.find(condition)
if __name__ == "__main__":

    db = get_db() # uncomment this line if you want to run this locally
    command(db)