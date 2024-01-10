import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Define the neural network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights with random values
        self.weights_input_hidden = np.random.uniform(size=(input_size, hidden_size))
        self.weights_hidden_output = np.random.uniform(size=(hidden_size, output_size))

    def forward(self, inputs):
        # Forward pass
        self.hidden_layer_input = np.dot(inputs, self.weights_input_hidden)
        self.hidden_layer_output = sigmoid(self.hidden_layer_input)

        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output)
        self.predicted_output = sigmoid(self.output_layer_input)

        return self.predicted_output

    def backward(self, inputs, targets, learning_rate):
        # Backward pass
        error = targets - self.predicted_output

        # Calculate the gradients
        output_error = error * sigmoid_derivative(self.predicted_output)
        hidden_layer_error = output_error.dot(self.weights_hidden_output.T) * sigmoid_derivative(self.hidden_layer_output)

        # Update weights
        self.weights_hidden_output += self.hidden_layer_output.T.dot(output_error) * learning_rate
        self.weights_input_hidden += inputs.T.dot(hidden_layer_error) * learning_rate

    def train(self, inputs, targets, epochs, learning_rate):
        for epoch in range(epochs):
            # Forward and backward pass for each training example
            for i in range(len(inputs)):
                input_data = np.array([inputs[i]])
                target_data = np.array([targets[i]])

                self.forward(input_data)
                self.backward(input_data, target_data, learning_rate)

            # Calculate and print the mean squared error for each epoch
            mse = np.mean((targets - self.predict(inputs))**2)
            print(f"Epoch {epoch + 1}/{epochs}, Mean Squared Error: {mse}")

    def predict(self, inputs):
        # Make predictions
        return self.forward(np.array(inputs))

# Example usage
# Assuming a binary classification task with 2 input features, 2 hidden layer neurons, and 1 output neuron
input_size = 2
hidden_size = 2
output_size = 1

# Generate random training data
np.random.seed(0)
inputs = np.random.rand(100, input_size)
targets = np.random.randint(2, size=(100, 1))

# Initialize the neural network
neural_network = NeuralNetwork(input_size, hidden_size, output_size)

# Train the neural network
neural_network.train(inputs, targets, epochs=1000, learning_rate=0.1)

# Make predictions
new_data = np.array([[0.2, 0.8], [0.6, 0.4]])
predictions = neural_network.predict(new_data)
print("Predictions:", predictions)
