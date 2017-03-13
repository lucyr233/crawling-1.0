from scrapy import Item,Field

class aditem(item):
    url=Field()
    title=Field()
    content=Field()
