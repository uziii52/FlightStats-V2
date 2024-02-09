import mysql.connector
#import csv
import pandas as pd
from mysql.connector import Error
import matplotlib.pyplot as plt
from sqlFunctions import create_connection1, create_table1, create_table2, create_table3, create_table4, insert_data

#SQL USER CREATION
def create_connection2():
    """Create a database connection."""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='login_system',
            user='root',  
            password= '8913'  
        )
        if conn.is_connected():
            return conn
    except mysql.connector.Error as e:
        print(e)

def create_user(conn, username, password):
    """Create a new user in the users table."""
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        print("User created successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")

def verify_user(conn, username, password):
    """Verify user credentials."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()
        return result is not None
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return False



