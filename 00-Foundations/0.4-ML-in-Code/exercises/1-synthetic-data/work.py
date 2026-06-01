import numpy as np
import matplotlib.pyplot as plt

def generate_synthetic_data(num_points):
    x = np.random.rand(num_points) * 10
    noise = np.random.normal(0, 1, num_points)
#     np.random.normal(0, 1, num_points) generates a NumPy array of length num_points, where each element is a random number drawn from a normal (Gaussian) distribution with:

# mean = 0

# standard deviation = 1
    y = 3 * x + 2 + noise
    return x, y




# explaining above function : 

# the function genarate_synthetic data takes an argument num_points which specifies hwo many points to generate 
# 1. It generates `num_points` random x values between 0 and 10 using `np.random.rand(num_points) * 10`.
# 2. It creates random noise from a normal distribution with mean 0 and standard deviation 1 using `np.random.normal(0, 1, num_points)`.
# 3. It calculates the corresponding y values using the linear equation `y = 3x + 2` and adds the generated noise to create a more realistic dataset.

# what does random.rand and random.normal do ? 

# `np.random.rand(num_points)` generates an array of `num_points` random numbers uniformly distributed between 0 and 1. When multiplied by 10, it scales the values to be between 0 and 10.
# `np.random.normal(0, 1, num_points)` generates an array of `num_points` random numbers drawn from a normal (Gaussian) distribution with a mean of 0 and a standard deviation of 1. This is often used to simulate noise in data.

# .random is a sub-module within NumPy that contains functions for generating random numbers

# Function	What it does
# np.random.rand(n)	Generates n random numbers between 0 and 1 (uniform distribution)
# np.random.normal(mean, std, n)	Generates n random numbers from a normal (Gaussian) distribution
# np.random.uniform(low, high, n)	Generates n random numbers uniformly between low and high
# np.random.randint(low, high, n)	Generates n random integers between low (inclusive) and high (exclusive)





# Generate 10 points
x, y = generate_synthetic_data(10)

#here we are calling a fucntion 



#  these lines of code are used to visualize the generated synthetic data using a scatter plot., the linrary used  here is matplotlib.pyplot which is commonly imported as plt.
#   x, y – the data arrays to plot. The first argument is the x-coordinates, second is the y-coordinates

plt.scatter(x, y, color='blue', label='Noisy data')
# plt.scatter us a function from matplotlib.pyplot that screates a scatter plot of the data points . scatter plot means a type of plot that displays individual data points as markers on a to dimensions graph with x and y axis , in this case we are plotting x values on the x axis and y values on the y axis 
# color='blue' – sets the color of all points to blue.

# label='Noisy data' – assigns a name to this dataset, which will appear in the legend.

# What it does: Draws 10 points (or however many x and y have) on the plot. Each point's position is determined by the corresponding values in the x and y arrays. The points will be colored blue, and they will be labeled "Noisy data" in the legend.

plt.xlabel('x')

# Line 2: plt.xlabel('x')
# plt.xlabel – sets the label text on the x-axis.

# 'x' – the string that appears below the x-axis.

# What it does: Labels the horizontal axis as "x".




plt.ylabel('y')

# same as above but fro the y axis 


plt.title('Synthetic Data: y = 3x + 2 + noise')


# Line 4: plt.title('Synthetic Data: y = 3x + 2 + noise')
# plt.title – adds a title above the plot.

# The string inside is the title text.

# What it does: Gives context to the viewer about what the plot represents.


plt.legend()
# Line 5: plt.legend()
# plt.legend – displays the legend box on the plot.

# It automatically uses the label strings from previous plotting commands (like label='Noisy data').

# What it does: Shows a small box that maps colors/styles to data descriptions.

plt.grid(True, alpha=0.3)

# Line 6: plt.grid(True, alpha=0.3)
# plt.grid – adds a grid behind the data points.

# True – turns the grid on (default is off).

# alpha=0.3 – sets transparency of the grid lines. 1.0 is solid, 0.0 is invisible. 0.3 means 30% opacity (faint grey lines).

# What it does: Makes it easier to estimate coordinates of points.



plt.show()

# Line 7: plt.show()
# plt.show() – displays the plot window.

# This is the final command that actually renders the plot on screen. Without it, nothing would appear (in scripts/notebooks without %matplotlib inline).

# What it does: Renders all the previous commands and pops up the plot.