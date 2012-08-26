from crawlers.base import BaseComicCrawler
from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup

class JoyOfTech(BaseComicCrawler):
	def __init__(self):
		super(JoyOfTech, self).__init__('Joy of Tech', 'geekculture.com', 100, 'Utenlandske')
		self.url = "http://www.geekculture.com/joyoftech/%s" % (self._imagelink())
	
	def _imagelink(self):
		content = urlfetch.fetch('http://www.geekculture.com/joyoftech/').content
		soup = BeautifulSoup(content)		
		return soup.find('img', {'alt': 'The Joy of Tech comic'})['src']