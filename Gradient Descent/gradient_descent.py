import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import csv

def cost(data, theta0, theta1):
	# theta0 is b
	# theta1 is m
	sumation = 0
	n = len(data)
	for i in range(n):
		xi = data.iloc[i].area
		yi = data.iloc[i].price
		h_theta = theta1*xi + theta0
		sumation = sumation + (h_theta - yi)**2

	return (1/(2*n)) * sumation

# create csv file for training data
with open('data.csv', 'w', newline='') as f:
	thewriter = csv.writer(f)
	thewriter.writerow(['area', 'price'])
	thewriter.writerow([26, 550])
	thewriter.writerow([30, 565])
	thewriter.writerow([32, 610])
	thewriter.writerow([36, 680])
	thewriter.writerow([40, 725])

# read csv file
data = pd.read_csv('data.csv')

# plot data
# print('\n[+] Showing plot...')
# plt.xlabel('area (sqr ft)')
# plt.ylabel('price (US$)')
# plt.title('Housing Price Training Fit')
# plt.scatter(data.area, data.price, color='red', marker='+')
# plt.show()

# creating coordinates for J(theta0, theta1)
x = np.linspace(0,600000,15)
y = []
for i in range(1,30,2):
	y.append(int(cost(data,150,i)))

plt.title('Cost Function')
plt.xlabel('Theta1')
plt.ylabel('J(theta1)')
plt.plot(x, y, color='blue')
plt.plot(x[1],y[1],'ro') 
plt.show()