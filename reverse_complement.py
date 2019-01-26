def Reverse(text):
	rev = ""
	for char in text:
		rev = char + rev
	return rev

def Complement(text):
	comp = ""
	for char in text:
		if char == "A":
			comp = comp + "T"
		elif char == "T":
			comp = comp + "A"
		elif char == "C":
			comp = comp + "G"
		elif char == "G":
			comp = comp + "C"
	return comp

def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern)
    Pattern = Complement(Pattern)
    return Pattern