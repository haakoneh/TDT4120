from sys import stdin
from itertools import repeat

def merge_sort(A):
    if len(A) < 2:
        return A
    result = []
    mid = int(len(A)/2)
    b = merge_sort(A[:mid])
    c = merge_sort(A[mid:])
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

def merge(decks):
	merged_deck = []
	for deck in decks:
		merged_deck += deck
	merge_sorted = merge_sort(merged_deck)
	char_list = []
	for tuppel in merge_sorted:
		char_list += tuppel[1]
	return ''.join(char_list)

decks = []
for line in stdin:
    (index, list) = line.split(':')
    deck = zip(map(int, list.split(',')), repeat(index))
    decks.append(deck)
print merge(decks)