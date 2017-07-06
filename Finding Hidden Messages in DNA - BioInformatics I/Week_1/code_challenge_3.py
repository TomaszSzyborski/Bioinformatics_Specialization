import sys # you must import "sys" to read from STDIN

line = sys.stdin.read().strip() # read in the input from STDIN

nucleotides = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'} 

complement = []

for letter in line:
	complement.append(nucleotides[letter])

strand = ''.join(complement[::-1])

print(strand)