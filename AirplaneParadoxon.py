'''One hundred people line up to board an airplane with one hundred passenger seats. Each passenger get on one at a time to select his or her assigned seat.The first passenger in line makes a mistake and chooses (randomly) a wrong seat. Each subsequent passenger takes his or her seat if available, otherwise a random unoccupied seat. You are the last passenger. What is the probability that you can get your own seat? from: Understanding Probability, 3ed, p. 59'''

import numpy as np

n = 100 # number of passengers = number of seats available
runs = 10000 # number of repeats

success = np.zeros(n)
for r in range(runs):
	seats = np.zeros(n)
	idx_rand = np.random.random_integers(0,n-1) # first passenger chooses randomly
	# idx_rand = np.random.random_integers(1,n-2) # first passenger is allowed to sit anywhere, except in his own or the last passengers seat	
	# idx_rand = np.random.random_integers(1,n-1) # first passenger is allowed to sit anywhere, except in his own seat
	seats[idx_rand] = 1 # first passengers occupies seat idx_rand
	for i in range(1,n):
		# if seats is empty, sit down, otherwise sit randomly
		if seats[i] == 0:
			seats[i] = 1
			success[i] += 1
		else:
			idx_empty = np.where(seats == 0)[0] # index of empty seats
			idx_rand = idx_empty[np.random.random_integers(0,n-1-i)] # choose one randomly
			seats[idx_rand] =1

# print probability of last m passengers to sit in the right place
m = 10
print "runs: %d, passengers: %d" % (runs, n)
print "passenger: " + ''.join(["%d\t\t" % (i+1) for i in range(n-m,n)])
print "frequency: " + ''.join(["%.3f\t" % i for i in (1.0*success[n-m:]/runs)])