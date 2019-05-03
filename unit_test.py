import ciphers
import hack
import pytest

def test_encode_vigenere_1():
    In = 'ATTACKATDAWN'
    assert(ciphers.encode_vigenere(In, 'LEMON') == 'LXFOPVEFRNHR')


def test_encode_vigenere_2():
    In = 'ATTACkatdawn'
    assert(ciphers.encode_vigenere(In, 'LEMON') == 'LXFOPvefrnhr')


def test_decode_vigenere():
    In = 'LXFOPVEFRNHR'
    assert(ciphers.decode_vigenere(In, 'LEMON') == 'ATTACKATDAWN')


def test_encode_caesar():
    In = 'hello world'
    assert(ciphers.encode_caesar(In, 5) == 'mjqqt btwqi')


def test_decode_caesar_1():
    In = 'mjqqt btwqi'
    assert(ciphers.decode_caesar(In, 5) == 'hello world')


def test_decode_caesar_2():
    In = 'ohoh upRvNkh Ul yhzopmyblzo'
    assert(ciphers.decode_caesar(In, 7) == 'haha niKoGda Ne rashifruesh')


def test_encode_vernam():
    key = 'EVTIQWXQVVOPMCXREPYZ'
    In = 'ALLSWELLTHATENDSWELL'
    assert ciphers.encode_vernam(In, key) == 'EGEAMAIBOCOIQPAJATJK'


def test_decode_vernam():
    key = 'EVTIQWXQVVOPMCXREPYZ'
    In = 'EGEAMAIBOCOIQPAJATJK'
    assert ciphers.decode_vernam(In, key) == 'ALLSWELLTHATENDSWELL'


def test_hack_caesar_1():
    for k in range(26):
        i = open('./testsrc/text_1.txt', 'r')
        o = open('input.txt', 'w')
        start = i.read()
        o.write(ciphers.encode_caesar(start, k))
        i.close()
        o.close()
        i = open('input.txt', 'r')
        assert(hack.hack_caesar(i.read(), './testsrc/model_caesar.txt') == ciphers.encode_caesar(start, 0))
        i.close()


def test_hack_caesar_2():
    for k in range(26):
        i = open('./testsrc/text_2.txt', 'r')
        o = open('input.txt', 'w')
        start = i.read()
        o.write(ciphers.encode_caesar(start, k))
        i.close()
        o.close()
        i = open('input.txt', 'r')
        assert(hack.hack_caesar(i.read(), './testsrc/model_caesar.txt') == ciphers.encode_caesar(start, 0))
        i.close()


#test_hack('text_1.txt', 'model.txt')
# test_hack('text_2.txt', 'model.txt')

#print('ALL TESTS PASSED')