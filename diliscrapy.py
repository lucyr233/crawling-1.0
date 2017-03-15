'''
# -*- coding: utf-8 -*-
import scrapy


class dili(scrapy.Spider):
    name = "dili"
    host="http://www.1point3acres.com/bbs/forum-82-1"
    start_urls= ['http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=249692']

    def start_request(self):
        for url in self.start_urls:
            yield Request(url=url,callback=self.parse)

    def parse(self, response):
        #selector=Selector(response)
        item=aditem()
        item['title'] = response.xpath('//title/text()').extract()
        item['url']=response.xpath("//link[@rel='canonical']/@href").extract()
        item['content']=response.xpath("//*[@class='pcb']/li/text()").extract()
        #next = selector.xpath("//[@class='y']/a[@title=“下一主题”]@herf")

        next_item=response.xpath("//[@class='y']/a[@title=“下一主题”]/@href").extract()
        if nex_item is not None:
            next_item=response.urljoin(next_item)
            yield scrpay.Request(nest_item,self.parse)

'''

import scrapy
#from tutorial.items import aditem

class dili(scrapy.Spider):
    name='dili'
    start_urls = ['http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=249692']

    def parse(self,response):
        #items = []
        #items=aditem()
        #item['title'] = response.xpath('//title/text()').extract()
        #item['url'] = response.xpath("//link[@rel='canonical']/@href").extract()
        #item['content'] = response.xpath("//[@class='pcb']/li/text()").extract()
        #items.append(item)
        title= response.xpath('//title/text()').extract()
        link= response.xpath("//link[@rel='canonical']/@href").extract()
        content= response.xpath("//div[@class='pcb']/li/text()").extract()

        print (title,link,content)