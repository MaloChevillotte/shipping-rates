# -*- coding: utf-8 -*-
import os
import scrapy
from scrapy.selector import Selector
import json

class JobsSpider(scrapy.Spider):
    name = 'rates'
    allowed_domains = ['moverdb.com']

    def start_requests(self):
        start_urls= []
        f = open(os.path.join(os.getcwd(), 'selected_links.json'), 'rb')
        data = json.load(f)
        for link in data:
            start_urls.append(link)
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        if len(response.css('table').extract()) == 2:
            for i in range(2):
                filename = 'rates-%s-%d.json' % (page, i)
                table = []
                selected_table = response.css('table').extract()[i]
                for element in Selector(text=selected_table).xpath('//tr').extract():
                    table.append(Selector(text=element).xpath('//td/text()').extract())
                with open(filename, 'wb') as f:
                    json.dump(table, f)
        else:
            filename = 'rates-%s.json' % page
            table = []
            for element in response.css('tr').extract():
                table.append(Selector(text=element).xpath('//td/text()').extract())
            with open(filename, 'wb') as f:
                json.dump(table, f)
