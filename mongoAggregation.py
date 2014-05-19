#!/usr/bin/env python
"""
The tweets in our twitter collection have a field called "source". This field describes the application
that was used to create the tweet. Following the examples for using the $group operator, your task is
to modify the 'make-pipeline' function to identify most used applications for creating tweets.
As a check on your query, 'web' is listed as the most frequently used application.
'Ubertwitter' is the second most used.

Please modify only the 'make_pipeline' function so that it creates and returns an aggregation pipeline
that can be passed to the MongoDB aggregate function. As in our examples in this lesson, the aggregation
pipeline should be a list of one or more dictionary objects.
Please review the lesson examples if you are unsure of the syntax.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine, you have to install MongoDB,
download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.

Please note that the dataset you are using here is a smaller version of the twitter dataset
used in examples in this lesson.
If you attempt some of the same queries that we looked at in the lesson examples,
your results will be different.
"""


def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def agg_group():
    """
        select source,count(source)
        from tweets
        --where length(source)>3
        group by source
        sort by count desc
        limit 10
    """

    # complete the aggregation pipeline
    pipeline = [
    {"$group":{ "_id":"$source", "count": {"$sum": 1} }},
    {"$sort":{ "count" : -1}},
    {"$limit" : 10}
    ]

def agg_project():

    """
    from user
    #where time_zone="Brasilia" and statuses_count>100
    #select screen_name,statuses_count as tweets, followers_count as followers
    sort by count desc
    """

    match = {"$match": {"user.time_zone":"Brasilia"}}
    project = {"$project":{"screen_name":"$user.screen_name",
                           "tweets":"$user.statuses_count",
                           "followers":"$user.followers_count"}}
    sort = {"$sort":{"followers":-1}}
    limit = {"$limit":1}
    pipeline = [ match,project,sort,limit]

    return pipeline

def agg_multi_stage():
    # complete the aggregation pipeline
    match = {"$match" : {"country": "India"}}
    unwind = {"$unwind": "$isPartOf"}
    group = {"$group": {"_id":"$isPartOf","avg_region":{"$avg":"$population"}}}
    group_pop = {"$group" : {"avg" : {"$avg":"$avg_region"},"_id":None}}
    pipeline = [ match, unwind, group,group_pop]
    return pipeline

def agg_unwind():
    # complete the aggregation pipeline
    unwind = {"$unwind" : "$isPartOf"}
    group = {"$group" : {"_id" : "$isPartOf","count":{"$sum":1}}}
    sort = {"$sort" : {"count":-1}}
    match = {"$match":{"country":"India"}}
    pipeline = [match,unwind,group,sort]
    return pipeline

def agg_count():
    group = {"$group":{"_id":"$user.screen_name",
                       "tweet_texts":{"$push":"$text"},
                       "count":{"$sum":1}}}
    sort = {"$sort" : {"count" : -1}}
    limit = {"$limit" : 5}
    return pipeline

def tweet_sources(db, pipeline):
    limited_source_length_tweet = db.tweets.find({"source" : {"$exists":True}, "$where":"this.source.length > 3"})
    result = limited_source_length_tweet.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('tweeter')
    pipeline = make_pipeline()
    result = tweet_sources(db, pipeline)
    import pprint
    pprint.pprint(result)
