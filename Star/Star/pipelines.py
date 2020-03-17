# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Star import settings
import pymongo
import pymysql

class StarPipeline(object):
    def process_item(self, item, spider):
        print("===================")
        # print(item['starName'])
        # print(item['starDay'])
        print("===================")
        return item
class StarmongoPipeline(object):
    def __init__(self):
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT
        conn = pymongo.MongoClient(host=host,port=port)
        db = conn.star
        self.myset = db.star3


    def process_item(self,item,spider):
        bookInfo = dict(item)
        self.myset.insert(bookInfo)
        print("存入数据庫成功")
        return item

class StarmysqlPipeline(object):
    def __init__(self):
        host = settings.MYSQL_HOST
        user = settings.MYSQL_USER
        pwd = settings.MYSQL_PWD
        dbName = settings.MYSQL_DB
        self.db = pymysql.connect(host=host,user=user,
                     password = pwd,
                     db = dbName,
                     charset = "utf8")
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        '''    starName = scrapy.Field()
    starDay = scrapy.Field()
    all1 = scrapy.Field()
    all2 = scrapy.Field()
    love1 = scrapy.Field()
    love2 = scrapy.Field()
    business1 = scrapy.Field()
    business2 = scrapy.Field()
    money1 = scrapy.Field()
    money2 = scrapy.Field()'''
        ins = 'insert into starTable values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        L = [item['starName'],item['starDay'],item['all1'],\
             item['all2'],item['love1'], \
             item['love2'],item['business1'], \
             item['business2'],item['money1'],item['money2']]
        self.cursor.execute(ins,L)
        self.db.commit()
















