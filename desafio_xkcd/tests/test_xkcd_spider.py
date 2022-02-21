from tests import SpiderTestCase
from tests.fixtures import response_from_file
from desafio_xkcd.spiders.xkcd_spider import XKCDSpider


class TestXKCDSpider(SpiderTestCase):

    def setUp(self) -> None:
        self.spider = XKCDSpider()

    def test_find_all_attr_href(self) -> None:
        response = response_from_file('html/archive_page.html')
        hrefs = self.spider.extract_hrefs_from_archive(response)
        self.assertEqual(len(hrefs), 2582)

    def test_parse_archive_page_call_find_url_image_to_download(self) -> None:
        response = self.execute_method(
            name_method='parse_archive_page',
            fixture='html/archive_page.html'
        )
        url = 'http://www.exemplo.com/2583/'
        requests = response['requests']
        self.assertEqual(len(requests), 2582)
        self.assertEqual(requests[0].url, url)
        self.assertEqual(requests[0].callback, self.spider.find_url_image_to_download)
        self.assertEqual(requests[0].cb_kwargs['href'], '/2583/')

    def test_find_attr_src(self) -> None:
        response = response_from_file('html/2583_page.html')
        src = self.spider.extract_src_from_image(response)
        self.assertEqual(src, '//imgs.xkcd.com/comics/chorded_keyboard.png')

    def test_find_url_image_to_download_return_items(self) -> None:
        response = self.execute_method(
            name_method='find_url_image_to_download',
            fixture='html/2583_page.html',
            cb_kwarks=dict(href='/2583/')
        )
        items = [{
            'image_urls': [
                'http://imgs.xkcd.com/comics/chorded_keyboard.png'
            ]
        }]
        self.assertEqual(response['items'], items)
