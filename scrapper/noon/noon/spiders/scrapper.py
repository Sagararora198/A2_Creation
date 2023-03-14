import  scrapy
from scrapy import Request
from ..items import NoonItem

class noonscraper(scrapy.Spider):
    name = 'detail'
    start_urls = [

    ]
    def __init__(self):
        url = 'https://www.noon.com/egypt-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?limit=50&page='
        for page in range(1,63):
            self.start_urls.append(url+str(page))


    def parse(self,response):
        href_links = response.css('span.productContainer>a::attr(href)').extract()
        for href in href_links:
            full_link = 'https://www.noon.com' + href
            yield Request(full_link,callback=self.parse_product,cb_kwargs={'full_link':full_link})



    def parse_product(self,response,full_link):
        items = NoonItem()
        brand_name = response.css('.fWufbI::text').extract()
        product_name = response.css('.glmpuV::text').extract()
        model_number = response.css('.modelNumber::text').extract()
        currency = response.css('.priceNow::text').extract_first()

        price = response.css('.priceNow::text')[2].get()


        sold_by = response.css('.allOffers::text').extract()
        star = response.css('.bFgxSY::text').extract()
        items['brand_name'] = brand_name
        items['product_name'] = product_name
        items['model_number'] = model_number
        items['currency'] = currency
        items['price'] = price
        items['sold_by'] = sold_by
        items['star'] = star
        items['full_link'] = full_link
        yield items





#
#
#
#
#
#
#
#
# from scrapy.spiders import XMLFeedSpider
# from myproject.items import TestItem
#
# class MySpider(XMLFeedSpider):
#     name = 'example.com'
#     allowed_domains = ['example.com']
#     start_urls = ['http://www.example.com/feed.xml']
#     iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
#     itertag = 'item'
#
#     def parse_node(self, response, node):
#         self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))
#
#         item = TestItem()
#         item['id'] = node.xpath('@id').get()
#         item['name'] = node.xpath('name').get()
#         item['description'] = node.xpath('description').get()
#         return item
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# from scrapy.spiders import CSVFeedSpider
# from myproject.items import TestItem
#
# class MySpider(CSVFeedSpider):
#     name = 'example.com'
#     allowed_domains = ['example.com']
#     start_urls = ['http://www.example.com/feed.csv']
#     delimiter = ';'
#     quotechar = "'"
#     headers = ['id', 'name', 'description']
#
#     def parse_row(self, response, row):
#         self.logger.info('Hi, this is a row!: %r', row)
#
#         item = TestItem()
#         item['id'] = row['id']
#         item['name'] = row['name']
#         item['description'] = row['description']
#         return item
#
#
#
