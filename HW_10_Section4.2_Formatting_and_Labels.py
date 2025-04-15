import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure with subplots
fig, axes = plt.subplots(2, 1, figsize=(8, 8))

# First subplot
axes[0].plot(x, y1, label="sin(x)", color='blue')
axes[0].set_xlabel("X-axis", fontsize=12, fontname='Arial', color='darkred')  # Custom X-axis label
axes[0].set_ylabel("Y-axis", fontsize=12, fontname='Arial', color='darkgreen')  # Custom Y-axis label
axes[0].set_title("Sine Function", fontsize=14, fontname='Verdana', color='purple')  # Custom title
axes[0].legend(loc="upper right")  # Add legend
axes[0].grid(True, linestyle='--', alpha=0.5)  # Customize gridlines

# Annotation
axes[0].text(2, 0.5, "Peak", fontsize=10, color='black')  # Add text annotation
axes[0].annotate("Turning Point", xy=(3.14, 0), xytext=(5, 0.5),
                 arrowprops=dict(facecolor='black', arrowstyle="->"))  # Arrow annotation

# Second subplot
axes[1].plot(x, y2, label="cos(x)", color='orange')
axes[1].set_xlabel("X-axis", fontsize=12, fontname='Arial', color='darkred')
axes[1].set_ylabel("Y-axis", fontsize=12, fontname='Arial', color='darkgreen')
axes[1].set_title("Cosine Function", fontsize=14, fontname='Verdana', color='purple')
axes[1].legend(loc="upper right")
axes[1].grid(True, linestyle='--', alpha=0.5)

# Customize axes properties using gca and set
for ax in axes:
    ax.set_xlim([0, 10])  # Set X-axis limits
    ax.set_ylim([-1.5, 1.5])  # Set Y-axis limits
    ax.set_xticks(np.arange(0, 11, 2))  # Customize X-axis ticks
    ax.set_yticks(np.arange(-1.5, 2, 0.5))  # Customize Y-axis ticks

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()
