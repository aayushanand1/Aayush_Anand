#!/usr/bin/env python
# coding: utf-8

# ## Build a simple trading strategy 

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# ### 1. Munging the stock data and add two columns - MA10 and MA50

# In[7]:


#import FB's stock data, add two columns - MA10 and MA50
#use dropna to remove any "Not a Number" data
fb = pd.read_csv('facebook.csv')
fb['MA10'] = fb['Close'].rolling(10).mean()
fb['MA50'] = fb['Close'].rolling(50).mean()
fb = fb.dropna()
fb.head()


# ### 2. Add "Shares" column to make decisions base on the strategy 

# In[8]:


#Add a new column "Shares", if MA10>MA50, denote as 1 (long one share of stock), otherwise, denote as 0 (do nothing)

fb['Shares'] = [1 if fb.loc[ei, 'MA10']>fb.loc[ei, 'MA50'] else 0 for ei in fb.index]
fb


# In[9]:


#Add a new column "Profit" using List Comprehension, for any rows in fb, if Shares=1, the profit is calculated as the close price of 
#tomorrow - the close price of today. Otherwise the profit is 0.

#Plot a graph to show the Profit/Loss

fb['Close1'] = fb['Close'].shift(-1)
fb['Profit'] = [fb.loc[ei, 'Close1'] - fb.loc[ei, 'Close'] if fb.loc[ei, 'Shares']==1 else 0 for ei in fb.index]
fb['Profit'].plot()
plt.axhline(y=0, color='red')


# ### 3. Use .cumsum() to display our model's performance if we follow the strategy 

# In[10]:


#Use .cumsum() to calculate the accumulated wealth over the period

fb['wealth'] = fb['Profit'].cumsum()
fb.tail()


# In[39]:


def BollBnd(Df,n):
    df = Df
    df['MA'] = df['Close'].rolling(n).mean()
    df['BB_up'] = df['Close'].rolling(n).mean() + 2*df['MA'].rolling(n).std()
    df['BB_dn'] = df['Close'].rolling(n).mean() - 2*df['MA'].rolling(n).std()
    df['BB_Width'] = df['BB_up'] - df['BB_dn']
    df.dropna(inplace=True)
    return df


# In[56]:


BollBnd(fb,20)
BollBnd(fb,20).iloc[1:,[13,14,15]].plot()

fb.head()


# In[ ]:



   


# In[1]:


#plot the wealth to show the growth of profit over the period

fb['wealth'].plot()
plt.title('Total money you win is {}'.format(fb.loc[fb.index[-2], 'wealth']))


# 

# In[ ]:





# In[ ]:





# In[ ]:




