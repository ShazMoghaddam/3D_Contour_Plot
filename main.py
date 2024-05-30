import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# Create a meshgrid of x and y values
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)


# Define a function to calculate the z value (height) based on x and y
def f(a, b):
    return np.sin(np.sqrt(a ** 2 + b ** 2))


# Calculate the z value for the meshgrid
Z = f(X, Y)
# Create a three-dimensional contour plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
contour = ax.contour3D(X, Y, Z, 50, cmap="viridis")

# Add labels and color bar.
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
fig.colorbar(contour, ax=ax, label="Z values")

# Show the plot.
plt.show()
