import scrapy
from ..items import PDF_spider
class MySpider(scrapy.Spider):
    name = 'pd_spider'

    def start_requests(self):
       # start_url = input('Enter the URL to scrape: ')
        start_url = 'https://www.dccourts.gov/court-of-appeals/dccarules'
        #https://www.dccourts.gov/court-of-appeals/dccarules
        
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        # Extract data from the main page if needed
        # ...
        items = PDF_spider()

        all_div_quotes = response.css('.only-first-thead-show')

        for  quote in all_div_quotes:
            title = quote.css('.table-td-c-t::text').get()
            download_link = quote.css('.col-md-2 a:nth-child(1)::attr(href)').get()
            items['rule_name'] = title
            items['pdf_link'] = download_link
            # item = {'title': title, 'download_link': download_link}
            yield items
