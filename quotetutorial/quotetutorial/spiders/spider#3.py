import scrapy

class DCCARulesSpider(scrapy.Spider):
    name = 'dccarules'
    start_urls = ['https://www.dccourts.gov/court-of-appeals/dccarules']

    def parse(self, response):
        # Get all the divs that contain the PDF information
        pdf_divs = response.css('.only-first-thead-show')

        # Loop through each div and extract the PDF title and download link
        for pdf_div in pdf_divs:
            title = pdf_div.css('.table-td-c-t::text').get()
            download_link = pdf_div.css('.col-md-2 a:nth-child(1)::attr(href)').get()

            # Yield a dictionary with the extracted information
            yield {
                'title': title,
                'download_link': download_link
            }

