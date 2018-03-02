
# coding: utf-8

# In[24]:


#    ___            _____  ___  ____
#   / _ \___ ___ __/ / _ \|_  |/ __/
#  / ___/ _ `/ // / /\_, / __/_\ \  
# /_/   \_,_/\_,_/_//___/____/___/  
#                                 

# Scripted: Paul92S
# Date: 02/03/18
# gitVersion: 0.1

# 500k transactions over the last ≈17hrs 
#Looping through page numbers using url manipulation
#for i in range(1,10000):
#adding results to a dF for analysis

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

dfs = []

url = "https://etherscan.io/txs?p="

for index in range(1, 10000):
    res = requests.get(url+str(index))
    soup = BeautifulSoup(res.content,'lxml')
    table = soup.find_all('table')[0]
    
    print("Collecting dataFrame no. "+ str(index))
    df = pd.read_html(str(table))
    
    df_list = pd.read_html(str(table))
    df = pd.concat(df_list)  # this line is what you're missing
    dfs.append(df)

print("Combining to single dF to Move to Local File.......")
print("Please wait!")

final_df = pd.concat(dfs)
final_df.to_csv('Desktop/scrape.csv')
print( tabulate(final_df, headers='keys', tablefmt='psql'))


# ---- Extra dF work ----
#df[0].shape
#df[0].count()
#df_Values = df[0].iloc[:,6] Collecing Ether
#print(df_Values)

