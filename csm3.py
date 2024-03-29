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
selected_features = data.columns[:-1].tolist()

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(data.iloc[:, :-1], data['target'], test_size=0.2, random_state=42)

while len(selected_features) > 1:
    worst_feature = None
    worst_model = None
    worst_mse = float('inf')

    for feature in selected_features:
        current_features = selected_features.copy()
        current_features.remove(feature)

        X_train_subset = X_train[current_features]
        X_test_subset = X_test[current_features]

        model = LinearRegression()
        model.fit(X_train_subset, y_train)
        predictions = model.predict(X_test_subset)

        mse = mean_squared_error(y_test, predictions)

        if mse < worst_mse:
            worst_mse = mse
            worst_feature = feature
            worst_model = model

    selected_features.remove(worst_feature)

    print(f"Removed feature: {worst_feature}, MSE: {worst_mse:.4f}")

print("\nFinal Selected Features:", selected_features)
print("\nFinal Model Coefficients:", worst_model.coef_)
print("\nIntercept:", worst_model.intercept_)
