# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.field()
    images = scrapy.field()
    preparation_time = scrapy.field()
    cooking_time = scrapy.field()
    serves =  scrapy.field() 
    methods = scrapy.field() 
    ingredients = scrapy.field() 
    chef_details = scrapy.field()
    