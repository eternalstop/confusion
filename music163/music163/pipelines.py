# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings


class Music163Pipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(
            host=settings['mysql_host'],
            user=settings['mysql_user'],
            password=settings['mysql_passwd'],
            database=settings['mysql_dbname']
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute('truncate table sings;')
        self.conn.commit()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """INSERT INTO sings(sing_id, playlist_id, name, singer, album, lyrics, count_comments, hot_comments) values (%s, %s, %s, %s, %s, %s, %s, %s) """,
                (
                    item['sing_id'], item['playlist_id'], item['name'], item['singer'], item['album'], item['lyrics'], item['count_comments'], item['hot_comments']
                 )
            )
            self.conn.commit()
        except pymysql.Error as e:
            print(e)
        return item
