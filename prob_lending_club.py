
# coding: utf-8

# In[4]:

import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic('matplotlib inline')

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')


# In[2]:

loansData.dropna(inplace=True)


# In[5]:

loansData.boxplot(column='Amount.Funded.By.Investors')

plt.show()


# In[6]:

loansData.hist(column='Amount.Funded.By.Investors')
plt.show()


# In[7]:

import scipy.stats as stats
plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()


# In[8]:

loansData.boxplot(column='Amount.Requested')

plt.show()

#histogram
loansData.hist(column='Amount.Requested')
plt.show()

#QQ plot
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()


# The Lending Club would appear from the histogram to be funding clients above what was requested. However the median in both cases is $10,000 although the range is smaller in the funding category. 
