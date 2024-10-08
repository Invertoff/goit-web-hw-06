SELECT AVG(gr.grade) AS avg_grade
FROM grades gr
JOIN subjects sb ON gr.subject_id = sb.id
WHERE sb.teacher_id = 1  -- Вкажіть конкретний teacher_id
AND gr.student_id = 1;  -- Вкажіть конкретний student_id
