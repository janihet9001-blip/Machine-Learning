import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Data
data = {
    'size': [1000, 1500, 2000],
    'bedrooms': [2, 3, 4],
    'price': [30, 50, 80]
}

df = pd.DataFrame(data)

# Input and Output
X = df[['size', 'bedrooms']]
Y = df['price']

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Model
model = LinearRegression()
model.fit(X_scaled, Y)

# Prediction (IMPORTANT: scale input)
new_data = [[1800, 3]]
new_scaled = scaler.transform(new_data)

print(model.predict(new_scaled))

# Coefficients
print("Coefficients (m1, m2):", model.coef_)
print("Intercept (b):", model.intercept_)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['size'], df['bedrooms'], Y)

ax.set_xlabel('Size')
ax.set_ylabel('Bedrooms')
ax.set_zlabel('Price')

plt.show()