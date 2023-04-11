import scrapy
from ..items import QuotetutorialItem

class QouteSpider(scrapy.Spider):
    name = "quotes"
    page_number = 2
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        items = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items
        
        # next_page = response.css('li.next a::attr(href)').get()
        next_page = 'https://quotes.toscrape.com/page/'+ str(QouteSpider.page_number) + '/'
        print(next_page)

        if QouteSpider.page_number < 11:
            QouteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
    

        # if next is not None:
        #     yield response.follow(next_page, callback = self.parse)

        # # Export the data to a JSON file
        # filename = 'quotes.json'
        # with open(filename, 'w') as f:
        #     f.write(items.to_json())
        # self.log('Saved file %s' % filename)
