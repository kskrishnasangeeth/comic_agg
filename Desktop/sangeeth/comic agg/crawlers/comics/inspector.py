from crawlers.base import BaseComicCrawler
from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup

class Inspector(BaseComicCrawler):
	def __init__(self):
		super(Inspector, self).__init__('Inspector Dangers Quiz', 'gocomics.com', 100, 'Utenlandske')
		self.url = self._imagelink()
	
	def _imagelink(self):
		content = urlfetch.fetch('http://www.gocomics.com/inspector-dangers-crime-quiz',headers = {'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"}).content
		soup = BeautifulSoup(content)
		for img in soup.findAll('img'):
			if img["src"].startswith("http://assets.amuniversal.com/"):
				return img["src"]
		raise Exception
