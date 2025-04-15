import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define the data
x = np.linspace(-np.pi, np.pi, 100)
y = np.linspace(-np.pi, np.pi, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)  # Surface function

# Create a 3D surface plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)  # Add a colorbar
ax.set_title("3D Surface Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()

# Create a 3D wireframe plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
wire = ax.plot_wireframe(X, Y, Z, color='blue', linewidth=0.7)
ax.set_title("3D Wireframe Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()

# Animate rotation of the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none')

plt.ion()
for angle in range(0, 360, 10):
    ax.view_init(elev=30, azim=angle)
    plt.draw()
    fig.canvas.flush_events()
    plt.pause(0.2)

plt.ioff()
plt.show()

# Add 3D contours
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
contour = ax.contour3D(X, Y, Z, levels=50, cmap='inferno')
fig.colorbar(contour, ax=ax, shrink=0.5, aspect=10)
ax.set_title("3D Contour Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
