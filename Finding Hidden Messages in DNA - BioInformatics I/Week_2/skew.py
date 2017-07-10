import sys

def skew(Genome):
    skew = [0]

    for i in range(0, len(Genome)):
        if Genome[i] == 'C':
            skew.append(skew[i] - 1)
        elif Genome[i] == 'G':
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])
    return skew

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines() # read in the input from STDIN
    genome_1 = lines[0].strip()

    answer = skew(genome_1)

    for num in answer:
        print(num)