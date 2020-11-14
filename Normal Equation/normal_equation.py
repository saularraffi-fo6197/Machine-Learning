import numpy as np
import matplotlib.pyplot as plt

'''The model has a problem ---> the bedroom to price relationship is inverse'''

def normal_equation(x, y):
	ones = np.ones((x.shape[0], 1))
	x = np.append(ones, x, axis=1)
	theta = np.linalg.pinv(x.T * x) * (x.T * y)
	return theta

if __name__ == '__main__':
	# area, bedrooms, age
	x = np.matrix([[2600, 3, 20], [3000, 4, 15], [3200, 3, 18], [3600, 3, 30], [4000, 5, 8]])
	# prices
	y = np.matrix([[550000], [565000], [610000], [595000], [760000]])

	weights = normal_equation(x,y)

	x1 = 2500
	x2 = 4
	x3 = 20
	price = weights.item(0) + (weights.item(1)*x1) + (weights.item(2)*x2) + (weights.item(3)*x3)
	print('\n[+] Area: {}, Bedrooms: {}, Age: {}'.format(x1, x2, x3))
	print('Prediction: ${}'.format(int(price)))

	x1 = 5000
	x2 = 4
	x3 = 20
	price = weights.item(0) + (weights.item(1)*x1) + (weights.item(2)*x2) + (weights.item(3)*x3)
	print('\n[+] Area: {}, Bedrooms: {}, Age: {}'.format(x1, x2, x3))
	print('Prediction: ${}'.format(int(price)))

	x1 = 5000
	x2 = 2
	x3 = 20
	price = weights.item(0) + (weights.item(1)*x1) + (weights.item(2)*x2) + (weights.item(3)*x3)
	print('\n[+] Area: {}, Bedrooms: {}, Age: {}'.format(x1, x2, x3))
	print('Prediction: ${}'.format(int(price)))

	x1 = 5000
	x2 = 2
	x3 = 30
	price = weights.item(0) + (weights.item(1)*x1) + (weights.item(2)*x2) + (weights.item(3)*x3)
	print('\n[+] Area: {}, Bedrooms: {}, Age: {}'.format(x1, x2, x3))
	print('Prediction: ${}'.format(int(price)))