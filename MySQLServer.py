import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',         # Default MySQL username
            password=''          # Empty password, change if you have one
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if not exists (no SELECT or SHOW)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

            cursor.close()
            connection.close()

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

if __name__ == "__main__":
    create_database()
