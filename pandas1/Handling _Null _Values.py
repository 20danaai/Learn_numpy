import pandas as pd
import numpy as np
results=pd.read_csv('ai/data/results.csv')
results
results[results.isna()]
results.loc[[0,1],'team']=np.nan # made the values nan
results
results.isna().sum() # Check for missing values in each column and count their number , isna() return true or false , sum() to some how many Nan i have
results.fillna(100) # Fill in Nan values
results=results.fillna(results['year'].mean()) #  Imputation : filling missing values with  the mean of place , ex: Average age of employees in the company
results
results.loc[[2,3],['melad']]=np.nan
results.loc[[0,1],['melad']]=15
results
results['place']=results['place'].interpolate() # Use with time series , Guessing based on adjacent values , ex : Temperatures or stock prices
results
results.dropna() # Remove Nan
results.dropna(subset=['type']) # Delete only  Nan in a type column
results[results.notna()] # Show column don't have Nan values
