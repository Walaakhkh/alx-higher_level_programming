-- List namba yema of records with same_score in 'second_table'
SELECT score, COUNT(1) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
