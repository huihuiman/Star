# -*- coding: utf-8 -*-
import subprocess

import scrapy
from Star.items import StarItem
import datetime

class StarSpider(scrapy.Spider):
    name = 'star'
    allowed_domains = ['astro.click108.com.tw']
    todayTime = datetime.date.today()
    todayTime = str(todayTime)
    print(todayTime)
    times = "http://astro.click108.com.tw/daily_1.php?iAcDay="+todayTime+"&iAstro="
    url = times
    offset = 1
    start_urls = [url + str(offset)]

    def parse(self, response):
        for i in range(0,12):
            yield scrapy.Request(self.url+str(i),callback=self.parseHtml)

    def parseHtml(self,response):
        base_list = response.xpath('//div[@class="TODAY_CONTENT"]')

        for base in base_list:
            item = StarItem()
            item['starName'] = base.xpath('./h3/text()').extract()[0][2:5] #星座名稱
            todayTime = datetime.date.today()
            todayTime = str(todayTime)
            item['starDay'] = todayTime #當天日期
            item['all1'] = base.xpath('./p/span/text()').extract()[0] #整體運勢期望
            item['all2'] = base.xpath('./p/text()').extract()[0] #整體運勢
            item['love1'] = base.xpath('./p/span/text()').extract()[1] #愛情運勢期望
            item['love2'] = base.xpath('./p/text()').extract()[1] #愛情運勢
            item['business1'] = base.xpath('./p/span/text()').extract()[2] # 事學業運勢期望
            item['business2'] = base.xpath('./p/text()').extract()[2] #事學業運勢
            item['money1'] = base.xpath('./p/span/text()').extract()[3] #財運運勢期望
            item['money2'] = base.xpath('./p/text()').extract()[3] #財運運勢
            yield item


