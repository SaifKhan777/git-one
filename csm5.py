import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Generate some example data (binary classification with both classes)
np.random.seed(42)
X = 2 * np.random.rand(200, 2)
y = (3 * X[:, 0] + 2 * X[:, 1] + 1 + np.random.randn(200)) > 0

# Ensure there are examples from both classes
while len(np.unique(y)) < 2:
    y = (3 * X[:, 0] + 2 * X[:, 1] + 1 + np.random.randn(200)) > 0

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic regression model
logreg_model = LogisticRegression()

# Train the model
logreg_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = logreg_model.predict(X_test)

# Evaluate the model using confusion matrix
conf_mat = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

# Print the confusion matrix and accuracy
print("Confusion Matrix:")
print(conf_mat)
print("\nAccuracy:", accuracy)

# Visualize confusion matrix using a colorful heatmap
sns.heatmap(conf_mat, annot=True, fmt="d", cmap="viridis", cbar=False,
            xticklabels=["Predicted 0", "Predicted 1"],
            yticklabels=["Actual 0", "Actual 1"])
plt.xlabel("Predicted label")
plt.ylabel("True label")
plt.title("Confusion Matrix")
plt.show()

# Additional evaluation metrics
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
