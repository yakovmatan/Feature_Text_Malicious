from pymongo.errors import PyMongoError
from fetcher import Fetcher



class Data:

    def __init__(self):
        self.connection = Fetcher()
        self.skipper_counter = 0
        self.collection = self.connection.db[self.connection.collection_name]
        self.antisemitic = None
        self.not_antisemitic = None


    def get_100_messages(self):
        try:
            result = self.collection.find({}, {"_id": 0}).skip(self.skipper_counter).limit(100)
            self.skipper_counter += 100
            return result
        except PyMongoError:
            return {"error": "database_error"}


    def split_data_per_category(self, documents, category="Antisemitic"):
        category1 = []
        category2 = []
        for document in documents:
            if document[category]:
                category1.append(document)
            else:
                category2.append(document)

        self.antisemitic = category1
        self.not_antisemitic = category2