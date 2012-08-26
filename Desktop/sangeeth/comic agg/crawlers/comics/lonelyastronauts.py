from crawlers.base import BaseComicCrawler
from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup

class LonelyAstronauts(BaseComicCrawler):
	def __init__(self):
		super(LonelyAstronauts, self).__init__('LonelyAstronauts', 'agreeablecomics.com/loneliestastronauts', 80 , 'Utenlandske')
		self.url = self._imagelink()
	
	def _imagelink(self):
		content = urlfetch.fetch('http://www.agreeablecomics.com/loneliestastronauts').content
		soup = BeautifulSoup(content)
		for img in soup.findAll('img'):
			if img["src"].startswith("http://www.agreeablecomics.com/loneliestastronauts/comics/"):

				return img["src"]
		raise Exception
