from sys import stdin, maxint

inf = 10000

def korteste_rute(rekkefolge, nabomatrise, byer):
	for k in range(byer):
		for i in range(byer):
			for j in range(byer):
				nabomatrise[i][j] = min(nabomatrise[i][j], nabomatrise[i][k] + nabomatrise[k][j])
	rute = 0
	navaerende = rekkefolge[0]

	for neste in rekkefolge[1:]:
		vei = nabomatrise[navaerende][neste]
		if vei == inf:
			return 'umulig'
				
		rute += vei
		navaerende = neste
		
	return rute 


testcases = int(stdin.readline())
for test in range(testcases):
	byer = int(stdin.readline())
	rekkefolge = [int(by) for by in stdin.readline().split()]
	rekkefolge.append(rekkefolge[0])
	nabomatrise = []
	
	for by in range(byer):
		naborad = map(lambda x: inf if x == '-1' else int(x), stdin.readline().split())
		nabomatrise.append(naborad)
		
	print korteste_rute(rekkefolge, nabomatrise, byer)


	