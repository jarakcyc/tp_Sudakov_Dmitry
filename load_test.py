import ciphers
import hack
import pytest
import time

beta = 20


def setup():
    print('\n')


def get_time(file, func, key):
    i = open(file, 'r')
    text = i.read()
    i.close()
    start_time = time.time()
    exec('ciphers.{}(text, {})'.format(func, key))
    return time.time() - start_time


# caesar
def test_encode_caesar():
    avg = 0
    with open('./testsrc/Crime_and_Punishment.txt', 'r') as f:
        txt = f.read()
    for i in range(beta):
        file = './testsrc/Crime_and_Punishment.txt'
        avg += get_time(file, 'encode_caesar', 15)
    print('test_encode_caesar execute time: {} on text of {} symbols'.format(avg / beta, len(txt)))


def test_decode_caesar():
    avg = 0
    with open('./testsrc/Crime_and_Punishment.txt', 'r') as f:
        txt = f.read()
    for i in range(beta):
        file = './testsrc/Crime_and_Punishment.txt'
        avg += get_time(file, 'decode_caesar', 15)
    print('test_decode_caesar execute time: {} on text of {} symbols'.format(avg / beta, len(txt)))


# vigenere
def test_encode_vigenere():
    avg = 0
    with open('./testsrc/Crime_and_Punishment.txt', 'r') as f:
        txt = f.read()
    for i in range(beta):
        file = './testsrc/Crime_and_Punishment.txt'
        avg += get_time(file, 'encode_vigenere', "'helloworld'")
    print('test_encode_vigenere execute time: {} on text of {} symbols'.format(avg / beta, len(txt)))


def test_decode_vigenere():
    avg = 0
    with open('./testsrc/Crime_and_Punishment.txt', 'r') as f:
        txt = f.read()
    for i in range(beta):
        file = './testsrc/Crime_and_Punishment.txt'
        avg += get_time(file, 'decode_vigenere', "'helloworld'")
    print('test_decode_vigenere execute time: {} on text of {} symbols'.format(avg / beta, len(txt)))


# vernam
def test_encode_vernam():
    avg = 0
    with open('./testsrc/Crime_and_Punishment.txt', 'r') as f:
        txt = f.read()
    for i in range(beta):
        file = './testsrc/Crime_and_Punishment.txt'
        avg += get_time(file, 'encode_vernam', "'helloworld'")
    print('test_encode_vernam execute time: {} on text of {} symbols'.format(avg / beta, len(txt)))


def test_decode_vernam():
    avg = 0
    with open('./testsrc/Crime_and_Punishment.txt', 'r') as f:
        txt = f.read()
    for i in range(beta):
        file = './testsrc/Crime_and_Punishment.txt'
        avg += get_time(file, 'decode_vernam', "'helloworld'")
    print('test_decode_vernam execute time: {} on text of {} symbols'.format(avg / beta, len(txt)))


# hack caesar
def test_hack_caesar():
    i = open('./testsrc/Crime_and_Punishment.txt', 'r')
    o = open('input.txt', 'w')
    start = i.read()
    o.write(ciphers.encode_caesar(start, 15))
    i.close()
    o.close()
    i = open('input.txt', 'r')
    start_time = time.time()
    assert(hack.hack_caesar(i.read(), './testsrc/model_caesar.txt') == start)
    print('test_hack_caesar execute time: {} on text of {} symbols'.format(time.time() - start_time, len(start)))
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
    start_time = time.time()
    assert(hack.hack_vigenere(i.read(), './testsrc/model_caesar.txt') == start)
    print('test_hack_vigenere execute time: {} on text of {} symbols'.format(time.time() - start_time, len(start)))
    i.close()
