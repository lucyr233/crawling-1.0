#update, it's not working becuase I did not set up pipeline, it's weird that the wiki website works quoted by my tutor.

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
-*- coding: utf-8 -*-
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
        
 #the error shows as following:
'''
2017-03-14 21:33:07 [scrapy.core.scraper] ERROR: Spider error processing <GET http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=249692> (referer: None)
Traceback (most recent call last):
  File "C:\Users\R\Anaconda3\lib\site-packages\twisted\internet\defer.py", line 653, in _runCallbacks
    current.result = callback(current.result, *args, **kw)
  File "C:\Users\R\tutorial\tutorial\spiders\diliscrapy.py", line 48, in parse
    print (title2)
  File "C:\Users\R\Anaconda3\lib\encodings\cp437.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_map)[0]
UnicodeEncodeError: 'charmap' codec can't encode characters in position 14-17: character maps to <undefined>
'''
# and this errors does not show up when I use similar frame to crawl a english website
