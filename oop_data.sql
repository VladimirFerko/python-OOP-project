-- TABLE SCHOOLS IS ONE ITEM FROM ARRAY FOR SCHOOLS

CREATE TABLE "Schools"(
	school_id			INT				NOT NULL,
	school_name 		VARCHAR(64)		NOT NULL,
	school_adress		VARCHAR(64)		NOT NULL,
	CONSTRAINT "school_id"	PRIMARY KEY  ("school_id")
);

-- COURSES TABLE IS ONE ITEM FROM SCHOOL.COURSES LIST

CREATE TABLE "Courses"(
	id_course				SERIAL			NOT NULL,
	course_name				VARCHAR(64)		NOT NULL,
	course_specification	VARCHAR(64)		NOT NULL,
	school_id				INT				NOT NULL,
	CONSTRAINT school_fk	FOREIGN KEY	 (school_id) REFERENCES "Schools" (school_id)
);

INSERT INTO "Schools" (school_id, school_name, school_adress) VALUES (1 ,'elektrotechnicka', 'presov')
INSERT INTO "Courses" (course_name, course_specification, school_id) VALUES ('coding', 'python', 1)

SELECT * FROM "Schools"
INNER JOIN "Courses"
	ON "Schools".school_id = "Courses".school_id