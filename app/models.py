from . import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    firstname = db.Column(db.String(80), unique=True)
    lastname = db.Column(db.String(80), unique=True)
#     age = db.Column(db.Float, unique=True)
    sex = db.Column(db.String(120), unique=True)
    image = db.Column(db.String(120), unique=True)
    
    def __init__(self,username,firstname,lastname,sex):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
#         self.age = age
        self.sex = sex
        
    def __repr__(self):
        return '<Profile %r %r %r %r>' % (self.username,self. firstname,self.lastname,self.sex)