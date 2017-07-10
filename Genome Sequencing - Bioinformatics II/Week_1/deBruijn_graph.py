from collections import defaultdict
import sys
# kmers = sys.stdin.readlines()

#kmers = ["GCGA","CAAG","AAGA","GCCG","ACAA","AGTA","TAGG","AGTA","ACGT","AGCC","TTCG","AGTT","AGTA","CGTA","GCGC","GCGA","GGTC","GCAT","AAGC","TAGA","ACAG","TAGA","TCCT","CCCC","GCGC","ATCC","AGTA","AAGA","GCGA","CGTA"]
# kmers = ["GCGA","CAAG","AAGA","GCCG","ACAA","AGTA","TAGG","AGTA","ACGT","AGCC","TTCG","AGTT","AGTA","CGTA","GCGC","GCGA","GGTC","GCAT","AAGC","TAGA","ACAG","TAGA","TCCT","CCCC","GCGC","ATCC","AGTA","AAGA","GCGA","CGTA"]
kmers = ["GCGA","CAAG","AAGA","GCCG","ACAA","AGTA","TAGG","AGTA","ACGT","AGCC","TTCG","AGTT","AGTA","CGTA","GCGC","GCGA","GGTC","GCAT","AAGC","TAGA","ACAG","TAGA","TCCT","CCCC","GCGC","ATCC","AGTA","AAGA","GCGA","CGTA"]
# kmers = [kmer.strip() for kmer in kmers]
# name = input().strip()
# with open(name+".txt", "r") as f:
# 	kmers = f.readlines()
# 	kmers = [kmer.strip() for kmer in kmers]

print(kmers)
#DeBrujin from graphs
'''
tuples = [(kmer[:len(kmer) - 1], kmer[1:]) for kmer in kmers]
dd = defaultdict(set)
for t in tuples:
    dd[t[0]].add(t[1])
print (*(sorted([key + ' -> ' + ','.join(sorted([v for v in value]))
                       for key, value in dd.items()])),sep ='\n')
'''
#print(kmers)
composition = kmers

def deBruijnGraph(kmers):
    k = len(kmers[0])
    graph = {}
    for i in range(len(kmers)):
        try:
            graph[kmers[i][:-1]].append(kmers[i][1:])
        except:
            graph[kmers[i][:-1]] = [kmers[i][1:]]
    return graph

graph = deBruijnGraph(composition)
print(graph)
with open("bruj_answer.txt", "w") as f:
	g = sorted([key + ' -> ' + ','.join(sorted([v for v in value])) for key, value in graph.items()])
	ii = [i.strip() for i in g]
	f.write('\n'.join(ii).strip())
print (*(sorted([key + ' -> ' + ','.join(sorted([v for v in value]))
                       for key, value in graph.items()])))