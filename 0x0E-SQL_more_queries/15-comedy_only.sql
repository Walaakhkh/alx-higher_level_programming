-- This script lists all Comedy shows in the database
-- Results are sorted in ascending order by show title

-- Select show titles from tv_shows table
SELECT s.title
FROM tv_shows s
-- Join with tv_show_genres to get genre IDs for each show
JOIN tv_show_genres sg ON s.id = sg.show_id
-- Join with tv_genres to filter for Comedy genre
JOIN tv_genres g ON sg.genre_id = g.id
-- Filter by the genre name "Comedy"
WHERE g.name = 'Comedy'
-- Sort by show title in ascending order
ORDER BY s.title ASC;
