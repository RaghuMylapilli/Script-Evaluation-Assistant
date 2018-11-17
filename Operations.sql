--Creating trigger for before insert on Student tested --
create trigger before_student_insert before insert on Student
for each row 
begin
	if length(new.reg_id) < 12 then signal sqlstate '45000';
	end if;
	if new.email_id not like '%@%.%' then signal sqlstate '45001';
	end if;
	if new.dir not like '%/%' then signal sqlstate '34234';
	end if;
	if new.dob >= now() then signal sqlstate '23678' ;
	end if;
end;
--Creating trigger before insert on grade table tested--
create trigger before_grade_insert before insert on Grade
for each row
begin 
	if length(new.reg_id) < 12 then signal sqlstate '45231';
	end if;
	if new.grade > 15 then signal sqlstate '34257';
	end if;
	if new.date_of_grading != curdate() then signal sqlstate '56742';
	end if;
end;
--Creating avg marks function--
create function avg_marks(regid char(12))
returns float deterministic
begin
    declare avg_ float;
    select avg(grade) into avg_ from grade
    where reg_id = regid;
    return avg_;
end;
--Creating trigger after insert on grade table--
create trigger update_marks_insert after insert on Grade
for each row
begin
    update student
    set marks = avg_marks(new.reg_id)
    where reg_id = new.reg_id;
end;
--Creating trigger after update on Grade Table--
create trigger update_marks_update after update on Grade
for each row
begin
    if new.grade > 15 then signal sqlstate '34257';
	end if;
    update student
    set marks = avg_marks(new.reg_id)
    where reg_id = new.reg_id;
end;