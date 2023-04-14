# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotetutorialItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
    
class PDF_spider(scrapy.Item):
    # define the fields for your item here like:
    rule_name = scrapy.Field()
    pdf_link = scrapy.Field()