import sys

def hamming_distance(genome1,genome2):
	score = 0
	if len(genome1) != len(genome2):
		print("Not matched lengths")
	else:
		for i in range(len(genome1)):
			if genome1[i] != genome2[i]:
				score += 1
	return score

if __name__ == '__main__':
	lines = sys.stdin.read().splitlines() # read in the input from STDIN

	genome_1 = lines[0].strip()
	genome_2 = int(lines[1].strip())

	answer = hamming_distance(genome_1,genome_2)
	print(answer)