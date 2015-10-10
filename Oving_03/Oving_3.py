from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def bygg(ordliste):
	root = Node()
	for (ord, pos) in ordliste:
		node = root
		for char in ord:
			if not char in node.barn:
				node.barn[char] = Node()
			node = node.barn[char]
		node.posi.append(pos)
	return root
	
def posisjoner(ord, indeks, node):
	if indeks >= len(ord):
		return node.posi
	elif ord[indeks] == '?':
		pos = []
		for char in node.barn.values(): 
			pos += posisjoner(ord, indeks + 1, char)
		return pos
	elif ord[indeks] in node.barn:
		return posisjoner(ord, indeks + 1, node.barn[ord[indeks]])
	else:
		return []


def testing(ordliste):
	for ord in ordliste:
		word = ord[0]
		char = word[0]
		print char
	print 'test'
	
try:
    ord = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append( (o,pos) )
        pos += len(o) + 1
    # testing(ordliste)
		
    toppnode = bygg(ordliste)
    for sokeord in stdin:
        sokeord = sokeord.strip()
        print sokeord + ":",
        posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print p,
        print
except:
    traceback.print_exc(file=stderr)