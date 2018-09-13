-- Creating Database
create database Shazam;
-- Using/naviagte to Shazam database
use Shazam;
-- Creating Student Table
create table Student (
	regid char(12) primary key,
	first_name varchar(15) not null,
	middle_name varchar(15),
	last_name varchar(15) not null,
	dob date not null,
	gpa float(2) not null,
	dir varchar(50) not null
);
-- Creating PythonScript Table
create table PythonScript (
	pyid char(4) primary key,
	script varchar(10) unique not null,
	upload_time timestamp not null,
	grade char(1)
);
-- Creating Author Table
create table Author (
	regid char(12)
	pyid char(4) 
); 
-- Adding regid fk constraint
alter table Author
add constraint regid_fk foreign key(regid)
references Student(regid);
-- Adding pyid fk constriant
alter table Author
add constraint pyid_fk foreign key(pyid)
references PythonScript(pyid);
-- Creating course plan Table
create table CoursePlan (
	week integer not null,
	script varchar(10) unique not null
);
-- Adding script foreign key constraint
alter table CoursePlan
add constraint script_fk foreign key(script)
references PythonScript(script);