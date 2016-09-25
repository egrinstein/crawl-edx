# -*- coding: utf-8 -*-
from scrapy import Spider
from mooc_crawler.items import EDXItem
from scrapy.http import Request
import json
from BeautifulSoup import BeautifulSoup

SEARCH_URL="https://www.edx.org/api/v1/catalog/search?page=1&page_size=1254&partner=edx&content_type[]=courserun&content_type[]=program&featured_courses_ids=course-v1%3AMichiganX+UX501x+3T2016%2Ccourse-v1%3ARITx+PM9001x+1T2017%2Ccourse-v1%3AMITx+CTL.SC0x+3T2016%2Ccourse-v1%3AUBCx+Marketing1x+3T2015%2Ccourse-v1%3AMicrosoft+DAT206x+6T2016%2Ccourse-v1%3AHarvardX+CS50+X&featured_programs_uuids=988e7ea8-f5e2-4d2e-998a-eae4ad3af322%2C1ebad934-b064-4003-8214-1a5d6e21bb7c%2C1a0c2175-cf1b-4375-ae71-166ffa84abb3%2C10339d1d-239d-4e36-b524-8ce0fdf2d0c0%2C2fc3236d-78a9-45a1-8c0c-fc290e74259e%2C38dde1fd-e9a4-4f4b-9c87-87a3d0161830"

RATINGS_URL ="https://www.coursetalk.com/widgets/api/review-data?course=%s&provider=edx&rating_stats="
INSTRUCTORS_URL = "https://www.edx.org/api/catalog/v2/courses/"

def save_body(body,fname):
    with open(fname,'wt') as f:
        f.write(body)

class EdxSpider(Spider):
    name = "edx"
    allowed_domains =["edx.org","https://www.edx.org",
                       "coursetalk.com","https://www.coursetalk.com/"]
    start_urls = (
    	SEARCH_URL,
	)

    def parse(self, response):
        data = json.loads(response.body)
        print "FIRST KEYS:",data.keys()

        data = data[u'objects'][u'results']
        print 'SECOND KEYS:',data[0].keys()
        
        for d in data:
            item = EDXItem()
            for key in d:
                try:
                    if key == u'full_description' or key == u'title' or key == u'short_description':
                        item[key] = BeautifulSoup(d[key]).text.replace(u'&amp','and')
                    else:
                        item[key] = d[key]
                except:
                    continue
            if u'number' not in item.keys():
                continue
            else:
                ratings_url = RATINGS_URL %item['number']
                request = Request(ratings_url,callback=self.parse_reviews)
                request.meta['item'] = item
                yield request

    def parse_reviews(self,response):
        item = response.meta['item']
        data = json.loads(response.body)[item['number']]
        try:
            item['rating'] = data[u'rating']
            item['review_count'] = data[u'review_count']
        except KeyError:
            pass    
        instructors_url = INSTRUCTORS_URL + item['key']
        request = Request(instructors_url,callback=self.parse_instructors)
        request.meta['item'] = item
        return request
    def parse_instructors(self,response):
        item = response.meta['item']
        data = json.loads(response.body)
        item['length'] = data['length']
        item['effort'] = data['effort']
        item['prerequisites'] = BeautifulSoup(data['prerequisites']).text
        i=1

        for instr in data[u'staff']:
            item['instructor_%d'%i] = instr[u'title']

            if u'position' in instr:
                item['org_instructor_%d'%i] = instr[u'position'][u'organization_name']
            elif u'display_position' in instr:
                item['org_instructor_%d'%i] = instr[u'display_position'][u'org']
            else:
                print 'KALABANGA',instr
            i+=1
            if i > 5: # if you want more for some reason, add to items.
                break

        return item

