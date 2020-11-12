import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import csv

def cost(m, b):
	sumation = 0
	n = len(data)
	for i in range(n):
		xi = data.iloc[i].area
		yi = data.iloc[i].price
		h_theta = m*xi + b
		sumation = sumation + (h_theta - yi)

	return (1/(2*n)) * (sumation**2)

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
print('\n[+] Showing plot...')
plt.xlabel('area (sqr ft)')
plt.ylabel('price (US$)')
plt.title('Housing Price Training Fit')
plt.scatter(data.area, data.price, color='red', marker='+')
# plt.show()

# alpha = 1
# theta0 = theta0 - cost(5)

print(cost(15, 150))
print(cost(12, 200))