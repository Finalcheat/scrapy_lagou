#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
import re
from lagou.items import LagouItem


class LagouJobSpider(scrapy.Spider):
    '''
    lagou job spider
    '''

    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = [
        'http://www.lagou.com/jobs/1396934.html?source=home_hot&i=home_hot-0',
        #  'http://www.lagou.com/zhaopin/C++/',
    ]

    def parse_list(self, response):
        job_links = response.xpath('//li[@class="con_list_item"]/div/div/div/a[@class="position_link"]')
        print job_links
        for a in job_links:
            href = a.xpath('@href').extract()
            print href


    def parse(self, response):
        item = LagouItem()

        title = response.xpath('//dl[@id="job_detail"]/dt/h1/@title').extract()
        item['title'] = title[0] if title else ''

        job_source = response.xpath('//dl[@id="job_detail"]/dt/h1/div/text()').extract()
        item['job_source'] = job_source[0] if job_source else ''

        job_request = response.xpath('//dd[@class="job_request"]/p/span/text()')
        if len(job_request) >= 4:
            item['salary'] = job_request[0].extract()
            item['location'] = job_request[1].extract()
            item['work_experience'] = job_request[2].extract()
            item['education'] = job_request[3].extract()

        job_temptation = response.xpath('//dd[@class="job_request"]/p[2]/text()').extract()
        if job_temptation:
            job_temptation = job_temptation[0]
            result = re.findall(u'职位诱惑 : (.*)', job_temptation)
            if result:
                item['job_temptation'] = result[0]

        description = response.xpath('//dd[@class="job_bt"]/p').extract()
        _d = ''
        for r in description:
            _d += r
        item['description'] = _d

        yield item
