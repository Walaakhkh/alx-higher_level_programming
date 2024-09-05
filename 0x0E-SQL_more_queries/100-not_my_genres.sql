-- This script lists all genres that are not linked to the show Dexter
-- Genres are sorted in ascending order by genre name

-- Subquery to find the genre IDs linked to Dexter
SELECT g.name
FROM tv_genres g
LEFT JOIN tv_show_genres sg ON g.id = sg.genre_id
LEFT JOIN tv_shows s ON sg.show_id = s.id AND s.title = 'Dexter'
WHERE s.title IS NULL
ORDER BY g.name ASC;
