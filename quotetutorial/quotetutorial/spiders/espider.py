import scrapy

class MySpider(scrapy.Spider):
    name = 'espider'
    
    def start_requests(self):
        # Prompt the user to input the website to crawl
        url = input('Enter the URL to scrape: ')
        
        # Prompt the user to input the CSS selector for the links to follow
        #follow_css = input('Enter the CSS selector for links to follow: ')
        
        # Prompt the user to input the CSS selector for the data to scrape
        data_css = input('Enter the CSS selector for the data to scrape: ')
        
        yield scrapy.Request(url=url, callback=self.parse, meta={
            #'follow_css': follow_css,
            'data_css': data_css
        })
    
    def parse(self, response):
        # Extract the CSS selectors for the links to follow and the data to scrape
        #follow_css = response.meta.get('follow_css')
        data_css = response.meta.get('data_css')
        
        # Follow the links and continue crawling
        # for link in response.css(follow_css):
        #     yield response.follow(link, self.parse)
            
        # Extract the data and store it in separate items
        for datum in response.css(data_css).css().getall():
            item = {}
            item['data'] = datum
            
            yield item
