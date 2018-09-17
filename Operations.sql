-- Changing Delimiter --
DELIMITER $
-- Creating trigger for audit insert
create trigger before_student_update before update on Student 
for each row 
begin 
	insert into Student_audit
	set reg_id = old.reg_id,
	name = old.name,
	marks = old.marks,
	action = 'before update',							
	change_of_time = timestamp(now()); 
end$
-- Resetting Delimiter --
DELIMITER ;
-- Changing Delimiter --
DELIMITER $
-- Creting trigger for audit insert --
create trigger after_student_update after update on Student 
for each row 
begin 
	insert into Student_audit
	set reg_id = old.reg_id,
	name = new.name,
	marks = new.marks,
	action = 'after update',
	change_of_time = timestamp(now()); 
end$
-- Resetting Delimiter --
DELIMITER ;
-- Creating triiger for audit insert --
create trigger after_student_delete after delete on Student 
for each row 
begin 
	insert into Student_audit
	set reg_id = old.reg_id,
	name = old.name,
	marks = old.marks,
	action = 'delete',
	change_of_time = timestamp(now()); 
end$
-- Resetting delimiter --
DELIMITER ;
-- Changing Delimiter --
DELIMITER $
-- Creating trigger --
create trigger after_student_insertion after insert on Student 
for each row 
begin 
	insert into Student_audit
	set reg_id = new.reg_id,
	name = new.name,
	marks = new.marks,
	action = 'insertion',
	change_of_time = timestamp(now());
end$
-- Resetting delimiter --
DELIMITER ; 
-- changind delimiter --
DELIMITER $
-- creting trigger
create trigger before_student_insertion before insert on Student 
for each row 
begin 
	if length(reg_id) < 12 then set reg_id = null
	if marks > 15 then set marks = null 	
end$
-- Resetting delimiter--
DELIMITER ;
--changing delimiter--
DELIMITER $
--creating trigger on Grade Table--
create trigger after_grade_insertion after insert on Grade
for each row
begin
	insert into Grade_audit
	set reg_id=new.reg_id,
	script_id=new.script_id,
	grade=new.grade,
	action='insert',
	change_of_time=timestamp(now());
ends$
--creating trigger after update on Grade Table--
create trigger after_grade_update after update on Grade
for eeach row
begin
	insert into Grade_audit
	set reg_id=old.reg_id,
	script_id=old.script_id,
	grade=new.grade,
	action='update',
	change_of_time=timestamp(now());
ends$
