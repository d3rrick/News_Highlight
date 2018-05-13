class Article:
	
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
		return f"Article : id {self.id} name {self.name} title {self.title}"

class Source:
	def __init__(self, id, name,description,url,category,language,country):
		
		self.id = id 
		self.name = name
		self.description=description
		self.url = url
		self.category=category
		self.language=language 
		self.country = country

	def __repr__(self):
		return f"Source : id {self.id} name {self.name} title {self.description}"

