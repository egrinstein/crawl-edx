# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from mooc_crawler.items import MOOCItem
from scrapy.http import Request
import json
from BeautifulSoup import BeautifulSoup
import re
SIZE = 100
SEARCH_URL="https://www.edx.org/api/v1/catalog/search?page=1&page_size=100&partner=edx&content_type[]=courserun&content_type[]=program&featured_courses_ids=course-v1%3AMichiganX+UX501x+3T2016%2Ccourse-v1%3ARITx+PM9001x+1T2017%2Ccourse-v1%3AMITx+CTL.SC0x+3T2016%2Ccourse-v1%3AUBCx+Marketing1x+3T2015%2Ccourse-v1%3AMicrosoft+DAT206x+6T2016%2Ccourse-v1%3AHarvardX+CS50+X&featured_programs_uuids=988e7ea8-f5e2-4d2e-998a-eae4ad3af322%2C1ebad934-b064-4003-8214-1a5d6e21bb7c%2C1a0c2175-cf1b-4375-ae71-166ffa84abb3%2C10339d1d-239d-4e36-b524-8ce0fdf2d0c0%2C2fc3236d-78a9-45a1-8c0c-fc290e74259e%2C38dde1fd-e9a4-4f4b-9c87-87a3d0161830"



def save_body(body,fname):
    with open(fname,'wt') as f:
        f.write(body)

class EdxSpider(Spider):
    name = "edx"
    allowed_domains = ["edx.org","https://www.edx.org"]
    start_urls = (
    	SEARCH_URL,
	)

    def parse(self, response):
        data = json.loads(response.body)
        
        data = data[u'objects'][u'results']
        for d in data:
            item = MOOCItem()
            for key in d:
                try:
                    if key == u'full_description':
                        item[key] = BeautifulSoup(d[key]).text
                    else:
                        item[key] = d[key]
                except:
                    continue
            yield item
