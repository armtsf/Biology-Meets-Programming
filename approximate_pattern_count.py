def ApproximatePatternCount(Pattern, Text, d):
    count = 0
    k = len(Pattern)
    n = len(Text)
    for i in range(n - k + 1):
        if HammingDistance(Text[i : i + k], Pattern) < d + 1:
            count += 1
    return count

def HammingDistance(p, q):
    dis = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dis += 1
    return dis