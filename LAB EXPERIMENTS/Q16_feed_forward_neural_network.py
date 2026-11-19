import math
inputs = [1.0, 0.5]
weights = [[0.2, 0.4], [0.3, 0.1]]
biases = [0.1, 0.2]
def sigmoid(x): return 1/(1+math.exp(-x))
hidden = [sigmoid(sum(x*w for x,w in zip(inputs, row)) + b) for row,b in zip(weights,biases)]
out = sigmoid(hidden[0]*0.7 + hidden[1]*0.6 + 0.1)
print("Input layer:", inputs)
print("Hidden layer:", [round(v,4) for v in hidden])
print("Network output:", round(out,4))
