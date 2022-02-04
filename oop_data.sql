CREATE TABLE "Student" (
	student_id 			SERIAL			PRIMARY KEY,
	student_name		VARCHAR(64)		NOT NULL,
	student_surname		VARCHAR(64)		NOT NULL,
	grade				INT				NOT NULL,
	id_course			INT				NULL,
	registered_date		TIMESTAMP		NULL
);

CREATE TABLE "Professor"(
	professor_id		SERIAL			PRIMARY KEY,
	professor_degree	VARCHAR(10)		NULL,
	professor_name		VARCHAR(64)		NOT NULL,
	professor_surname	VARCHAR(64)		NOT NULL
);

SELECT * FROM "Student"