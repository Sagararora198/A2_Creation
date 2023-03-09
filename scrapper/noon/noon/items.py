# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NoonItem(scrapy.Item):
    brand_name = scrapy.Field()
    product_name = scrapy.Field()
    model_number = scrapy.Field()
    currency = scrapy.Field()
    price = scrapy.Field()
    sold_by = scrapy.Field()
    star = scrapy.Field()
    full_link = scrapy.Field()
