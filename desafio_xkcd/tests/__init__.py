from unittest import TestCase
from scrapy.http import Request
from scrapy.item import Item
from tests.fixtures import response_from_file


class SpiderTestCase(TestCase):

    def setUp(self):
        self.spider = None

    def generate_response(self, generator):
        items = []
        requests = []
        for item in generator:
            if isinstance(item, Request):
                requests.append(item)
            elif isinstance(item, dict) or isinstance(item, Item):
                items.append(item)
            else:
                raise Exception
        return {
            'items': items,
            'requests': requests
        }

    def execute_method(self, name_method, fixture, meta={}, cb_kwarks={}, url='', extensao='html'):
        response = response_from_file(fixture, url, encoding='latin1', meta=meta, extensao=extensao)
        method = getattr(self.spider, name_method)
        generator = method(response, **cb_kwarks)
        return self.generate_response(generator)
