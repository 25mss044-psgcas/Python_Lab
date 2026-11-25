import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="college_db"
    )

    if conn.is_connected():
        print("Connected to MySQL database successfully.")
        cursor = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            id INT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            department VARCHAR(50)
        )
        """

        cursor.execute(create_table_query)
        print("Table 'students' created successfully.")

except mysql.connector.Error as err:
    print(f"Database Error: {err}")

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection closed.")