# Airflow-ETL-by-Python

with load_src_data.py
We use the task decorator to define our tasks in Airflow. We get the connection details for the Postgres with the Basehook.

1. grab the tables we want to extract data from SQL Server’s system schema. Simply loop through the tables and query them. 
2. queried the source and obtained data as Pandas dataframe. then store this data to Postgres tables. 
3. call the to_sql function and prefix the table name with “src” to indicate that this is a source table.
