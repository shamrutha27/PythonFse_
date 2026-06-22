import mysql.connector
import time

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Shamu@2711",
    database="college_db"
)

cursor = conn.cursor()

start = time.time()

cursor.execute("""
SELECT
e.enrollment_id,
s.first_name,
s.last_name,
e.grade
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

end = time.time()

print("Queries executed = 1")
print("Time =", end-start)

# N+1 Problem:
# One query retrieves all enrollments.
# Then N additional queries retrieve student names.
# Total queries = N+1.

# Sample Data:
# 11 enrollments
# Total queries = 12

# JOIN Solution:
# Retrieves all data using one query.
# Total queries = 1

# In a real application with 10000 enrollments:
# N+1 approach executes 10001 queries.
# JOIN approach executes only 1 query.

# N+1 is usually caused by ORM lazy loading.
# It can be fixed using eager loading (JOIN, select_related, joinedload).