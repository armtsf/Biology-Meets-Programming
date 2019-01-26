def PatternMatching(Text, Pattern):
	pat_len = len(Pattern)
	positions = []
	for i in range(len(Text) - pat_len + 1):
		tmp = Text[i : i + pat_len]
		if tmp == Pattern:
			positions.append(i)
	return positions