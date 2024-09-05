-- This script lists all shows that do not have the genre Comedy
-- Shows are sorted in ascending order by their title

SELECT s.title
FROM tv_shows s
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id
LEFT JOIN tv_genres g ON sg.genre_id = g.id AND g.name = 'Comedy'
WHERE g.name IS NULL
ORDER BY s.title ASC;
