from django.test import TestCase
from apps.gallery.models import *
# Create your tests here.


class ModelTestCase(TestCase):
    def setUp(self):
        Gallery.objects.create(title="gallery1 title", description="gallery1 description")
        Gallery.objects.create(title="gallery2 title", description="gallery2 description")

    def test_gallery_create(self):
        gallery1 = Gallery.objects.get(title="gallery1 title")
        gallery2 = Gallery.objects.get(title="gallery2 title")
        self.assertEqual(gallery1.description, 'gallery1 description')
        self.assertEqual(gallery2.description, 'gallery2 description')
        self.assertEqual(gallery1.title, 'gallery1 title')
        self.assertEqual(gallery2.title, 'gallery2 title')
