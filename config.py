import os #this is an inbult method that allows access to the operating system variables like the environment and directories

class Config:
	"""this is the base config class that sets out some variables"""
	NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country={}&category={}&apiKey={}'
	NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
	NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
	SECRET_KEY = os.environ.get("SECRET_KEY")

class ProdConfig(Config):
	"""this configuration class is for setting production variables"""

	DEBUG = False

class DevConfig(Config):
	"""this configuration class is for setting development variables"""
	DEBUG = True


config_options = {
	'development' : DevConfig,
	'production' : ProdConfig
}