-- Creating Database --
create database Shazam;
-- Using/naviagte to Shazam database --
use Shazam;
-- Creating Student Table --
create table Student (
	reg_id char(12) primary key,
	first_name varchar(15) not null,
	middle_name varchar(15),
	last_name varchar(15) not null,
	dob date not null,
	gpa float(2) not null,
	dir varchar(50) not null
);
-- Creating Script Table --
create table Script (
    script_id char(2) primary key,
    script_name varchar(20) unique not null,
    script_desc varchar(100),
    script_input varchar(100) not null
);
-- Creating Grading Table --
create table Grade (
    reg_id char(12) not null,
    script_id varchar(20) not null,
    grade integer not null
);
-- adding reg_id constraint --
alter table Grade
add constraint regid_fk foreign key(reg_id)
references Student(reg_id);
-- adding script_id constraint --
alter table Grade
add constraint script_fk foreign key(script_id)
references Script(script_id);