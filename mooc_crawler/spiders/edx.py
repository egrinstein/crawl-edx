# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from mooc_crawler.items import MoocCrawlerItem
from scrapy.utils.response import open_in_browser
from scrapy.http import Request

BASE_URL = "https://www.edx.org" 

class EdxSpider(Spider):
    name = "edx"
    allowed_domains = ["edx.org/course"]
    start_urls = (
    	BASE_URL+'/course',
	)

    def parse(self, response):
       	courses = Selector(response).xpath('//div[starts-with(@class,"course-card")]')
	course_links = Selector(response).xpath('//a[@class="course-link"]/@href').extract()
	print course_links
	open_in_browser(response)		
	for course in course_links:
		if course[0] == '/':
			course = BASE_URL + course
		#item = MoocCrawlerItem()
		#item['university'] = course.xpath('div[@class="label"]/text()').extract()[0] 
		#item["url"] = EdxSpider.start_urls[0] + course.xpath('a/@href').extract()[0]
		#item['title'] = course.xpath('div[@class="title"]/p/text()').extract()[0]
		item = Request(course, callback=self.parse_page) 
		yield item
    def parse_page(self,response):
	open_in_browser(response)
	item = MoocCrawlerItem()
	
