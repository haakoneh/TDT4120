from sys import *
import traceback
from collections import defaultdict
from heapq import *


def subgraftetthet(nabomatrise, root_node):
	n = len(nabomatrise)
	inside = [False] * n
	inside[root_node] = True
	queue = [root_node] # BFS
	while len(queue) > 0:
		from_ = queue.pop(0)
		for to_ in range(0, n):
			if nabomatrise[from_][to_] and not inside[to_]:
				inside[to_] = True
				queue.append(to_)
	noder = 0
	kanter = 0
	for from_ in range(0, n):
		if not inside[from_]:
			noder += 1
			for to_ in range(0, n):
				if nabomatrise[from_][to_] and not inside[to_]:
					kanter += 1
	if noder == 0:
		return 0.0
	else:
		return float(kanter) / float(noder**2)


try:
    n = int(stdin.readline())
    nabomatrise = [None] * n # rader
    for i in range(0, n):
        nabomatrise[i] = [False] * n # kolonner
        linje = stdin.readline()
        for j in range(0, n):
            nabomatrise[i][j] = (linje[j] == '1')
    # print(nabomatrise)
    for linje in stdin:
        start = int(linje)
        # print(start)
        print "%.3f" % (subgraftetthet(nabomatrise, start) + 1E-12)
except:
    traceback.print_exc(file=stderr)