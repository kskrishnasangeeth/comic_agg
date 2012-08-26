import wsgiref.handlers
from google.appengine.ext import webapp
from models.picture import Picture


class PictureHandler(webapp.RequestHandler):
	def get(self):
		key = self.request.path.split('/')[-1]
		picture = Picture.get(key)
		if not picture:
			self.error(404)
			return
		self.response.headers['Content-Type'] = picture.content_type.__str__()
		self.response.out.write(picture.picture)

def main():
	app = webapp.WSGIApplication([
	(r'.*', PictureHandler)])
	wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()