-- Creating Database --
create database SEA;
-- Using/naviagte to Sea database --
use SEA;
-- Creating Student Table --
create table Student (
	reg_id char(12) primary key,
    name varchar(50) not null,
	dob date not null,
	dir varchar(50) not null,
	marks integer not null
);
-- Creating Script Table --
create table Script (
    script_id char(4) primary key,
    script_name varchar(20) unique not null,
    script_desc varchar(100),
    script_input varchar(100)
);
-- Creating Grading Table --
create table Grade (
    reg_id char(12) not null,
    script_id char(4) not null,
    grade integer not null
);
--Creating Student_audit Table --
create table Student_audit (
	reg_id char(12) ,
        name varchar(50),
	marks integer ,
	action varchar(10),
	change_of_time timestamp 
);
--Creating Script_audit Table -- 
create table Script_audit (
    script_id char(4) ,
    script_name varchar(20) ,
    action varchar(10),
    change_of_time timestamp 
	
);
--Creating Grade_audit Table --
create table Grade_audit(
    reg_id char(12) ,
    script_id char(4),
    grade integer,
    action varchar(10),
    change_of_time timestamp 
);
-- adding reg_id constraint --
alter table Grade
add constraint regid_fk foreign key(reg_id)
references Student(reg_id);
-- adding script_id constraint --
alter table Grade
add constraint scriptid_fk foreign key(script_id)
references Script(script_id);
