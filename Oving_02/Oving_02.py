from sys import stdin

# var ikke definert i den gamle python-versjonen som 
# ligger paa noen av stud sine maskiner
True = 1
False = 0

class Node:
    barn = None 
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = 0

def dfs(rot):
	stack = [rot]
	while stack:
		temp = stack[len(stack) - 1]
		if temp.ratatosk:
			return len(stack) - 1
		if temp.nesteBarn == len(temp.barn):
			stack.pop()
		else:
			stack.append(temp.barn[temp.nesteBarn])
			temp.nesteBarn += 1
			
def bfs(rot):
	queue = [(rot, 0)]
	while queue:
		temp, depth = queue.pop(0)
		if temp.ratatosk:
			return depth
		for child in temp.barn:
			queue.append((child, depth + 1))

funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])

if funksjon == 'dfs':
    print dfs(start_node)
elif funksjon == 'bfs':
    print bfs(start_node)
elif funksjon == 'velg':
    print dfs(start_node)
	