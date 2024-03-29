import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score, RepeatedKFold
import matplotlib.pyplot as plt

# Generate example data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Ridge regression model
alpha = 1.0
ridge_model = Ridge(alpha=alpha)

# Cross-validation
n_folds, n_repeats = 5, 10
rkf = RepeatedKFold(n_splits=n_folds, n_repeats=n_repeats, random_state=42)
mae_scores = -cross_val_score(ridge_model, X, y.ravel(), scoring='neg_mean_absolute_error', cv=rkf)

# Report mean absolute error
mean_mae = np.mean(mae_scores)
print("Mean Absolute Error:", mean_mae)

# Fit the model on the entire dataset
ridge_model.fit(X, y)

# Make predictions on the entire dataset
y_pred = ridge_model.predict(X)

# Plot results
plt.scatter(X, y, label="Actual")
plt.plot(X, y_pred, color='red', label="Predicted")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Ridge Regression with Cross-Validation")
plt.legend()
plt.show()
