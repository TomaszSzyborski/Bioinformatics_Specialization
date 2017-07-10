import sys
import numpy as np

def dpmanhattantourist(n,m,down,right):
	s = np.zeros((n+1,m+1), dtype=int)
	for i in range(1,n+1):
		s[i][0] = s[i-1][0] + down[i-1][0]
	for j in range(1,m+1):
		s[0][j] = s[0][j-1] + right[0][j-1]
	for i in range(1,n+1):
		for j in range(1,m+1):
			s[i][j] = max(s[i-1][j]+down[i-1][j],s[i][j-1]+right[i][j-1])
	
	return s[n][m]

if __name__ == '__main__':
	# filename = sys.stdin.read().strip()
	filename = "dataset_261_10.txt"
	with open(filename) as file:
		data = []
		for line in file:
			data.append(line[:-1])

	n,m = map(int,data[0].split())

	down = []
	right = []

	for i in range(1,n+1):
		d = [int(num) for num in data[i].strip().split()]
		down.append(d)

	for j in range(n+2,2*n+3):
		r = [int(num) for num in data[j].strip().split()]
		right.append(r)
		
	print(dpmanhattantourist(n,m,down,right))


# import scipy
# silnia = scipy.math.factorial
# def binomialCoeff(m,n):
#     return ( int(silnia(m+n)/(float(silnia(m)*silnia(n))))   )

# binomialCoeff(16,12)