import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Load data
data = pd.read_csv("Data/data.csv")

# Step 2: Separate input and output
X = data[['size']] #Input
Y = data['price']  #Output

# Step 3: Train-Test Split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

# Step 4: Train model
model = LinearRegression()
model.fit(X_train,Y_train)

# Step 5: Predict
Y_pred = model.predict(X_test)

# Step 6: Evaluate
mse = mean_squared_error(Y_test, Y_pred)

print("MSE:", mse)

# Step 7: Predict new value
print("Prdict:",model.predict(pd.DataFrame([[1900]], columns=['size'])))

import matplotlib.pyplot as plt

# Plot actual data
plt.scatter(X, Y)

# Plot regression line
plt.plot(X, model.predict(X))

plt.xlabel("Size")
plt.ylabel("Price")
plt.title("Linear Regression")

plt.show()