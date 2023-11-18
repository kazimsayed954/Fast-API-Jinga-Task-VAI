# models.py
import mysql.connector

class Database:
    @staticmethod
    def get_db_connection():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="test1_vactic_assesment"
        )

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def get_user_by_credentials(username, password):
        db = Database.get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            return User(user[0], user[1])  # Assuming user[0] is username and user[1] is password
        return None

    def save_to_db(self):
        db = Database.get_db_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (self.username, self.password))
        db.commit()
        cursor.close()

    @staticmethod
    def get_all_users():
        db = Database.get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT username, password FROM users")
        user_list = [User(username, password) for (username, password) in cursor]
        cursor.close()
        db.close()  # Close the database connection
        return user_list

