import sys
from collections import defaultdict
from itertools import combinations, product

def rev_comp(sequence):
	rev_comp = ''
	for nucleotide in sequence:
		if nucleotide == 'A':
			rev_comp = rev_comp + 'T'
		elif nucleotide == 'T':
			rev_comp = rev_comp + 'A'
		elif nucleotide == 'G':
			rev_comp = rev_comp + 'C'
		elif nucleotide == 'C':
			rev_comp = rev_comp + 'G'
	rev_comp = rev_comp[::-1]
	return rev_comp


def kmer_mismatches(kmer, d):
    mismatches = [kmer] 
    alt_bases = {'A':'CGT', 'C':'AGT', 'G':'ACT', 'T':'ACG'}
    for dist in range(1, d+1):
        for change_indices in combinations(range(len(kmer)), dist):
            for substitutions in product(*[alt_bases[kmer[i]] for i in change_indices]):
                new_mistmatch = list(kmer)
                for idx, sub in zip(change_indices, substitutions):
                    new_mistmatch[idx] = sub
                mismatches.append(''.join(new_mistmatch))
    return mismatches

def frequentwords_mismatches_reverse(seq, k, d):
    kmer_freq = defaultdict(int)
    for i in range(len(seq)-k+1):
        kmer_freq[seq[i:i+k]] += 1
        kmer_freq[rev_comp(seq[i:i+k])] += 1

    mismatch_count = defaultdict(int)
    for kmer, freq in kmer_freq.items():
        for mismatch in kmer_mismatches(kmer, d):
            mismatch_count[mismatch] += freq

    max_count = max(mismatch_count.values())    
    return sorted([kmer for kmer, count in mismatch_count.items() if count == max_count])

if __name__ == '__main__':
    # lines = sys.stdin.read().splitlines() # read in the input from STDIN
    name = sys.argv[1]
    with open(name, 'r') as f:
        lines = f.readlines()
        genome_1 = lines[0].strip()
        kmer, number= list(map(int, lines[1].strip().split()))

    answer = frequentwords_mismatches_reverse(genome_1,kmer,number)
    print(" ".join(list(map(str, list(answer)))))


