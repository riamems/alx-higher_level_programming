-- 13-remove_records_score_less_than_or_equal_5.sql
-- Script to remove records with a score <= 5 in the table.

-- Remove records with a score <= 5
DELETE FROM `second_table`
WHERE `score` <= 5;
