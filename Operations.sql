--Creating trigger for before insert on Student tested --
create trigger before_student_insert before insert on Student
for each row 
begin
	if length(new.reg_id) < 12 then signal sqlstate '45000';
	end if;
	if new.email_id not like '%@%' then signal sqlstate '45001';
	end if;
	if new.dir not like '%/%' then signal sqlstate '34234';
	end if;
	if new.dob >= now() then signal sqlstate '23678' ;
	end if;
end;
-- Creating trigger for audit insert tested --
create trigger before_student_update before update on Student 
for each row 
begin 
	insert into Student_audit
    	set reg_id = old.reg_id,
       		 name = old.name,
		dob = old.dob,
		email_id = old.email_id,
		dir = old.dir,
		marks = old.marks,
		action = 'before update',							
        time_of_change = timestamp(now()); 
end;
-- Creting trigger for audit insert tested--
create trigger after_student_update after update on Student 
for each row 
begin 
	insert into Student_audit
    	set reg_id = old.reg_id,
         	 name = new.name,
		dob = old.dob,
		email_id = old.email_id,
		dir = old.dir,
		marks = new.marks,
		action = 'after update',
        time_of_change = timestamp(now()); 
end;
-- Creating trigger for audit insert tested --
create trigger after_student_delete after delete on Student 
for each row 
begin 
	insert into Student_audit
    	set reg_id = old.reg_id,
      	        name = old.name,
		dob = old.dob,
		email_id = old.email_id,
		dir = old.dir,
		marks = old.marks,
		action = 'delete',
        time_of_change = timestamp(now()); 
end;
-- Creating after trigger tested --
create trigger after_student_insertion after insert on Student 
for each row 
begin 
	insert into Student_audit
	set reg_id = new.reg_id,
		name = new.name,
		dob = new.dob,
		email_id = new.email_id,
		dir = new.dir,
	        marks = new.marks,
		action = 'insertion',
	time_of_change = timestamp(now());
end;
--Creating trigger before insert on grade table tested--
create trigger before_grade_insert before insert on Grade
for each row
begin 
	if length(new.reg_id) < 12 then signal sqlstate '45231';
	end if;
	if new.grade > 10 then signal sqlstate '34257';
	end if;
	if new.date_of_grading != curdate() then signal sqlstate '56742';
	end if;
end;
--Creating trigger after insert on grade table tested--
create trigger after_grade_insert after insert on Grade
for each row
begin
	insert into Grade_audit
	set reg_id = new.reg_id,
	script_id = new.script_id,
	grade = new.grade,
	date_of_grading = new.date_of_grading,
	action = 'insertion',
	time_of_change = timestamp(now());
end;
--Creating trigger after update on Grade Table tested--
create trigger after_grade_update after update on Grade
for each row
begin
	insert into Grade_audit
	set reg_id = old.reg_id,
	script_id = old.script_id,
	grade = new.grade,
	date_of_grading = new.date_of_grading,
	action = 'after update',
	time_of_change = timestamp(now());
end;
--Creating trigger before update on Grade Table tested--
create trigger before_grade_update before update on Grade
for each row
begin
	insert into Grade_audit
	set reg_id = old.reg_id,
	script_id = old.script_id,
	grade = old.grade,
	date_of_grading = old.date_of_grading,
	action = 'before update',
	time_of_change = timestamp(now());
end;
--Creating trigger for deletion on Grade Table tested--
create trigger delete_grade after delete on Grade
for each row
begin
	insert into Grade_audit
	set reg_id = old.reg_id,
	script_id = old.script_id,
	grade = old.grade,
	date_of_grading = old.date_of_grading,
	action = 'delete',
	time_of_change = timestamp(now());
end;