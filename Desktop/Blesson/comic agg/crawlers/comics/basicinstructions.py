from crawlers.base import BaseComicCrawler
from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup

class Smbc(BaseComicCrawler):
	def __init__(self):
		super(BasicInstructions, self).__init__('basicinstructions', 'basicinstructions.net', 140, 'Utenlandske')
		self.url = self._imagelink()
	
	def _imagelink(self):
		content = urlfetch.fetch('http://www.questionablecontent.net').content
		soup = BeautifulSoup(content)
		for img in soup.findAll('img'):
			if img["src"].startswith("http://basicinstructions.net/storage/"):
				return img["src"]
		raise Exception
