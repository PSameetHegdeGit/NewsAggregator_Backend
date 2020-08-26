from pymongo import *

class DatabaseAccess():

    def __init__(self):
        self.access = MongoClient('mongodb+srv://admin:<newsaggregatoradministrator>@newsaggregatordb.tsujr.mongodb.net/<NewsAggregatorDB>?retryWrites=true&w=majority')


