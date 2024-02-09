import mysql.connector
#import csv
import pandas as pd
from mysql.connector import Error
import matplotlib.pyplot as plt


from google.cloud import bigquery
from google.oauth2 import service_account

#create connection with bigquerry
credentials = service_account.Credentials.from_service_account_file('C:/Users/azaan/OneDrive/Desktop/revature_project0 -/spherical-list-412116-9074ef0e6dfe.json') 
project_id = 'spherical-list-412116' 
client = bigquery.Client(credentials=credentials, project=project_id)

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
        print("-------------")
    except Error as e:
        print(e)

def create_table2(conn, table_name, columns2):
    """Create a table in the database."""
    try:
        cursor = conn.cursor()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns2})"
        cursor.execute(create_table_query)
        print("-------------")
    except Error as e:
        print(e)

def create_table3(conn, table_name, columns3):
    """Create a table in the database."""
    try:
        cursor = conn.cursor()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns3})"
        cursor.execute(create_table_query)
        print("-------------")
    except Error as e:
        print(e)

def create_table4(conn, table_name, columns4):
    """Create a table in the database."""
    try:
        cursor = conn.cursor()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns4})"
        cursor.execute(create_table_query)
        print("-------------")
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
        print("-------------")
    except Error as e:
        print(e)

def total_domestic_passengers_from_db(client, table_name):
    query = f"""
        SELECT SUM(Passengers_Domestic) as total_passengers
        FROM `spherical-list-412116.dataset_test.{table_name}`
    """
    results = client.query(query)
    
    for row in results:
        print(f"Total Domestic Passengers: {row['total_passengers']}")

def total_international_passengers_from_db(client, table_name):
    query = f"""
        SELECT SUM(Passengers_International) as total_passengers
        FROM `spherical-list-412116.dataset_test.{table_name}`
    """
    results = client.query(query)
    
    for row in results:
        print(f"Total Domestic Passengers: {row['total_passengers']}")

def highest_asm_domestic_from_db(client, table_name):
    query = f"""
        SELECT MAX(ASM_Domestic) as highest_asm_domestic
        FROM `spherical-list-412116.dataset_test.{table_name}`
    """
    results = client.query(query)
    
    for row in results:
        print(f"Highest ASM Domestic: {row['highest_asm_domestic']}")

def highest_asm_international_from_db(client, table_name):
    query = f"""
        SELECT MAX(ASM_International) as highest_asm_international
        FROM `spherical-list-412116.dataset_test.{table_name}`
    """
    results = client.query(query)
    
    for row in results:
        print(f"Highest ASM International: {row['highest_asm_international']}")

def highest_rpm_domestic_from_db(client, table_name):
    query = f"""
        SELECT MAX(RPM_Domestic) as highest_rpm_domestic
        FROM `spherical-list-412116.dataset_test.{table_name}`
    """
    results = client.query(query)
    
    for row in results:
        print(f"Highest RPM Domestic: {row['highest_rpm_domestic']}")

def highest_rpm_international_from_db(client, table_name):
    query = f"""
        SELECT MAX(RPM_International) as highest_rpm_international
        FROM `spherical-list-412116.dataset_test.{table_name}`
    """
    results = client.query(query)
    
    for row in results:
        print(f"Highest RPM International: {row['highest_rpm_international']}")