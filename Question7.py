import numpy as np

d = 
8num = np.zeros(d)

sumup = 0
for i in range(np.power(10,d)):
	val = 1
	for j in range(d):
		num[j] = i % 10
		i = (i - num[j]) / 10
		if num[j] != 0:
			val *= num[j]
	sumup += val
print "Sum: %d" % sumup
print "Last digit: %d" % (sumup % 10)