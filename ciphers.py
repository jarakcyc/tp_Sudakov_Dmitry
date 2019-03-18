def shift_symbol(c, add):
	cur_key = ord(c)
	if (ord(c.lower()) >= ord('a') and ord(c.lower()) <= ord('z')):
		if (c.lower() == c):
			cur_key -= ord('a')
		else:
			cur_key -= ord('A')
		cur_key = (cur_key + add) % 26
		if (c.lower() == c):
			cur_key += ord('a')
		else:
			cur_key += ord('A')
	return chr(cur_key)

def caesar(text, key, flag):
	key += (abs(key) // 26 + 1) * 26
	key %= 26
	if (flag == True):
		add = key
	else:
		add = 26 - key
	res = ""
	for line in text:
		for c in list(line): 
			res += shift_symbol(c, add)
	return res

def encode_caesar(text, key):
	return caesar(text, key, 1)
def decode_caesar(text, key):
	return caesar(text, key, 0)

def vigenere(text, key, flag):
	res = ""
	for line in text:
		cnt = (len(line) + len(key)) // len(key)
		codeline = key * cnt
		symbols = list(line)
		for i in range(len(symbols)):
			c = symbols[i]
			codesymbol = list(codeline)[i]
			if (flag == True):
				add = ord(codesymbol.lower()) - ord('a')
			else:
				add = 26 - (ord(codesymbol.lower()) - ord('a'))
			res += shift_symbol(c, add)
	return res

def encode_vigenere(text, key):
	return vigenere(text, key, 1)
def decode_vigenere(text, key):
	return vigenere(text, key, 0)