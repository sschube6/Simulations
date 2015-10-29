import numpy as np

runs = 10000000
max_games = 1000
start_br = 10
win = 2
lose = -1


ruin = 0
for i in range(runs):
	br_diff = (win-lose)*np.random.random_integers(0,1,size=(max_games))+lose
	br_diff[0] = start_br
	if any(np.cumsum(br_diff) <= 0):
		ruin += 1
print ruin
print np.power((np.power(5,0.5)-1)/2,10)