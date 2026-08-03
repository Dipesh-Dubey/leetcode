# Write your MySQL query statement below
with cte as(
select Employee.name as Employee,Employee.salary as Salary,Department.name as Department,dense_rank() over(partition by departmentId order by salary desc) as rn
from Employee join Department
on Department.id = Employee.departmentId
)


select Department,Employee,Salary
from cte 
where rn = 1




