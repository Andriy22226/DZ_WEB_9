import scrapy
import re

class GetLinksSpider(scrapy.Spider):
    name = "get_links"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for link in response.xpath():
            yield
            # urls.append()
            
