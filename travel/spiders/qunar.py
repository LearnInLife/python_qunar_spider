# -*- coding: utf-8 -*-
import scrapy
import json
from travel.items import TravelItem


class QunarSpider(scrapy.Spider):
    name = 'qunar'
    allowed_domains = ['piao.qunar.com']
    offset = 15
    page = 1
    url = 'http://piao.qunar.com/ticket/list.json?keyword=%E4%B8%AD%E5%9B%BD&page='
    start_urls = [url + str(page)]

    # 下一页链接的提取规则，返回匹配的链接对象链接
    # page_link = LinkExtractor(allow=r'?&page=\d+')
    #
    # rules = [
    #     Rule(page_link, callback='parse_item')
    # ]

    def parse(self, response):
        travel_data = json.loads(response.body_as_unicode())['data']
        total_count = travel_data['totalCount']
        sight_list = travel_data['sightList']
        print(total_count)
        for sight_item in sight_list:
            # print(sight_item)
            item = TravelItem()
            item['name'] = sight_item['sightName']
            if 'star' in sight_item:
                item['level'] = sight_item['star']
            else:
                item['level'] = '暂无'
            item['province'] = sight_item['districts']
            item['price'] = sight_item['qunarPrice']
            item['sales'] = sight_item['saleCount']
            item['score'] = sight_item['score']
            item['loaction'] = sight_item['address']
            if 'intro' in sight_item:
                item['slogan'] = sight_item['intro']
            else:
                item['slogan'] = '暂无'
            point = sight_item['point'].split(',')
            item['longitude'] = point[0]
            item['latitude'] = point[1]
            yield item

        if (self.page * 15) < total_count:
            self.page += 1
            yield scrapy.Request(self.url + str(self.page), callback=self.parse)

        # for each in response.xpath(".//div[@class='result_list']/div[@class='sight_item']"):
        #     item = TravelItem()
        #     # name = scrapy.Field()
        #     # level = scrapy.Field()
        #     # province = scrapy.Field()
        #     # price = scrapy.Field()
        #     # sales = scrapy.Field()
        #     # hot = scrapy.Field()
        #     # loaction = scrapy.Field()
        #     # slogan = scrapy.Field()
        #     # longitude = scrapy.Field()
        #     # latitude = scrapy.Field()
        #     item['name'] = each.xpath(".//h3[@class='sight_item_caption']/text()").extract()[0]
        #     item['level'] = each.xpath(".//span[@class='level']/text()").extract()[0]
        #     item['province'] = each.xpath(".//span[@class='area']/a/text()").extract()[0]
        #     item['price'] = each.xpath(".//span[@class='area']/a/text()").extract()[0]
        # yield item
