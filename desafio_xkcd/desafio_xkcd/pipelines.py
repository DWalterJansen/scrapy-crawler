# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import hashlib

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.python import to_bytes


class DesafioXkcdPipeline:
    def process_item(self, item, spider):
        return item

class CustomImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = hashlib.md5(to_bytes(request.url)).hexdigest()
        return f'{image_guid}.jpg'