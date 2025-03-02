import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = np.pow(5 * x, 5) + np.pow(3 * x, 2) - np.pow(4 * x, 3)

fig, ax = plt.subplots()
plt.plot(x, y)
plt.show()