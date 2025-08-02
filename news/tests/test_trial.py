from django.test import TestCase
from news.models import News
import unittest


class TestNews(TestCase):
    TITLE = 'Заголовок'
    TEXT = 'Текст'

    @classmethod
    def setUpTestData(cls):
        cls.news = News.objects.create(
            title=cls.TITLE,
            text=cls.TEXT,
        )

    @unittest.skip('Skip')
    def test_successful_creation(self):
        news_count = News.objects.count()
        self.assertEqual(news_count, 1)

    @unittest.skip('Skip')
    def test_title(self):
        self.assertEqual(self.news.title, self.TITLE)
