from google.appengine.ext import db

class Picture(db.Model):
	name = db.StringProperty(required=True)
	host = db.StringProperty(required=True)
	url = db.LinkProperty(required=True)
	group = db.StringProperty(required=True)
	picture = db.BlobProperty(required=True)
	content_type = db.StringProperty(required=True)
	date = db.DateProperty(required=True)
	sort_order = db.IntegerProperty(required=True)