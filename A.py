import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
    

data = pd.read_csv('data/cars.csv')
key = 'year'
d = data[key].dropna()

print(scipy.stats.describe(d))

series = d.to_numpy()
# plt.hist(series, bins=120)
# plt.show()

hist = np.histogram(series, bins=120)
print(len(hist))

dist = scipy.stats.exponnorm.fit(hist, 1.5)

print(dist)
plt.plot(range(1900, 2021), [dist.pdf(x) for x in range(1900, 2021)])

plt.show()
