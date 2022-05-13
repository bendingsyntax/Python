import numpy as np

def hTan(x):
    return abs(np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

def deriv_hTan(x):
    fx = hTan(x)
    return fx * (1 - fx)

def mean_square_error(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()

class NN:
    def __init__(self):
        #Weights
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()

        #Biases
        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()

    def feedforward(self, x):
        h1 = hTan(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        h2 = hTan(self.w3 * x[0] + self.w4 * x[1] + self.b2)
        o1 = hTan(self.w5 * h1 + self.w6 * h2 + self.b3)
        return o1

    def train(self, data, all_y_trues):
        learn_rate = .1
        epochs = 1000

        for epoch in range(epochs):
            for x, y_true in zip(data, all_y_trues):
                sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                h1 = hTan(sum_h1)

                sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                h2 = hTan(sum_h2)

                sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = hTan(sum_o1)
                y_pred = o1

                d_L_d_ypred = -2 * (y_true - y_pred)

                d_ypred_d_w5 = h1 * deriv_hTan(sum_o1)
                d_ypred_d_w6 = h2 * deriv_hTan(sum_o1)
                d_ypred_d_b3 = deriv_hTan(sum_o1)

                d_ypred_d_h1 = self.w5 * deriv_hTan(sum_o1)
                d_ypred_d_h2 = self.w6 * deriv_hTan(sum_o1)

                d_h1_d_w1 = x[0] * deriv_hTan(sum_h1)
                d_h1_d_w2 = x[1] * deriv_hTan(sum_h1)
                d_h1_d_b1 = deriv_hTan(sum_h1)

                d_h2_d_w3 = x[0] * deriv_hTan(sum_h2)
                d_h2_d_w4 = x[1] * deriv_hTan(sum_h2)
                d_h2_d_b2 = deriv_hTan(sum_h2)

                self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
                self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1

                self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
                self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
                self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2

                self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
                self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
                self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_b3

            if epoch % 10 == 0:
                y_pred = np.apply_along_axis(self.feedforward, 1, data)
                loss = mean_square_error(all_y_trues, y_pred)
                print("Epoch %d loss: %.3f" % (epoch, loss))
data = np.array([
    [-2, -1],
    [25, 6],
    [17, 4],
    [-15, -6],
])
all_y_trues = np.array([
    1,
    1,
    1,
    1,
])

network = NN()
network.train(data, all_y_trues)