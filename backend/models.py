from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Comment(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.String(25))