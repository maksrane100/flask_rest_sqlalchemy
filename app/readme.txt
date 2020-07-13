This project demonstrates use of SQLAlchemy with MySQL. Rest API Using Flask, MySql and SQLAlchemy.
Also demonstrates pagination.

How To Run Project:

Download the zip file and extract it in a folder e.g. flask_api

c:\flask_api\app>main.py

Create address using http://127.0.0.1:5000/address/post

sample post request below:

{
	
	"address1":"2000 Sunnyvale Blvd.",
	"address2":"Apt 1000",
	"city":"Sunnyvale",
	"state":"CA",
	"zip":"94085",
	"country":"USA"
}

Create profile using http://127.0.0.1:5000/profile/post


sample post request below:


{
	
	"about_myself":"I am working in IT",
	"gender":"Male",
	"age":24,
	"undergraduate_degree":"BE",
	"graduate_degree":"MS",
	"occupation":"Software Engineer",
	"occupation_details":"ABC Computers",
	"work_location_city":"Sunnyvale",
	"work_location_country":"USA",
	"salary_details":"120000",
	"profile_status":"Active"
}

Create contact using http://127.0.0.1:5000/contact/post

sample post request below:

{
	
	"primary_email":"nitin@test.com",
	"secondary_email":"nitin.patil@test.com",
	"phone_no_area_code":"001",
	"phone_no":"9252224444"
}


Create user using http://127.0.0.1:5000/users/post

sample post request below:

{
	
	"email":"ganesh@test.com",
	"username":"ganesh",
	"first_name":"Ganesh",
	"last_name":"Patil",
	"password":"ganesh",
	"address_id":1,
	"profile_id":1,
	"contact_id":1
	
}


Test getting users using following url:
http://127.0.0.1:5000/users?page=1&per_page=4
