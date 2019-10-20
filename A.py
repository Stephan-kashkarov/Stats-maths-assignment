import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import exponnorm as f, describe
import scipy.special as sse
from scipy.optimize import curve_fit
    
#pylint: disable=no-member
f = lambda x, l, s, m: 0.5*l*np.exp(0.5*l*(2*m+l*s*s-2*x))*sse.erfc((m+l*s*s-x)/(np.sqrt(2)*s))

data = pd.read_csv('data/cars.csv')

d = np.array(filter(lambda x: int(x) >= 1950, data['year'].dropna().to_numpy()))

print(describe(d))

# plt.show()
bins = (2020 - 1950)

params = f.fit(d)[1:]
print(params)
data_range = range(1950, 2021)
pdf = f.pdf(data_range, 1.5, *params)
fig, ax1 = plt.subplots()
ax1.margins(x=0, y=0)
ax1.set_xlabel('Year')
ax1.set_ylabel('Count', color="tab:blue")
ax1.hist(d, bins=bins)

ax2 = ax1.twinx()

color = 'tab:red'
ax2.margins(x=0, y=0)
ax2.set_ylabel('Probalility', color=color)
ax2.plot(data_range, pdf, color=color)
ax2.tick_params(axis='y', labelcolor=color)


# plt
fig.tight_layout()
plt.show()
