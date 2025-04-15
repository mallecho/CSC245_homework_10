import matplotlib.pyplot as plt
import numpy as np

# Data for the plots
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 12]
x = np.random.normal(0, 1, 1000)  # Random normal data for histogram
scatter_x = np.random.uniform(0, 10, 100)  # Scatter plot data (x)
scatter_y = scatter_x + np.random.normal(0, 1, 100)  # Noisy y data
scatter_size = np.random.uniform(20, 200, 100)  # Size variable for scatter plot
area_x = np.linspace(0, 10, 100)
area_y1 = np.sin(area_x)
area_y2 = np.cos(area_x)

# Bar plot
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.grid(axis='y', linestyle='-', alpha=0.5)  # Changed to solid line for compatibility
plt.show()

# Horizontal bar plot
plt.figure(figsize=(10, 6))
plt.barh(categories, values, color='lightcoral', edgecolor='black', alpha=0.7)
plt.title("Horizontal Bar Plot")
plt.xlabel("Values")
plt.ylabel("Categories")
plt.grid(axis='x', linestyle='-', alpha=0.5)  # Changed to solid line for compatibility
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(x, bins=30, color='gold', edgecolor='black', alpha=0.8)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='-', alpha=0.5)  # Changed to solid line for compatibility
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(scatter_x, scatter_y, s=scatter_size, c='purple', alpha=0.6, edgecolors='none')  # Removed edgecolors warning
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True, linestyle='-', alpha=0.5)  # Changed to solid line for compatibility
plt.show()

# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightpink', 'lightyellow'])
plt.title("Pie Chart")
plt.show()

# Area plot
plt.figure(figsize=(10, 6))
plt.fill_between(area_x, area_y1, color='blue', alpha=0.5, label="sin(x)")
plt.fill_between(area_x, area_y2, color='orange', alpha=0.5, label="cos(x)")
plt.title("Area Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True, linestyle='-', alpha=0.5)  # Changed to solid line for compatibility
plt.show()

# Stacked area plot
plt.figure(figsize=(10, 6))
plt.stackplot(area_x, area_y1, area_y2, labels=["sin(x)", "cos(x)"], colors=['blue', 'orange'], alpha=0.5)
plt.title("Stacked Area Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc="upper right")
plt.grid(True, linestyle='-', alpha=0.5)  # Changed to solid line for compatibility
plt.show()





#Use Cases:


#Bar and Horizontal Bar Plots:
#Ideal for visualizing categorical data, comparisons, or rankings.


#Histogram:
#Useful for analyzing distributions or frequency of data points.


#Scatter Plot:
#Great for visualizing relationships or correlations between noisy data with an extra dimension (e.g., size or color).


#Pie Chart:
#Effective for showing proportions of categorical data but can become cluttered with too many categories.


#Area and Stacked Area Plots:

#Area plots highlight trends over a continuous range, while stacked area plots emphasize the contribution of individual components to the total.