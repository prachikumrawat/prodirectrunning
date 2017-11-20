import pymongo
from pymongo import MongoClient
import time
import unicodecsv
import os
import sys
from pprint import pprint

import pymongo
from pymongo import MongoClient
from utilities.spider_settings import spider_settings


class ProdirectPipeline(object):

    def __init__(self, category_name, **kwargs):
        self.category_name = category_name
        self.db_connect()

    @classmethod
    def from_crawler(cls, crawler):
        category_name = crawler.settings['category_name']
        db_name = crawler.settings.get('db_name')
        if db_name:
            return cls(category_name, db_name=db_name)
        else:
            return cls(category_name)

    def db_connect(self):
        client = MongoClient('mongodb://localhost:27017/')
        # self.db = client[self.db_name]
        # self.collection = self.db[self.category_name]

        # if 'Prodirect_Running' in self.db_name:
        #     if 'y' in raw_input('Erase previous data for {} (Y/N): '.format(self.category_name)).lower():
        #         self.collection.drop()

    def open_spider(self, spider):
        '''Dropping previously scraped databases '''
        print 'Opening..'
        # self.db[self.category_name].drop()

    def close_spider(self, spider):
        print 'Closing..'

    def get_inventory(self, sku_suffix, script_type, category_name, **kwargs):
        client = MongoClient('mongodb://localhost:27017/')
        master_db = client['Prodirect_Running']
        self.collection_name = category_name
        master_collection = master_db.collection_name.find()
        if script_type == "replenishment":
            cursor = master_collection.find()

        print 'Total fetched skus which match {} = {}'.format(sku_suffix, cursor.count())
























    # def __init__(self):
    #     self.spider_object ={}
    #     connection = MongoClient(
    #         spider_settings['MONGODB_SERVER'],
    #         spider_settings['MONGODB_PORT'])
    #     db = connection[spider_settings['MONGODB_DB']]
    #     # assert isinstance(spider_settings, object)
    #     self.collection = db[spider_settings['MENS_RUNNING_COLLECTION']]
    #     #                      spider_settings['RUNNING_COLLECTION'],
    #     #                     spider_settings['MASTERFILE_COLLECTION']]
    #
    # # def __init__(self):
    # #     self.duplicates = {}
    # #     dispatcher.connect(self.spider_opened, signals.spider_opened)
    # #     dispatcher.connect(self.spider_closed, signals.spider_closed)
    #
    # def spider_opened(self, spider):
    #     self.spider_object[spider] = set()
    #
    # def spider_closed(self, spider):
    #     del self.spider_object[spider]
    #
    # # def process_item(self, item, spider):
    # #     if item['id'] in self.duplicates[spider]:
    # #         raise DropItem("Duplicate item found: %s" % item)
    # #     else:
    # #         self.duplicates[spider].add(item['id'])
    # #         return item
    #
    def process_item(self, item,spider):
        if item['id'] in self.spider_object[spider]:
            self.collection.insert_one(dict(item))
            return item



# class MongoDB_Connection(object):

    # def write_database(self, script_type, category_name):
    #     client = MongoClient('mongodb://localhost:27017/')
    #     db_client = client['ProdirectDB']
    #
    #     if category_name == "Mens Running":
    #         collection = db_client['Mens Running']
    #     elif category_name == "Running":
    #         collection = db_client['Running']
    #     else:
    #         print "Incorrect choice! The script will now terminate, please rerun and choose a valid choice"
    #         time.sleep(5)
    #         sys.exit("Script terminated")
    #
    #     if script_type == "replenishment":
    #         cursor = collection.insert_one()
    #
    #     print 'Total fetched items = {}'.format(cursor.count())
    #
    #     masterfile_asin_list = []
    #     for row in cursor:
    #         masterfile_asin_list.append(row['asin'].strip())
    #     return masterfile_asin_list


