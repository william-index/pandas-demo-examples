import pandas as pd
import numpy as np

ws2 = pd.read_csv('data/ws2.csv')
# remove column
ws2_new = ws2.drop('ext price', axis=1) #removes column # axis 0 = row, 1 = column

# rename columns
ws2_new.rename(columns={'name': 'client'}, inplace=True)
headers = ws2_new.columns.tolist()

# filter specific clients
ws2_new_query = ws2_new.query('client == ["Jerde-Hilpert", "Kulas Inc"]')

# filter any unit price above 90.00
ws2_number = ws2_new[ws2_new['unit price'] >= 90.00].head()

# Creates a new table with the total sum of unitprice accross all rows for each name
ws2_group = pd.pivot_table(
                ws2,
                index=["name"],
                values=["unit price"],
                aggfunc=np.sum)

print ws2_group.head()
