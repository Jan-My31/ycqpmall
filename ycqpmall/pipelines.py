# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# class YcqpmallPipeline(object):
#     def process_item(self, item, spider):
#         return item

from twisted.enterprise import adbapi
import pymysql
import pymysql.cursors
from ycqpmall.db.dbhelper import DBHelper
import codecs
import json
from logging import log
from scrapy.utils.project import get_project_settings
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import re


class writeMysqlPipeline(object):
    # 连接数据库
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        # 插入数据库
        self.db.insert(item)
        return item





class SaveImagesPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        """

        :param request:  每一个图片下载管道请求
        :param response:
        :param info:
        :param strip :清洗Windows系统的文件夹非法字符，避免无法创建目录
        :return:每套图的分类目录
        """
        item = request.meta['item']
        folder = item['title']
        folder_strip = folder.strip()
        image_guid = request.url.split('/')[-1]
        filename = u'imge/{0}/{1}'.format(folder_strip, image_guid)
        return filename

    def get_media_requests(self, item, info):
        """

        :param item: spider.py中返回的item
        :param info:
        :return:
        """
        for image_url in item['image_url']:
            # referer = item['url']  # 处理防盗链
            yield Request(image_url,meta={'item': item})  # 配合


    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['image_paths'] = image_path
        return item
