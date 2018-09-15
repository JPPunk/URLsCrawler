#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Jasper


from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from process_url import Edit

if __name__ == "__main__":
   process = CrawlerProcess(get_project_settings())
   process.crawl('firstspider')
   process.start()

   edit2 = Edit()
   edit2.editing()
   edit2.multi(edit2.store,edit2.outcome)
   edit2.tworows(edit2.outcome,edit2.domains)
   edit2.csv_to_db()






