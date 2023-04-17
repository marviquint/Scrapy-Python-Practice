import scrapy

class MySpider(scrapy.Spider):
    name = 'sapphire1_891'

    def start_requests(self):
       # start_url = input('Enter the URL to scrape: ')
        start_url = 'https://govt.westlaw.com/azrules/Browse/Home/Arizona/ArizonaCourtRules/ArizonaStatutesCourtRules?guid=N10250A40715611DAA16E8D4AC7636430&transitionType=CategoryPageItem&contextData=(sc.Default)'
        
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        # Extract data from the main page if needed
        # ...

        # Follow links to other pages
        # for link in response.css('#co_contentColumn li+ li a::attr(href)').getall():
        #     yield scrapy.Request(url=response.urljoin(link), callback=self.parse_link)
        for link in response.css('#co_contentColumn li+ li a::attr(href)').getall():
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_link)

    def parse_link(self, response):
        # Extract data from the link page
        # ...
        # Extract title first
        rule_name = '\u000A'.join(response.css('#title').css('::text').getall())
        # Extract the rules content
        data = '\u000A'.join(response.css('#co_document').css('::text').getall())
        
        # Store the data in an item
        item = {}
        item[''+rule_name] = data
        
        yield item
        # Follow more links if needed
        for i, link in response.css('#co_contentColumn li+ li a::attr(href)').getall():
            print("PAGE: "+link[i])
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_link)

