import numpy as np

y_true = np.array([27])
y_pred = np.array([10])

def mse_loss(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()

print(mse_loss(y_true, y_pred))