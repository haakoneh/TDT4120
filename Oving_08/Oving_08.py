from sys import stdin, stderr

def beste_sti(nm, sans):
	parents = [None]*len(sans)
	weights = [0]*len(sans)
	weights[0] = sans[0]
	nodes = [i for i in range(len(sans))]
	while len(nodes) > 0:
		largest = weights[nodes[0]]
		current_node = nodes[0]
		for node in nodes:
			if weights[i] > largest:
				largest = weights[i]
				current_node = node
		nodes.pop(nodes.index(current_node))
		for i in range(len(sans)):
			if nm[current_node][i] and weights[i] < weights[current_node]*sans[i]:
				weights[i] = weights[current_node]*sans[i]
				parents[i] = current_node
		if current_node == len(sans) - 1:
			break

	if parents[-1] is not None:
		best_road = [len(sans) - 1]
		parent = parents[-1]
		while parent is not None:
			best_road.append(parent)
			parent = parents[parent]
		return "-".join(str(i) for i in reversed(best_road))
	else:
		return str(0)
	
			
n = int(stdin.readline())
sannsynligheter = [float(x) for x in stdin.readline().split()]
nabomatrise = []
for linje in stdin:
    naborad = [0] * n
    naboer = [int(nabo) for nabo in linje.split()]
    for nabo in naboer:
        naborad[nabo] = 1
    nabomatrise.append(naborad)
print beste_sti(nabomatrise, sannsynligheter)
