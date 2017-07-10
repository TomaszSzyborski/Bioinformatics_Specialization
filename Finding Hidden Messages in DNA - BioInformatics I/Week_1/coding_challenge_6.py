# put your python code here
import sys # you must import "sys" to read from STDIN
import re
from collections import Counter, defaultdict
import itertools

# lines = sys.stdin.read().splitlines() # read in the input from STDIN
# genome = lines[0].strip()
# number = int(lines[1].strip())

# SET_1
genome = "AGGTGAATTCGTGGTCCACCACAACTACCTACAATTTGGCTTTCTGGCTCGGATACTGCTTTTAACGGGGTATAGAAGAGCCCAGATCAGACAGTCTTGCGTGATCAAGGCTTTGCTACCCTATAATGGGATAGCCACAGGGGCGTGTTAACGCGGGATCAAGAGGCGCCTTGCAGAGTATTTAGTCGAGTGGACAAGTGGAAAGCGATGAATAAACGCAACGGCACCTGGGTCGAACGTGCTCCGTGCTGTCTCTTTTAGAGTGCTTAAACTACCTGGTATCTCACGCATTCTATCGTGCGCCTCATCACAGGCCAACAGGTTTTTTGTGTAGAACCGGCCACAACTGCCTTATATTCTCTCGTTCCAAAGGTCGGGCATATACTAACCAATATCGGTTCTAAAAAGTTGGTGCCTTGTAGATCCGGTGTTCGGGAGTTGCAGGTGTAATGGGTCGCTGTTCATATGTTGGAAGTTTATGATCTTTACCCCTTCGAGACTTTGTGCGGTCCTCCACAGCCGTCGTTGGAGACCCGACACAAAACGAATGGAATTCTTGCAAGTATCAGTAAAAAATACGATCCTTACAGCTCAGCGCGATTAGTGATGTCTATTACTATAGGGTCGATAATAGGAACGTTATGCAACTACTACAACACGAAACCC"
number= 5 

numbertosymbol = {0:'A', 1:'C', 2:'G', 3:'T'}
symboltonumber = {'A':0, 'C':1, 'G':2, 'T':3}

def numbertopattern2(n, k):
	pattern = [numbertosymbol[0] for el in range(k)]
	for i in range(k - 1, -1, -1):
		pattern[i]= numbertosymbol[n % 4]
		n /= 4
	return ''.join(pattern)
		    
def numbertopattern(index, k):
	if k == 1:
		return numbertosymbol[index]
	prefixindex = index / 4
	r = int(index % 4)
	prefixpattern = numbertopattern(prefixindex, k - 1)
	return prefixpattern + numbertosymbol[r]

def patterntonumber(pattern):
	if len(pattern)  == 0:
		return 0
	return 4 * patterntonumber(pattern[:-1]) + symboltonumber[pattern[-1]]

def compute_frequency(text,k):
	freq_arr = [0 for _ in range(4**k)]
	for i in range(len(text) - k + 1):
		pattern = text[i:i+k]
		j = patterntonumber(pattern)
		freq_arr[j] = freq_arr[j] + 1
	return freq_arr

print(' '.join(list(map(str, compute_frequency(genome,number)))))