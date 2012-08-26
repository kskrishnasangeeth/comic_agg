import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.api import urlfetch
from crawlers.comics.bizarro1 import Bizarro1

class TestHandler(webapp.RequestHandler):
	def get(self):
		bizarro = Bizarro1()
		self.response.out.write(bizarro.url)

def main():
	app = webapp.WSGIApplication([
	(r'.*', TestHandler)])
	wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()