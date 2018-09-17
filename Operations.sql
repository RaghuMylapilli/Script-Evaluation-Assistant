-- for dropping the trigger we use the procedures so that it will also be covered in our project -- 
--for calling any procedure we simply write  call procedure_name() -- 
--Before writing trigger we have to change the  delimiter from ; to $ --

--creating triggers and procedures on Student table only ---

create procedure drop_before_student_update()
drop trigger before_student_update;

create procedure drop_after_student_update()
drop trigger after_student_update;

create procedure drop_after_student_delete()
drop trigger after_student_delete;

create procedure drop_after_student_insertion()
drop trigger after_student_insertion;

create procedure drop_before_student_insertion()
drop trigger before_student_insertion;

""" trigger on before update """

DELIMITER $
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
DELIMITER ;

""" trigger on after update """

DELIMITER $
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
DELIMITER ;

--as there is no need of trigger for before delete .. we write it only for after deletion --
""" trigger on after delete """

DELIMITER $
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
DELIMITER ;
 
""" trigger on after insertion """

DELIMITER $
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
DELIMITER ; 

--as we are giving the constraints as not null for all attributes if we make condition on attribute if it not satisfied we make it as null then it immediately raises an error --
"""trigger on before insertion """

DELIMITER $
create trigger before_student_insertion before insert on Student 
for each row 
begin 
	if length(reg_id) < 12 then set reg_id = null
	if marks > 10 then set marks = null 	
end$
DELIMITER ; 

	
  
--creating triggers and procedures on Script table only ---

	
