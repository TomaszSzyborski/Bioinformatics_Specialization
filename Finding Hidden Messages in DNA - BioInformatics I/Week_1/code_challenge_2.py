import sys # you must import "sys" to read from STDIN
import re
from collections import Counter
# lines = sys.stdin.read().splitlines() # read in the input from STDIN

# string = lines[0].strip()
# k = int(lines[1].strip())

##SET_1
# string = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
# k = 4
#answer = "TGG"

#SET_2
# string = "TGGTAGCGACGTTGGTCCCGCCGCTTGAGAATCTGGATGAACATAAGCTCCCACTTGGCTTATTCAGAGAACTGGTCAACACTTGTCTCTCCCAGCCAGGTCTGACCACCGGGCAACTTTTAGAGCACTATCGTGGTACAAATAATGCTGCCAC"
# k = 3
# answer = "TGG"

##SET_3
# string = "CAGTGGCAGATGACATTTTGCTGGTCGACTGGTTACAACAACGCCTGGGGCTTTTGAGCAACGAGACTTTTCAATGTTGCACCGTTTGCTGCATGATATTGAAAACAATATCACCAAATAAATAACGCCTTAGTAAGTAGCTTTT"
# k = 4
# answer = "TTTT"

# string = "ATACAATTACAGTCTGGAACCGGATGAACTGGCCGCAGGTTAACAACAGAGTTGCCAGGCACTGCCGCTGACCAGCAACAACAACAATGACTTTGACGCGAAGGGGATGGCATGAGCGAACTGATCGTCAGCCGTCAGCAACGAGTATTGTTGCTGACCCTTAACAATCCCGCCGCACGTAATGCGCTAACTAATGCCCTGCTG"
# k = 5
# answer = "AACAA"

# string = "CCAGCGGGGGTTGATGCTCTGGGGGTCACAAGATTGCATTTTTATGGGGTTGCAAAAATGTTTTTTACGGCAGATTCATTTAAAATGCCCACTGGCTGGAGACATAGCCCGGATGCGCGTCTTTTACAACGTATTGCGGGGTAAAATCGTAGATGTTTTAAAATAGGCGTAAC"
# k= 5
# answer = "AAAAT GGGGT TTTTA"

# string = "GACTCATCATATACCGCGTGTTCTTCGACTCATCATATACCGCGGACTCATCAGACTCATCACGATAGCCGGACTCATCATGTTCTTCCGATAGCCGCGATAGCCGTGTTCTTCTGTTCTTCTTATCTCCGATAGCCGTTATCTCGACTCATCACGATAGCCGCGATAGCCGTGTTCTTCTGTTCTTCTTATCTCTGTTCTTCGACTCATCATTATCTCTGTTCTTCGACTCATCACGATAGCCGTTATCTCGACTCATCATGTTCTTCTATACCGCGTATACCGCGTTATCTCCGATAGCCGGACTCATCAGACTCATCATGTTCTTCTGTTCTTCTTATCTCTTATCTCTATACCGCGGACTCATCATTATCTCTATACCGCGGACTCATCACGATAGCCGGACTCATCATGTTCTTCGACTCATCAGACTCATCATGTTCTTCGACTCATCATTATCTCTTATCTCTATACCGCGGACTCATCATGTTCTTCGACTCATCACGATAGCCGTGTTCTTCTTATCTCTTATCTCTTATCTCTGTTCTTCGACTCATCAGACTCATCATGTTCTTCCGATAGCCGTTATCTCGACTCATCATGTTCTTCTTATCTCGACTCATCATATACCGCGTATACCGCGTATACCGCGTTATCTCTTATCTCTTATCTCGACTCATCATTATCTCTGTTCTTCGACTCATCATGTTCTTCCGATAGCCGCGATAGCCGGACTCATCAGACTCATCATTATCTCTATACCGCGTGTTCTTCTATACCGCGTATACCGCGGACTCATCACGATAGCCGTATACCGCGTGTTCTTC"
# k = 13

string = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
k =3

def sliding_string_window(string, k):
	list_of_substrings = []
	for i in range(len(string)-k+1):
		list_of_substrings.append(string[i:i+k])
	return list_of_substrings

def most_occuring_substring(list_of_substrings):
	most_common_words = []
	c = Counter(list_of_substrings).most_common()
	max_number = c[0][1]
	for element in c:
		if element[1] >= max_number:
			most_common_words.append(element[0].strip())
	return most_common_words

sd = sliding_string_window(string,k)
m = most_occuring_substring(sd)

g=[]
for i in m:
	g.append((string.find(i), i))

print(g)
print(sorted(g))

print(' '.join(m))