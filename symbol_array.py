def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    array[0] = PatternCount(symbol, Genome[0:n//2])

    for i in range(1, n):
        array[i] = array[i-1]

        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

def PatternCount(Pattern, Text):
	pat_len = len(Pattern)
	count = 0
	for i in range(len(Text) - pat_len + 1):
		tmp = Text[i : i + pat_len]
		if tmp == Pattern:
			count += 1
	return count