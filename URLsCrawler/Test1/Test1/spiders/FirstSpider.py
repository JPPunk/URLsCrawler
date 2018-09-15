# -*- coding: utf-8 -*-
import csv
import scrapy
from Test1.items import FirstSpiderItem


class MySpider1(scrapy.Spider):
    name = 'firstspider'
    allowed_domains = []
    start_urls = []

    with open("input.csv", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            allowed_domains.append(row[0])
            start_urls.append(row[1])

    def parse(self, response):
        sel = scrapy.Selector(response)
        links_in_one_page = sel.xpath('//a[@href]')

        for link_sel in links_in_one_page:
            item = FirstSpiderItem()
            link = str(link_sel.re('href="(.*?)"')[0])
            if link:
                if not link.startswith('http'):
                    link = response.url + link
                yield scrapy.Request(link, callback=self.parse)

                if response.status>=200 and response.status<400:
                   item['link'] = link
                   yield item
                else: continue




