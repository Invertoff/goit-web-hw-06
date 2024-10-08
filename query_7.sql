SELECT s.name, gr.grade
FROM grades gr
JOIN students s ON gr.student_id = s.id
WHERE s.group_id = 1  -- Вкажіть конкретний group_id
AND gr.subject_id = 1;  -- Вкажіть конкретний subject_id
