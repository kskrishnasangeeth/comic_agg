from google.appengine.api import urlfetch
from datetime import date, timedelta, datetime, time as dtime
import time

class BaseComicCrawler(object):
	headers = {}
	def __init__(self, name, host, sort_order, group):
		self.name = name
		self.host = host
		self.group = group
		self.timezone = 1
		self.sort_order = sort_order
	
	def fetch(self):
		return urlfetch.fetch(self.url, headers=self.headers)
	
	@property
	def date(self):
		return datetime.now() + timedelta(hours = 2)