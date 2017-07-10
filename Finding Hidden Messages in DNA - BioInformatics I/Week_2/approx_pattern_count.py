import sys


def hamming_distance(genome_1,genome_2):
	score = 0
	if len(genome_1) != len(genome_2):
		print("Error")
	else:
		for i in range(len(genome_1)):
			if genome_1[i] != genome_2[i]:
				score += 1
	return score

def approx_pattern_matching(kmer, genome, hamming_score):
	count = 0
	for i in range(len(genome) - len(kmer) + 1):
		pattern = genome[i:i+len(kmer)]
		score = hamming_distance(kmer,pattern)
		if score <= hamming_score:
			count += 1
	return count

if __name__ == '__main__':
	lines = sys.stdin.read().splitlines() # read in the input from STDIN
	genome_1 = lines[0].strip()
	genome_2 = lines[1].strip()
	number = int(lines[2].strip())
	answer = approx_pattern_matching(genome_1,genome_2,number
	print(answer)