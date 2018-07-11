# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TravelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #'景点名称', '级别', '所在区域', '起步价', '销售量', '热度', '地址', '标语', '经度'，'纬度'
    #https://apis.map.qq.com/ws/geocoder/v1/?address=%E5%B1%B1%E8%A5%BF%E7%9C%81%E5%A4%A7%E5%90%8C%E6%98%AF%E9%98%B3%E9%AB%98%E5%8E%BF%E7%BD%97%E6%96%87%E7%9A%82%E9%95%87%E5%AD%A4%E5%B1%B1%E5%BA%99%E6%9D%91%E4%B8%9C&key=4ACBZ-APUWW-B5MR6-RWFMJ-TD2NV-SPBIN
    name = scrapy.Field()
    level = scrapy.Field()
    province = scrapy.Field()
    price = scrapy.Field()
    sales = scrapy.Field()
    score = scrapy.Field()
    loaction = scrapy.Field()
    slogan = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()