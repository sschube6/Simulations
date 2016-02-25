import numpy as np
import matplotlib.pyplot as plt

payout_max = 20
games = 10000

x = np.zeros(shape=(games, payout_max-1), dtype=int)
x[:, :-1] = np.random.randint(0, 2, size=(games, payout_max-2))

for i in np.arange(payout_max-3):
    x[:, i+1] = x[:, i] * x[:, i+1]

y = np.zeros(shape=(games, payout_max-1), dtype=int)
for i in np.arange(payout_max-2):
    y[:, i] = x[:, i] == x[:, i+1]
idx1, idx2 = np.nonzero((y[:, :-1]) == 0)

winning_amount = np.zeros(games, dtype=int)
winning_amount[:] = 2
winning_amount[idx1] = 2**(idx2+2)

xaxis = np.arange(1, games+1)
plt.plot(xaxis, np.cumsum(winning_amount)*1.0/xaxis)
plt.show()
