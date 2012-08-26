from crawlers.base import BaseComicCrawler

class SixChix(BaseComicCrawler):
	def __init__(self):
		super(SixChix, self).__init__('Six Chix', 'cserver.it-content.com',80, 'Norske')
		self.url = "http://cserver.it-content.com/retriever.php?id=31&date=%s" % (self.date.strftime("%Y%m%d"))