'''What is the probability that out of n people at least two have the same birthday?'''

import numpy

days = 365		# number of days
people = [15, 20, 22, 23, 25, 30, 40, 50, 70] # list with number of people
N = 10000 # number of repeats

# loop over the list of people
people = numpy.array(people)
results = numpy.zeros(people.size)
for i in range(0, people.size):
	#simulate N runs
	success = 0. # count variable for when any birthday is not unique
	for j in range(0,N):
		sim = numpy.random.random_integers(1,days,size=people[i])
		if sim.size != numpy.unique(sim).size:
			success += 1.
	results[i] = success/N
print "people " + ''.join(["  %2.2i  " % i for i in people])
print "prob.  " + ''.join(["%0.3f " % i for i in results])