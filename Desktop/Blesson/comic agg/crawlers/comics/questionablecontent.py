from crawlers.base import BaseComicCrawler
from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup

class QuestionableContent(BaseComicCrawler):
	def __init__(self):
		super(QuestionableContent, self).__init__('questionablecontent', 'questionablecontent.net', 140, 'Utenlandske')
		self.url = self._imagelink()
	
	def _imagelink(self):
		content = urlfetch.fetch('http://www.questionablecontent.net').content
		soup = BeautifulSoup(content)
		for img in soup.findAll('img'):
			if img["src"].startswith("http://www.questionablecontent.net/comics/"):
				return img["src"]
		raise Exception
