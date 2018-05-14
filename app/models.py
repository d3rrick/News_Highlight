class Article:
	""" this class is a blue print for creating article instances"""
	
	def __init__(self,id,name,author,title,description,url,image,published):
		self.id = id
		self.name=name
		self.author=author
		self.title=title
		self.description=description
		self.url=url
		self.image = image
		self.published=published

	def __repr__(self):
		"""the represent dunder method is to return a legible format to other developers of istances of this class"""
		return f"Article : id {self.id} name {self.name} title {self.title}"

class Source:
	"""this class acts as a blue print of source instances"""
	def __init__(self, id, name,description,url,category,language,country):
		
		self.id = id 
		self.name = name
		self.description=description
		self.url = url
		self.category=category
		self.language=language 
		self.country = country
	def __repr__(self):
		"""the represent dunder method is to return a legible format to other developers of istances of this class"""
		return f"Source : id {self.id} name {self.name} title {self.description}"

