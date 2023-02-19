import pandas as pd

dict1 ={'a':1, 'b':2, 'c':3, 'd':4}   
  
# Define Dictionary 2     
dict2 ={'a':5, 'b':6, 'c':7, 'd':8, 'e':9} 
  
# Define Data with dict1 and dict2
Data = {'first':dict1, 'second':dict2} 
  
# Create DataFrame 
df = pd.DataFrame(Data)  
print(df)
print(df.groupby('first')['second'].transform('min'))

print(df['first'][0].tolist())
# print(df.loc['a','first'])
# df1=pd.DataFrame()
# print("Printing first")
# c=df1[0]
# print(c)