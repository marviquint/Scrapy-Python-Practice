import scrapy
import urllib.request
class MySpider(scrapy.Spider):
    name = 'myspider'

    def start_requests(self):
        # Prompt the user to input the website to crawl
        url = input('Enter the URL to scrape: ')

        # Prompt the user to input the CSS selector for the links to follow
        follow_css = input('Enter the CSS selector for links to follow: ')

        # Prompt the user to input the CSS selector for the data to scrape
        data_css1 = input('Enter the CSS selector for the data to scrape: ')
        data_css2 = input('Enter the CSS selector for the data to scrape: ')

        yield scrapy.Request(url=url, callback=self.parse, meta={
            'follow_css': follow_css,
            'rule_Name': data_css1,
            'pdf_link': data_css2
        })

    def parse(self, response):
        # Extract the CSS selectors for the links to follow and the data to scrape
        follow_css = response.meta.get('follow_css')
        data_css1 = response.meta.get('rule_Name')
        data_css2 = response.meta.get('pdf_link')

        # Follow the links and continue crawling
        for link in response.css(follow_css):
            yield response.follow(link, self.parse)

        # Extract the data and store it in separate items
        for i, datum in enumerate(response.css(data_css1).getall()):
            item = {}
            item['rule_Name'] = datum
            item['pdf_link'] = response.css(data_css2).getall()[i]
            yield item
            # Download the PDF file
            pdf_link = response.css(data_css2).getall()[i]
            self.download_pdf(pdf_link)

    def download_pdf(self, pdf_link):
        # Download the PDF file
        urllib.request.urlretrieve(pdf_link, "filename.pdf")

            
