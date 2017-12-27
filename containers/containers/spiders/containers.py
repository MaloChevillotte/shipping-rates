# -*- coding: utf-8 -*-
import scrapy
import os

class JobsSpider(scrapy.Spider):
    name = 'containers'
    allowed_domains = ['moverdb.com']
    start_urls = ['https://moverdb.com/container-shipping/']

    def parse(self, response):
        for link in response.css('a').xpath('@href'):
            yield {
                'link': link.extract()
            }
