# -*- coding: utf-8 -*-
import scrapy


class dili(scrapy.Spider):
    name = "dili"
    host="http://www.1point3acres.com/bbs/forum-82-1"
    start_urls= ［"http://www.1point3acres.com/bbs/
    forum.php?mod=viewthread&tid=234188&extra=page%3D1%26filter%3Dsortid%26sortid%3D164%26sortid%3D164"］
    def start_request(self):
        for url in self.start_urls
            yield Request(url=url,callback=self.parse)

    def parse(self, response):
        selector=Selector(response)
        item['title'] = selector.xpath('//title/text()').extract()
        item['url']=selector.xpath("//*[@class='xg1']/a/@herf")
        item['content']=selector.xpath("//*[@class='pcb']/li/text()").extract
        #next = selector.xpath("//[@class='y']/a[@title=“下一主题”]@herf")

        next_item=response.xpath("//[@class='y']/a[@title=“下一主题”]@herf")
        if nex_item is not None:
            next_item=resonse.urljoin(next_item)
            yield scrpay.Request(nest_item,self.parse)
