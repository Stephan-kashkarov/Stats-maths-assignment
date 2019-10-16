import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def distribution_graph(series, title='distribution'):
    plt.title(title)
    plt.hist(series.to_numpy(), bins=100)
    plt.show()

data = pd.read_csv('data/climate.csv')

for key in data.keys()[1:]:
    print(key)
    # try:
    distribution_graph(data[key], title=key)
    # except:
    #     pass
