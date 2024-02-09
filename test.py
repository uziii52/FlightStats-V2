import mysql.connector
#import csv
import pandas as pd
from mysql.connector import Error
import matplotlib.pyplot as plt



# SQL Functions
def create_connection1():
    """Create a database connection."""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='dataset_test',
            user='root',
            password='8913'
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(e)

def create_table1(conn, table_name, columns1):
    """Create a table in the database."""
    try:
        cursor = conn.cursor()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns1})"
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' created successfully.")
    except Error as e:
        print(e)

def create_table2(conn, table_name, columns2):
    """Create a table in the database."""
    try:
        cursor = conn.cursor()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns2})"
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' created successfully.")
    except Error as e:
        print(e)

def create_table3(conn, table_name, columns3):
    """Create a table in the database."""
    try:
        cursor = conn.cursor()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns3})"
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' created successfully.")
    except Error as e:
        print(e)

def create_table4(conn, table_name, columns4):
    """Create a table in the database."""
    try:
        cursor = conn.cursor()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns4})"
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' created successfully.")
    except Error as e:
        print(e)

def insert_data(conn, table_name, data):
    """Insert data into the table."""
    try:
        cursor = conn.cursor()
        for index, row in data.iterrows():
            # Replace NaN values with None (NULL in MySQL)
            row = row.where(pd.notna(row), None)

            # Use placeholders in the query to handle NULL values
            insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s']*len(row))})"
            cursor.execute(insert_query, tuple(row))
        conn.commit()
        print("Data inserted successfully.")
    except Error as e:
        print(e)

def total_domestic_passengers_from_db(conn, table_name):
    """Retrieve the total domestic passengers from the database."""
    try:
        cursor = conn.cursor()
        query = f"SELECT SUM(Passengers_Domestic) FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchone()
        total_passengers = result[0]
        print(f"Total domestic passengers: {total_passengers}")
    except Error as e:
        print(e)

def total_international_passengers_from_db(conn, table_name):
    """Retrieve the total domestic passengers from the database."""
    try:
        cursor = conn.cursor()
        query = f"SELECT SUM(Passengers_International) FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchone()
        total_passengers = result[0]
        print(f"Total international passengers: {total_passengers}")
    except Error as e:
        print(e)

def highest_asm_domestic_from_db(conn, table_name):
    """Retrieve the highest ASM (Airline Seat Mile) for domestic flights from the database."""
    try:
        cursor = conn.cursor()
        query = f"SELECT MAX(ASM_Domestic) FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchone()
        highest_asm_domestic = result[0]
        print(f"Highest ASM for Domestic flights: {highest_asm_domestic}")
    except Error as e:
        print(e)

def highest_asm_international_from_db(conn, table_name):
    """Retrieve the highest ASM (Airline Seat Mile) for international flights from the database."""
    try:
        cursor = conn.cursor()
        query = f"SELECT MAX(ASM_International) FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchone()
        highest_asm_international = result[0]
        print(f"Highest ASM for International flights: {highest_asm_international}")
    except Error as e:
        print(e)

def highest_rpm_domestic_from_db(conn, table_name):
    """Retrieve the highest ASM (Airline Seat Mile) for domestic flights from the database."""
    try:
        cursor = conn.cursor()
        query = f"SELECT MAX(RPM_Domestic) FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchone()
        highest_rpm_domestic = result[0]
        print(f"Highest RPM for Domestic flights: {highest_rpm_domestic}")
    except Error as e:
        print(e)

def highest_rpm_international_from_db(conn, table_name):
    """Retrieve the highest ASM (Airline Seat Mile) for international flights from the database."""
    try:
        cursor = conn.cursor()
        query = f"SELECT MAX(RPM_International) FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchone()
        highest_rpm_international = result[0]
        print(f"Highest ASM for International flights: {highest_rpm_international}")
    except Error as e:
        print(e)

#PLOTTING Function - matplotlib
def compare_passengers(conn, table_name):
    """Compare domestic and international passengers using a bar chart."""
    try:
        cursor = conn.cursor()

        # Query to get the sum of passengers for domestic and international flights
        query_domestic = f"SELECT SUM(Passengers_Domestic) FROM {table_name}"
        cursor.execute(query_domestic)
        result_domestic = cursor.fetchone()

        query_international = f"SELECT SUM(Passengers_International) FROM {table_name}"
        cursor.execute(query_international)
        result_international = cursor.fetchone()

        # Prepare data for plotting
        labels = ['Domestic', 'International']
        values = [result_domestic[0], result_international[0]]

        # Plotting the bar chart
        plt.bar(labels, values, color=['blue', 'green'])
        plt.title('Comparison of Passengers' )
        plt.xlabel('Flight Location')
        plt.ylabel('Total Passengers')
        plt.show()

    except Error as e:
        print(e)

