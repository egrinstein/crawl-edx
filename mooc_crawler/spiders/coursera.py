# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request 
from mooc_crawler.items import MoocCrawlerItem
from scrapy.utils.response import open_in_browser

BASE_URL = 'https://www.coursera.org'

def create_urls():
	NUM_PAGES = 79
	ITEMS_PER_PAGE = 20
	BASE_ST_URL = 'https://www.coursera.org/courses/?languages=en&query=&start='
	start_urls = range(0,(NUM_PAGES+1)*ITEMS_PER_PAGE,ITEMS_PER_PAGE)
	start_urls =  map(lambda x: BASE_ST_URL+str(x),start_urls)
	return start_urls

class CourseraSpider(Spider):
    name = "coursera"
    allowed_domains = ["https://www.coursera.org","www.coursera.org","coursera.org"]
    start_urls = create_urls()
    def parse(self, response):
		items = []	
		courses = Selector(response).xpath('//a[@class="rc-OfferingCard nostyle"]')

		for course in courses:
			item = MoocCrawlerItem()
			item["url"] = BASE_URL + course.xpath('@href').extract()[0]

			course = course.xpath('div[@class="offering-content"]/div[@class="horizontal-box"]/div[@class="offering-info flex-1"]')
			item["university"] = course.xpath('div[@class="text-light offering-partner-names"]/span/text()').extract()
			
			if not item['university']:
				continue
			else:
				item['university'] = item['university'][0] 
			item['title'] = course.xpath('div[@class="horizontal-box"]/h2[@class="color-primary-text headline-1-text flex-1"]/text()').extract()[0]
			return items

