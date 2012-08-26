from crawlers.base import BaseComicCrawler
from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup

class TomToles(BaseComicCrawler):
	def __init__(self):
		super(TomToles, self).__init__('Tom Toles', 'washingtonpost.com', 120, 'Utenlandske')
		self.headers = { "Referer": 'http://www.gocomics.com/tomtoles/' }
		self.url = self._imagelink()
	
	def _imagelink(self):
		content = urlfetch.fetch('http://www.gocomics.com/tomtoles/').content
		soup = BeautifulSoup(content)
		for img in soup.findAll('img'):
			if img["src"].startswith("http://imgsrv.gocomics.com/dim/?fh="):
				return img["src"]
		raise Exception