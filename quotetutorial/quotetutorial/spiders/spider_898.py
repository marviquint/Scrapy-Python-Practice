import scrapy

class MySpider(scrapy.Spider):
    name = 'sapphire_898'

    def start_requests(self):
        # start_url = input('Enter the URL to scrape: ')
        start_url = 'https://casetext.com/rule/vermont-court-rules/vermont-rules-for-environmental-court-proceedings'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        
        yield scrapy.Request(url=start_url, headers=headers, callback=self.parse)

    def parse(self, response):
        # Extract data from the main page if needed
        # Follow links to other pages
        for link in response.css('.item-content .title::attr(href)').getall():
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_link, headers=response.request.headers)

    def parse_link(self, response):
        # Extract data from the link page
        # ...
        # Extract title first
        rule_name = '\u000A'.join(response.css('.codified-law-title').css('::text').getall())
        # Extract the rules content
        data = '\u000A'.join(response.css('.historicalNote , .note , #pa1 , .codified-law-title , .currency-info').css('::text').getall())
        
        # Store the data in an item
        item = {}
        item[''+rule_name] = data
        
        yield item
        # Follow more links if needed
        for i, link in response.css('.item-content .title::attr(href)').getall():
            print("PAGE: "+link[i])
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_link, headers=response.request.headers)
