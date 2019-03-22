import ciphers
import hack

In = 'ATTACKATDAWN'
assert(ciphers.encode_vigenere(In, 'LEMON') == 'LXFOPVEFRNHR')

In = 'ATTACkatdawn'
assert(ciphers.encode_vigenere(In, 'LEMON') == 'LXFOPvefrnhr')

In = 'LXFOPVEFRNHR'
assert(ciphers.decode_vigenere(In, 'LEMON') == 'ATTACKATDAWN')

In = 'hello world'
assert(ciphers.encode_caesar(In, 5) == 'mjqqt btwqi')

In = 'mjqqt btwqi'
assert(ciphers.decode_caesar(In, 5) == 'hello world')

In = 'ohoh upRvNkh Ul yhzopmyblzo'
assert(ciphers.decode_caesar(In, 7) == 'haha niKoGda Ne rashifruesh')

def test_hack(text, model):
    for k in range(26):
        i = open(text, 'r')
        o = open('input.txt', 'w')
        start = i.read()
        o.write(ciphers.encode_caesar(start, k))
        i.close()
        o.close()
        i = open('input.txt', 'r')
        assert(hack.hack_caesar(i.read(), model) == ciphers.encode_caesar(start, 0))
        i.close()
test_hack('text_1.txt', 'model.txt')
# test_hack('text_2.txt', 'model.txt')

print('ALL TESTS PASSED')