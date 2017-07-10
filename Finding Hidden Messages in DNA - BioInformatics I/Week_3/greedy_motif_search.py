import sys

file_name = sys.stdin.read().strip() # read in the input from STDIN

dna = []
global k,t

with open(file_name) as f:
	for line in f:
		if len(line.split()) > 1:
			k,t = map(int,line.split())
		else:
			dna.append(line[:-1])

def count(motifs):
    count = {} 
    k = len(motifs[0])
    for symbol in "GCAT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def profile(motifs):
    t = len(motifs)
    k = len(motifs[0])
    profile = {}
    profile = count(motifs)
    for symbol in 'GCAT':
        for j in range(k):
            profile[symbol][j] = profile[symbol][j]/float(t)
    return profile

def consensus(motifs):
    
    k = len(motifs[0])
    counts = count(motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequent_symbol = ""
        for symbol in "GCAT":
            if counts[symbol][j] > m:
                m = counts[symbol][j]
                frequent_symbol = symbol
        consensus += frequent_symbol
    return consensus

def score(motifs):
    profile = count(motifs)
    _consensus = consensus(motifs)
    t = len(motifs)
    score = 0
    for i in range(len(motifs[0])):
        score = score + (t - profile[_consensus[i]][i])
    return score

def pr(text, profile):
    pr = 1
    for i in range(len(text)):
        pr = pr*profile[text[i]][i]
    return pr

def profile_most_probable_pattern(text, profile):
    T = len(text)
    K = len(profile['A'])
    prob = 0
    x = text[0:K]
    for i in range(T - K + 1):
        subtext = text[i:i+K]
        temp_prob = pr(subtext,profile)
        if temp_prob > prob:
            prob = temp_prob
            x = subtext
    return x

def greedy_motif_search(dna, k, t):
    best_motifs = []
    for i in range(0, t):
        best_motifs.append(dna[i][0:k])
    n = len(dna[0])
    for i in range(n-k+1):
        motifs = []
        motifs.append(dna[0][i:i+k])
        for j in range(1, t):
            P = profile(motifs[0:j])
            motifs.append(profile_most_probable_pattern(dna[j], P))
        if score(Motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs

ans = greedy_motif_search(dna,k,t)
for result in ans:
	print(result)
