from application import db 

# Create our database for us.
db.drop_all()
db.create_all()