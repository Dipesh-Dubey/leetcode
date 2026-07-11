# Write your MySQL query statement below
with t1 as(select *,count(managerId)
from Employee
group by managerId
having count(*) >= 5)

select Employee.name
from Employee join t1
on Employee.id = t1.managerId