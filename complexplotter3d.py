import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

f = lambda z: (-1+0j)**(1/z)

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure(figsize=(10, 10))
ax = fig.gca(projection='3d')
z = np.linspace(1, 10, 1000)
x = np.real(f(z))
y = np.imag(f(z))
ax.plot(x, y, z, label='complex')
ax.set_xlabel("Real")
ax.set_ylabel("Imaginary")
ax.legend()

plt.show()

