import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)
cursor = conn.cursor()

insert_query = "INSERT INTO students (id, name, department) VALUES (%s, %s, %s)"
records = [(1, "Arjun", "CSE"), (2, "Divya", "ECE")]
cursor.executemany(insert_query, records)
conn.commit()
print(f"{cursor.rowcount} records inserted.")

print("\n--- Records After Insert ---")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

update_query = "UPDATE students SET department = %s WHERE id = %s"
cursor.execute(update_query, ("AI & DS", 1))
conn.commit()
print("\nRecord ID 1 updated.")

delete_query = "DELETE FROM students WHERE id = %s"
cursor.execute(delete_query, (2,))
conn.commit()
print("Record ID 2 deleted.")

print("\n--- Final Table Records ---")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()