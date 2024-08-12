import pandas as pd
import matplotlib as plt

data = pd.read_csv('monthly-sunspots.csv')

def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].
        y = points.iloc[i].
        total_error += 