'''
 *
 * Author : Imanpal Singh <imanpalsingh@gmail.com>
 * Date created : 01-02-2020
 * Date modified : 02-02-2020
 * Description :  Data analysis on the novel cornoavirus data
 *
'''

'''
 *
 * Change log
 * (0.0.1) Added Supervised Learning Methods 
 *
'''


# Imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder as LB
from sklearn.preprocessing import normalize as norm
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


############################### Loading dataset##########################

dataset = pd.read_csv('2019_nCOV_data.csv')


#################################### Data preprocessing ###################

#Checking for missing values

print("Missing Values\n",dataset.isnull().any()) # Province/State feature appears to have missing data

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
dataset['Date of January 2020'] = dates 
    

'''
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



sns.lineplot(dataset['Date of January 2020'], dataset['Confirmed'],color='k',linewidth=2.5)
sns.lineplot(dataset['Date of January 2020'], dataset['Deaths'],color='red', linewidth=2.5)
sns.lineplot(dataset['Date of January 2020'], dataset['Recovered'], linewidth=2.5)


# Confirmed cases in total vs dates
confirmed = dataset.groupby('Date of January 2020')['Confirmed'].sum().reset_index()
sns.lineplot(confirmed['Date of January 2020'],confirmed['Confirmed'], label = "Confirmed cases in total", color='black')

# Deaths in the world on the basis of dates
deaths = dataset.groupby('Date of January 2020')['Deaths'].sum().reset_index()
sns.lineplot(deaths['Date of January 2020'],deaths['Deaths'], label = "Deaths in total", color='red')

# Recovery cases in total vs dates
Recovered = dataset.groupby('Date of January 2020')['Recovered'].sum().reset_index()
sns.lineplot(Recovered['Date of January 2020'],Recovered['Recovered'], label = "Recovery cases in total", color='blue')
plt.legend()

###################### Statistical Analysis #########################
'''
print("Data Summary\n",dataset.describe())

# Gathering Feature Matrix and vector of prediction
X = dataset.iloc[:,[0,1,2,4,5]].values
y = dataset.iloc[:,3].values # Deaths

# Not splitting into train test set 

# Label encoding Categorical valus
lab = LB()
X[:,0] = lab.fit_transform(X[:,0].astype(str))
X[:,1] = lab.fit_transform(X[:,1].astype(str))

#normalizing
X = norm(X)

#Building the model

# Linear Regression
lin_reg = LinearRegression()

lin_reg.fit(X,y)
print("Feature : Coefficient ")
for coeff,feature in zip(lin_reg.coef_,dataset.columns[[0,1,2,4,5]]):
    print(feature ,' : ', coeff )

print("Intercept : ", lin_reg.intercept_)

# Polynomial Regression
poly = PolynomialFeatures(2)
X = poly.fit_transform(X)
lin_reg.fit(X,y)

print("Feature : Coefficient ")
for coeff,feature in zip(lin_reg.coef_,dataset.columns[[0,1,2,4,5]]):
    print(feature ,' : ', coeff )

print("Intercept : ", lin_reg.intercept_)
