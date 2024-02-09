import mysql.connector

def create_connection():
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

def main():
    conn = create_connection()

    while True:
        print("1. Create New User\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            create_user(conn, username, password)

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if verify_user(conn, username, password):
                print("Login successful!")
            else:
                print("Login failed. Incorrect username or password.")

        elif choice == '3':
            conn.close()
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


main()