import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')

plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

x = df['Year']
y = df['CSIRO Adjusted Sea Level']
res = linregress(x, y)
x1 = list(range(1880, 2050))
y1 = [res.slope*i + res.intercept for i in x1]
plt.plot(x1, y1, 'r', label='Best fit line (all data)')

df2 = df[df['Year'] >= 2000]
x2 = df2['Year']
y2 = df2['CSIRO Adjusted Sea Level']
res2 = linregress(x2, y2)
x3 = list(range(2000, 2050))
y3 = [res2.slope*i + res2.intercept for i in x3]
plt.plot(x3, y3, 'g', label='Best fit line (2000 onwards)')

plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

plt.show()
