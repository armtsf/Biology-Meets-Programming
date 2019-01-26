def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Score(Motifs):
    score = 0;
    consensus = Consensus(Motifs)
    t = len(Motifs)
    for j in range(len(consensus)):
        for i in range(t):
            if Motifs[i][j] != consensus[j]:
                score += 1
    return score
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    profile = Count(Motifs)
    for symbol in "ACGT":
        for j in range(len(profile[symbol])):

            profile[symbol][j] = profile[symbol][j] / t;
    return profile

def Pr(Text, Profile):
    pr = 1;
    for i in range(len(Text)):
        pr = pr * Profile[Text[i]][i]
    return pr

def ProfileMostProbablePattern(text, k, profile):
    ans = ""
    pr = -1;
    for i in range(len(text) - k + 1):
        t = text[i:i + k]
        newPr = Pr(t, profile)
        if newPr > pr:
            ans = t
            pr = newPr
    return ans

def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

     