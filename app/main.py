#############################################################################
####################### Rest API Using Flask, MySql and SQLAlchemy ##########
####################### Also demonstrates pagination ########################
#############################################################################
#############################################################################

from flask import Flask, abort, jsonify, request
from werkzeug.exceptions import HTTPException
from datetime import datetime
from models import db
from models.user import Address, Profile, Contact, Siteuser
import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://newuser:password@localhost/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  True
db1 = SQLAlchemy(app)


@app.errorhandler(Exception)
def handle_error(e):
	""" Handle all exceptions and always return json """
	code = 500
	if isinstance(e, HTTPException):
		code = e.code
	return jsonify(error=str(e), code=code), code


@app.route('/', methods=['GET'])
def index():
	return jsonify({
		'msg': 'API working',
	})


@app.route('/users', methods=['GET'])
def get_user_list():
	""" Get paginated posts with url variable `page` and `per_page`
	"""
	page = int(request.args.get('page', 1))
	per_page = int(request.args.get('per_page', 10))

	users = Siteuser.query.order_by(Siteuser.id.asc()).paginate(page, per_page, error_out=False)
	result = [post.as_dict() for post in users.items]

	return jsonify({
		'page': page,
		'per_page': per_page,
		'total': users.total,
		'result': result,
	})


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
	""" Get the user with request URL arg `id`
	"""
	user = Siteuser.query.get(id)
	if not user:
		return abort(404)

	return jsonify(user.as_dict())


@app.route('/users/post', methods=['POST'])
def create_post():
	""" Create post with request data
	"""
	params = request.get_json()

	if (not params or 'email' not in params or 'username' not in params or 'first_name' not in params
	or 'last_name' not in params):
		return jsonify({'error': 'Arguments Missed'}), 400

	user = Siteuser(
		email=params['email'],
		username=params['username'],
		first_name=params['first_name'],
		last_name=params['last_name'],
		password=params['password'],
		address_id=params['address_id'],
		profile_id=params['profile_id'],
		contact_id=params['contact_id'],
		
	)
	db.session.add(user)
	db.session.commit()

	return jsonify({'result': 'success', 'id': user.id}), 201







@app.route('/address/post', methods=['POST'])
def create_department_post():
	""" Create address with request data
	"""
	params = request.get_json()


	address = Address(
		address1=params['address1'],
		address2=params['address2'],
		city=params['city'],
		state=params['state'],
		zip=params['zip'],
		country=params['country'],		
	)
	db.session.add(address)
	db.session.commit()

	return jsonify({'result': 'success', 'id': address.address_id}), 201
	
	
	
@app.route('/profile/post', methods=['POST'])
def create_profile_post():
	""" Create address with request data
	"""
	params = request.get_json()


	profile = Profile(
		about_myself=params['about_myself'],
		gender=params['gender'],
		age=params['age'],
		undergraduate_degree=params['undergraduate_degree'],
		graduate_degree=params['graduate_degree'],
		occupation=params['occupation'],	
		occupation_details=params['occupation_details'],	
		work_location_city=params['work_location_city'],	
		work_location_country=params['work_location_country'],	
		salary_details=params['salary_details'],	
		profile_status=params['profile_status'],		
	)
	db.session.add(profile)
	db.session.commit()

	return jsonify({'result': 'success', 'id': profile.profile_id}), 201

	
@app.route('/contact/post', methods=['POST'])
def create_contact_post():
	""" Create contact with request data
	"""
	params = request.get_json()


	contact = Contact(
		primary_email=params['primary_email'],
		secondary_email=params['secondary_email'],
		phone_no_area_code=params['phone_no_area_code'],
		phone_no=params['phone_no'],	
	)
	db.session.add(contact)
	db.session.commit()

	return jsonify({'result': 'success', 'id': contact.contact_id}), 201
	


	
@app.route('/address', methods=['GET'])
def get_address_list():
	""" Get paginated posts with url variable `page` and `per_page`
	"""
	page = int(request.args.get('page', 1))
	per_page = int(request.args.get('per_page', 2))

	addresses = Address.query.order_by(Address.address_id.asc()).paginate(page, per_page, error_out=False)
	result = [address.as_dict() for address in addresses.items]
	
	return jsonify({
		'page': page,
		'per_page': per_page,
		'total': addresses.total,
		'result': result,
	})


	
	
@app.route('/profiles', methods=['GET'])
def get_profile_list():
	""" Get paginated profiles with url variable `page` and `per_page`
	"""
	page = int(request.args.get('page', 1))
	per_page = int(request.args.get('per_page', 2))

	profiles = Profile.query.order_by(Profile.id.asc()).paginate(page, per_page, error_out=False)
	result = [profile.as_dict() for profile in profiles.items]
	
	return jsonify({
		'page': page,
		'per_page': per_page,
		'total': profiles.total,
		'result': result,
	})


@app.route('/contacts', methods=['GET'])
def get_contact_list():
	""" Get paginated contacts with url variable `page` and `per_page`
	"""
	page = int(request.args.get('page', 1))
	per_page = int(request.args.get('per_page', 2))

	contacts = Contact.query.order_by(Contact.id.asc()).paginate(page, per_page, error_out=False)
	result = [contact.as_dict() for contact in contacts.items]
	
	return jsonify({
		'page': page,
		'per_page': per_page,
		'total': contacts.total,
		'result': result,
	})




if __name__ == '__main__':
	app.run(host='127.0.0.1', debug=True, port=5000)
