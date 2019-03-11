# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YcqpmallItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #字母
    letter =scrapy.Field()

    # 品牌
    brand = scrapy.Field()

    # 车系
    car_series = scrapy.Field()

    #车系链接
    car_url =scrapy.Field()

class AnliItem(scrapy.Item):
    #车系名称
    head_name =scrapy.Field()
    #案例名称
    anli_name=scrapy.Field()

    #案例链接
    anli_link =scrapy.Field()

class DetailItem(scrapy.Field):
    #标题
    title=scrapy.Field()
    # #车辆信息
    # vehicle_info =scrapy.Field()
    # #故障现象
    # fault_phenomenon=scrapy.Field()
    #
    # #故障分析
    # fault_analysis =scrapy.Field()
    # #解决步骤
    # Solving_steps =scrapy.Field()
    # #案例备注
    # Case_notes =scrapy.Field()

    #详情页
    detail =scrapy.Field()

    image_url=scrapy.Field()
    image_urls = scrapy.Field()  # 图片的下载地址， 该字段是存储图片的列表
    # 图片下载路径、url和校验码等信息（图片全部下载完成后将信息保存在images中）
    images = scrapy.Field()
    image_paths = scrapy.Field()  # 图片本地存储路径(相对路径
