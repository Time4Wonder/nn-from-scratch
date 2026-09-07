#example script of one layer with 3 neurons. Without an activations function.
import numpy as np

# batch size of 3, shape(3,)
inputs  = [[1,2,3,2.5],
           [2.0,5.0,-1.0,2.0],
           [-1.5,2.7, 3.3, -0.8]]

# weihts of 3 neurons
weights =  [[0.2,0.8, -0.5, 1.0],
            [0.5, -0.91,0.26, -0.5],
            [-0.26,-0.27,0.17,0.87]]

# biases of the 3 neurons
biases = [2,3, 0.5]

print(weights)
print(np.array(inputs).T)
output = np.dot(inputs, np.array(weights).T) + biases
print(output)
