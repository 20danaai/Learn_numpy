import pandas as pd
olympics=pd.read_excel('ai/data/olympics-data.xlsx',sheet_name=1) # Read the seconde page,0=first page,None=all page,(start with the left page)
#Parquet and Csv don't need sheet_name
results=pd.read_csv('ai/data/results.csv')
results.head() # Show me every things
results.tail() # Last to the first
results.sample(10) # Random raw values from all pages
results.sample(10,random_state=1) # I want these ten random values to be the same every time i run the code
#results.loc[Rows,Coloumns]
results.loc[0] # Show me all the dataframe first row
results.loc[[0,1,2]]
results.loc[2:6]
results.loc[5:8,'event'] # just show me the columns event 
results.loc[ : ,["year",'team']]
results.iloc[ :5, :2]
#Loc:location,we use the name
#Iloc:integer location , we use the number, not enclude the end
#results.index=results["team"] # Change the index to the name team
#results.loc['Jean Montariol':'Jacques Brugnon'] # Slicing the datafram using labels in index
results.loc[1:3,'place']=100 # Change the value from 1;3 raw
results.head()
results.sort_values('year') # Sorted columns
results.sort_values(['year','as']) # Multiple columns sorting 
results.sort_values(['year','as'],ascending=False) # The first column takes priority followed by the second
results.sort_values(['year','as'],ascending=[0,1]) # I can sort each column individually : 0 means descending,1 means ascending
#for index,row in results.iterrows():
   # print(index)
    #print(row)
    #print('\n')
bios=pd.read_csv('ai/data/bios.csv')
bios.loc[bios['height_cm']>215],['name','height_cm']
bios[(bios['height_cm']>216)&(bios['born_country']=='USA')]
bios[bios['name'].str.contains('Dana')] # Show me the name start with dana
bios[bios['name'].str.contains('Dana',case=False)] # Ignore case
bios[bios['name'].str.contains('Dana|keith',case=False)]
