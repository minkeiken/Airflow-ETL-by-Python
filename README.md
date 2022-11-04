# Airflow-ETL-by-Python

with load_src_data.py to Extract:
We use the task decorator to define our tasks in Airflow. We get the connection details for the Postgres with the Basehook.

1. grab the tables we want to extract data from SQL Server’s system schema. Simply loop through the tables and query them. 
2. queried the source and obtained data as Pandas dataframe. then store this data to Postgres tables. 
3. call the to_sql function and prefix the table name with “src” to indicate that this is a source table.

with extract_src_products.py to Transform:
To transform the product tables, we will query the source table from postgres into a dataframe. We will use pandas to implement transformations.

1.  remove any unnecessary columns, by inputting the list of columns we want to keep into a new dataframe called revised. For null values in numeric columns, let’s replace them with zeros and for missing values in string columns, let’s put “NA” instead.
2. rename the columns where the column names contain English. We have finished all the transformations, so let’s save this to a staging table using the `to_sql()` function.
3. perform similar operations on Product Subcategory and Product Category tables. Drop the unwanted columns and rename a few columns,
4.  save the updates to tables with “src” prefix.

with prdProduct_model.py, to build the final product model, we will query all three tables. There is data type mismatch so will convert the column to integer.

Then, we merge the three DataFrames into a single dataframe and save it into a table with the “prd” prefix.
