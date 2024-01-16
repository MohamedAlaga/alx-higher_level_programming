-- script that lists the number of records with the same score in the table second_table
SELECT SCORE,COUNT(SCORE) AS number FROM second_table GROUP BY SCORE ORDER BY SCORE DESC;
