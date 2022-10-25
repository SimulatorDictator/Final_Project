# How your databases are going to look.
from application import db

class Games(db.Model):
    gid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

class Customers(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    table_ = db.Column(db.Integer)
    fk_gid = db.Column(db.Integer, db.ForeignKey('games.gid'))
