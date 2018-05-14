import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
	'''
	Test Class to test the behaviour of the Source class
	'''
	def setUp(self):
		'''
		Set up method that will run before every Test
		'''
		self.new_source = Source("unique id","new times","this article is about how to spend your mornings efficiently","https://google.com","health","us","en")

	def test_instance(self):
		'''
		A method that will run to test whether an instance is of Article class.
		'''
		self.assertTrue(isinstance(self.new_source,Source))
	def test_correct_instatiation(self):
		"""
		A method that allows testing whether instatiation is done properly
		"""
		self.assertEqual(self.new_source.id,"unique id")

		
