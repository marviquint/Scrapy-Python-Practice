import scrapy

class MySpider(scrapy.Spider):
    name = 'sapphire2_70'

    def start_requests(self):
        start_url = input('Enter the URL to scrape: ')
        #start_url = ''
        #https://www.dccourts.gov/court-of-appeals/dccarules
        
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        # Extract data from the main page if needed
        # ...
        all_div_quotes = response.css('.only-first-thead-show')

        for  quotes in all_div_quotes:
            title = quotes.css('.table-td-c-t::text').extract()
            download_link = quotes.css('.col-md-2 a:nth-child(1)::attr(href)').extract()
            items ={}
            items['title'] = title
            items['author'] = download_link
            yield items

            title = ''
            download_link = ''

