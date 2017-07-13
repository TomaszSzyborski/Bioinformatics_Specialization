import sys

def hamming_distance(genome1,genome2):
	score = 0
	if len(genome1) != len(genome2):
		print("Error")
	else:
		for i in range(len(genome1)):
			if genome1[i] != genome2[i]:
				score += 1
	return score

def approx_matching(kmer,genome,hamming_score):
	start_points = []
	for i in range(len(genome) - len(kmer) + 1):
		score = hamming_distance(kmer,genome[i:i+len(kmer)])
		if hamming_score>=score:
			start_points.append(i)
	return start_points

if __name__ == '__main__':
	# lines = sys.stdin.read().splitlines() # read in the input from STDIN
	name = sys.argv[1]
	with open(name, 'r') as f:
		lines = f.readlines()
		genome_1 = lines[0].strip()
		genome_2 = lines[1].strip()
		number = int(lines[2].strip())
	answer = approx_matching(genome_1,genome_2,number)
	print(' '.join(list(map(str, answer))))
	#for num in answer:
	#	print(num)