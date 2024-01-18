-- 12-update_bob_score.sql
-- Script to update the score of Bob to 10 in the table

-- Update the score of Bob to 10
UPDATE `second_table`
SET `score` = 10
WHERE `name` = "Bob";
