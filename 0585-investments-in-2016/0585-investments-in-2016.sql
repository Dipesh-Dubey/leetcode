# Write your MySQL query statement below
with tnew as(
    SELECT *
    FROM Insurance
    WHERE (lat, lon) IN (
        SELECT lat, lon
        FROM Insurance
        GROUP BY lat, lon
        HAVING COUNT(*) = 1
    )
)

select round(sum(tiv_2016),2) as tiv_2016
from tnew
where tiv_2015 in (
    select tiv_2015
    from Insurance
    group by tiv_2015
    having count(tiv_2015) > 1
)
