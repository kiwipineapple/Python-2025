DROP Database IF EXISTS hospital_management;
CREATE DATABASE hospital_management;
USE hospital_management;

DROP TABLE IF EXISTS doctor;
DROP TABLE IF EXISTS hospital;

CREATE TABLE hospital (
	hospital_id INT PRIMARY KEY AUTO_INCREMENT,
    hospital_name VARCHAR(50),
    bed_count INT NOT NULL
);

CREATE TABLE doctor (
	doctor_id INT PRIMARY KEY,
    doctor_name VARCHAR(50),
    hospital_id INT NOT NULL,
    FOREIGN KEY (hospital_id) REFERENCES hospital(hospital_id) ON DELETE RESTRICT,
    joining_date DATE NOT NULL,
    speciality VARCHAR(50),
    salary INT NOT NULL,
    experience VARCHAR(50) DEFAULT NULL
);

INSERT INTO
	hospital
    (hospital_id, hospital_name, bed_count)
VALUES
	(1, 'Mayo Clinic', 200), 
	(2, 'Cleveland Clinic', 400), 
	(3, 'Johns Hopkins', 1000), 
	(4, 'UCLA Medical Center', 1500);
    
INSERT INTO 
	doctor
    (doctor_id, doctor_name, hospital_id, joining_date, speciality, salary, experience)
VALUES
	(101, 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL), 
	(102, 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL), 
	(103, 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL), 
	(104, 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', NULL), 
	(105, 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL), 
	(106, 'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL), 
	(107, 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL), 
	(108, 'Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL);
