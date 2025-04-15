import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.animation import FuncAnimation

# Task 1: Use ginput() to capture mouse clicks and annotate those points
def ginput_example():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o-')
    plt.title("Click on Points to Annotate")
    points = plt.ginput(n=2, timeout=30)  # Allow two clicks
    for point in points:
        ax.annotate(f"({point[0]:.2f}, {point[1]:.2f})", xy=point, textcoords="offset points", xytext=(10, 10),
                    arrowprops=dict(arrowstyle='->'))
    plt.show()

# Task 2: Add interactivity using sliders
def slider_example():
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.25, bottom=0.25)
    t = np.arange(0.0, 1.0, 0.001)
    s = np.sin(2 * np.pi * t)
    l, = plt.plot(t, s, lw=2)

    ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])  # Slider location
    slider = Slider(ax_slider, 'Frequency', 0.1, 10.0, valinit=1.0)

    def update(val):
        freq = slider.val
        l.set_ydata(np.sin(2 * np.pi * freq * t))
        fig.canvas.draw_idle()

    slider.on_changed(update)
    plt.show()

# Task 3: Use datacursormode to explore points interactively
def datacursor_example():
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y, label="sin(x)")
    ax.set_title("Explore Points Interactively")
    plt.legend()
    plt.show()

# Task 4: Create an animated line plot using animatedline()
def animated_line_example():
    import matplotlib
    print(f"Using backend: {matplotlib.get_backend()}")  # Check the current backend
    matplotlib.use("TkAgg")  # Ensure a compatible backend for animations

    fig, ax = plt.subplots()
    x_data, y_data = [], []
    line, = ax.plot([], [], lw=2, color="blue")

    ax.set_xlim(0, 10)
    ax.set_ylim(-1.5, 1.5)
    ax.set_title("Animated Line Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    # Initialize the plot
    def init():
        line.set_data([], [])
        return line,

    # Update the plot on each frame
    def update(frame):
        x_data.append(frame)
        y_data.append(np.sin(frame))
        line.set_data(x_data, y_data)
        return line,

    ani = FuncAnimation(
        fig, update, frames=np.linspace(0, 10, 100), init_func=init, blit=False  # Disabled blit for broader compatibility
    )
    plt.show()

# Task 5: Combine plot3() and comet3() to show 3D trajectories over time
def comet3_example():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    t = np.linspace(0, 20, 500)
    x = np.sin(t)
    y = np.cos(t)
    z = t / 10

    def update(num):
        ax.clear()
        ax.plot(x[:num], y[:num], z[:num], 'b-')  # Trajectory
        ax.scatter(x[num], y[num], z[num], c='r', marker='o')  # Current point
        ax.set_xlim([-1.1, 1.1])
        ax.set_ylim([-1.1, 1.1])
        ax.set_zlim([0, 2])
        ax.set_title("3D Trajectory Over Time")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_zlabel("Z-axis")

    ani = FuncAnimation(fig, update, frames=len(t), interval=50)
    plt.show()

# Call each function to test the respective tasks
ginput_example()
slider_example()
datacursor_example()
animated_line_example()
comet3_example()
