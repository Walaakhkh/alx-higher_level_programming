-- This script lists all genres associated with the show "Dexter"
-- The results are sorted in ascending order by genre name.

-- Select genre names from the tv_genres table
SELECT g.name
FROM tv_genres g
-- Join with tv_show_genres to get the genre IDs linked to shows
JOIN tv_show_genres sg ON g.id = sg.genre_id
-- Join with tv_shows to filter by the show title "Dexter"
JOIN tv_shows s ON sg.show_id = s.id
-- Filter for the specific show "Dexter"
WHERE s.title = 'Dexter'
-- Sort genres by name in ascending order
ORDER BY g.name ASC;
