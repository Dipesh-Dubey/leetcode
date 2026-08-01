# Write your MySQL query statement below
with cte as(
    select product_id,new_price,change_date,row_number() over(partition by product_id order by change_date desc) as rn
    from Products
    where change_date <= '2019-08-16'
)

select distinct(product_id),new_price as price
from cte
where rn = 1

union

select distinct(product_id),10
from Products
where Products.product_id not in (select product_id from cte)
