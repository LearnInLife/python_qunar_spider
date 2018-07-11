# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pandas as pd
from openpyxl import Workbook


class TravelPipeline(object):
    def __init__(self):
        # self.point_file = open('point.json', 'w')
        self.point_list = []
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['景点名称', '级别', '所在区域', '起步价', '销售量', '热度', '地址', '标语', '经度', '纬度'])
        # self.trave_list = []

    def process_item(self, item, spider):
        json_geo = dict()
        json_geo['lng'] = item['longitude']
        json_geo['lat'] = item['latitude']
        json_geo['count'] = item['sales']

        self.point_list.append(json_geo)
        self.ws.append([item['name'], item['level'], item['province'], item['price'], item['sales'], item['score'],
                        item['loaction'],item['slogan'],item['longitude'],item['latitude']])
        # self.trave_list.append(item)
        return item

    def close_spider(self, spider):
        # writer = pd.ExcelWriter('景点信息.xlsx')
        # df = pd.DataFrame(self.trave_list, columns=['景点名称', '级别', '所在区域', '起步价', '销售量', '热度', '地址', '标语', '经度', '纬度'])
        # df.to_excel(writer, 'Sheet1')
        # writer.save()
        self.wb.save('景点信息.xlsx')

        with open('point.json', 'w') as f:
            f.write(json.dumps(self.point_list))
