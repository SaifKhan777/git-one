import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=100):
        self.weights = np.zeros(input_size + 1)
        self.learning_rate = learning_rate
        self.epochs = epochs

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        return 1 if summation > 0 else 0

    def train(self, training_inputs, labels):
        for _ in range(self.epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)

# Example usage:
# Suppose you have training data for OR gate
training_inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

labels = np.array([0, 1, 1, 1])  # OR gate labels

# Create and train the perceptron
perceptron = Perceptron(input_size=2)
perceptron.train(training_inputs, labels)

# Test the trained perceptron
test_inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

for test_input in test_inputs:
    prediction = perceptron.predict(test_input)
    print(f"Input: {test_input}, Prediction: {prediction}")
