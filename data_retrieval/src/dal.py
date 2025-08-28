from pymongo.errors import PyMongoError
from mongodb_connection import DbConnection



class Dal:

    def __init__(self, collection1="tweets_antisemitic", collection2='tweets_not_antisemitic'):
        self.connection = DbConnection()
        self.collection1 = self.connection.db[collection1]
        self.collection2 = self.connection.db[collection2]

    def find_all_tweets_antisemitic(self):
        try:
            return list(self.collection1.find({}, {'_id': 0}))
        except PyMongoError:
            return {"error": "database_error"}

    def find_all_tweets_not_antisemitic(self):
        try:
            return list(self.collection2.find({}, {'_id': 0}))
        except PyMongoError:
            return {"error": "database_error"}