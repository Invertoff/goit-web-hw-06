from faker import Faker
import random
from datetime import datetime
import sqlite3

# Підключення до бази даних
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# Увімкнення підтримки зовнішніх ключів
cursor.execute('PRAGMA foreign_keys = ON;')

# Створення таблиці груп
cursor.execute('''
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
''')

# Створення таблиці студентів із зовнішнім ключем до таблиці groups
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE CASCADE
);
''')

# Створення таблиці викладачів
cursor.execute('''
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
''')

# Створення таблиці предметів із зовнішнім ключем до таблиці teachers
cursor.execute('''
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id) ON DELETE SET NULL
);
''')

# Створення таблиці оцінок із зовнішніми ключами до таблиць students і subjects
cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    grade REAL,
    date TEXT,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
);
''')

# Збереження змін
conn.commit()

# Наповнення бази даних за допомогою Faker
fake = Faker()

# Додаємо групи
groups = ["Group A", "Group B", "Group C"]
for group in groups:
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (group,))

# Додаємо викладачів
teachers = [fake.name() for _ in range(5)]
for teacher in teachers:
    cursor.execute("INSERT INTO teachers (name) VALUES (?)", (teacher,))

# Додаємо предмети та прив'язуємо їх до викладачів
subjects = ["Math", "Physics", "Biology", "Chemistry", "History"]
for subject in subjects:
    teacher_id = random.randint(1, 5)
    cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject, teacher_id))

# Додаємо студентів та їх групи
for _ in range(50):
    name = fake.name()
    group_id = random.randint(1, 3)
    cursor.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))

# Додаємо студентам оцінки по предметам
for student_id in range(1, 51):
    for subject_id in range(1, 6):
        for _ in range(5):  # Додаємо 5 оцінок кожному студенту
            grade = random.uniform(60, 100)
            date = fake.date_this_year().strftime('%Y-%m-%d')
            cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                           (student_id, subject_id, grade, date))

# Збереження змін
conn.commit()

print("База даних створена та заповнена.")

# Приклад запиту для перегляду студентів з оцінками по групі та предмету
group_id = 1  # Задайте конкретний group_id
subject_id = 2  # Задайте конкретний subject_id

cursor.execute('''
SELECT s.name, gr.grade
FROM grades gr
JOIN students s ON gr.student_id = s.id
WHERE s.group_id = ? AND gr.subject_id = ?;
''', (group_id, subject_id))

results = cursor.fetchall()

print(f"\nРезультати для групи {group_id} і предмету {subject_id}:")
for row in results:
    print(f"Student: {row[0]}, Grade: {row[1]}")

# Закриття підключення
conn.close()
