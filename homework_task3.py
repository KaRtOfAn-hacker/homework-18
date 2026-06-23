import pandas as pd
import numpy as np

np.random.seed(0)
transactions_df = pd.DataFrame({
    'TransactionID': range(1, 100001),
    'UserID': np.random.randint(1, 1001, size=100000),
    'ProductID': np.random.randint(1, 500, size=100000),
    'Date': pd.date_range(start='2023-01-01', periods=100000, freq='T'),
    'Amount': np.random.uniform(10.0, 1000.0, size=100000)
})

products_df = pd.DataFrame({
    'ProductID': range(1, 501),
    'ProductName': [f'Product{i}' for i in range(1, 501)]
})

# 1
transactions_df = transactions_df.set_index(['UserID', 'ProductID'])

# 2
transactions_df['Amount'] = transactions_df['Amount'].astype('float32')

# 3
products_df = products_df.set_index(['UserID', 'ProductID'])  # Приклад, може бути індекс ProductID
merged = pd.merge(transactions_df, products_df, left_index=True, right_index=True)
