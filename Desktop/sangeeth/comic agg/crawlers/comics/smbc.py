from crawlers.base import BaseComicCrawler
from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup

class Smbc(BaseComicCrawler):
	def __init__(self):
		super(Smbc, self).__init__('Smbc','smbc-comics.com', 110, 'Utenlandske')
		self.url = self._imagelink()
	
	def _imagelink(self):
		content = urlfetch.fetch('http://www.smbc-comics.com').content
		soup = BeautifulSoup(content)
		for img in soup.findAll('img'):
			if img["src"].startswith("http://www.smbc-comics.com/comics/"):
				return img["src"]
		raise Exception
