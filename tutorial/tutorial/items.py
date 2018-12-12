# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class weapon_ig_message(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    # img = scrapy.Field()
    # the lowest price in the very item
    selling_price = scrapy.Field()
    # the item sold history
    selling_date = scrapy.Field()
