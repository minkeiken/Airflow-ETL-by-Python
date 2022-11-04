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

finally , with dag_task_grp.py, to declare a DAG and define some properties. First it is the schedule interval, we will set this to nine AM, with a Cron expression. Then we define a start date, when this schedule should start, and we will set the catchup to false. Last, we set a tag for this DAG. Tag helps you group together multiple DAGs, and you can use it to filter DAGs from the UI.

Under Dag we define TaskGroups to call our tasks. We group the related tasks under one group. We set the dependency between tasks and the define the order in which they should run. We will see the visual representation in the UI. Finally, We define the order of the TaskGroups and in which order Airflow should execute them. Once saved the completed DAG will appear in the Airflow UI. You will have to enable it to take effect. This is how we automate our ETL pipeline with Airflow.
