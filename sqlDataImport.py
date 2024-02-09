import mysql.connector
#import csv
import pandas as pd
from mysql.connector import Error
import matplotlib.pyplot as plt
from sqlFunctions import create_connection1, create_table1, create_table2, create_table3, create_table4, insert_data

#SQL DATA IMPORT
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