def main1():
    conn = create_connection1()

    if conn is not None:
        csv_file_path1 = 'C:/Users/azaan/OneDrive/Desktop/revature_project0/AIrline DataSet/data/Alaska_Airlines/AS-BOS.csv' 
        csv_file_path2 = 'C:/Users/azaan/OneDrive/Desktop/revature_project0/AIrline DataSet/data/Delta_Airlines/DL-ATL.csv'
        csv_file_path3 = 'C:/Users/azaan/OneDrive/Desktop/revature_project0/AIrline DataSet/data/United_Airlines/UA-ORD.csv'
        csv_file_path4 = 'C:/Users/azaan/OneDrive/Desktop/revature_project0/AIrline DataSet/data/ExpressJet/EV-ATL.csv' # DATA SET CSV PATHS

        table_name1 = 'airline1'
        table_name2 = 'airline2'
        table_name3 = 'airline3'
        table_name4 = 'airline4'  #desired table name

        # Read CSV file into a DataFrame
        csv_data1 = pd.read_csv(csv_file_path1)
        csv_data2 = pd.read_csv(csv_file_path2)
        csv_data3 = pd.read_csv(csv_file_path3)
        csv_data4 = pd.read_csv(csv_file_path4)

        # Create a table1 in the database based on CSV columns
        columns1 = ', '.join([f'{col} VARCHAR(255)' for col in csv_data1.columns])
        create_table1(conn, table_name1, columns1)

        columns2 = ', '.join([f'{col} VARCHAR(255)' for col in csv_data2.columns])

        create_table2(conn, table_name2, columns2)

        columns3 = ', '.join([f'{col} VARCHAR(255)' for col in csv_data3.columns])

        create_table3(conn, table_name3, columns3)

        columns4 = ', '.join([f'{col} VARCHAR(255)' for col in csv_data4.columns])

        create_table4(conn, table_name4, columns4)





        # Insert data into the table
        insert_data(conn, table_name1, csv_data1)
        insert_data(conn, table_name2, csv_data2)
        insert_data(conn, table_name3, csv_data3)
        insert_data(conn, table_name4, csv_data4)


        # Close the database connection
        conn.close()


main1()

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

