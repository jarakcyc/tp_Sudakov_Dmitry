import ciphers
import hack
import pytest

def test_1():
    In = 'ATTACKATDAWN'
    assert(ciphers.encode_vigenere(In, 'LEMON') == 'LXFOPVEFRNHR')


def test_2():
    In = 'ATTACkatdawn'
    assert(ciphers.encode_vigenere(In, 'LEMON') == 'LXFOPvefrnhr')


def test_3():
    In = 'LXFOPVEFRNHR'
    assert(ciphers.decode_vigenere(In, 'LEMON') == 'ATTACKATDAWN')


def test_4():
    In = 'hello world'
    assert(ciphers.encode_caesar(In, 5) == 'mjqqt btwqi')


def test_5():
    In = 'mjqqt btwqi'
    assert(ciphers.decode_caesar(In, 5) == 'hello world')


def test_6():
    In = 'ohoh upRvNkh Ul yhzopmyblzo'
    assert(ciphers.decode_caesar(In, 7) == 'haha niKoGda Ne rashifruesh')


'''
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
'''