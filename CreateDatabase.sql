-- Creating Database --
create database SEA;
-- Using/naviagte to Sea database --
use SEA;
-- Creating Student Table --
create table Student (
    reg_id char(12) primary key,
    name varchar(50) not null,
    dob date not null,
    email_id varchar(30) not null,
    dir varchar(50) not null,
    marks integer not null
);
-- Creating Script Table --
create table Script (
    script_id char(4) primary key,
    script_name varchar(20) unique not null,
    script_week integer not null,
    script_desc varchar(100),
    script_input varchar(100),
    script_runtime varchar(20) not null,
    co varchar(4) not null
);
-- Creating Grading Table --
create table Grade (
    reg_id char(12) not null,
    script_id char(4) not null,
    grade integer not null,
    date_of_grading date not null
);
-- adding reg_id constraint --
alter table Grade
add constraint regid_fk foreign key(reg_id)
references Student(reg_id);
-- adding script_id constraint --
alter table Grade
add constraint scriptid_fk foreign key(script_id)
references Script(script_id);
-- adding course outcomes table --
create table CourseOutcomes (
    co  varchar(4) primary key,
    co_desc varchar(30) not null
);
-- adding co constraint --
alter table Script
add constraint co_fk foreign key(co)
references CourseOutcomes(co);