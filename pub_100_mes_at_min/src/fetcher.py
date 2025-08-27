import os
import pymongo
from pymongo.errors import PyMongoError

class Fetcher:

    def __init__(self):
        self.collection_name = os.getenv("MONGODB_COLLECTION", "tweets")

        try:
            mongo_user = os.getenv("MONGODB_USER","IRGC_NEW")
            mongo_password = os.getenv("MONGODB_PASSWORD", "iran135")
            mongo_db = os.getenv("MONGODB_DATABASE","IranMalDB")

            self.client = pymongo.MongoClient(f"mongodb+srv://{mongo_user}:{mongo_password}@cluster0.6ycjkak.mongodb.net/")

            self.db = self.client[mongo_db]
        except PyMongoError as e:
            raise RuntimeError(f"MongoDB connection error: {e}")