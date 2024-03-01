import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import csv
import datetime
import pandas as pd
import calmap
import matplotlib.pyplot as plt

class ExerciseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exercise Tracker")

        # Apply a modern theme
        style = ThemedStyle(root)
        style.set_theme("arc")

        self.root.geometry("400x200")

        self.pushup_label = ttk.Label(root, text="Pushups:")
        self.pushup_label.pack(pady=10)

        self.pushup_entry = ttk.Entry(root)
        self.pushup_entry.pack(pady=1)

        self.mountain_climber_label = ttk.Label(root, text="Mountain Climbers:")
        self.mountain_climber_label.pack(pady=10)

        self.mountain_climber_entry = ttk.Entry(root)
        self.mountain_climber_entry.pack(pady=1)

        self.confirm_button = ttk.Button(root, text="Confirm", command=self.confirm_action)
        self.confirm_button.pack(pady=20)

    def confirm_action(self):
        # Get the current date
        current_date = datetime.date.today().strftime('%Y-%m-%d')

        # Get pushup and mountain climber values from entry widgets
        pushup_value = self.pushup_entry.get()
        mountain_climber_value = self.mountain_climber_entry.get()

        # Open the CSV file in append mode and write the new data
        with open('D:\Coding\exercise-tracker\exercise_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([current_date, pushup_value, mountain_climber_value])

        # Clear the entry widgets after saving data
        self.pushup_entry.delete(0, tk.END)
        self.mountain_climber_entry.delete(0, tk.END)

        # Update the plot
        self.update_plot()

    def update_plot(self):
        # Load the data from the CSV file
        df = pd.read_csv('D:\Coding\exercise-tracker\exercise_data.csv')

        # Ensure the "day" column is of datetime type
        df['day'] = pd.to_datetime(df['day'])

        # Create a calendar heatmap for the "mountain_climber" column with a green colormap
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))  # Create two subplots vertically stacked

        # Plot the calendar heatmap for "pushup" in the first subplot
        calmap.yearplot(df.set_index('day')['pushup'], year=2024, ax=ax1, cmap='YlGn', fillcolor='grey', vmin=0, vmax=40)
        ax1.set_title('Pushups Calendar Heatmap - 2024 (Green Tones)')

        # Plot the calendar heatmap for "mountain_climber" in the second subplot
        calmap.yearplot(df.set_index('day')['mountain_climber'], year=2024, ax=ax2, cmap='YlGn', fillcolor='grey', vmin=0, vmax=40)
        ax2.set_title('Mountain Climbers Calendar Heatmap - 2024 (Green Tones)')

        # Adjust layout to prevent overlap
        plt.tight_layout()

        # Show the plots
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExerciseTrackerApp(root)
    root.mainloop()
