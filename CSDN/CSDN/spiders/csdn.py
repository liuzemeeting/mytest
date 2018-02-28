# -*- coding: utf-8 -*-
import scrapy
from CSDN.items import CsdnItem

class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    # allowed_domains = ['www.blog.csdn.net']
    start_urls = ['http://blog.csdn.net/liuzemeeting']

    def parse(self, response):
        print(response.body.decode())
        for item in response.xpath("//div[@class = 'article_title']/h1/span"):
            oneitem = CsdnItem()
            oneitem["title"] = item.xpath("./a/text()").extract()
            oneitem["url"] = item.xpath("./a/@href")
            yield scrapy.Request()
