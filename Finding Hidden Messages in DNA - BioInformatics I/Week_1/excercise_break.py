with open("Vibrio_cholerae.txt", "r") as f:
	string = f.read().strip()

substring="CTTGATCAT"

def sliding_string_window(string, substring):
	list_of_substring_indexes = []
	for i in range(len(string)-len(substring)+1):
		if string[i:i+len(substring)] == substring:
			list_of_substring_indexes.append(i)
	return list_of_substring_indexes

normal = sliding_string_window(string, substring)
to_file = ' '.join(map(str, normal))

with open("excercise_break_answer.txt", "w") as f:
	f.write(to_file)
