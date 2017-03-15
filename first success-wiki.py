import scrapy
from tutorial.items import aditem

class dili(scrapy.Spider):
    name='dili'
    start_urls=['https://en.wikipedia.org/wiki/False_discovery_rate']

    def parse(self, response):
        items=[]
        item=aditem()
        item['title'] = response.xpath('//title/text()').extract()
        item['link'] = response.xpath("//link[@rel='canonical']/@href").extract()
        items.append(item)
        
        return item
        
 # how to use the item.py in crawling is that import the item class.
