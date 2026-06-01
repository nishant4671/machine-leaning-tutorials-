# Generate 10 synthetic data points with a known linear relationship (e.g., y = 3x + 2 + noise). Plot them.



import numpy as np  # numpy is a library ofr the numerical operations in pyhton , we are going to use it  
import matplotlib.pyplot as plt  # matplotlib is a library for plotting in python, we are going to use it to plot the data points

# what does plotting mean ? Plotting refers to the process of creating a visual representation of data. It involves using graphs, charts, or other visual tools to display the relationships between different variables in a dataset. In this context, we will be plotting the synthetic data points to visualize the linear relationship between the independent variable (x) and the dependent variable (y). This helps us understand how well the data follows the expected linear pattern (y = 3x + 2 + noise).





# Generate 10 synthetic data points with a known linear relationship (e.g., y = 3x + 2 + noise)

def generate_synthetic_data(num_points):
    x = np.random.rand(num_points) * 10     # Generate random x values between 0 and 10
    noise = np.random.normal(0, 1, num_points)  # Generate random noise with mean 0 and standard deviation 1
    y = 3 * x + 2 + noise  # Calculate y values based on the linear relationship with added noise
    return x, y



# what we did in the fiunctin above , we defined a function called generate_synthetic_data that takes in the number of data pints we want to generate as an argument 

# x = np.random.rand(num_points) * 10 meaning of this line 
# this line generates an array of random numbers 
# between 0 and 1 using np.random.rand(num_points) and then scales it to be between 0 and 10 by multiplying it by 10. This gives us the x values for our synthetic data points.


