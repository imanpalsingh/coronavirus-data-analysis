'''
 *
 * Author : Imanpal Singh
 * Date created : 01-02-2020
 * Date modified : 01-02-2020
 * Description :  Data analysis on the novel cornoavirus data
 *
'''

'''
 *
 * Change log
 *
'''


# Imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




############################### Loading dataset##########################

dataset = pd.read_csv('2019_nCOV_data.csv')


#################################### Data preprocessing ###################

#Checking for missing values
print(dataset.isnull().any()) # Province/State feature appears to have missing data

#Serial no is not required as it doesn't add any benefit
dataset = dataset.drop('Sno',1)

#The province have Nan values the data. Assigning a new category named unkown.
dataset['Province/State'] = dataset['Province/State'].replace(np.nan,'unkown' , regex=True)

# Since all the dates are in year 2020 and in januray thus only date is requred. Also the time variance is not much
# Taking the dates only
dates = []
for each_date in dataset['Last Update']:
   dates.append(each_date.split('/')[1])
    
# Replacing th original column with new feature engineered one
dataset = dataset.drop('Last Update',1)
dataset['Date of Januaray 2020'] = dates 
    


#################### Exploratory data analysis ########################

sns.set(style="whitegrid")
# Province 
# Province/Satate vs cases confirmed
fig,ax = plt.subplots()
sns.barplot(dataset['Confirmed'],dataset['Province/State'],)

# Province/Satate vs cases of deaths
fig,ax = plt.subplots()
sns.barplot(dataset['Deaths'],dataset['Province/State'],)


# Province/Satate vs cases of recovered
fig,ax = plt.subplots()
sns.barplot(dataset['Recovered'],dataset['Province/State'],)


# Country
fig,ax = plt.subplots()
sns.barplot(dataset['Confirmed'],dataset['Country'])

fig,ax = plt.subplots()
sns.barplot(dataset['Deaths'],dataset['Country'])

fig,ax = plt.subplots()
sns.barplot(dataset['Recovered'],dataset['Country'])



sns.lineplot(dataset['Date of Januaray 2020'], dataset['Confirmed'],color='k',linewidth=2.5)
sns.lineplot(dataset['Date of Januaray 2020'], dataset['Deaths'],color='red', linewidth=2.5)
sns.lineplot(dataset['Date of Januaray 2020'], dataset['Recovered'], linewidth=2.5)

