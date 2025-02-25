from pymongo import MongoClient

class MongoDBClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = MongoClient("mongodb://admin:adminpassword@mongodb:27017")
            cls._instance.db = cls._instance.client["mydatabase"]
        return cls._instance

    def get_collection(self, collection_name):
        return self.db[collection_name]

# Global instance
mongo_client = MongoDBClient()
