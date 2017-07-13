import sys

def _skew(genome):
    skew = [0]
    for i in range(0, len(genome)):
        if genome[i] == 'C':
            skew.append(skew[i] - 1)
        elif genome[i] == 'G':
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])
    return skew

def min_skew(genome):
    skew = _skew(genome)
    minimum = min(skew)
    return [i for i, val in enumerate(skew) if val == minimum]

def max_skew(genome):
    skew = _skew(genome)
    maximum = max(skew)
    return [i for i, val in enumerate(skew) if val == maximum]

if __name__ == '__main__':
    #lines = sys.stdin.read().splitlines() # read in the input from STDIN
    #genome_1 = lines[0].strip()
    name = "dataset_7_6.txt"
    with open(name, 'r') as f:
        genome_1 = f.read()

    answer = min_skew(genome_1)

    for num in answer:
        print(num)