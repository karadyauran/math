import numpy as np
import matplotlib.pyplot as plt

A = np.array([2, 3, 4])
u = np.array([-2, -3, -4])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, A[0], A[1], A[2], color='black', label='Vector')
ax.quiver(0, 0, 0, u[0], u[1], u[2], color='red', label='C Vector')

ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_zlim([0, 10])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()
