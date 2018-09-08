# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Music163Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sing_id = scrapy.Field()
    playlist_id = scrapy.Field()
    name = scrapy.Field()
    singer = scrapy.Field()
    album = scrapy.Field()
    lyrics = scrapy.Field()
    count_comments = scrapy.Field()
    hot_comment = scrapy.Field()

