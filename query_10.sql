SELECT sb.name
FROM grades gr
JOIN subjects sb ON gr.subject_id = sb.id
WHERE gr.student_id = 1  -- Вкажіть конкретний student_id
AND sb.teacher_id = 1;  -- Вкажіть конкретний teacher_id
