# -*- coding: utf-8 -*-

import pymysql
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings  #导入seetings配置

class DBHelper():
    '''这个类也是读取settings中的配置，自行修改代码进行操作'''

    def __init__(self):
        settings = get_project_settings()  #获取settings配置，设置需要的信息

        dbparams = dict(
            host=settings['MYSQL_HOST'],  #读取settings中的配置
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            charset='utf8',  #编码要加上，否则可能出现中文乱码问题
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )


        '''
        
        
# 数据库地址
MYSQL_HOST = 'localhost'
# 数据库用户名:
MYSQL_USER = 'root'
#数据库密码
MYSQL_PASSWORD = '121314'
#数据库端口
MYSQL_PORT = 3306
#数据库名称
MYSQL_DBNAME = 'ycqpmall'
#数据库编码
MYSQL_CHARSET = 'utf8'
        
        
        '''
        #**表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        self.dbpool = dbpool

    def connect(self):
        return self.dbpool

    #插入数据
    def insert(self, item):
        #这里定义要插入的字段
        sql = "insert into  image_ceshi  (title,image_url) values(%s,%s)"
        #调用插入的方法
        query = self.dbpool.runInteraction(self._conditional_insert, sql, item)
        #调用异常处理方法
        query.addErrback(self._handle_error)
        return item

    #写入数据库中
    def _conditional_insert(self, canshu, sql, item):
        #取出要存入的数据，这里item就是爬虫代码爬下来存入items内的数据
        params = (item['title'], item['image_url'])
        canshu.execute(sql, params)

    #错误处理方法
    def _handle_error(self, failue):
        print('--------------database operation exception!!-----------------')
        print(failue)
