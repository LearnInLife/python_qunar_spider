# coding=utf-8


from pyecharts import Bar, Page
import random
import xlrd


def readexcel():
    excel = xlrd.open_workbook(u'景点信息.xlsx')
    sheet_names = excel.sheet_names();
    for sheet_name in sheet_names:
        sheet = excel.sheet_by_name(sheet_name)
        i = 1
        # 将excel数据遍历出来存储在数组中
        info_list = []
        while i < sheet.nrows:
            row = sheet.row_values(i)
            i += 1
            row[2] = row[2].split('·')[0]
            info_list.append(row)

        # 对数据按销量进行排序,降序
        info_list.sort(key=lambda li: li[4], reverse=True)
        # 取出销量前20
        top20_list = info_list[0:20]
        top20_name = []
        top20_sale = []
        for item in top20_list:
            top20_name.append(item[0])
            top20_sale.append(item[4])

        # 计算城市的景点数
        province_dic = dict()
        for item in info_list:
            province_name = item[2]
            count = province_dic.get(province_name)
            if count:
                count += 1
            else:
                count = 1
            province_dic[province_name] = count
        # 按数量排序
        province_sort = sorted(province_dic.items(), key=lambda p: p[1])
        # 城市列表
        province_list = []
        # 景点数量
        sight_count = []
        for value in province_sort:
            province_list.append(value[0])
            sight_count.append(value[1])

        # 生成图表
        page = Page()
        # 销量前20
        sale_top20(page, top20_name, top20_sale)
        # 景点数
        province_sight(page, province_list, sight_count)
        page.render()


def sale_top20(page, attr, data):
    bar = Bar('热门景点销量')
    bar.add('top20', attr, data, is_label_show=True, label_pos='top', xaxis_rotate=30,
            xaxis_label_textsize=10, xaxis_margin=1)
    page.add_chart(bar, '销量top20')


def province_sight(page, attr, data):
    bar = Bar('城市景点数',height=600)
    bar.add('景点数', attr, data, is_label_show=True, label_pos='right', is_convert=True, bar_category_gap='50%')
    page.add_chart(bar, '城市景点数')


if __name__ == '__main__':
    readexcel()
