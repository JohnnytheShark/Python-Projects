import numpy as np
import pandas as pd

#Formatting for dollar value column
df['column'] = df['column'].astype(float).apply(lambda x: "${:,.2f}".format(x))

#Mulitple columns selected: 
df.iloc[:,3:] = df.iloc[:,3:].astype(float).applymap(lambda x: "${:,.2f}".format(x))
