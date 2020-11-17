import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(x, y, iterations, alpha):
	m_curr = b_curr = 0
	n = len(x) # should be same length as y

	plt.xlabel('x-axis')
	plt.ylabel('y-axis')
	plt.title('Gradient Descent, alpha: {}, iterations: {}'.format(alpha, iterations))
	plt.scatter(x, y, color='red', marker='+')

	for i in range(iterations):
		y_predicted = m_curr*x + b_curr

		plt.plot(x, y_predicted, color='blue')

		cost = (1/n) * sum([val**2 for val in (y - y_predicted)])
		bd = -(2/n) * sum((y - y_predicted)) # derivative of b
		md = -(2/n) * sum((y - y_predicted) * x) # derivative of m
		m_curr = m_curr - alpha * md # update m
		b_curr = b_curr - alpha * bd # update b
		
		print('m {}, b {}, cost {}, iterations {}'.format(m_curr,b_curr,cost,i))

	plt.plot(x, y_predicted, color='red')
	plt.show()

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x, y, 100, 0.001)
gradient_descent(x, y, 100, 0.01)
gradient_descent(x, y, 100, 0.08)