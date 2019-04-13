from django.test import TestCase
from apps.blog.models import *
# Create your tests here.


class BlogTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="label1")
        Tag.objects.create(name="label2")
        Category.objects.create(name="catecory1")
        Category.objects.create(name="catecory2")
        Article.objects.create(title="This is article1 title", content="This is article1 content",
                               category=Category.objects.get(name="catecory1"), pub_time=now())
        Article.objects.create(title="This is article2 title", content="This is article2 content",
                               category=Category.objects.get(name="catecory2"), pub_time=now())

    def test_tag_create(self):
        label1 = Tag.objects.get(name="label1")
        label2 = Tag.objects.get(name="label2")
        self.assertEqual(label1.name, 'label1')
        self.assertEqual(label2.name, 'label2')

    def test_catecory_create(self):
        catecory1 = Category.objects.get(name="catecory1")
        catecory2 = Category.objects.get(name="catecory2")
        self.assertEqual(catecory1.name, 'catecory1')
        self.assertEqual(catecory2.name, 'catecory2')

    def test_article_create(self):
        Article1 = Article.objects.get(title="This is article1 title")
        Article2 = Article.objects.get(title="This is article2 title")
        self.assertEqual(Article1.title, 'This is article1 title')
        self.assertEqual(Article2.title, 'This is article2 title')
        self.assertEqual(Article1.content, 'This is article1 content')
        self.assertEqual(Article2.content, 'This is article2 content')
        self.assertIn(Article1.category.name, 'catecory1')
        self.assertIn(Article2.category.name, 'catecory2')
