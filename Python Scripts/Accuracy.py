import numpy as np
y_true = [0, 0, 1, 1, 0, 1, 0, 1, 0]
y_pred = [0, 0, 1, 0, 0, 1, 0, 1, 1]

def accuracy():
    acc = np.sum(np.equal(y_true, y_pred)) / len(y_true)
    return round(acc, 4)
print(accuracy())
