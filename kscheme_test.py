import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from src.data_gen import get_voting_power

N = 10 # number of nodes
K = N  # max value of k

R = np.arange(1, N + 1, dtype=int) # ranks

ax = plt.figure().gca()
plt.title('Family of voting power functions on k-scheme', fontweight='bold')
plt.xlabel('Rank')
plt.ylabel('Voting power')
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

for k in range(1, K + 1):
    vp = get_voting_power(N, k)
    plt.plot(R, vp, marker='o', label=f'k={k}')

plt.legend()
plt.show()
