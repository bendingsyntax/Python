import numpy as np

def sigmond(x):
    return 1 / (1 + np.exp(-x))

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return sigmond(total)

class OurNeuralNetwork:
    def __init__(self):
        weights = np.array([0, 1])
        bais = 0

        self.h1 = Neuron(weights, bais)
        self.h2 = Neuron(weights, bais)
        self.o1 = Neuron(weights, bais)

    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)
        print(out_h1)
        print(out_h2)
        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))

        return out_o1

network = OurNeuralNetwork()
x = np.array([2, 3])
print(network.feedforward(x))