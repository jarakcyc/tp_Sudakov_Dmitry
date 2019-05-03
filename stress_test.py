import ciphers
import hack
import pytest


# caesar
def test_caesar():
    with open('./testsrc/Crime_and_Punishment.txt', 'r') as f:
        txt = f.read()
    assert ciphers.decode_caesar(ciphers.encode_caesar(txt, 17), 17) == txt


# vigenere
def test_vigenere():
    with open('./testsrc/Crime_and_Punishment.txt', 'r') as f:
        txt = f.read()
    assert ciphers.decode_vigenere(ciphers.encode_vigenere(txt, 'hellodimas'), 'hellodimas') == txt


# vernam
def test_vernam():
    with open('./testsrc/Crime_and_Punishment.txt', 'r') as f:
        txt = f.read()
    assert ciphers.decode_vernam(ciphers.encode_vernam(txt, 'hellodimas'), 'hellodimas') == txt


# hack caesar
def test_hack_caesar():
    i = open('./testsrc/Crime_and_Punishment.txt', 'r')
    o = open('input.txt', 'w')
    start = i.read()
    o.write(ciphers.encode_caesar(start, 15))
    i.close()
    o.close()
    i = open('input.txt', 'r')
    assert(hack.hack_caesar(i.read(), './testsrc/model_caesar.txt') == start)
    i.close()


# hack vigenere
def test_hack_vigenere():
    i = open('./testsrc/Crime_and_Punishment.txt', 'r')
    o = open('input.txt', 'w')
    start = i.read()
    o.write(ciphers.encode_vigenere(start, 'dimasius'))
    i.close()
    o.close()
    i = open('input.txt', 'r')
    assert(hack.hack_vigenere(i.read(), './testsrc/model_vigenere.txt') == start)
    i.close()
