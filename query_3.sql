SELECT s.group_id, AVG(gr.grade) AS avg_grade
FROM grades gr
JOIN students s ON gr.student_id = s.id
WHERE gr.subject_id = 1  -- Вкажіть конкретний subject_id
GROUP BY s.group_id;
