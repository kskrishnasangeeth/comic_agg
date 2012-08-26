import wsgiref.handlers
from datetime import date
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from models.picture import Picture

class MainHandler(webapp.RequestHandler):
	def get(self):
		pictures = db.GqlQuery('SELECT * FROM Picture WHERE date = :1 ORDER BY sort_order', date.today())
		values = {
			'pictures': pictures
		}
		self.response.out.write(
			template.render('../templates/main.html', values))

class TextHandler(webapp.RequestHandler):
	def get(self):
		pictures = db.GqlQuery('SELECT * FROM Picture WHERE date = :1 ORDER BY sort_order', date.today())
		for picture in pictures:
			self.response.out.write("%s;%s%s;%s;%s\n" % (picture.name, "http://3.cechackers.appspot.com/comic/", picture.key(), picture.group, picture.host))

def main():
	app = webapp.WSGIApplication([(r'.*\.txt', TextHandler),(r'.*', MainHandler)])
	wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()
