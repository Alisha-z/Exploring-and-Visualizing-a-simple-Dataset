# Step 1: Import the necessary libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2: Load the dataset
iris = sns.load_dataset("iris")

# Step 3: Look at the basic structure
print("Shape of the dataset:", iris.shape)  # rows, columns
print("\nColumn names:", iris.columns.tolist())
print("\nFirst five rows:")
print(iris.head())

# Step 4: Dataset information
print("\nInfo about dataset:")
print(iris.info())

# Step 5: Statistical summary
print("\nSummary statistics:")
print(iris.describe())

# Scatter plot: Sepal Length vs Sepal Width
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
plt.title("Sepal Length vs Width")
plt.show()


# Histogram of all numeric columns
iris.hist(figsize=(10, 6))
plt.suptitle("Histograms of Iris Features")
plt.tight_layout()
plt.show()

# Box plots to check for outliers
sns.boxplot(data=iris)
plt.title("Box Plot of All Features")
plt.show()
