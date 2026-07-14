# Write your MySQL query statement below
(select Users.name as results
from Users join MovieRating
on Users.user_id = MovieRating.user_id
group by Users.user_id 
order by count(*) desc, Users.name asc
limit 1)

union all

(select Movies.title as results
from Movies join MovieRating
on Movies.movie_id = MovieRating.movie_id
where created_at > '2020-01-31' and created_at <= '2020-02-29'
group by Movies.movie_id
order by avg(MovieRating.rating) desc, Movies.title asc
limit 1)
