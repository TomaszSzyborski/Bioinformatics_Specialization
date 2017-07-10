def convolution(spec):
	convolution_list = [str(i-j) for i in spec for j in spec if i-j > 0]
	return convolution_list

if __name__ == '__main__':
	filename = sys.stdin.read().strip()
	with open(filename) as file:
	for line in file:
		spectrum = map(int,line.split())

	ans = convolution(spectrum)
	for res in ans:
		print(res)
	with open('res.txt', 'w') as output_data:
		output_data.write(' '.join(convolution(spectrum)))


