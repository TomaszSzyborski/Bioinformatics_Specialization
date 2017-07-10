import sys # you must import "sys" to read from STDIN
import re
lines = list(map(strip, sys.stdin.read().splitlines())) # read in the input from STDIN


def find_overllaping_occurences(string, substring):
	return len(re.findall('(?='+substring+')', string))

print(find_overllaping_occurences(lines[0], lines[1]))