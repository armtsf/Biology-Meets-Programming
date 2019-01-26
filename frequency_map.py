def PatternCount(Text, Pattern):
	pat_len = len(Pattern)
	count = 0
	for i in range(len(Text) - pat_len + 1):
		tmp = Text[i : i + pat_len]
		if tmp == Pattern:
			count += 1
	return count

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    for i in range(n - k + 1):
		Pattern = Text[i : i + k]
		freq[Pattern] = PatternCount(Text, Pattern)
    return freq

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
				words.append(key)
    return words