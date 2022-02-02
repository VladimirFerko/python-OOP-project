CREATE TABLE "Student" (
	student_id 			SERIAL			PRIMARY KEY,
	student_name		VARCHAR(64)		NOT NULL,
	student_surname		VARCHAR(64)		NOT NULL,
	grade				INT				NOT NULL,
	id_course			INT				NULL,
	registered_date		TIMESTAMP		NULL
);

SELECT * FROM "Student"