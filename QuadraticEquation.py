'''Find probability of equation Ax^2+Bx+C=0 has real roots when A, B, C are randomly choosen in interval (-l,l).'''

import numpy as np

runs = 100000
interval = (1, 10, 100, 1000, 10000)

frequency = []
for l in interval:
	M_rand = np.random.rand(3,runs) # random matrix
	M_rand = l*(2*M_rand-1)
	A = M_rand[0,:]
	B = M_rand[1,:]
	C = M_rand[2,:]

	# Ax^2+Bx+C=0
	# p = B/A. q = C/A
	# solution: x = -p/2 +- sqrt(p^2/4-q)
	# real if p^2 >= 4q
	# re-substitution: B^2 >= 4AC

	success = sum(B*B >= 4*A*C)
	frequency.append(1.0 * success/runs)

print "Interval            " + ''.join(["(-%5d,%5d)\t" % (i,i) for i in interval])
print "Fraction real roots " + ''.join(["%14.3f\t" % i for i in frequency])


print"\nCase of non-zero integers:"

frequency = []
for l in interval:
	M_rand = np.random.random_integers(1,l,size=(3,runs)) # random matrix
	sign = 2*np.random.random_integers(0,1,size=(3,runs))-1 # random sign
	M_rand = sign*M_rand

	A = M_rand[0,:]
	B = M_rand[1,:]
	C = M_rand[2,:]

	# Ax^2+Bx+C=0
	# p = B/A. q = C/A
	# solution: x = -p/2 +- sqrt(p^2/4-q)
	# real if p^2 >= 4q
	# re-substitution: B^2 >= 4AC

	success = sum(B*B >= 4*A*C)
	frequency.append(1.0 * success/runs)

print "Interval            " + ''.join(["[-%5d,%5d]\t" % (i,i) for i in interval])
print "Fraction real roots " + ''.join(["%14.3f\t" % i for i in frequency])
