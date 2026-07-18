# Write your MySQL query statement below
WITH tnew AS (
    SELECT
        customer_id,
        order_date,
        customer_pref_delivery_date,
        DENSE_RANK() OVER (
            PARTITION BY customer_id
            ORDER BY order_date
        ) AS rn
    FROM Delivery
)

SELECT
    round(sum(if(order_date = customer_pref_delivery_date,1,0))/count(*) * 100,2) as immediate_percentage
FROM tnew
WHERE rn = 1 


