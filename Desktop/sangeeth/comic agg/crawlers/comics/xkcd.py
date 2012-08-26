from crawlers.base import BaseComicCrawler
from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup

class Xkcd(BaseComicCrawler):
	def __init__(self):
		super(Xkcd, self).__init__('xkcd', 'imgs.xkcd.com', 140, 'Utenlandske')
		self.url = self._imagelink()
	
	def _imagelink(self):
		content = urlfetch.fetch('http://www.xkcd.com').content
		soup = BeautifulSoup(content)
		for img in soup.findAll('img'):
			if img["src"].startswith("http://imgs.xkcd.com/comics/"):
				return img["src"]
		raise Exception