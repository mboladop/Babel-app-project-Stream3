import os
from pymongo import MongoClient


MONGODB_URI = "mongodb://mboladop:mboladop1@ds147420.mlab.com:47420/babel-chatapp-project"
MONGODB_NAME = "babel-chatapp-project"

print(MONGODB_URI)

with MongoClient(MONGODB_URI) as conn:
    db = conn[MONGODB_NAME]

    cats = db['chat-messages'].find()
    for cat in cats:
        print(cat)