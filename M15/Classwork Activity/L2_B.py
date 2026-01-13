import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10, 11, 1)
y1 = (2*x) + 1
y2 = (2*x*x) + 2
y3 = (3*x*x*x) + 3
plt.plot(x, y1, 'g', linewidth=3, label='y=2x+1')
plt.plot(x, y2, 'r', linewidth=3, label='y=2x^2+2')
plt.fill_between(x, y2, y3, color='g', alpha=0.5)
plt.plot(x, y3, 'b', linewidth=3, label='y=3x^3+3')
plt.legend()
plt.grid()
plt.show()