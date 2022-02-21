# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import hashlib
import os
from io import BytesIO
from PIL import Image
from scrapy.utils.misc import md5sum

# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline


class CustomImagePipeline(ImagesPipeline):

    def __init__(self, store_uri, download_func=None, settings=None):
        super().__init__(store_uri, download_func, settings)
        dir = os.path.dirname(os.path.realpath(__file__))
        self.dir = os.path.join(dir, self.store.basedir)

    def custom_file_path(self, image: Image):
        image_guid = hashlib.md5(image.tobytes()).hexdigest()
        return f'{image_guid}.png'

    def get_images(self, response, request, info, *, item=None):
        orig_image = self._Image.open(BytesIO(response.body))
        width, height = orig_image.size
        if width < self.min_width or height < self.min_height:
            raise ImagesPipeline.ImageException(
                "Image too small "
                f"({width}x{height} < "
                f"{self.min_width}x{self.min_height})"
            )

        image, buf = self.convert_image(orig_image)
        path = self.custom_file_path(image)
        yield path, image, buf

        for thumb_id, size in self.thumbs.items():
            thumb_path = self.thumb_path(request, thumb_id, response=response, info=info)
            thumb_image, thumb_buf = self.convert_image(image, size)
            yield thumb_path, thumb_image, thumb_buf

    def convert_image(self, image, size=None):
        if image.format == 'PNG' and image.mode == 'RGBA':
            background = self._Image.new('RGBA', image.size, (255, 255, 255))
            background.paste(image, image)
            image = background.convert('RGB')
        elif image.mode == 'P':
            image = image.convert("RGBA")
            background = self._Image.new('RGBA', image.size, (255, 255, 255))
            background.paste(image, image)
            image = background.convert('RGB')
        elif image.mode != 'RGB':
            image = image.convert('RGB')

        if size:
            image = image.copy()
            image.thumbnail(size, self._Image.ANTIALIAS)

        buf = BytesIO()
        image.save(buf, 'PNG')
        return image, buf

    def image_downloaded(self, response, request, info, *, item=None):
        checksum = None
        for path, image, buf in self.get_images(response, request, info, item=item):
            if checksum is None:
                buf.seek(0)
                checksum = md5sum(buf)
            width, height = image.size
            if not os.path.isfile(os.path.join(self.dir, path)):
                self.store.persist_file(
                    path, buf, info,
                    meta={'width': width, 'height': height},
                    headers={'Content-Type': 'image/jpeg'})
        return checksum
