import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import linear_model
import csv

# create csv file for training data
with open('training_data.csv', 'w', newline='') as f:
	thewriter = csv.writer(f)
	thewriter.writerow(['area', 'price'])
	thewriter.writerow([2600, 550000])
	thewriter.writerow([3000, 565000])
	thewriter.writerow([3200, 610000])
	thewriter.writerow([3600, 680000])
	thewriter.writerow([4000, 725000])

# read csv file
df_train = pd.read_csv('training_data.csv')

# printing data
print('\nTraining Data')
print(df_train)
print('\n')

# fit linear regression model
reg = linear_model.LinearRegression()
reg.fit(df_train[['area']], df_train.price)

# fitted linear regression model equation
x = np.linspace(2000,5000,100)
m = reg.coef_
b = reg.intercept_

y = m*x + b

# plot data
print('[+] Showing plot...')

plt.xlabel('area (sqr ft)')
plt.ylabel('price (US$)')
plt.title('Housing Price Training Fit')
plt.scatter(df_train.area, df_train.price, color='red', marker='+')

plt.plot(x, y, color='blue')
plt.show()

# create csv file for test data
with open('test_data.csv', 'w', newline='') as f:
	thewriter = csv.writer(f)
	thewriter.writerow(['area'])
	thewriter.writerow([1000])
	thewriter.writerow([1500])
	thewriter.writerow([2300])
	thewriter.writerow([3540])
	thewriter.writerow([4120])
	thewriter.writerow([4560])
	thewriter.writerow([5490])
	thewriter.writerow([3460])
	thewriter.writerow([4750])
	thewriter.writerow([2300])
	thewriter.writerow([9000])
	thewriter.writerow([5600])
	thewriter.writerow([7100])

# read csv file
df_test = pd.read_csv('test_data.csv')

# use linear regression to obtain predictions for each test input
predictions = reg.predict(df_test)

# add price column and export to csv
df_test['price'] = predictions
df_test.to_csv('predictions.csv', index=False)

# printing data
print('\nPredictions')
print(df_test)

# plot data
print('\n[+] Showing plot...')

plt.xlabel('area (sqr ft)')
plt.ylabel('price (US$)')
plt.title('Housing Price Predictions')
plt.scatter(df_test.area, df_test.price, color='red', marker='+')
plt.show()