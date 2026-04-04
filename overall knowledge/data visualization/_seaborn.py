import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# One of Seaborn's significant advantages is its ability to produce visually appealing plots with minimal effort.
#       A large part of this comes from its built-in themes,
#       which control the overall aesthetic properties like background color, grid lines, and font choices.

def seabs():
    # Generate some simple data
    x = np.linspace(0, 10, 50)
    y = np.sin(x)

    # Default Matplotlib plot (for comparison)
    plt.figure()  # Start a new figure
    plt.plot(x, y)
    plt.title("Default Matplotlib Style")
    plt.show()

    # Now, set a Seaborn style and plot again
    sns.set_theme(style="whitegrid")  # Apply the 'whitegrid' style

    plt.figure()  # Start another new figure
    plt.plot(x, y)
    plt.title("Seaborn 'whitegrid' Style")
    plt.show()

    # Try another style
    sns.set_theme(style="ticks")  # Apply the 'ticks' style

    plt.figure()
    plt.plot(x, y)
    plt.title("Seaborn 'ticks' Style")
    plt.show()

    # Reset to default theme parameters (useful for notebooks)
    # sns.reset_defaults()

# seabs()

# Categorical (or Qualitative) Palettes: These palettes are best used when you want to distinguish discrete categories that do not have an inherent order.
# Each color in the palette should be distinct.

def categorical_sns():
    # Visualize the 'deep' categorical palette
    print("Seaborn 'deep' palette:")
    sns.palplot(sns.color_palette("deep"))
    plt.show()

    # Visualize the 'colorblind' palette
    print("Seaborn 'colorblind' palette:")
    sns.palplot(sns.color_palette("colorblind"))
    plt.show()

# categorical_sns()

# Sequential Palettes: These palettes are suitable for representing numerical data that progresses from low to high values (or vice-versa).
def sequential_sns():
    # Visualize the 'Blues' sequential palette
    print("Seaborn 'Blues' sequential palette:")
    sns.palplot(sns.color_palette("Blues"))
    plt.show()

    # Visualize the 'viridis' sequential palette
    print("Seaborn 'viridis' sequential palette:")
    sns.palplot(sns.color_palette("viridis", n_colors=8))  # Specify number of colors
    plt.show()

# sequential_sns()

# Diverging Palettes: These palettes are used for numerical data where the values diverge from a meaningful midpoint (often zero).
def diverging_pallete():
    # Visualize the 'coolwarm' diverging palette
    print("Seaborn 'coolwarm' diverging palette:")
    sns.palplot(sns.color_palette("coolwarm", n_colors=7))
    plt.show()

    # Visualize the 'RdBu' diverging palette
    print("Seaborn 'RdBu' diverging palette:")
    sns.palplot(sns.color_palette("RdBu", n_colors=9))
    plt.show()

# diverging_pallete()

def scatter_sns():
    # Create sample data
    np.random.seed(42)
    data = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100),
        'category': np.random.choice(['A', 'B', 'C'], 100)
    })

    print(data.head())

    # Create scatter plot using the 'bright' palette
    plt.figure(figsize=(6, 4))  # Set figure size for better web display
    sns.scatterplot(data=data, x='x', y='y', hue='category', palette='bright')
    plt.title('Scatter Plot with Categorical Palette')
    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    plt.tight_layout()  # Adjust layout
    plt.show()

def line_sns():
    # Sample data: Temperature over 10 days
    days = np.arange(1, 11)
    temperature = np.array([15, 16, 18, 17, 19, 21, 20, 22, 21, 23])

    # Create a DataFrame
    temp_df = pd.DataFrame({'Day': days, 'Temperature': temperature})

    # Create the line plot using Seaborn
    plt.figure(figsize=(8, 4))  # Set figure size for better readability
    sns.lineplot(x='Day', y='Temperature', data=temp_df)

    plt.title('Temperature Trend over 10 Days')
    plt.xlabel('Day')
    plt.ylabel('Temperature (°C)')
    plt.grid(True, linestyle='--', alpha=0.6)  # Add a light grid
    plt.show()

# line_sns()

def various_plot():
    # Load the example dataset
    tips = sns.load_dataset("tips")

    # Display the first few rows to understand the data
    print(tips.head())

    plt.figure(figsize=(8, 5))
    sns.kdeplot(data=tips, x="total_bill", color="#f76707", fill=True)  # fill adds color under the curve
    plt.title("KDE of Total Bill Amounts")
    plt.xlabel("Total Bill ($)")
    plt.ylabel("Density")
    plt.show()

    # boxplot
    sns.boxplot(data=tips, x="day", y="total_bill", palette="viridis", hue='sex')  # using a different palette
    plt.title("Total Bill Distribution by Day")
    plt.xlabel("Day of the Week")
    plt.ylabel("Total Bill ($)")
    plt.show()

    # violin
    sns.violinplot(data=tips, x="day", y="total_bill", palette="plasma", hue='sex',
                   inner="quartile")  # inner='quartile' shows quartiles inside
    plt.title("Total Bill Distribution by Day (Violin Plot)")
    plt.xlabel("Day of the Week")
    plt.ylabel("Total Bill ($)")
    plt.show()

    # Joint-plot
    sns.jointplot(data=tips, x="total_bill", y="tip", kind="scatter", color="#37b24d")
    plt.suptitle("Joint Distribution of Total Bill and Tip", y=1.0)  # Adjust title position
    plt.tight_layout()
    plt.show()

# various_plot()

def add_text_to_plot():
    # Sample data
    x = np.linspace(0, 2 * np.pi, 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    # Create the plot
    plt.figure(figsize=(8, 5))  # Create a figure
    plt.plot(x, y_sin, label='sin(x)', color='#1c7ed6')  # Blue
    plt.plot(x, y_cos, label='cos(x)', color='#fd7e14')  # Orange
    plt.title('Sine and Cosine Waves')
    plt.xlabel('Angle (radians)')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)

    # Add text using plt.text()
    plt.text(np.pi / 2, 1.05, 'Sine peak', ha='center', va='bottom', color='#1c7ed6')
    plt.text(np.pi, -1.05, 'Cosine minimum', ha='center', va='top', color='#fd7e14')
    plt.text(4, 0, 'Intersection point', ha='left', va='center', fontsize=9, color='#495057')  # Gray

    plt.ylim(-1.5, 1.5)  # Adjust y-limits to make space for text
    plt.show()

    save_plot(plt)

def save_plot(plot):
    plot.savefig('sine_wave_plot.png')

add_text_to_plot()