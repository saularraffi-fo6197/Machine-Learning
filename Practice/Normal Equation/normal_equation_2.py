import numpy as np

def normal_equation(X, y):
	ones = np.ones((X.shape[0], 1))
	X = np.append(ones, X, axis=1)
	W = np.dot(np.linalg.pinv(np.dot(X.T, X)), np.dot(X.T, y))
	return W

if __name__ == '__main__':
	x = [[2600, 3, 20], [3000, 4, 15], [3200, 3, 18], [3600, 3, 30], [4000, 5, 8]]
	y = [[550000], [565000], [610000], [595000], [760000]]

	x = np.matrix(x)
	y = np.matrix(y)

	theta = normal_equation(x, y)
	print(theta)

	x1 = 4000
	x2 = 3
	x3 = 20
	price = theta.item(0) + (theta.item(1)*x1) + (theta.item(2)*x2) + (theta.item(3)*x3)