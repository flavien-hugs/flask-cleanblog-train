from datetime import date

from . import db



"""
class Author:
    id: int primary key
    auth_firstname: str
    auth_lastname: str
    auth_birthdate: date
    auth_created: date
"""


class Author(db.Model):
	__tablename__ = "author"
	
	id = db.Column(db.Integer, primary_key=True)
	auth_firstname = db.Column(db.String(80), nullable=False)
	auth_lastname = db.Column(db.String(100), nullable=False)
	auth_birthdate = db.Column(db.Date, default=date.today())
	auth_created = db.Column(db.Date, default=date.today())

	def save(self):
		db.session.add(self)
		db.session.commit()

	def update(self, auth_firstname, auth_lastname, auth_birthdate):
		self.auth_firstname = auth_firstname
		self.auth_lastname = auth_lastname
		self.auth_birthdate = auth_birthdate
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()


"""
class Post:
    id: int primary key
    post_title: str
    post_subtitle: str
    post_content: str (Text)
    post_author: str
    post_posted: date
"""


class Post(db.Model):
	__tablename__ = "post"
	id = db.Column(db.Integer, primary_key=True)
	post_title = db.Column(db.String(80), nullable=False)
	post_subtitle = db.Column(db.String(100), nullable=False)
	post_content = db.Column(db.Text, nullable=False)
	post_author = db.Column(db.String(80), nullable=False)
	post_posted = db.Column(db.Date, default=date.today())

	def __str__(self):
		return self.post_title

	def save(self):
		db.session.add(self)
		db.session.commit()

	def update(self, post_title, post_subtitle, post_content, post_author):
		self.post_title = post_title
		self.post_content = post_subtitle
		self.post_content = post_content
		self.post_author = post_author
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()
