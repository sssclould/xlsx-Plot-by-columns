
import os
import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

def read_csv_file(filename):

    columns = []
    
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if not row:  
                continue
            
         
            for i, value in enumerate(row):
                if len(columns) <= i:
                    columns.append([])
                columns[i].append(value)
    

    non_empty_columns = []
    for col in columns:
        if any(col):  
            non_empty_columns.append(col)
        else:
            break  

    return non_empty_columns

def plot_and_save_column(data, column_name, save_dir=".", file_extension="png"):

    #y_data=data[1:] 
    #y_data = list(map(float, data[1:]))

    y_data = [float(value) for value in data[1:] if value.strip() and value != '--']
    ymax = max(y_data)
    ymin = min(y_data)

    plt.figure(figsize=(35, 20))
    plt.plot(y_data)
    #plt.title(f"Column: {column_name}")
    
    plt.axhline(y=ymax, color='r', linestyle='--', label=f'ymax={ymax:.4f}')
    plt.axhline(y=ymin, color='g', linestyle='--', label=f'ymin={ymin:.4f}')
    plt.legend()
    
    plt.grid()
    plt.xlabel("Index")
    plt.ylabel("Value")

    ax = plt.gca()
    ax.yaxis.set_major_locator(MaxNLocator(nbins=30)) 

    file_name = f"{column_name}.{file_extension}"
    save_path = os.path.join(save_dir, file_name)
    
   
    plt.savefig(save_path)
    plt.close()
    print(f"Saved: {save_path}")

def main():
    input_filename = "input.csv"
    
 
    columns = read_csv_file(input_filename)
    
  
    for i, column in enumerate(columns):
  
        column_name = column[0] if column[0] else f"Column_{i}"
        plot_and_save_column(column, column_name)

if __name__ == "__main__":
    main()