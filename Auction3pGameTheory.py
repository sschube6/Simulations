import numpy as np

N = 200
alpha = np.zeros(N-1)
alpha[-1] = 1
alpha[-2] = np.sqrt(3)

for k in range(3,N):
	alpha_km1 = alpha[-(k-1)]
	alpha_km2 = alpha[-(k-2)]
	alpha[-k] = np.sqrt(np.power(alpha_km1+alpha_km2,4)/(4*alpha_km2*alpha_km2) - np.sum(alpha*alpha))
# print alpha

p = np.zeros(N)
p[-1] = 1/(np.sum(alpha)+1)
p[:-1] = alpha*p[-1]
print p

tribonacci = 1.83928675521
pp = np.ones(N)
pp *= (tribonacci-1)/tribonacci
for i in range(N):
	pp[i] /= np.power(tribonacci,i)
# print pp


# test an alternative strategy of bidding number n with probability 2^(-n)
palt = np.ones(N)
for i in range(N):
	palt[i] *= np.power(2.,-i-1)

EV_paltVS2palt = 0
EV_pVS2palt = 0
for i in range(N):
	if i == 0:
		EV_paltVS2palt += palt[i] * np.power(1-np.cumsum(palt)[i],2)
		EV_pVS2palt += p[i] * np.power(1-np.cumsum(palt)[i],2)
	else:
		EV_paltVS2palt += palt[i] * (np.cumsum(palt*palt)[i-1] + np.power(1-np.cumsum(palt)[i],2))
		EV_pVS2palt += p[i] * (np.cumsum(palt*palt)[i-1] + np.power(1-np.cumsum(palt)[i],2))
print EV_paltVS2palt
print EV_pVS2palt
# EV_pVS2palt = p[0] * np.power(1-palt[0],2) + p[1] * np.power(1-palt[0]-palt[1])


# print (p[-2])
# print np.power(1-p[0],2)
# print np.sum(p[:-2]*p[:-2])+p[-1]*p[-1]
# print np.sum(p[:-1]*p[:-1])
print np.sum(palt*palt)
print np.sum(p*p)