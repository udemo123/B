import matplotlib.pyplot as plt  
import numpy as np

var_x = np.array([1,34,67,39,7,9,12,35,10,3])
var_y = np.array([1,3,4,7,97,45,23,51,99,50])

plt.scatter(var_x,var_y)
plt.title('Scatter Plot')
plt.show() 