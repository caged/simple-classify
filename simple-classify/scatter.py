import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

df = pd.read_csv('data/results.csv')
df = df[(df['season'] == '2014-15')]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df.G, df.F, df.C, c='r', marker='o')

ax.set_xlabel('Guard')
ax.set_ylabel('Forward')
ax.set_zlabel('Center')

plt.show()
