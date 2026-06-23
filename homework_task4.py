import pandas as pd

df_sales = pd.DataFrame({
    'SaleID': [2001, 2002, 2003, 2004, 2005],
    'StoreID': [10, 20, 10, 30, 20],
    'ProductID': [301, 302, 303, 301, 304],
    'UnitsSold': [50, 60, 70, 80, 90]
})

df_suppliers = pd.DataFrame({
    'SupplierID': [401, 402, 403, 404],
    'ProductID': [301, 302, 303, 305],
    'SupplierName': ['Supplier A', 'Supplier B', 'Supplier C', 'Supplier D']
})

# 1
df_sales = df_sales.set_index(['StoreID', 'ProductID'])

# 2
merged = pd.merge(df_sales, df_suppliers, on='ProductID')

# 3
merged_validated = pd.merge(df_sales, df_suppliers, on='ProductID', validate='many_to_one')

# 4
merged_with_suffix = pd.merge(df_sales, df_suppliers, on='ProductID', suffixes=('_sales', '_supplier'))
