import numpy as np
import pandas as pd

#Formatting for dollar value column
df['column'] = df['column'].astype(float).apply(lambda x: "${:,.2f}".format(x))

#Mulitple columns selected: 
df.iloc[:,3:] = df.iloc[:,3:].astype(float).applymap(lambda x: "${:,.2f}".format(x))

#Formatting multiple columns to floats
data[data.columns[3:]] = data.iloc[:,3:].astype(str).replace(r'[$,\s]',"",regex=True).applymap(lambda x: pd.to_numeric(x))
