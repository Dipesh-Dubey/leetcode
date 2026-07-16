# Write your MySQL query statement below
with tnew as(
    select *
    from Orders
    where order_date>'2020-01-31' and order_date<'2020-03-01'
)

select product_name, sum(tnew.unit) as unit    
from Products join tnew
on Products.product_id = tnew.product_id
group by tnew.product_id
having sum(tnew.unit) >= 100
