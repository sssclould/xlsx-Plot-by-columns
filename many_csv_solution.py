import os
import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

def read_first_column_from_csv(filename):
    first_column = []

    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row:  
                first_column.append(row[0])

    return first_column

def plot_and_save_column(data, filename, save_dir=".", file_extension="png"):
    try:
        #y_data = [float(value) for value in data[1:] if value.strip()]
        #y_data = [float(value) for value in data[0:] if value.strip() and value.replace('.', '', 1).isdigit()]
        y_data = [float(value) for value in data[0:] if value.strip() and value != '--']
    except ValueError:
        print(f"Warning: Could not convert all values to float for {filename}.")
        return

    ymax = max(y_data)
    ymin = min(y_data)

    plt.figure(figsize=(35, 20))
    plt.plot(y_data)
    
    plt.axhline(y=ymax, color='r', linestyle='--', label=f'ymax={ymax:.4f}')
    plt.axhline(y=ymin, color='g', linestyle='--', label=f'ymin={ymin:.4f}')
    plt.legend()
    
    plt.grid()
    plt.xlabel("Index")
    plt.ylabel("Value")

    ax = plt.gca()
    ax.yaxis.set_major_locator(MaxNLocator(nbins=30))

    file_name = f"{os.path.splitext(filename)[0]}.{file_extension}"
    save_path = os.path.join(save_dir, file_name)
    
    plt.savefig(save_path)
    plt.close()
    print(f"Saved: {save_path}")

def process_all_csv_files_in_dir(directory="."):
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            full_path = os.path.join(directory, filename)
            first_column = read_first_column_from_csv(full_path)
            if first_column:  
                plot_and_save_column(first_column, filename)

if __name__ == "__main__":
    process_all_csv_files_in_dir()