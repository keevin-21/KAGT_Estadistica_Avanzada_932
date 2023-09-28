# -*- coding: utf-8 -*-
"""
Kevin Alejandro Gonzalez Torres - 372354

September 27th 2023

Regresión lineal simple, R cuadrada y normalidad de los residuos
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import pandas as pd

# Data
y_values = [790, 1160, 929, 865, 1140, 929, 1109, 1365, 1112, 1150, 980, 990, 1112,
            1252, 1326, 1330, 1365, 1280, 1119, 1328, 1584, 1428, 1365, 1415, 1415,
            1465, 1490, 1725, 1523, 1705, 1605, 1746, 1235, 1390, 1405, 1395]

x_values = [99, 95, 95, 90, 105, 105, 90, 92, 98, 99, 99, 101, 99, 94, 97, 97, 99, 104, 104,
            105, 94, 99, 99, 99, 99, 102, 104, 114, 109, 114, 115, 117, 104, 108, 109, 120]

# Polynomial regression model of degree 9
model_coefficients = np.polyfit(x_values, y_values, 9)
prediction_function = np.poly1d(model_coefficients)

# Predicted values
y_predicted = prediction_function(x_values)

# R-squared score
r_squared = r2_score(y_values, y_predicted)
print("R-squared score: ", r_squared)

# Generate points for the regression line
x_regression = range(90, 120)
y_regression = prediction_function(x_regression)

# Scatter plot of the data
plt.scatter(x_values, y_values)
# Plot the regression line
plt.plot(x_regression, y_regression, c="g")

# Calculate errors
errors = [actual - predicted for actual, predicted in zip(y_values, y_predicted)]
print("Errors: ", errors)

# Mean error
mean_error = np.mean(errors)
print("Mean error: ", mean_error)

# Standard deviation of errors
std_error = np.std(errors)
print("Standard deviation of errors: ", std_error)

# Error histogram
plt.figure()
plt.title("Error Histogram")
plt.xlabel("Error")
plt.ylabel("Frequency")
plt.hist(errors, bins=20, edgecolor='red')
plt.show()
