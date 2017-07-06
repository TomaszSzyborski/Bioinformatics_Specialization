# put your python code here
import sys # you must import "sys" to read from STDIN


lines = sys.stdin.read().splitlines()# read in the input from STDIN
index = int(lines[0].strip())
k = int(lines[1].strip())

number_to_symbol = {0:'A', 1:'C', 2:'G', 3:'T'}
symbol_to_number = {'A':0, 'C':1, 'G':2, 'T':3}
		    
def number_to_pattern(n, k):
    pattern = [number_to_symbol[0] for el in range(k)]
    for i in range(k - 1, -1, -1):
        key=n%4
        pattern[i]= number_to_symbol[int(key)]
        n /= 4
    return ''.join(pattern)
		    

print(number_to_pattern(index, k))