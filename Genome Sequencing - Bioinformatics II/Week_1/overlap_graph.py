import sys

def suffix(t):
	return t[1:]

def prefix(t):
	return t[:-1]

def overlap_graph(reads):
	overlaps = []
	for j in sorted(reads):
		for i in reads:
			if suffix(i) == prefix(j):
				overlaps.append(i + " -> " + j)
	return overlaps

if __name__ == '__main__':
	#file_name = sys.stdin.read().strip()
	file_name = input().strip()
	seqs = []
	# seqs = [line.strip() for line in sys.stdin.readlines()]
	with open(file_name) as file:
		for line in file:
			seqs.append(line[:-1])

	answer = overlap_graph(seqs)
	with open("answer_overlap_graph.txt", "w") as f:
		f.write('\n'.join(answer))
	# for s in ans:
	# 	print(s.strip())