from crawlers.base import BaseComicCrawler
from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup

class CyanideHappiness(BaseComicCrawler):
	def __init__(self):
		super(CyanideHappiness, self).__init__('Cyanide & Happiness', 'explosm.net', 87, 'Utenlandske')
		self.url = self._imagelink()
	
	def _imagelink(self):
		content = urlfetch.fetch('http://www.explosm.net/comics/new/').content
		soup = BeautifulSoup(content)
		for img in soup.findAll('img'):
			if img["src"].startswith("http://www.explosm.net/db/files/Comics/"):
				return img["src"]
		raise Exception