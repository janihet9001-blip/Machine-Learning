# Step 1: Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# Step 2: Mean
mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

# Step 3: Calculate slope (m)
num = sum((x[i] - mean_x) *(y[i] - mean_y) for i in range (len(x)))
den = sum((x[i] - mean_x) ** 2 for i in range (len(x)))

m = num / den

# Step 4 : Calulate intercept(b)

b = mean_y - m * mean_x

print("Slope (m):", m)
print("Intercept (b):", b)

x_new = 6
y_pred = m*x_new + b 

print("Prediction for x=6:", y_pred)

# Calculate MSE
total_error = 0

for i in range(len(x)):
    y_hat = m * x[i] + b
    total_error += (y[i] - y_hat) ** 2

mse = total_error / len(x)
print("Mean Squared Error:", mse)

import matplotlib.pyplot as plt

# Original points
plt.scatter(x, y)

# Regression line
y_line = [m * xi + b for xi in x]
plt.plot(x, y_line)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression")

plt.show()