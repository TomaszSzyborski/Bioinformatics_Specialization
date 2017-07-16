import sys

def make_edges(seqs):
	edges = []
	for read in seqs:
		edges.append(read[:-1]+ ' -> ' +read[1:])
	return edges

def reconstruct_string(edges):
	from collections import OrderedDict
	string_dict = OrderedDict()
	for line in edges:
		string_dict[line.strip().split(' -> ')[0]] = line.strip().split(' -> ')[1] 
	# string_dict = {line.strip().split(' -> ')[0]:line.strip().split(' -> ')[1] for line in edges}
	head = list(filter(lambda x: x not in list(string_dict.values()), list(string_dict.keys())))[0]
	tail = list(filter(lambda x: x not in list(string_dict.keys()), list(string_dict.values())))[0]
	print(tail)
	reconstructed_str = head[0]
	current_str = head
	while current_str != tail:
		current_str = string_dict[current_str]
		reconstructed_str += current_str[0]
		# print(current_str)
	reconstructed_str += tail[1:]

	return reconstructed_str


if __name__ == '__main__':
	data = []
	file_name = sys.argv[1]
	with open(file_name) as input_data:
		for line in input_data:
			data.append(line.strip())
	# k = int(data[0])
	reads = data[1:]
	edges = make_edges(reads)
	answer = reconstruct_string(edges)
	# print(answer)
	with open("answer_string_reconstruction.txt", "w") as data_output:
		data_output.write(answer)
