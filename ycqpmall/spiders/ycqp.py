# -*- coding: utf-8 -*-
import scrapy
from urllib.request import quote, unquote
from ycqpmall.items import YcqpmallItem,AnliItem,DetailItem
import re


class YcqpSpider(scrapy.Spider):
    name = 'ycqp'
    allowed_domains = ['http://qczl.ycqpmall.com/']
    start_urls = ['http://qczl.ycqpmall.com/XmData/Anli']
    base_url = 'http://qczl.ycqpmall.com'

    def parse(self, response):
        base_url = 'http://qczl.ycqpmall.com'
        node_list =response.xpath('//*[@id="list"]/div[5]/ul/li')
        for node in node_list:
            item = YcqpmallItem()

            #品牌
            brand=node.xpath('./a/text()').extract_first()
            if brand !=  None:
                item['brand'] =brand
                # print(brand)
            #车系
            for car in node.xpath('./ul/li/a'):
                car_series =car.xpath('./text()').extract()[0]
                # print(car_series)

                car_url =car.xpath('./@href').extract()[0]


                car_url=base_url +car_url
                # print(car_url)
                item['car_series']=car_series
                item['car_url'] =car_url

                yield scrapy.Request(url=item['car_url'],callback=self.anli_parse,dont_filter = True)

    def anli_parse(self,response):
        item=AnliItem()
        base_url = 'http://qczl.ycqpmall.com'

        #head头名称
        head_name =response.xpath('/html/body/header/h1/text()').extract()[0]
        # print(head_name)
        item['head_name']=head_name

        for anli in response.xpath('/html/body/div/ul/li/a'):

            #案例名称
            anli_name =anli.xpath('./text()').extract()[0]

            #案例链接名称
            anli_link =anli.xpath('./@href').extract()[0]

            anli_link =base_url +anli_link

            item['anli_name']=anli_name
            item['anli_link']=anli_link



            yield scrapy.Request(url=item['anli_link'],callback=self.detail_parse, dont_filter=True)



    def detail_parse(self,response):

        item=DetailItem()

        title =response.xpath('/html/head/title/text()').extract()[0]
        item['title']=title
        print(title)

        # detail = response.xpath('string(/html/body/div/div)').extract()[0]
        # item['detail'] =detail
        # print(detail)


        yield item

        if response.xpath('/html/body/div/div//img/@src'):
            for image_url in response.xpath('/html/body/div/div//img/@src').extract():

                item['image_url']=image_url
                print(image_url)
                yield item
        else:
            pass
















