# pip install pandas
# pip install openpyxl

import pandas as pd

data = {
    "ID": [1, 2, 3],
    "Name": ["Ali", "Sara", "Omar"],
    "Salary": [50000, 60000, 55000]
}
df = pd.DataFrame(data)

df.to_excel("employees.xlsx", index=False)

df_read = pd.read_excel("employees.xlsx")
print(df_read[['Name', 'Salary']])