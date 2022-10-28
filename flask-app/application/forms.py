# Links the database with your routes, by creating input forms. 

from unicodedata import name
from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import StringField, SubmitField, SelectField, IntegerField

from application.models import Games, Customers 

class CustomerForm(FlaskForm):
    name = StringField("Name")
    table_ = IntegerField("Table number")
    fk_gid = IntegerField("Game ID")
    submit = SubmitField("Submit")

class GameForm(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Submit")
