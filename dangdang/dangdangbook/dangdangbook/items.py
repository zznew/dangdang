# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    detail = scrapy.Field()
    price = scrapy.Field()
    comment = scrapy.Field()
    label = scrapy.Field()
    author = scrapy.Field()
    time = scrapy.Field()
    press = scrapy.Field()
