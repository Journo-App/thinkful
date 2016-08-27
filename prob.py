%matplotlib inline #stylizing the graphs
import collections
import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

# creates a list of data
# got idea from other Thinkful student to use range operator to generate numbers but there are drawbacks:
# all occur exactly same number of times 
data = [i for i in range(-100,100)]
print(data)

# counts the number of instances in the list
count = collections.Counter(data)
print(count)

#calculates frequency
for k,v in count.items():
    print("The frequency of "+str(k)+" is "+str(float(v)/len(data)))

#boxplot
plt.boxplot(data)
plt.show()

#histogram
plt.hist(data, histtype='bar')
plt.show()

#QQ-plot
plt.figure()
graph = stats.probplot(data, dist="norm", plot=plt)
