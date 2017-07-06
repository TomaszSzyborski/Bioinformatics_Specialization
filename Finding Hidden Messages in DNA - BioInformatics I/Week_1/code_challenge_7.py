# put your python code here
import sys # you must import "sys" to read from STDIN

lines = sys.stdin.read()# read in the input from STDIN

genome = lines.strip()


numbertosymbol = {0:'A', 1:'C', 2:'G', 3:'T'}
symboltonumber = {'A':0, 'C':1, 'G':2, 'T':3}

def patterntonumber(pattern):
	if len(pattern)  == 0:
		return 0
	return 4 * patterntonumber(pattern[:-1]) + symboltonumber[pattern[-1]]

print(patterntonumber(genome))