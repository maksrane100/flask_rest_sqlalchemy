------------------------------------------------------------------------------- 
------- First Create Database "flask_db" and create following tables ----------
-------------------------------------------------------------------------------

CREATE TABLE address(
   address_id INT NOT NULL AUTO_INCREMENT,
   address1 VARCHAR(64),
   address2 VARCHAR(64),
   city VARCHAR(64),
   state VARCHAR(64),
   zip VARCHAR(64),
   country VARCHAR(64),
   PRIMARY KEY ( address_id )
);

CREATE TABLE profile(
   profile_id INT NOT NULL AUTO_INCREMENT,
   about_myself TEXT,
   gender VARCHAR(10),
   age INT,
   undergraduate_degree VARCHAR(100),
   graduate_degree VARCHAR(100),
   occupation VARCHAR(100),
   occupation_details TEXT,
   work_location_city VARCHAR(64),
   work_location_country VARCHAR(64),
   salary_details VARCHAR(64),
   profile_status VARCHAR(12),
   PRIMARY KEY ( profile_id )
);


CREATE TABLE contact(
   contact_id INT NOT NULL AUTO_INCREMENT,
   primary_email VARCHAR(30),
   secondary_email VARCHAR(30),
   phone_no_area_code VARCHAR(4),
   phone_no VARCHAR(10),
   PRIMARY KEY ( contact_id )
);

CREATE TABLE siteuser(
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(60) NOT NULL UNIQUE,
	username VARCHAR(60) NOT NULL UNIQUE,
	first_name VARCHAR(60),
	last_name VARCHAR(60),
	password VARCHAR(128) NOT NULL,
	address_id int,
	profile_id int,
	contact_id int,
	is_admin BOOLEAN,
	PRIMARY KEY ( id ),
	FOREIGN KEY (profile_id) REFERENCES profile(profile_id),
	FOREIGN KEY (address_id) REFERENCES address(address_id),
	FOREIGN KEY (contact_id) REFERENCES contact(contact_id)
);