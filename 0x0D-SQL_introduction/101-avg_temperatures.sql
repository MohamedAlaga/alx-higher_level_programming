-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city , avg(value) as avg_temp FROM hbtn_0c_0.temperatures GROUP BY CITY ORDER BY avg_temp DESC;
