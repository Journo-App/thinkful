
# coding: utf-8

# In[37]:

from scipy import stats
import collections
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic('matplotlib inline')
import numpy as np
import statsmodels.api as sm

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')


# In[38]:

loansData['Interest.Rate'][0:5]


# In[39]:

loansData['Loan.Length'][0:5]


# In[40]:

loansData['FICO.Range'][0:5]


# In[41]:

loansData.dropna(inplace=True)


# In[42]:

#remove % symbol from interest rate and convert to float
loansData['Interest.Rate'] = [float(interest[0:-1])/100 for interest in loansData['Interest.Rate']]


# In[43]:

loansData['Interest.Rate'][0:1]


# In[44]:

#remove "month" at the end of loan length and convert to integer
loansData['Loan.Length'] = [int(length[0:-7]) for length in loansData['Loan.Length']]


# In[45]:

loansData['Loan.Length'][0:1]


# In[46]:

#create a new column called Fico Score with lower limit value
loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]


# In[47]:

cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))


# In[48]:

cleanFICORange[0:5]


# In[49]:

cleanFICORange = cleanFICORange.map(lambda x: [int(n) for n in x])


# In[50]:

cleanFICORange[0:5]


# In[51]:

cleanFICORange[0:5].values[0]


# In[52]:

type(cleanFICORange[0:5].values[0][0])


# In[53]:

loansData['FICO.Range'] = cleanFICORange


# In[54]:

loansData['FICO.Range'][0:5]


# In[55]:

loansData['FICO.Range'][0:5].values[0][0]


# In[56]:

type(loansData['FICO.Range'][0:5].values[0][0])


# In[57]:

plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()


# In[58]:

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))


# In[59]:

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']


# In[60]:

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()


# In[61]:

x = np.column_stack([x1,x2])


# In[62]:

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()


# In[63]:

f.summary()


# In[ ]:



