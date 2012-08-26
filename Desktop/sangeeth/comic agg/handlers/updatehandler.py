import wsgiref.handlers
import logging
from google.appengine.ext               import webapp, db
from google.appengine.api.urlfetch      import DownloadError
from google.appengine.api.labs          import taskqueue
from datetime                           import date
from models.picture                     import Picture

#from crawlers.comics.bizarro2           import Bizarro2
#from crawlers.comics.bizarro3           import Bizarro3
from crawlers.comics.cyanidehappiness   import CyanideHappiness
from crawlers.comics.dennis             import Dennis
#from crawlers.comics.fagprat            import Fagprat
#from crawlers.comics.faktafraverden     import FaktaFraVerden
from crawlers.comics.joyoftech          import JoyOfTech
#from crawlers.comics.lunch              import Lunch
#from crawlers.comics.nemi1              import Nemi1
#from crawlers.comics.nemi2              import Nemi2
#from crawlers.comics.nemi3              import Nemi3
from crawlers.comics.sixchix            import SixChix
#from crawlers.comics.sixchix2           import SixChix2
#from crawlers.comics.skavlansark        import SkavlansArk
from crawlers.comics.tomtoles           import TomToles
#from crawlers.comics.wulffmorgenthaler  import WulffmorgentHaler
from crawlers.comics.xkcd               import Xkcd
from crawlers.comics.questionablecontent import QuestionableContent
from crawlers.comics.hark		import Hark
from crawlers.comics.smbc		import Smbc
from crawlers.comics.lonelyastronauts	import LonelyAstronauts
from crawlers.comics.calvin		import Calvin
from crawlers.comics.dilbert    import Dilbert
from crawlers.comics.freshlysqueezed	import Freshly
from crawlers.comics.inspector	import Inspector
class UpdateHandler(webapp.RequestHandler):
	comics_classes = {'CyanideHappiness':CyanideHappiness, 'Dennis': Dennis, 'JoyOfTech': JoyOfTech, 'SixChix': SixChix, 'Xkcd': Xkcd, 'QuestionableContent': QuestionableContent, 'Hark' : Hark, 'Smbc' : Smbc, 'LoneyAstronauts': LonelyAstronauts, 'Calvin': Calvin, 'Dilbert' : Dilbert, 'Freshly' : Freshly, 'Inspector' : Inspector }
	def get(self):
		for k,v in self.comics_classes.iteritems():
			taskqueue.add(url='/update', params={'key': k}, method='POST')
		
	def post(self):
		try:
			logging.info('Updating started - %s' % self.request.get('key'))
			comic = self.comics_classes[self.request.get('key')]()
			response = comic.fetch()
			content_type = response.headers["content-type"]
			picture = response.content

			if not content_type.startswith("image/"):
				logging.info('Content-type is not an image')
				return
			
			rows = db.GqlQuery('SELECT * FROM Picture WHERE date = :1 and name = :2 and host = :3', date.today(), comic.name, comic.host)
			
			if rows.count() > 0:
				if rows[0].picture == picture:
					return
				else:
					for row in rows:
						row.delete()
			
			
			db_object = Picture(
			name=comic.name,
			host=comic.host,
			group=comic.group,
			url=comic.url,
			picture=picture,
			content_type=content_type,
			date=date.today(),
			sort_order=comic.sort_order)
			
			logging.info('Saving new picture')
			
			db_object.put()
		except Exception, e:
			logging.error(e)

def main():
	app = webapp.WSGIApplication([
	(r'.*', UpdateHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()
