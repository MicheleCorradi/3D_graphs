from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.outer(np.linspace(-2,2,10), np.ones(10))
y = x.copy().T
z = np.cos(x ** 2 + y ** 3)
fig = plt.figure()
#sintassi per il plotting 3-D
ax = plt.axes(projection = '3d')
#sintassi per il plotting
ax.plot_surface(x,y,z, cmap='viridis', edgecolor='green')
ax.set_title('Surface plot python.hub')
plt.show()