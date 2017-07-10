import sys

def reverse(p):
	x = p[::-1]
	x = [-i for i in x]
	return x


def greedysort(p):
	n = len(p)
	pos = 0
	perms = []
	while pos < n:
		nums = [abs(i) for i in p[pos:]]
		min_pos = nums.index(min(nums)) + pos
		p[pos:min_pos+1] = reverse(p[pos:min_pos+1])
		#print '('+' '.join('+'+str(i) if i>0 else str(i) for i in p)+')'
		perms.append('('+' '.join('+'+str(i) if i>0 else str(i) for i in p)+')')
		if p[pos] < 0:
			p[pos] = -p[pos]
			#print '('+' '.join('+'+str(i) if i>0 else str(i) for i in p)+')'
			perms.append('('+' '.join('+'+str(i) if i>0 else str(i) for i in p)+')')
		pos += 1
	return perms

if '__name__' == '__main__':
	filename = sys.stdin.read().strip()
	seq = ''
	with open(filename) as file:
		for line in file:
			seq += line[:-1]

	seq = list(map(int,seq[1:-1].split()))

	ans = greedysort(seq)
	#print greedysort(ans)
	print(ans)