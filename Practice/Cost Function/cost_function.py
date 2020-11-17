import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import csv

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

# printing data
print('\nTraining Data')
print(data)

# setting up plot linespace
x = np.linspace(20,50,5)

# defining list of m's and b's
weightsList = [[12,200], [15,150]]

for weights in weightsList:
	m = weights[0]
	b = weights[1]
	y = m*x + b

	# cost function --> (1/2n)sum_from_1_to_n(h_theta_i - yi)^2
	summation = 0
	n = len(data)
	for i in range(n):
		xi = data.iloc[i].area
		yi = data.iloc[i].price
		h_theta = m*xi + b
		summation = summation + (h_theta - yi)**2

	cost = (1/(2*n)) * summation
	print('\n[+] m = ' + str(m) + ', b = ' + str(b))
	print('[+] Cost function result --> ' + str(cost))

	# plot data
	print('\n[+] Showing plot...')
	plt.xlabel('area (sqr ft)')
	plt.ylabel('price (US$)')
	plt.title('Housing Price Training Fit')
	plt.scatter(data.area, data.price, color='red', marker='+')
	plt.plot(x, y, color='blue')
	plt.show()