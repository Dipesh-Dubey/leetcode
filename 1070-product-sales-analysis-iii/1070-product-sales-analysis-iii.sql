# Write your MySQL query statement below
with t as (
    SELECT *,
           dense_rank() OVER (
               PARTITION BY product_id
               ORDER BY year
           ) AS rn
    FROM Sales
) 
SELECT product_id, year AS first_year, quantity, price
FROM t
WHERE rn = 1;

