import pandas as pd

df_a = pd.DataFrame({
    'EmployeeID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Department': ['HR', 'Engineering', 'Marketing']
})

df_b = pd.DataFrame({
    'EmployeeID': [4, 5],
    'Name': ['David', 'Eva'],
    'Department': ['Finance', 'IT']
})

# 1
combined = pd.concat([df_a, df_b], ignore_index=True)

# 2
combined_with_keys = pd.concat([df_a, df_b], keys=['Group_A', 'Group_B'])

# 3
print(combined_with_keys)
