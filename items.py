# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProdirectItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    image = scrapy.Field()
    product_url = scrapy.Field()
