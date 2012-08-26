from crawlers.base import BaseComicCrawler

class Dennis(BaseComicCrawler):
	def __init__(self):
		super(Dennis, self).__init__('Dennis the Menace', 'est.rbma.com', 90, 'Utenlandske')
		self.headers = { "Referer": 'http://www.kingfeatures.com/features/comics/dennis/aboutMaina.php' }
		self.url = "http://est.rbma.com/content/Dennis_The_Menace?date=%s" % (self.date.strftime("%Y%m%d"))
