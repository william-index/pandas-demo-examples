import pandas as pd
import numpy as np

# read file
ws1 = pd.read_csv('data/ws1.csv')

# show first or last n (default 5)
head = ws1.head(6)
tail = ws1.tail(2)

# create new column with a value based on other columns in row
ws1['Grand Total'] = ws1["Jan"] + ws1["Feb"] + ws1["Mar"] + ws1["Apr"] + ws1["May"] + ws1["Jun"]
ws1['Total'] = ws1.sum(axis=1) - ws1['Grand Total'] #only sums numberic values

print ws1
