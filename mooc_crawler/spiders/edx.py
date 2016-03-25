# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from mooc_crawler.items import MoocCrawlerItem

class EdxSpider(Spider):
    name = "edx"
    allowed_domains = ["edx.org/course"]
    start_urls = (
        'http://www.edx.org/course/',
    )

    def parse(self, response):
       	courses = Selector(response).xpath('//div[starts-with(@class,"course-card")]')
	
	for course in courses:
		item = MoocCrawlerItem()
		
		item['university'] = course.xpath('div[@class="label"]/text()').extract()[0] 
		item["url"] = EdxSpider.start_urls[0] + course.xpath('a/@href').extract()[0]
		item["start_date"] = course.xpath('div[@class="date"]/text()').extract()[0]
		item['title'] = course.xpath('div[@class="title"]/p/text()').extract()[0]
		yield item
		
