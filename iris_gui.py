import tkinter as tk
from tkinter import messagebox
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the iris dataset
iris = sns.load_dataset("iris")

# Plot functions
def show_scatter_plot():
    sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
    plt.title("Sepal Length vs Width")
    plt.show()

def show_histogram():
    iris.hist(figsize=(10, 6))
    plt.suptitle("Histograms of Iris Features")
    plt.tight_layout()
    plt.show()

def show_box_plot():
    sns.boxplot(data=iris)
    plt.title("Box Plot of All Features")
    plt.show()

# GUI setup
window = tk.Tk()
window.title("Iris Data Visualizer")
window.geometry("400x300")
window.configure(bg="#f0f0f0")

# Title label
label = tk.Label(window, text="Iris Dataset Charts", font=("Helvetica", 16), bg="#f0f0f0")
label.pack(pady=20)

# Buttons
btn1 = tk.Button(window, text="Show Scatter Plot", command=show_scatter_plot, width=25)
btn1.pack(pady=10)

btn2 = tk.Button(window, text="Show Histogram", command=show_histogram, width=25)
btn2.pack(pady=10)

btn3 = tk.Button(window, text="Show Box Plot", command=show_box_plot, width=25)
btn3.pack(pady=10)


# --- Add Your Name Here ---
signature = tk.Label(window, text="Created by Alisha", font=("Arial", 10, "italic"), bg="#f0f0f0", fg="gray")
signature.pack(side="bottom", pady=10)


# Run the GUI loop
window.mainloop()
