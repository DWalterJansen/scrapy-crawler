from typing import List
import scrapy


class XKCDSpider(scrapy.Spider):
    name = 'xkcd'

    def start_requests(self) -> None:
        urls = [
            'https://xkcd.com/archive/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_archive_page)

    def extract_hrefs_from_archive(self, response) -> List:
        return response.css('div#middleContainer a::attr(href)').getall()

    def parse_archive_page(self, response, **kwargs) -> None:
        for href in self.extract_hrefs_from_archive(response):
            yield response.follow(href, callback=self.find_url_image_to_download, cb_kwargs=dict(href=href))

    def extract_src_from_image(self, response) -> str:
        return response.css('div#comic img::attr(src)').get()

    def find_url_image_to_download(self, response, href) -> None:
        relative_url_image = self.extract_src_from_image(response)
        if relative_url_image:
            url_image = response.urljoin(relative_url_image)
            yield {
                'image_urls': [url_image]
            }
        else:
            self.logger.info(f'URL Not Find: {href}')
