import datetime
import scrapy
import json
from ..items import NoonSpiderItem
from scrapy import Request
class dealsSpider(scrapy.Spider):
    name = 'deals'

    url = 'https://www.noon.com/uae-en/all-p-fbn-ae/generic/?limit=150&page={}&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc'
    def start_requests(self):
        for i in range(1,51):
            yield Request(url=self.url.format(i))
    def parse(self,response):
        href_links = response.css('.productContainer a::attr(href)').extract()
        for href in href_links:
            full_link = 'https://www.noon.com' + href
            yield Request(full_link,callback=self.parse_product)
    def parse_product(self,response):
        items = NoonSpiderItem()
        product_links = response.url
        link_list = product_links.split("/")
        sku =  link_list[5]
        sku_link = f"https://www.noon.com/_svc/catalog/api/v3/u/l/{sku}/p/"
        items['skulinks'] = sku_link
        yield Request(url=sku_link,headers={'x-locale': 'en-ae'},callback=self.parse_json)


    def parse_json(self,response):
        today = datetime.datetime.now()
        today = today.strftime("%b-%d-%Y %H:%M:%S")
        product = response.json()
        product['date'] = today
        yield {
            "product": product
        }



