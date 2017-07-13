import sys
from itertools import product
#genome = "TGCAT"

name = sys.argv[1]

with open(name, 'r') as f:
	lines = f.readlines()
	genome = lines[0].strip()
	neighborhood = int(lines[1].strip())

# genome = "ACGT"
# neighborhood = 3
def hamming_distance(genome1,genome2):
	score = 0
	if len(genome1) != len(genome2):
		print("Error")
	else:
		for i in range(len(genome1)):
			if genome1[i] != genome2[i]:
				score += 1
	return score

print(len(genome))
first_genome = genome[:]
print(neighborhood)
l = len(genome)
genome = "ACGT"

# possibilities = product(genome, repeat=len(genome))
possibilities = product(genome, repeat=l)
possibilities = list(map(''.join, possibilities))

possibilities = [p for p in possibilities if hamming_distance(first_genome, p) <= neighborhood]
#IF POSSIBILITIES REQUIRED
# print('\n'.join(possibilities))
with open("neigh.txt", 'w') as f:
	f.write('\n'.join(possibilities))

# IF LENGTH REQUIRED
#print(len([p for p in possibilities if hamming_distance(genome, p) <= neighborhood]))