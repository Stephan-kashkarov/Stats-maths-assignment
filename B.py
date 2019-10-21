import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as ss
from scipy.optimize import curve_fit

data1 = pd.read_csv('data/rain_data1.csv').sort_values(by=['year'])
data2 = pd.read_csv('data/rain_data2.csv').sort_values(by=['year'])

func = lambda x, m, b: (m * x) + b

print(data1.keys())
print_data = lambda title, d: print(
f"""{title} - my non excel analysis pack
 - mean:               {d.mean()}
 - median:             {d.median()}
 - standard deviation: {d.std()}
 - skew:               {d.skew()}
 - kurtosis:           {d.kurtosis()}""")

print("Temperature:")
print_data("Temp - part 1", data1['temperature'])
print_data("Temp - part 2", data2['temperature'])

print("\nRainfall:")
print_data("Rain - part 1", data1['rainfall'])
print_data("Rain - part 2", data2['rainfall'])

def raw(ax, d, key):
    s1 = d['year'].to_numpy()
    s2 = d[key].to_numpy()
    ax.plot(s1, s2, ".")

def hist(ax, d, key):
    ax.hist(d[key].to_numpy())

def qq(ax, d1, key, title):
    ss.probplot(d1[key].to_numpy(), dist="norm", plot=ax)
    ax.set_title(title)


types = ["temperature", "rainfall"]
for f in [hist, raw]:
    for key in types:
        fig, (ax1, ax2) = plt.subplots(2, 1)
        for ax, key2, data in [(ax1, "part 1", data1), (ax2, "part 2", data2)]:
            ax.set_title(key2)
            f(ax, data, key)
        fig.suptitle(f"{key} - {f.__name__}")
        plt.show()
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle(f"Q-Q plots")
for key, axes in zip(types, [(ax1, ax2), (ax3, ax4)]):
    for ax, key2, data in [(axes[0], "part 1", data1), (axes[1], "part 2", data2)]:
        qq(ax, data, key, f"{key} - {key2}")
plt.show()




