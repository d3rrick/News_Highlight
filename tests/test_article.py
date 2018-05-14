import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
	 '''
    Test Class to test the behaviour of the Article class
    '''
	def setUp(self):
		 '''
        Set up method that will run before every Test
        '''
		self.new_article = Article(1,"new times",'NEW_TIMES',"the cool morning","this article is about how to spend your mornings efficiently","https://google.com","https://google.com/image.jpg",True)

	def test_instance(self):
		 '''
        A method that will run to test whether an instance is of Article class.
        '''
		self.assertTrue(isinstance(self.new_article,Article))
	def test_correct_instatiation(self):
		"""
		A method that allows testing whether instatiation is done properly
		"""
		self.assertEqual(self.new_article.id, 1)

		
if __name__ == '__main__':
	unittest()