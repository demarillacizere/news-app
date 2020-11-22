import unittest
from models import classes
Article = classes.Article


class TestNews(unittest.TestCase):
    '''
    Test the behavoiur of the Article class
    '''
    def setUp(self):
        #will run before every test
        self.new_article=Article("The US elections has been called off","It was announced yesterday","https://newsapi.org/v2/sources","https://bbc.com","2020-11-20")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_Article,Article))

    '''
    Test if our  Article class is initialized correctly
    '''
    def self_init(self):
        self.assertEqual(self.new_article.title,"The US elections has been called off")
        self.assertEqual(self.new_article.description,"It was announced yesterday")
        self.assertEqual(self.new_article.urlToImage,"https://newsapi.org/v2/sources")
        self.assertEqual(self.new_article.url,"https://bbc.com")
        self.assertEqual(self.new_article.publishedAt,"2020-11-20")

if __name__ == '__main__':
    unittest.main()