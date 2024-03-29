import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Convert to DataFrame for easier manipulation
data = pd.DataFrame(data=np.c_[X, y], columns=iris.feature_names + ['target'])

# Consider only the first two features (sepal length and sepal width) for simplicity
selected_features = []
remaining_features = data.columns[:-1].tolist()

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(data.iloc[:, :-1], data['target'], test_size=0.2, random_state=42)

while remaining_features:
    best_feature = None
    best_model = None
    best_mse = float('inf')         #set best mean squared error to infinity

    for feature in remaining_features:
        current_features = selected_features + [feature]
        X_train_subset = X_train[current_features]
        X_test_subset = X_test[current_features]

        model = LinearRegression()
        model.fit(X_train_subset, y_train)
        predictions = model.predict(X_test_subset)

        mse = mean_squared_error(y_test, predictions)

        if mse < best_mse:
            best_mse = mse
            best_feature = feature
            best_model = model

    selected_features.append(best_feature)
    remaining_features.remove(best_feature)

    print(f"Added feature: {best_feature}, MSE: {best_mse:.4f}")

print("\nFinal Selected Features:", selected_features)
print("\nFinal Model Coefficients:", best_model.coef_)
print("\nIntercept:", best_model.intercept_)
