from pymongo import MongoClient


# Connect to local MongoDB
class Connect(object):
    @staticmethod
    def connection():
        client = MongoClient("mongodb://localhost:27017/")
        # customer = client.customerdata.customer
        return client
