-- 11-list_records_score_greater_than_or_equal_10.sql
-- Script to list records with a score >= 10 in the table.

-- List records with a score >= 10, ordered by score (top first)
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
