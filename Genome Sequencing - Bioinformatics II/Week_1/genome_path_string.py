import sys

def path(reads):
	string = reads[0]
	s = ''.join([r[-1]for r in reads[1:]])

	return ''.join([string,s])

if __name__ == '__main__':
	# file_name = sys.stdin.read().strip()
	#lines = sys.stdin.readlines()
	
	# Test_0
	#lines =["ACCGA","CCGAA","CGAAG","GAAGC","AAGCT"]
	# test_3
	# lines=["TCGGGGAATGCATC","CGGGGAATGCATCA","GGGGAATGCATCAC","GGGAATGCATCACA","GGAATGCATCACAA","GAATGCATCACAAA","AATGCATCACAAAG","ATGCATCACAAAGT","TGCATCACAAAGTG","GCATCACAAAGTGC","CATCACAAAGTGCA","ATCACAAAGTGCAG"]
	#lines = [line.strip() for line in lines]
	seqs = []
	with open("dataset_198_3.txt") as file:
		for line in file:
			seqs.append(line[:-1])
	answer = path(seqs).strip()
	print(answer)