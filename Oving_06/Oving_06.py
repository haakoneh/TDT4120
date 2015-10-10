from sys import stdin

def sorter(A):
    if len(A) < 2:
        return A
    result = []          # moved!
    mid = int(len(A)/2)
    b = sorter(A[:mid])
    c = sorter(A[mid:])
    while (len(b) > 0) and (len(c) > 0):
            if b[0] > c[0]:
                result.append(c[0])
                c.pop(0)
            else:
                result.append(b[0])
                b.pop(0)
    result += b
    result += c
    return result

def finn(A, nedre, ovre):
	limit = [A[0], A[len(A) - 1]]	
	for least in A:
		if least <= nedre:
			limit[0] = least
		else:
			break
	for most in reversed(A):
		if most >= ovre:
			limit[1] = most
		else: 
			break
	return limit

liste = []
for x in stdin.readline().split():
    liste.append(int(x))
	
sortert = sorter(liste)

for linje in stdin:
    ord = linje.split()
    minst = int(ord[0])
    maks = int(ord[1])
    resultat = finn(sortert, minst, maks)
    print str(resultat[0]) + " " + str(resultat[1])