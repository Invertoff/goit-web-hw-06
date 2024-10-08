SELECT student_id, AVG(grade) AS avg_grade
FROM grades
WHERE subject_id = 1  -- Вкажіть конкретний subject_id
GROUP BY student_id
ORDER BY avg_grade DESC
LIMIT 1;
