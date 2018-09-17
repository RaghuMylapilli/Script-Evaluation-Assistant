-- Creating trigger for audit insert --
create trigger before_student_update before update on Student 
for each row 
begin 
	insert into Student_audit
    	set reg_id = old.reg_id,
        name = old.name,
		marks = old.marks,
		action = 'before update',							
        change_of_time = timestamp(now()); 
end;
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
end;
-- Creating trigger for audit insert --
create trigger after_student_delete after delete on Student 
for each row 
begin 
	insert into Student_audit
    	set reg_id = old.reg_id,
        name = old.name,
		marks = old.marks,
		action = 'delete',
        change_of_time = timestamp(now()); 
end;
-- Creating after trigger --
create trigger after_student_insertion after insert on Student 
for each row 
begin 
	insert into Student_audit
	set reg_id = new.reg_id,
	name = new.name,
	marks = new.marks,
	action = 'insertion',
	change_of_time = timestamp(now());
end;
-- --
create trigger after_grade_insertion after insert on Grade
for each row
begin
	insert into Grade_audit
	set reg_id=new.reg_id,
	script_id=new.script_id,
	grade=new.grade,
	action='insert',
	change_of_time=timestamp(now());
end;
--creating trigger after update on Grade Table--
create trigger after_grade_update after update on Grade
for each row
begin
	insert into Grade_audit
	set reg_id=old.reg_id,
	script_id=old.script_id,
	grade=new.grade,
	action='update',
	change_of_time=timestamp(now());
end;