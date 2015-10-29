import numpy as np

px = np.power(12,0.5)-3
py = (1-px)/2
pz = py

# player B and C play optimal according to values above
pxA = 0.2
pyA = 0.5
pzA = 1-pxA-pyA

Pwin = pxA *((1-px)*(1-px)) + pyA *(px*px + pz*pz) + pzA*(px*px+py*py)
print Pwin
print (px*px+py*py+pz*pz)

dim = 10
p = np.zeros(dim+1)
p[10] = 0
for i in reversed(range(dim)):
	p[i] = np.sqrt()