alpha = 26

def is_eng(s):
    s = s.lower()
    return bool(ord(s) >= ord('a') and ord(s) <= ord('z'))

def shift_symbol(c, add):
    while (add < 0):
        add += alpha
    cur_key = ord(c)
    if (is_eng(c)):
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
    key += (abs(key) // alpha + 1) * alpha
    key %= alpha
    if (flag == True):
        add = key
    else:
        add = alpha - key
    res = ""
    for c in list(text): 
        res += shift_symbol(c, add)
    return res

def encode_caesar(text, key):
    return caesar(text, key, 1)
def decode_caesar(text, key):
    return caesar(text, key, 0)

def vigenere(text, key, flag):
    res = ""
    cnt = (len(text) + len(key)) // len(key)
    codeline = key * cnt
    symbols = list(text)
    for i in range(len(symbols)):
        c = symbols[i]
        codesymbol = list(codeline)[i]
        if (flag == True):
            add = ord(codesymbol.lower()) - ord('a')
        else:
            add = alpha - (ord(codesymbol.lower()) - ord('a'))
        res += shift_symbol(c, add)
    return res

def encode_vigenere(text, key):
    return vigenere(text, key, 1)
def decode_vigenere(text, key):
    return vigenere(text, key, 0)

def encode_vernam(text, key):
    res = ""
    for c, x in zip(list(text), list(key)):
        s = c.lower()
        y = x.lower()
        nxt = c
        if (is_eng(s)):
            val = (ord(s) - ord('a')) ^ (ord(y) - ord('a'))
            nxt = chr(val + ord('a'))
            if (s != c):
                nxt = nxt.upper()
        res += nxt
    return res

def decode_vernam(text, key):
    return encode_vernam(text, key)

