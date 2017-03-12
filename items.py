# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#import scrapy
from scrapy import Item,Field

class aditem(item):
    url=Field()
    title=Field()
    bk=Field()
    yjs=Field()
    Tsum=Field()
    Gsum=Field()
    submarjor=Field()
    BG=Field()
    submittime=Field()
    location=Field()
    knowway=Field()

class contentitem(item):
    url=Field()
    title=Field()
    author=Field()

#class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#    pass
