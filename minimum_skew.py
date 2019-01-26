def MinimumSkew(Genome):
    positions = []
    skew = SkewArray(Genome)
    minimum = max(skew.values())
    for i in range(len(Genome)):
        if skew[i] == minimum:
            positions.append(i)
    return positions

def SkewArray(Genome):
    skew = {}
    skew[0] = 0
    for i in range(len(Genome)):
        if Genome[i] == "A":
            skew[i+1] = skew[i]
        if Genome[i] == "T":
            skew[i+1] = skew[i]
        if Genome[i] == "G":
            skew[i+1] = skew[i] + 1
        if Genome[i] == "C":
            skew[i+1] = skew[i] - 1
    return skew