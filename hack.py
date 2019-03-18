import ciphers
import math

def get_gistagram(text):
	cnt = [0] * 26
	for line in text:
		for c in list(line):
			val = ord(c.lower())
			if (val >= ord('a') and val <= ord('z')):
				cnt[val - ord('a')] += 1
	return cnt

base_gista = []

def get_base(model):
	f = open(model, 'r')
	lines = f.readlines()
	f.close()
	for x in lines:
		base_gista.append(int(x))

def match(gista):
	res = 0
	for i in range(26):
		res += abs(base_gista[i] - gista[i]) ** 2
	return res

def hack(text, model):
	get_base(model)
	best = -1
	shift = 0
	for key in range(26):
		cur = get_gistagram([ciphers.encode_caesar(text, key)])
		val = match(cur)
		if (best == -1 or val < best):
			best = val
			shift = key
	return ciphers.encode_caesar(text, shift)
