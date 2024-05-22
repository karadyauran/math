import numpy as np

X = np.array([1, 2, 3, 4])

weights = np.array([0.5, 1.5, -2.0, 1.0])

prediction = np.dot(X, weights)
print(f"Prediction: {prediction}")
