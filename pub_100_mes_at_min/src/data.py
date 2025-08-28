from pymongo.errors import PyMongoError
from fetcher import Fetcher



class Data:

    def __init__(self, connection: Fetcher):
        self.connection = connection
        self.skipper_counter = 0
        self.collection = self.connection.db[self.connection.collection_name]


    def get_100_messages(self):
        try:
            result = self.collection.aggregate([
                {'$sort': {'CreateDate': 1}},
                {'$skip': self.skipper_counter},
                {'$limit': 100},
                {'$project': {'_id': 0}}

            ])
            self.skipper_counter += 100
            return result
        except PyMongoError:
            return {"error": "database_error"}