def main():
    conn = create_connection2()

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
                conn.close()

                conn = create_connection1()

                ''''# Load the dataset
                file_path1 = 'C:/Users/azaan/OneDrive/Desktop/revature_project0/AIrline DataSet/data/Alaska_Airlines/AS-BOS.csv'
                df1 = pd.read_csv(file_path1)

                file_path2 = 'C:/Users/azaan/OneDrive/Desktop/revature_project0/AIrline DataSet/data/Delta_Airlines/DL-ATL.csv'
                df2 = pd.read_csv(file_path2)

                file_path3 = 'C:/Users/azaan/OneDrive/Desktop/revature_project0/AIrline DataSet/data/United_Airlines/UA-ORD.csv'
                df3 = pd.read_csv(file_path3)

                file_path4 = 'C:/Users/azaan/OneDrive/Desktop/revature_project0/AIrline DataSet/data/ExpressJet/EV-ATL.csv'
                df4 = pd.read_csv(file_path4)

                # Display the first few rows of the dataframe to understand its structure
                print(df1.head(10))

                total_domestic_passengers1 = df1['Passengers_Domestic'].sum()
                total_international_passengers1 = df1['Passengers_International'].sum()'''


                def display_airline_options():
                    print("Airline Options:")
                    print("1) Alaska Airlines")
                    print("2) Delta Airlines")
                    print("3) United Airlines")
                    print("4) ExpressJet")

                def display_flight_options():
                    print("\nFlight Options:")
                    print("1) ASM - Airline Seat Mile")
                    print("2) RPM - Rate per Mile")
                    print("3) Total Passengers")
                    print("b) Go back")

                def display_location_options():
                    print("\nLocation Options:")
                    print("1) Domestic")
                    print("2) International")
                    print("b) Go back")

                # Main program
                while True:
                    display_airline_options()

                    airline_choice = input("\nChoose an airline (1-4, or 'q' to quit): ")
                    if airline_choice.lower() == 'q':
                        break

                    if airline_choice in ['1', '2', '3', '4']:
                        while True:
                            display_flight_options()
                            flight_choice = input("\nChoose a flight option (1-3, or 'b' to go back): ")

                            if flight_choice == 'b':
                                break

                            if flight_choice in ['1', '2', '3']:
                                while True:
                                    display_location_options()
                                    location_choice = input("\nChoose a location option (1-2, or 'b' to go back): ")

                                    if location_choice == 'b':
                                        break

                                    # Here you can perform calculations or actions based on the chosen options
                                    print(f"Processing data for {airline_choice}, Flight Option {flight_choice}, Location Option {location_choice}...")

                                    #Total Passenger Details
                                    if airline_choice == "1" and flight_choice == "3" and location_choice == "1":
                                        total_domestic_passengers_from_db(conn, 'airline1')
                                    elif airline_choice == "1" and flight_choice == "3" and location_choice == "2":
                                        total_international_passengers_from_db(conn, 'airline1')
                                        compare_passengers(conn, f'airline{airline_choice}')
                                        
                                    
                                    elif airline_choice == "2" and flight_choice == "3" and location_choice == "1":
                                        total_domestic_passengers_from_db(conn, 'airline2')
                                    elif airline_choice == "2" and flight_choice == "3" and location_choice == "2":
                                        total_international_passengers_from_db(conn, 'airline2')
                                        compare_passengers(conn, f'airline{airline_choice}')

                                    elif airline_choice == "3" and flight_choice == "3" and location_choice == "1":
                                        total_domestic_passengers_from_db(conn, 'airline3')
                                    elif airline_choice == "3" and flight_choice == "3" and location_choice == "2":
                                        total_international_passengers_from_db(conn, 'airline3')
                                        compare_passengers(conn, f'airline{airline_choice}')

                                    elif airline_choice == "4" and flight_choice == "3" and location_choice == "1":
                                        total_domestic_passengers_from_db(conn, 'airline4')
                                    elif airline_choice == "4" and flight_choice == "3" and location_choice == "2":
                                        total_international_passengers_from_db(conn, 'airline4')
                                        compare_passengers(conn, f'airline{airline_choice}')
                                    
                                    #ASM - Airline Seat Mile Highest
                                    elif airline_choice == "1" and flight_choice == "1" and location_choice == "1":
                                        highest_asm_domestic_from_db(conn, 'airline1')
                                    elif airline_choice == "1" and flight_choice == "1" and location_choice == "2":
                                        highest_asm_international_from_db(conn, 'airline1')

                                    elif airline_choice == "2" and flight_choice == "1" and location_choice == "1":
                                        highest_asm_domestic_from_db(conn, 'airline2')
                                    elif airline_choice == "2" and flight_choice == "1" and location_choice == "2":
                                        highest_asm_international_from_db(conn, 'airline2')

                                    elif airline_choice == "3" and flight_choice == "1" and location_choice == "1":
                                        highest_asm_domestic_from_db(conn, 'airline3')
                                    elif airline_choice == "3" and flight_choice == "1" and location_choice == "2":
                                        highest_asm_international_from_db(conn, 'airline3')

                                    elif airline_choice == "4" and flight_choice == "1" and location_choice == "1":
                                        highest_asm_domestic_from_db(conn, 'airline4')
                                    elif airline_choice == "4" and flight_choice == "1" and location_choice == "2":
                                        highest_asm_international_from_db(conn, 'airline4')

                                    #RPM - Rate Per Mile Highest
                                    elif airline_choice == "1" and flight_choice == "2" and location_choice == "1":
                                        highest_rpm_domestic_from_db(conn, 'airline1')
                                    elif airline_choice == "1" and flight_choice == "2" and location_choice == "2":
                                        highest_rpm_international_from_db(conn, 'airline1')

                                    elif airline_choice == "2" and flight_choice == "2" and location_choice == "1":
                                        highest_rpm_domestic_from_db(conn, 'airline2')
                                    elif airline_choice == "2" and flight_choice == "2" and location_choice == "2":
                                        highest_rpm_international_from_db(conn, 'airline2')

                                    elif airline_choice == "3" and flight_choice == "2" and location_choice == "1":
                                        highest_rpm_domestic_from_db(conn, 'airline3')
                                    elif airline_choice == "3" and flight_choice == "2" and location_choice == "2":
                                        highest_rpm_international_from_db(conn, 'airline3')

                                    elif airline_choice == "4" and flight_choice == "2" and location_choice == "1":
                                        highest_rpm_domestic_from_db(conn, 'airline4')
                                    elif airline_choice == "4" and flight_choice == "2" and location_choice == "2":
                                        highest_rpm_international_from_db(conn, 'airline4')
                                    
                                    
                            else:
                                print("Invalid flight option. Please choose again.")
                    else:
                        print("Invalid airline choice. Please choose again.")
            else:
                print("Login failed. Incorrect username or password.")

        elif choice == '3':
            conn.close()
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


main()


