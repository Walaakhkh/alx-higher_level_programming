-- This script lists all shows and all genres linked to that show
-- Shows without genres will display NULL in the genre column
-- Results are sorted by show title and genre name

-- Select show titles and genre names
SELECT s.title, g.name
FROM tv_shows s
-- Left join with tv_show_genres to include all shows, even those without genres
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id
-- Left join with tv_genres to get the genre names
LEFT JOIN tv_genres g ON sg.genre_id = g.id
-- Sort by show title and genre name
ORDER BY s.title ASC, g.name ASC;
