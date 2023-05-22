import pandas as pd
import numpy as np

def input_output(file_path):
    df = pd.read_csv(f"{file_path}")
    x_column = df['x'].tolist()
    y_column = df['y'].tolist()

    return x_column, y_column