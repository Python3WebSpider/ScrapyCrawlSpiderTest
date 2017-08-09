# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class YouthSpider(CrawlSpider):
    name = 'youth'
    allowed_domains = ['news.youth.cn']
    start_urls = ['http://news.youth.cn/jsxw/index.htm']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="rdwz"]/ul//li'), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="fy"]//a[contains(., "下一页")]'), follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
