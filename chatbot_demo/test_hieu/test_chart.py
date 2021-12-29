import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

x = np.arange(0, 10, 0.1)
y = np.sin(x)

plt.plot(x, y)
fig.savefig('assets/saved_figure.png')
plt.close()