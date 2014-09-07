def shift(string, shift): #Uses an ASCII variant, a shift of 1 applied to 'z' goes to '{'
	out = []
	for char in string:
		out.append(chr(ord(char) - int(shift)))
	return "".join(out)
