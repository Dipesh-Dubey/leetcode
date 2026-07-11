# Write your MySQL query statement below
 
SELECT machine_id,ROUND(
           AVG(IF(activity_type='end', timestamp, NULL)) - AVG(IF(activity_type='start', timestamp, NULL)),3) as processing_time
FROM Activity
GROUP BY machine_id;