-- TABLE SCHOOLS IS ONE ITEM FROM ARRAY FOR SCHOOLS

CREATE TABLE "Schools"(
	school_id			INT						NOT NULL,
	school_name 		VARCHAR(64)				NOT NULL,
	school_adress		VARCHAR(64)		UNIQUE	NOT NULL,
	CONSTRAINT "school_pk"	PRIMARY KEY  ("school_id")
);

-- COURSES TABLE IS ONE ITEM FROM SCHOOL.COURSES LIST

CREATE TABLE "Courses"(
	id_course				INT				NOT NULL,
	course_name				VARCHAR(64)		NOT NULL,
	course_specification	VARCHAR(64)		NOT NULL,
	school_id				INT				NOT NULL,
	left_space 				INT				NOT NULL,
	CONSTRAINT school_fk	FOREIGN KEY	 (school_id) REFERENCES "Schools" (school_id),
	CONSTRAINT "course_pk"	PRIMARY KEY  ("id_course")
);

CREATE TABLE "Professors"(
	id_professor			INT				NOT NULL,
	professor_degree		VARCHAR(5)		NULL,
	professor_name			VARCHAR(24)		NOT NULL,
	professor_surname		VARCHAR(24)		NOT NULL,
	id_course				INT 			NOT NULL,
	school_id				INT				NOT NULL,
	CONSTRAINT "professor_pk"	PRIMARY KEY  ("id_professor"),
	CONSTRAINT course_fk	FOREIGN KEY (id_course) REFERENCES "Courses" (id_course),
	CONSTRAINT school_fk1	FOREIGN KEY (school_id) REFERENCES "Schools" (school_id)
);

CREATE TABLE "Students"(
	student_id 			INT				NOT NULL,
	student_name 		VARCHAR(64)		NOT NULL,
	student_surname		VARCHAR(64)		NOT NULL,
	student_grade 		INT 			NOT NULL,
	id_course			INT				NOT NULL,
	school_id			INT				NOT NULL,
	CONSTRAINT student_pk	PRIMARY KEY (student_id),
	CONSTRAINT student_fk 	FOREIGN KEY (id_course) REFERENCES "Courses"(id_course),
	CONSTRAINT school_fk2	FOREIGN KEY (school_id) REFERENCES "Schools" (school_id)
);

-- TESTING INSERTS

INSERT INTO "Schools" (school_id, school_name, school_adress) VALUES (1 ,'elektrotechnicka', 'presov')
INSERT INTO "Schools" (school_id, school_name, school_adress) VALUES (2 ,'strojnicka', 'bardejov')

INSERT INTO "Courses" (id_course, course_name, course_specification, school_id, left_space) VALUES (1, 'coding', 'python', 1, 5)

INSERT INTO "Professors" (id_professor, professor_degree, professor_name, professor_surname, id_course, school_id) VALUES (1, 'Ing.', 'Jan', 'Vavrek', 1, 1)

INSERT INTO "Students" (student_id, student_name, student_surname, student_grade, id_course, school_id) VALUES (1, 'Vladimir', 'Ferko', 1, 1, 1)

-- selecting to check results

SELECT * FROM "Schools"

SELECT * FROM "Courses"

SELECT * FROM "Professors"

SELECT * FROM "Students"

-- joins to run in python code

SELECT school_name, school_adress, course_name, course_specification, left_space, professor_degree, professor_name, professor_surname
FROM "Schools"
INNER JOIN "Courses"
ON "Schools".school_id = "Courses".school_id
INNER JOIN "Professors"
ON "Courses".school_id = "Professors".school_id

SELECT professor_degree, professor_name, professor_surname, course_name
            FROM "Professors"
            INNER JOIN "Courses"
            ON "Professors".id_course = "Courses".id_course
            WHERE "Professors".school_id = 1

-- deleting data
DELETE FROM "Schools"


-- dropping all tables
	
DROP TABLE "Courses", "Schools", "Professors","Students"