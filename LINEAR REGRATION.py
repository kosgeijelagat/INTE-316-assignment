import numpy as np
import matplotlib.pyplot as plt

# Generate some data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([1, 3, 2, 5, 4])

# Create and fit the model
model = LinearRegression()
model.fit(x, y)

# Predict
y_pred = model.predict(x)

# Plot the data and the regression line
plt.scatter(x, y, color='blue')
plt.plot(x, y_pred, color='red')
plt.show()
