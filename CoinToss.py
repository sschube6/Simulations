'''Simulates a series of coinflips and displays a histrogram of how long heads was in the lead'''
import numpy as np
import matplotlib.pyplot as plt

tosses = 20  # number of tosses
p = 0.5      # probability of heads
n = 100000   # repeats
w = np.random.randint(2, size=(n, tosses))

wexp = 0.5*np.arange(1, tosses+1)
nlead = np.sign(np.cumsum(w, axis=1) - wexp)
nlead[:, 1:] = np.sign(nlead[:, :-1]+nlead[:, 1:])

fig = plt.figure
plt.hist(np.sum(nlead > 0, axis=1), bins=tosses+1)
plt.show()
