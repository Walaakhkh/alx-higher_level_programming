-- This script lists all genres and the number of shows linked to each genre.
-- Results are sorted in descending order by the number of shows linked.

-- Select genre name and count of shows linked to that genre
SELECT g.name AS genre, 
       COUNT(sg.show_id) AS number_of_shows
FROM tv_genres g
-- Join with tv_show_genres to link genres with shows
LEFT JOIN tv_show_genres sg ON g.id = sg.genre_id
-- Group results by genre name
GROUP BY g.name
-- Exclude genres with no shows linked
HAVING number_of_shows > 0
-- Sort by the number of shows in descending order
ORDER BY number_of_shows DESC;
