from sys import stdin
from heapq import *

Inf = float(1e3000)
False = 0
True = 1

def prim(nm):
	n = len(nm)
	tre = []
	best_node = [None] * n
	lowest_egde = [Inf] * n
	not_found = range(1, n)
	previous = 0
	while len(not_found) > 0:
		for i in not_found:
			if nm[i][previous] < lowest_egde[i]:
				best_node[i] = previous
				lowest_egde[i] = nm[i][previous]
		current_egde = Inf
		for i in not_found:
			if lowest_egde[i] < current_egde:
				nestefra = i
				nestetil = best_node[i]
				current_egde = lowest_egde[i]
		tre.append( (nestefra,nestetil) )
		not_found.remove(nestefra)
		previous = nestefra
	return tre


def mst(nm):
	my_three = prim(nm)
	max = 0
	for(from_, to_) in my_three:
		if max < nm[from_][to_]:
			max = nm[from_][to_]
	return max

linjer = []
for str in stdin:
    linjer.append(str)
n = len(linjer)
nabomatrise = [None] * n
node = 0
for linje in linjer:
    nabomatrise[node] = [Inf] * n
    for k in linje.split():
        data = k.split(':')
        nabo = int(data[0])
        vekt = int(data[1])
        nabomatrise[node][nabo] = vekt
    node += 1
# print len(nabomatrise)
print mst(nabomatrise)