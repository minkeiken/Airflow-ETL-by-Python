@task()
def transform_srcProduct():
    conn = BaseHook.get_connection('postgres')
    engine = create_engine(f'postgresql://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}')
    pdf = pd.read_sql_query('SELECT * FROM public."src_DimProduct" ', engine)
    #drop columns
    revised = pdf[['ProductKey', 'ProductAlternateKey', 'ProductSubcategoryKey','WeightUnitMeasureCode', 'SizeUnitMeasureCode', 'EnglishProductName',
                   'StandardCost','FinishedGoodsFlag', 'Color', 'SafetyStockLevel', 'ReorderPoint','ListPrice', 'Size', 'SizeRange', 'Weight',
                   'DaysToManufacture','ProductLine', 'DealerPrice', 'Class', 'Style', 'ModelName', 'EnglishDescription', 'StartDate','EndDate', 'Status']]
    #replace nulls
    revised['WeightUnitMeasureCode'].fillna('0', inplace=True)
    revised['ProductSubcategoryKey'].fillna('0', inplace=True)
    revised['SizeUnitMeasureCode'].fillna('0', inplace=True)
    revised['StandardCost'].fillna('0', inplace=True)
    revised['ListPrice'].fillna('0', inplace=True)
    revised['ProductLine'].fillna('NA', inplace=True)
    revised['Class'].fillna('NA', inplace=True)
    revised['Style'].fillna('NA', inplace=True)
    revised['Size'].fillna('NA', inplace=True)
    revised['ModelName'].fillna('NA', inplace=True)
    revised['EnglishDescription'].fillna('NA', inplace=True)
    revised['DealerPrice'].fillna('0', inplace=True)
    revised['Weight'].fillna('0', inplace=True)
    # Rename columns with rename function
    revised = revised.rename(columns={"EnglishDescription": "Description", "EnglishProductName":"ProductName"})
    revised.to_sql(f'stg_DimProduct', engine, if_exists='replace', index=False)
    return {"table(s) processed ": "Data imported successful"}
