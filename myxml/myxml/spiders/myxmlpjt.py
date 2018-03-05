# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem

class MyxmlpjtSpider(XMLFeedSpider):
    name = 'myxmlpjt'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    iterator = 'xml' # you can change this; see the docs
    itertag = 'rss' # change it accordingly

    def parse_node(self, response, selector):
        i = MyxmlItem()
        i['title'] = selector.xpath('/rss/channel/item/title/text()').extract()
        i['link'] = selector.xpath('/rss/channel/item/link/text()').extract()
        for j in range(len(i['title'])):
            print(i['title'][j])
            print(i['link'][j])

        return i
