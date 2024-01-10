import numpy as np

class Neuralnetworkneuron:
  def __init__(self,w_size):
    self.weights = np.random.randn(w_size)
    self.bias = np.random.randn()

  def sigmoid(self,weightsum):
    res = 1/(1+np.exp(- weightsum))
    return res

  def calculate(self, inputs):
    weightsum = np.dot(inputs, self.weights) + self.bias
    result =self.sigmoid(weightsum)
    return result

inputsize = 4

neuralnet = Neuralnetworkneuron(inputsize)
# inputs=[]
# for i in range(inputsize):
#   inputs.append(float(input()))

inputs = [0.34,0.84,0.21,0.43]



output = neuralnet.calculate(inputs)
print(output)
