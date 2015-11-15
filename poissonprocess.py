'''
Poisson Process
This scripts simulates a poisson process. Individual events are arriving with an average rate k within the time [tstart, tend). The distribution as well as a histogram of the waiting times dt is plotted.
'''

import numpy as np
from matplotlib import pyplot

tstart = 0
tend = 100
k = 1

# generate random numbers u uniformly in [0, 1)
u = 1 - np.random.rand(int((tend-tstart)*k*10))
dt = -(1.0/k)*np.log(u)
t = tstart+np.cumsum(dt)
t = t[t < tend]

'''plotting'''
fig = pyplot.figure()

fig.add_subplot(211,
                title='Arrival times\n(at average rate k = %g per s)' % k,
                xlabel='time t in s')
pyplot.hlines(1, tstart, tend, colors='k')
pyplot.plot(t, np.ones(t.shape),
            linestyle='none',
            marker='|',
            markerfacecolor='none',
            markersize=100)
pyplot.ylim(0.9, 1.1)
pyplot.yticks([])

fig.add_subplot(212,
                title='Distribution of interval times',
                xlabel='interval time dt in s',
                ylabel='occurences')
pyplot.hist(dt[0:t.size])
fig.tight_layout()
pyplot.show()
