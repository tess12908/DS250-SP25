"""
In class notes - 4/29 
"""

#%%
#needs this to start up
import pandas as pd
import numpy as np
from lets_plot import *

LetsPlot.setup_html(isolated_frame=True)

#%%
# an example of a data frame - note yu can have dif data types 
df = pd.DataFrame(
{"a" : [5, 4, 6, 2, 3],
"b" : [7, 8, 9, 10, 11],
"c" : [10, 11, 12, 101, 0]})
print(df)

#%%
# to help us look st the data we can use this to list all of the columns 
df.columns

# this will print out the first 5 rows to look at a small part of it 
df.head

#will show only the first 2 rows 
df.head(n=2) 

#%%
#goal is to rename column a to duck 
df.rename(columns = {'a' : 'duck'})

#subset to only have duck and b columns  
df[['duck', 'b']]

#keep all rows were b is less then 9 
df.query('b' < 9 )

#find the min of duck
df.min('duck') #idk if this one works....

#%%



