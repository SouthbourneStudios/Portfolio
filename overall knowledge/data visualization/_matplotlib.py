import matplotlib.pyplot as plt
import numpy as np # Often used for generating sample data


def line():
    # Prepare the data
    x_values = np.array([0, 1, 2, 3, 4, 5])
    y_values = x_values ** 2  # Calculate y = x^2

    # Create the plot
    plt.figure()  # Optional: Create a new figure
    plt.plot(x_values, y_values) # single array args only provides one plotting, either x or y values

    # Add labels for clarity (more on this in a later section)
    plt.xlabel("X Values")
    plt.ylabel("Y Values (X squared)")
    plt.title("A Simple Line Plot")

    # Display the plot
    plt.show()

# Plotting Multiple Lines
def multiline():
    # Prepare data for two lines
    x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
    y1 = np.sin(x)
    y2 = np.cos(x)

    # Create the plot
    plt.figure()
    plt.plot(x, y1)  # First line (e.g., sine wave)
    plt.plot(x, y2)  # Second line (e.g., cosine wave)

    # Add labels and title
    plt.xlabel("X Value")
    plt.ylabel("Function Value")
    plt.title("Plotting Multiple Lines (Sine and Cosine)")

    # Display the plot
    plt.show()

# multiline()

# Scatter plots:
#       are a primary visualization tool used to understand the relationship between two distinct variables.

#       A scatter plot uses individual dots or markers to represent the values obtained for two different numerical variables.
#       One variable determines the position on the horizontal axis (x-axis), and the other determines the position on the vertical axis (y-axis).
#       Unlike line plots, the points are generally not connected by lines because the focus is on the pattern formed by the distribution of points,
#       not a sequential progression.

def scatter():
    # Sample data: Temperature (Celsius) and Scoops Sold
    temperatures = np.array([14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2])
    scoops_sold = np.array([215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408])

    # Create the figure and axes objects
    fig, ax = plt.subplots()

    # Create the scatter plot
    ax.scatter(temperatures, scoops_sold,
               c='#fd7e14',  # Orange color
               s=60,  # Larger marker size
               marker='s',  # Square marker
               alpha=0.7)  # Slight transparency

    # Add labels and title (as learned previously)
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Ice Cream Scoops Sold")
    ax.set_title("Temperature vs. Ice Cream Sales")

    # Display the plot
    plt.show()

def bar_chart():
    # Data
    fruit_types = ['Apples', 'Oranges', 'Bananas', 'Grapes']
    counts = [15, 12, 20, 8]

    # Create the figure and axes objects
    fig, ax = plt.subplots()

    # Create the bar chart with a different color
    # Vertical
    #ax.bar(fruit_types, counts, color='#74c0fc')  # Using a light blue color

    # Horizontal
    ax.barh(fruit_types, counts, color='#e74c3c')

    # Add labels and title for clarity
    ax.set_xlabel('Fruit Type')
    ax.set_ylabel('Quantity')
    ax.set_title('Number of Fruits in the Basket')

    # Display the plot
    plt.show()

# bar_chart()

def histogram():
    # Generate some sample data (e.g., test scores)
    # Using a normal distribution centered around 70 with a standard deviation of 10
    np.random.seed(42)  # for reproducible results
    scores = np.random.normal(loc=70, scale=10, size=200)

    print(scores.shape)

    # Create the histogram
    plt.figure(figsize=(8, 5))  # Optional: Adjust figure size
    plt.hist(scores, color='#339af0')  # Pass the data to plt.hist()

    # Add labels and title for clarity
    plt.xlabel("Test Score")
    plt.ylabel("Number of Students (Frequency)")
    plt.title("Distribution of Test Scores")

    # Display the plot
    plt.show()

# histogram()

# Understanding and controlling these bins is fundamental to creating informative histograms.
# The choice of bins can significantly alter the appearance and, consequently, the interpretation of the data's distribution.
def bins_histogram():
    # Generate some sample data
    np.random.seed(42)  # for reproducibility
    data = np.random.randn(200) * 1.5 + 5  # 200 points, mean=5, std=1.5

    # --- Plotting with different bin counts ---

    plt.figure(figsize=(12, 4))  # Create a figure to hold the subplots

    # Plot 1: Too few bins
    plt.subplot(1, 3, 1)  # (rows, columns, panel number)
    plt.hist(data, bins=5, color='#228be6', edgecolor='white')
    plt.title('Too Few Bins (bins=5)')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    # Plot 2: Default number of bins (Matplotlib decides)
    plt.subplot(1, 3, 2)
    plt.hist(data, color='#15aabf', edgecolor='white')  # Let Matplotlib choose bins
    plt.title('Default Bins')
    plt.xlabel('Value')
    # plt.ylabel('Frequency') # Optionally hide y-label for middle plot

    # Plot 3: Too many bins
    plt.subplot(1, 3, 3)
    plt.hist(data, bins=50, color='#40c057', edgecolor='white')
    plt.title('Too Many Bins (bins=50)')
    plt.xlabel('Value')
    # plt.ylabel('Frequency') # Optionally hide y-label

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()

bins_histogram()
