# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MOOCItem(scrapy.Item):
    number = scrapy.Field()
    partner = scrapy.Field()
    title = scrapy.Field()
    short_description = scrapy.Field()
    full_description = scrapy.Field()
    level_type = scrapy.Field()
    marketing_url = scrapy.Field()
    enrollment_start = scrapy.Field()
    enrollment_end = scrapy.Field()
    end = scrapy.Field()
    start = scrapy.Field()
    org = scrapy.Field()
    pacing_type = scrapy.Field()
    published = scrapy.Field()
    language = scrapy.Field()
    transcript_languages = scrapy.Field()
    availability = scrapy.Field()
    content_type = scrapy.Field()
    program_types = scrapy.Field()
