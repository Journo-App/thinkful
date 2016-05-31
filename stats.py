import pandas as pd
from scipy import stats
#need to go back and rewrite print statements

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()

data = [i.split(',') for i in data]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)


df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print("The mean of the household spending (in British pounds) on alcohol products in each of the 11 regions of Great Britain:") 

df['Alcohol'].mean()
print(df)

print("The median of the household spending on alcohol products in each of the 11 regions of Great Britain is 5.63 in British pounds")

print(df['Alcohol'].median())

print("The mode of the household spending on alcohol products in each of the 11 regions of Great Britain is 4 in British pounds.")   

print(stats.mode(df['Alcohol'])) 

print("The mode of the household spending on tobacco products in each of the 11 regions of Great Britain is 2.71 in British pounds.")

print(stats.mode(df['Tobacco'])) 

print("The median of the household spending on tobacco products in each of the 11 regions of Great Britain is 3.53 in British pounds.")

print(df['Tobacco'].median())

print("The mean of the household spending on tobacco products in each of the 11 regions of Great Britain is 3.62 in British pounds."


print(df['Tobacco'].mean())


print("The range between the largest and smallest values in terms of spending on alcohol products in 11 regions of Great Britain is 2.45 in British pounds.")  

print(max(df['Alcohol']) - min(df['Alcohol'])) #range 


print("The range between the largest and smallest values in terms of spending on tobacco products in 11 regions of Great Britain is 1.85 in British pounds.")  

print(max(df['Tobacco']) - min(df['Tobacco'])) #range


print("The standard deviation for alcohol products sales in Great Britain is small, .8.") 

print(df['Alcohol'].std())

print("The standard deviation for tobacco products sales in Great Britain is small, .6.") 

print(df['Tobacco'].std()) #standard deviation

print("Correlation:")

print("Variance measures the distance from the mean and characterizes the distribution of the data.") 

print(df['Alcohol'].var()) #variance

print(df['Tobacco'].var())
