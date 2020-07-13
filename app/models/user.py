#from models import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, abort, jsonify, request

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://newuser:password@localhost/flask_db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)




class Address(db.Model):
    __tablename__ = 'address'
    address_id = db.Column(db.Integer, primary_key=True)
    address1 = db.Column(db.String(64))
    address2 = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))    
    zip = db.Column(db.String(64))
    country = db.Column(db.String(64))

    def as_dict(self):
        return {	
            'address_id': self.address_id,
            'address1': self.address1,
            'address2': self.address2,
            'city': self.city,
            'state': self.state,
            'zip': self.zip,
            'country': self.country,            
        }
        
class Profile(db.Model):
    __tablename__ = 'profile'
    profile_id = db.Column(db.Integer, primary_key=True)
    about_myself = db.Column(db.String(2000))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    undergraduate_degree = db.Column(db.String(100))
    graduate_degree = db.Column(db.String(100))
    occupation = db.Column(db.String(100))
    occupation_details = db.Column(db.String(1000))
    work_location_city = db.Column(db.String(64))
    work_location_country = db.Column(db.String(64))
    salary_details = db.Column(db.String(64))
    profile_status = db.Column(db.String(12))
    work_location_city = db.Column(db.String(64))

    def as_dict(self):
        return {
            'profile_id': self.profile_id,
            'about_myself': self.about_myself,
            'gender': self.gender,
            'age': self.age,
            'undergraduate_degree': self.undergraduate_degree,
            'graduate_degree': self.graduate_degree,
            'occupation': self.occupation,
            'occupation_details': self.occupation_details,
            'work_location_city': self.work_location_city,    
            'work_location_country': self.work_location_country,    
            'salary_details': self.salary_details,    
            'profile_status': self.profile_status,    
            'work_location_city': self.work_location_city,    
        
        }
        
        
class Contact(db.Model):
    contact_id = db.Column(db.Integer, primary_key=True)
    primary_email = db.Column(db.String(30))
    secondary_email = db.Column(db.String(30))
    phone_no_area_code = db.Column(db.String(4))
    phone_no = db.Column(db.String(10))

    def as_dict(self):
        return {
            'contact_id': self.contact_id,
            'primary_email': self.primary_email,
            'secondary_email': self.secondary_email,
            'phone_no_area_code': self.phone_no_area_code,
            'phone_no': self.phone_no,
        }

        
class Siteuser(db.Model):
    """
    Create siteuser table
    """

    __tablename__ = 'siteuser'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password = db.Column(db.String(128))
    address_id = db.Column(db.Integer, db.ForeignKey('address.address_id'))
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.profile_id'))
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.contact_id'))
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Siteuser: {}>'.format(self.username)

    def as_dict(self):
        return {
            'email': self.email,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password,
            'address_id': self.address_id,
            'profile_id': self.profile_id,
            'contact_id': self.contact_id,
        }