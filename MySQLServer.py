import mysql.connector

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',       # Update with your MySQL username
            password=''        # Update with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

            cursor.close()
            connection.close()

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

if __name__ == "__main__":
    create_database()
