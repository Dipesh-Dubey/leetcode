# Write your MySQL query statement below
select Prices.product_id,round(
    ifnull(sum(price*units)/sum(units),0),2) as average_price
from Prices left join UnitsSold
on Prices.product_id = UnitsSold.product_id 
and Prices.start_date<=UnitsSold.purchase_date and UnitsSold.purchase_date<=Prices.end_date 
group by Prices.product_id  #groupby,having moves accross first element of group
