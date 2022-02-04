from typing import List
import scrapy

class XKCDSpider(scrapy.Spider):
    '''
    name: identifies the Spider. It must be unique within a project, that is, you can't set the same name for different Spiders.
    '''
    name = 'xkcd'

    '''
    must return an iterable of Requests (you can return a list of requests or write a generator function) which the Spider will begin to crawl from. Subsequent requests will be generated successively from these initial requests.
    '''
    def start_requests(self):
        urls = [
            'https://xkcd.com/archive/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    '''
    a method that will be called to handle the response downloaded for each of the requests made. The response parameter is an instance of TextResponse that holds the page content and has further helpful methods to handle it.
    '''
    def parse(self, response, **kwargs):
        for href in response.css('div#middleContainer a::attr(href)').getall():
            yield response.follow(href, callback=self.find_url_image_to_download)

    def find_url_image_to_download(self, response):
        relative_url_image = response.css('div#comic img::attr(src)').get()
        if relative_url_image:
            url_image = response.urljoin(relative_url_image)
            yield {
                'image_urls': [url_image]
            }
