import mysql.connector
import time

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Shamu@2711",
    database="college_db"
)

cursor = conn.cursor()

query_count = 1

start = time.time()

# Query 1
cursor.execute("SELECT * FROM enrollments")
enrollments = cursor.fetchall()

for row in enrollments:
    student_id = row[1]

    cursor.execute(
        "SELECT first_name,last_name FROM students WHERE student_id=%s",
        (student_id,)
    )

    name = cursor.fetchone()

    print(name)

    query_count += 1

end = time.time()

print("Queries executed =", query_count)
print("Time =", end-start)