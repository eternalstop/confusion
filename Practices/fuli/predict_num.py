# coding=utf-8

import matplotlib.pyplot as plt
import matplotlib.patches as mpatchs
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model


def get_data(file_name):
	data = pd.read_csv(file_name)
	x_parameter = []
	y_parameter = []
	for single_square_feet, single_price_value in zip(data['periods'], data['ball']):
		x_parameter.append([float(single_square_feet)])
		y_parameter.append(float(single_price_value))
	return x_parameter, y_parameter


def linear_model_main(X_parameters, Y_parameters, predict_value):
	# Create linear regression object
	regr = linear_model.LinearRegression()
	regr.fit(X_parameters, Y_parameters)
	predict_outcome = regr.predict(predict_value) // 1
<<<<<<< HEAD
	predictions = {'intercept': regr.intercept_, 'coefficient': regr.coef_, 'predicted_value': predict_outcome}
=======
	predictions = {'intercept': regr.intercept_,
	               'coefficient': regr.coef_,
	               'predicted_value': predict_outcome}
>>>>>>> b01c862ce99a29806808ae156c6d9774bfc2a0b9
	return predictions


# def show_linear_line(x_parameters, y_parameters):
# 	# Create linear regression object
# 	regr = linear_model.LinearRegression()
# 	regr.fit(x_parameters, y_parameters)
# 	plt.scatter(x_parameters, y_parameters, color='blue')
# 	plt.plot(x_parameters, regr.predict(y_parameters), color='red', linewidth=4)
# 	plt.xticks(())
# 	plt.yticks(())
# 	plt.show()


def show_line(x_parameters, y_parameters):
	plt.figure(figsize=(100, 50))
	ball, = plt.plot(x_parameters, y_parameters, "b")
	# 在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
	plt.xlabel("periods")
	# X轴标签
	plt.ylabel("Value")
	# Y轴标签
	plt.title("test")
	# 图标题
	plt.show()


x, y = get_data('blue.csv')
# print(x, y)
predictvalue = 2183
result = linear_model_main(x, y, predictvalue)
print("Intercept value ", result['intercept'])
print("coefficient", result['coefficient'])
print("Predicted value: ", result['predicted_value'])
show_line(x, y)
