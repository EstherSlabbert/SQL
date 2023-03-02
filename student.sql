CREATE TABLE Student (
  STU_NUM char(6),
  STU_SNAME varchar(15),
  STU_FNAME varchar(15),
  STU_INITIAL char(1),
  STU_STARTDATE date,
  COURSE_CODE char(3),
  PROJ_NUM int(2),
  PRIMARY KEY (STU_NUM)
);

INSERT INTO Student
VALUES (01, 'Snow', 'John', 'E', 05-Apr-2014, 201, 6);
INSERT INTO Student
VALUES (02, 'Stark', 'Arya', 'C', 12-Jul-17, 305, 11);

SELECT * FROM Student
WHERE COURSE_CODE = 305;

UPDATE Student
SET COURSE_CODE = 304
WHERE STU_NUM = 07;

DELETE FROM Student
WHERE STU_FNAME = 'Jamie' AND STU_SNAME = 'Lannister' AND STU_STARTDATE = 05-Sept-12 AND COURSE_CODE = 101 AND PROJ_NUM = 2;

UPDATE Student
SET PROJ_NUM = 14
WHERE STU_STARTDATE < 01-Jan-16 AND COURSE_CODE >= 201;

TRUNCATE TABLE Student;

DROP TABLE Student;