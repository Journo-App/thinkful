
# coding: utf-8

# In[3]:

from scipy import stats
import collections
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic('matplotlib inline')

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

print(freq)


# In[2]:

count_sum = sum(freq.values())
for k,v in freq.items():
  print("The frequency of cases " + str(k) + " is " + str(float(v) / count_sum))


# In[4]:

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()


# In[12]:

chi, p = stats.chisquare(list(freq.values()))
#print(chi)
#print(p)
print ("The chi square value is {0}, corresponding to a p value of {1}".format(chi,p))


# In[7]:

loansData.boxplot(column='Open.CREDIT.Lines')

plt.show()


# The range is about 20 with a median of 8. 

# In[ ]:



