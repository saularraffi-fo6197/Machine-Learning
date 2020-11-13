import pandas as pd
import numpy as np
from sklearn import linear_model
import csv
import math

# create csv file for training data
with open('data.csv', 'w', newline='') as f:
	thewriter = csv.writer(f)
	thewriter.writerow(['area', 'bedrooms', 'age', 'price'])
	thewriter.writerow([2600, 3, 20, 550000])
	thewriter.writerow([3000, 4, 15, 565000])
	thewriter.writerow([3200, None, 18, 610000])
	thewriter.writerow([3600, 3, 30, 595000])
	thewriter.writerow([4000, 5, 8, 760000])

# pandas data frame
df = pd.read_csv('data.csv')

# printing data
print('\nTraining Data')
print(df)

print('\n[+] Equation...\n')
print('  price = theta0 + (theta1 * area) + (theta2 * bedrooms) + (theta3 * age)')

# find average number of bedrooms
median_bedrooms = math.floor(df.bedrooms.median())

# fill missing bedroom data with the average number of bedrooms
df.bedrooms = df.bedrooms.fillna(median_bedrooms)

reg = linear_model.LinearRegression()
# list independent variables first, inside the [[]], then specify dependent variable
reg.fit(df[['area', 'bedrooms', 'age']], df.price)

print('\n[+] Listing optimal weights...\n')
print('   theta0: {}\n   theta1: {}\n   theta2: {}\n   theta3: {}\n'.format(reg.intercept_, 
	reg.coef_[0],  reg.coef_[1],  reg.coef_[2]))

# showing predictions
print('\n[+] Showing predictions...')
area = 3000
bedrooms = 3
age = 40
prediction = int(reg.predict([[area, bedrooms, age]]))
print('\n   area: {}, bedrooms: {}, age: {}'.format(area, bedrooms, age))
print('   Prediction: ${}'.format(prediction))

area = 3000
bedrooms = 4
age = 10
prediction = int(reg.predict([[area, bedrooms, age]]))
print('\n   area: {}, bedrooms: {}, age: {}'.format(area, bedrooms, age))
print('   Prediction: ${}'.format(prediction))

area = 5000
bedrooms = 3
age = 35
prediction = int(reg.predict([[area, bedrooms, age]]))
print('\n   area: {}, bedrooms: {}, age: {}'.format(area, bedrooms, age))
print('   Prediction: ${}'.format(prediction))