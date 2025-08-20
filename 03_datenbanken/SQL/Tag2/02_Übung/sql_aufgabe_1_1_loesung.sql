-- 1. Get all employees
select * from Employee;

-- 2. Display the first name and last name of all employees
SELECT First_name, Last_name from Employee;

-- 3. Display all the values of the “First_Name” column using the alias “Employee Name”
SELECT First_name as `Employee Name` from Employee;

-- 4. Get all “Last_Name”s in lowercase
SELECT LOWER(Last_name) from Employee;

-- 5. Get all “Last_Name”s in uppercase
SELECT UPPER(Last_name) from Employee;

-- 6. Get unique “DEPARTMENT”s (all Departments)
SELECT DISTINCT Departement from Employee;

-- 7. Get the first 4 characters of the “FIRST_NAME” column
SELECT SUBSTRING(First_name, 1, 4) as firstname from Employee;

-- 12. Get the employee’s first name after replacing ‘o’ with ‘#’
SELECT REPlACE(First_name, "o", "#") as firstname from Employee;

-- 13. Get the employee’s last name and first name in a single column separated by a ‘_’
SELECT CONCAT(First_name, "_", Last_name) as name from Employee;

-- 14. Get the year, month, and day from the “Joining_date” column
SELECT YEAR(Joining_date) as year, DAY(Joining_date) as day, MONTH(Joining_date) as month from Employee;

-- 15. Get all employees in ascending order by first name
SELECT * from Employee order by First_Name

-- 16. Get all employees in descending order by first name
SELECT * from Employee order by First_Name DESC

-- 17. Get all employees in ascending order by first name and descending order by salary
SELECT * from Employee order by First_Name, salary DESC

-- 18. Get employees whose first name is “Bob”
SELECT * from Employee WHERE first_name = "Bob"

-- 19. Get employees whose first name is “Bob” or “Alex”
SELECT * from Employee WHERE first_name = "Bob" or first_name = "Alex"


-- 21. Get all the details about employees whose first name begins with ‘B’
SELECT * from Employee WHERE first_name LIKE "B%"

-- 22. Get all the details about employees whose first name contains ‘o’
SELECT * from Employee WHERE first_name LIKE "%o%"

-- 23. Get all the details of the employees whose first name ends with ‘n’
SELECT * from Employee WHERE first_name LIKE "%n"

-- 26. Get all the details of employees whose salary is over 3,000,000
SELECT * from Employee WHERE salary > 3000000

-- 28. Get all the details about employees with a salary between 2,000,000 and 5,000,000
SELECT * from Employee WHERE salary >= 2000000 and salary <= 5000000
SELECT * from Employee WHERE salary Between 2000000 and 5000000

-- 30. Get all the details about employees whose joining year is “2019”
SELECT * from Employee where YEAR(Joining_date) = 2019

-- 31. Get all the details on employees whose participation month (Joining_date) is “January”
SELECT * from Employee where MONTH(Joining_date) = 1

-- 32. Get all the details of the employees who joined before March 1, 2019
SELECT * from Employee  where Joining_date < "2019-03-01"

-- 33. Get all the details on employees who joined after March 31, 2019
SELECT * from Employee  where Joining_date > "2019-03-31"

-- 38. Get the employee’s department and total salary, grouped by department
SELECT
    Department,
    SUM(salary) AS total_salary
FROM
    Employee
GROUP BY
    Department;

-- 39. Get the department and total salary, grouped by department, and sorted by total salary in descending order
SELECT
    Department,
    SUM(salary) AS total_salary
FROM
    Employee
GROUP BY
    Department
ORDER BY
    total_salary DESC;


-- 40. Get the department, the number of employees in that department, and the total salary grouped by department, and sorted by total salary in descending order
SELECT
    Department,
    COUNT(*) AS number_of_employees,
    SUM(salary) AS total_salary
FROM
    Employee
GROUP BY
    Department
ORDER BY
    total_salary DESC;

-- 41. Get the average salary by department in ascending order of salary
SELECT Departement, AVG(salary) as average_salary from Employee  group by Departement order by average_salary

-- 42. Get the maximum salary by department in ascending order of salary
SELECT Departement, MAX(salary) as max_salary from Employee  group by Departement order by max_salary

-- 44. Get the number of employees grouped by year and month of Joining_date
Select count(*) as anzahl, YEAR(Joining_date) as year, MONTH(Joining_date) as month from Employee group by year, month


