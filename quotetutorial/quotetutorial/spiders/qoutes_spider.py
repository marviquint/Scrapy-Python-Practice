import scrapy

class QouteSpider(scrapy.Spider):
    name = "qoutes"
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # title = response.css('title').extract()
        # yield {'titletext': title}
        #all_div_qoutes = response.css('div.qoute')[0]
        tile = response.css('span.text::text')[0].extract()
        author = response.css('.author::text')[0].extract()
        tag = response.css('.tag::text')[0].extract()
        yield {
            'title' : tile,
            'author' : author,
            'tag' : tag
        }

