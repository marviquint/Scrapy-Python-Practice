import scrapy
from ..items import QuotetutorialItem
class QouteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        items = QuotetutorialItem()

        title = response.css('span.text::text')[0].extract()
        author = response.css('.author::text')[0].extract()
        tag = response.css('.tag::text')[0].extract()

        items['title'] = title
        items['author'] = author
        items['tag'] = tag

        yield items

        # yield {
        #     'title' : tile,
        #     'author' : author,
        #     'tag' : tag
        # }

 # title = response.css('title').extract()
        # yield {'titletext': title}
        #all_div_qoutes = response.css('div.qoute')[0]