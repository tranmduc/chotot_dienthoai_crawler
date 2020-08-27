# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Dienthoai(Item):
    id = Field()
    url = Field()
    title = Field()
    price = Field()
    tel = Field()
    district = Field()
    seller = Field()
    seller_type = Field()
    crawled_time = Field()
    posted_time = Field()

    brand = Field()
    status = Field()
    storage = Field()
    series = Field()
    color = Field()
    ship = Field()
    guarantee = Field()