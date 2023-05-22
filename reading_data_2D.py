import pandas as pd
import numpy as np

def input_output(file_path):
    df = pd.read_csv(f"{file_path}")
    x0_column = df['x0'].tolist()
    x1_column = df['x1'].tolist()
    y_column = df['y'].tolist()
    
    x_column = []
    for i in range(len(x0_column)):
        r = (x0_column[i], x1_column[i])
        x_column.append(r)

    return x_column, y_column