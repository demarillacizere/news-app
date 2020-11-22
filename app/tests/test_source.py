import unittest
from models import classes
Source = classes.Source


class TestNews(unittest.TestCase):
    '''
    Test the behavoiur of the Article class
    '''
    def setUp(self):
        #will run before every test
        self.new_source=Source("igihe","Igihe","Rwanda's first","https://igihe.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    '''
    Test if our  source class is initialized correctly
    '''
    def self_init(self):
        self.assertEqual(self.new_source.id,"igihe")
        self.assertEqual(self.new_source.name,"Igihe")
        self.assertEqual(self.new_source.description,"Rwanda's first")
        self.assertEqual(self.new_source.url,"https://igihe.com")
        
if __name__ == '__main__':
    unittest.main()