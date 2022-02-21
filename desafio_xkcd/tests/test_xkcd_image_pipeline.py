from unittest import TestCase
from tests.fixtures import get_image_fixture
from desafio_xkcd.pipelines import CustomImagePipeline


class TestXKCDImagePipeline(TestCase):

    def setUp(self) -> None:
        self.store = 'images'
        self.pipeline = CustomImagePipeline(self.store)

    def test_file_path_with_hash_md5(self) -> None:
        local_file = '0a5b1f48f37043c53cdff9160d3d3b2f.png'
        image = get_image_fixture(f'images/{local_file}')
        md5_file_path = self.pipeline.custom_file_path(image)
        self.assertEqual(local_file, md5_file_path)
