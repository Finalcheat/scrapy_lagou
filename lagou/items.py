# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    job_source = scrapy.Field()
    salary = scrapy.Field()
    location = scrapy.Field()
    work_experience = scrapy.Field()
    education = scrapy.Field()
    job_temptation = scrapy.Field()
    description = scrapy.Field()
