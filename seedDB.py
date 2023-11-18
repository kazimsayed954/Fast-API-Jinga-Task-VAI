import mysql.connector

def seed_database():
    # Connect to MySQL server
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"  # Replace with your MySQL password
    )

    # Create a database if it doesn't exist
    db_cursor = db_connection.cursor()
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS test1_vactic_assessment")
    db_cursor.close()

    # Connect to the created database
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",  # Replace with your MySQL password
        database="test1_vactic_assessment"
    )

    # Create 'users' table if it doesn't exist
    table_cursor = db_connection.cursor()
    table_cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)
    table_cursor.close()

    # Insert initial data into the 'users' table
    initial_users = [
        ("admin", "admin"),
        ("test", "test"),
        # Add more users as needed
    ]

    insert_cursor = db_connection.cursor()
    insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    insert_cursor.executemany(insert_query, initial_users)
    db_connection.commit()
    insert_cursor.close()

    db_connection.close()

if __name__ == "__main__":
    seed_database()
