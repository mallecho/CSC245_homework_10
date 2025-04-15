import numpy as np
import matplotlib.pyplot as plt


# 1. Create a basic line plot of the function y = sin(x) over the interval [0, 2*pi]
x = np.linspace(0, 2 * np.pi, 100)  # Define x values
y_sin = np.sin(x)  # Compute y = sin(x)

plt.figure(figsize=(8, 5))  # Create a new figure
plt.plot(x, y_sin)  # Plot the sine function
plt.xlabel('x')  # Label the x-axis
plt.ylabel('y = sin(x)')  # Label the y-axis
plt.title('Sine Function')  # Add a title
plt.show()  # Display the plot

# 2. Explain the difference between plot(x, y), plot(y), and plot(x1, y1, x2, y2) in Python
# Example 1: plot(x, y) - Explicit x and y values
plt.figure()
plt.plot(x, y_sin)
plt.title('Example of plot(x, y)')
plt.show()

# Example 2: plot(y) - Implicit x values are indices
plt.figure()
plt.plot(y_sin)  # Only y is provided; x defaults to indices
plt.title('Example of plot(y)')
plt.show()

# Example 3: plot(x1, y1, x2, y2) - Multiple lines on the same plot
y_cos = np.cos(x)  # Compute y = cos(x)
plt.figure()
plt.plot(x, y_sin, label='y = sin(x)')
plt.plot(x, y_cos, label='y = cos(x)')
plt.title('Example of Multiple Lines')
plt.legend()  # Add a legend
plt.show()

# 3. Customize line styles, colors, and markers
plt.figure()
plt.plot(x, y_cos, 'r--o', label='y = cos(x)')  # Red dashed line with circle markers
plt.xlabel('x')
plt.ylabel('y = cos(x)')
plt.title('Cosine Function with Customized Line Style')
plt.legend()
plt.show()

# 4. Save a figure to a PNG file with 300 dpi using savefig()
plt.figure()
plt.plot(x, y_cos, 'r--o', label='y = cos(x)')
plt.xlabel('x')
plt.ylabel('y = cos(x)')
plt.title('Cosine Function with Customized Line Style')
plt.legend()
plt.savefig('cosine_function_300dpi.png', dpi=300)  # Save the plot as PNG with 300 DPI
plt.show()

# 5. Plot multiple lines on the same axes
plt.figure()
plt.plot(x, y_sin, 'b-', label='y = sin(x)', linewidth=2)  # Blue solid line
plt.plot(x, y_cos, 'r--o', label='y = cos(x)', linewidth=2)  # Red dashed line
plt.xlabel('x')
plt.ylabel('y')
plt.title('Multiple Lines on the Same Axes')
plt.legend(loc='best')  # Add legend
plt.grid(True)  # Add a grid
plt.axis([0, 2 * np.pi, -1.5, 1.5])  # Adjust axis limits
plt.show()
