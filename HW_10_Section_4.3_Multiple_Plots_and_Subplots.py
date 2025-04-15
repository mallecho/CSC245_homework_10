import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

# Data for plotting
x = np.linspace(0, 2 * np.pi, 500)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)  # Note: tangent function has discontinuities
y_exp = np.exp(x / 3)

# Create a 2x2 grid of subplots using subplot()
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)  # Top-left
plt.plot(x, y_sin, label='sin(x)', color='blue')
plt.title("Sine", fontsize=12)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.subplot(2, 2, 2)  # Top-right
plt.plot(x, y_cos, label='cos(x)', color='green')
plt.title("Cosine", fontsize=12)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.subplot(2, 2, 3)  # Bottom-left
plt.plot(x, y_tan, label='tan(x)', color='red')
plt.title("Tangent", fontsize=12)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.subplot(2, 2, 4)  # Bottom-right
plt.plot(x, y_exp, label='exp(x/3)', color='purple')
plt.title("Exponential", fontsize=12)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.tight_layout()

# Save figure with subplot() to a PDF
with PdfPages("subplot_example.pdf") as pdf:
    pdf.savefig()  # Save current figure
plt.close()

# Create the same plot using subplots()
fig, axes = plt.subplots(2, 2, figsize=(10, 8), sharex=True, sharey=True)

# Plot each function in its respective subplot
axes[0, 0].plot(x, y_sin, label='sin(x)', color='blue')
axes[0, 0].set_title("Sine")
axes[0, 0].grid(True)

axes[0, 1].plot(x, y_cos, label='cos(x)', color='green')
axes[0, 1].set_title("Cosine")
axes[0, 1].grid(True)

axes[1, 0].plot(x, y_tan, label='tan(x)', color='red')
axes[1, 0].set_title("Tangent")
axes[1, 0].grid(True)

axes[1, 1].plot(x, y_exp, label='exp(x/3)', color='purple')
axes[1, 1].set_title("Exponential")
axes[1, 1].grid(True)

# Synchronize zooming/panning across all axes
fig.tight_layout()
plt.subplots_adjust(hspace=0.4, wspace=0.4)
plt.savefig("subplots_example.pdf")  # Export to PDF

plt.show()

