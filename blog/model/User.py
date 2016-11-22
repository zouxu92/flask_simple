# -*- coding:utf-8 -*-
### orm框架flask-aqlalchemy实现创建、增删改查功能 --User表.
from blog import db

class User(db.Model):
	__tablename__ = 'b_user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(10), unique=True)
	password = db.Column(db.String(16))

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def __repr__(self):
		return '<User %r>' % self.username