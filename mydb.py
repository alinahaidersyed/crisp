import pymysql

try:
    # Connect to the MySQL server
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='password123'
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Create the 'crisp' database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS crisp")

    print("Database 'crisp' created successfully.")

except pymysql.Error as error:
    print("Error:", error)

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()