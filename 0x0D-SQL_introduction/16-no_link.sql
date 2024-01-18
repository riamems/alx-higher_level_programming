-- 16-list_records_with_names.sql
-- Script to list all records with a name value.

-- List all records with a name value, ordered by descending score
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
