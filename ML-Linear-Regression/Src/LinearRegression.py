### Manually solve the Promblem on Linear Regression


x = [1,2,3,4,5]
y = [2,4,5,4,5]

#Calulate mean
mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

#Calulate slope (m)
num = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range (len(x)))
den = sum((x[i] - mean_x) ** 2 for i in range (len(x)))

m = num/den

#Calulate intercept(b)
b = mean_y - m * mean_x

print("Slope(m):",m)
print("Intercept(b):",b)

#Predication
x_new = 6
y_pred = m * x_new + b

print("Prediction for x = 6:",y_pred) 


import matplotlib.pyplot as plt

plt.scatter(x, y, color='blue')
plt.plot(x, [m*i + b for i in x], color='red')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression")

plt.show()



### BY using Scikit Library
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt

# model = LinearRegression()
# model.fit([[1],[2],[3],[4],[5]],[2,4,5,4,5])

# print(model.predict([[6]]))

# plt.scatter(x,y,color = 'Blue')
# plt.plot(x,[m*i + b for i in x],color = 'red')

# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Linear Regression")

# plt.show()


