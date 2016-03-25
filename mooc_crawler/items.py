# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoocCrawlerItem(scrapy.Item):
	title = scrapy.Field()
	url = scrapy.Field()
	university = scrapy.Field()
	instructor_names = scrapy.Field()
	n_reviews = scrapy.Field()
	rating = scrapy.Field()	

