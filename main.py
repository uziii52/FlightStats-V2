from google.cloud import bigquery
from google.oauth2 import service_account

#create connection with bigquerry
credentials = service_account.Credentials.from_service_account_file('C:/Users/azaan/OneDrive/Desktop/revature_project0 -/spherical-list-412116-9074ef0e6dfe.json') 
project_id = 'spherical-list-412116' 
client = bigquery.Client(credentials=credentials, project=project_id)

import pandas as pd
from mysql.connector import Error
import matplotlib.pyplot as plt
from matplotlibfunc import compare_passengers
from sqlFunctions import create_connection1, create_table1, create_table2, create_table3, create_table4, insert_data, total_domestic_passengers_from_db,total_international_passengers_from_db,highest_asm_domestic_from_db,highest_asm_international_from_db,highest_rpm_domestic_from_db,highest_rpm_international_from_db
from sqlUserCreation import create_connection1,create_connection2, create_user, verify_user
import sqlDataImport
import matplotlibfunc
import sqlUserCreation
import sqlFunctions

sqlDataImport
matplotlibfunc
sqlUserCreation
sqlFunctions



#DASHBOARD WITH MAIN PROGRAM
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
                                        total_domestic_passengers_from_db(client, 'airline1')
                                    elif airline_choice == "1" and flight_choice == "3" and location_choice == "2":
                                        total_international_passengers_from_db(client, 'airline1')
                                        compare_passengers(conn, f'airline{airline_choice}')
                                        
                                    
                                    elif airline_choice == "2" and flight_choice == "3" and location_choice == "1":
                                        total_domestic_passengers_from_db(client, 'airline2')
                                    elif airline_choice == "2" and flight_choice == "3" and location_choice == "2":
                                        total_international_passengers_from_db(client, 'airline2')
                                        compare_passengers(conn, f'airline{airline_choice}')

                                    elif airline_choice == "3" and flight_choice == "3" and location_choice == "1":
                                        total_domestic_passengers_from_db(client, 'airline3')
                                    elif airline_choice == "3" and flight_choice == "3" and location_choice == "2":
                                        total_international_passengers_from_db(client, 'airline3')
                                        compare_passengers(conn, f'airline{airline_choice}')

                                    elif airline_choice == "4" and flight_choice == "3" and location_choice == "1":
                                        total_domestic_passengers_from_db(client, 'airline4')
                                    elif airline_choice == "4" and flight_choice == "3" and location_choice == "2":
                                        total_international_passengers_from_db(client, 'airline4')
                                        compare_passengers(conn, f'airline{airline_choice}')
                                    
                                    #ASM - Airline Seat Mile Highest
                                    elif airline_choice == "1" and flight_choice == "1" and location_choice == "1":
                                        highest_asm_domestic_from_db(client, 'airline1')
                                    elif airline_choice == "1" and flight_choice == "1" and location_choice == "2":
                                        highest_asm_international_from_db(client, 'airline1')

                                    elif airline_choice == "2" and flight_choice == "1" and location_choice == "1":
                                        highest_asm_domestic_from_db(client, 'airline2')
                                    elif airline_choice == "2" and flight_choice == "1" and location_choice == "2":
                                        highest_asm_international_from_db(client, 'airline2')

                                    elif airline_choice == "3" and flight_choice == "1" and location_choice == "1":
                                        highest_asm_domestic_from_db(client, 'airline3')
                                    elif airline_choice == "3" and flight_choice == "1" and location_choice == "2":
                                        highest_asm_international_from_db(client, 'airline3')

                                    elif airline_choice == "4" and flight_choice == "1" and location_choice == "1":
                                        highest_asm_domestic_from_db(client, 'airline4')
                                    elif airline_choice == "4" and flight_choice == "1" and location_choice == "2":
                                        highest_asm_international_from_db(client, 'airline4')

                                    #RPM - Rate Per Mile Highest
                                    elif airline_choice == "1" and flight_choice == "2" and location_choice == "1":
                                        highest_rpm_domestic_from_db(client, 'airline1')
                                    elif airline_choice == "1" and flight_choice == "2" and location_choice == "2":
                                        highest_rpm_international_from_db(client, 'airline1')

                                    elif airline_choice == "2" and flight_choice == "2" and location_choice == "1":
                                        highest_rpm_domestic_from_db(client, 'airline2')
                                    elif airline_choice == "2" and flight_choice == "2" and location_choice == "2":
                                        highest_rpm_international_from_db(client, 'airline2')

                                    elif airline_choice == "3" and flight_choice == "2" and location_choice == "1":
                                        highest_rpm_domestic_from_db(client, 'airline3')
                                    elif airline_choice == "3" and flight_choice == "2" and location_choice == "2":
                                        highest_rpm_international_from_db(client, 'airline3')

                                    elif airline_choice == "4" and flight_choice == "2" and location_choice == "1":
                                        highest_rpm_domestic_from_db(client, 'airline4')
                                    elif airline_choice == "4" and flight_choice == "2" and location_choice == "2":
                                        highest_rpm_international_from_db(client, 'airline4')
                                    
                                    
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