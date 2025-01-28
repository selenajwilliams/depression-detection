import matplotlib.pyplot as plt
import numpy as np

# this tests that GUI can be used in Oscar -- it can!

# Set up the figure and axis
fig, ax = plt.subplots()

# Create a circle with a center at (0, 0) and radius 1
circle = plt.Circle((0, 0), radius=1, edgecolor='blue', facecolor='none', linewidth=2)

# Add the circle to the axis
ax.add_patch(circle)

# Set the aspect ratio of the plot to be equal to ensure the circle is not distorted
ax.set_aspect('equal')

# Set limits for the plot
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Display the plot
plt.show()
