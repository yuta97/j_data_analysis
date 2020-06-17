# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:35:06 2020

@author: yuta97
"""

import scrapy


class SimpleSpider(scrapy.Spider):
    name = 'simple'
    allowed_domains = ['docs.pyq.jp']
    start_urls = ['https://docs.pyq.jp/_static/assets/scraping/test1.html']

    def parse(self, response):
        print(response.text)