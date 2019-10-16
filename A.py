import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def distribution_graph(series, title='distribution'):
    plt.title(title)
    plt.hist(series.to_numpy(), bins=100)
    plt.show()

data = pd.read_csv('data/climate.csv')

for key in data.keys()[1:]:
    d = data[key]

    print(f"{key} | var: {np.var(d)}, std: {np.std(d)}, mean: {np.mean(d)}")
    
    # try:
    distribution_graph(d, title=key)
    # except:
    #     pass
