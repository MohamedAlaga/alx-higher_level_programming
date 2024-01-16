-- Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city,avg(value) AS avg_temp FROM hbtn_0c_0.temperatures WHERE month = 8 OR month = 7 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
