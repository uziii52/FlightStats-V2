from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('C:/Users/azaan/OneDrive/Desktop/revature_project0 -/spherical-list-412116-9074ef0e6dfe.json') 

project_id = 'spherical-list-412116' 
client = bigquery.Client(credentials= credentials,project=project_id)

query = client.query(
   """SELECT * FROM `spherical-list-412116.dataset_test.airline2` LIMIT 1000"""
  )
results = query.result()

# Print the results
for row in results:
    print(row)