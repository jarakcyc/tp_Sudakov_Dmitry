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
    for i in range(beta):
        file = './testsrc/Crime_and_Punishment.txt'
        avg += get_time(file, 'encode_caesar', 15)
    print('test_encode_caesar execute time: {}'.format(avg / beta))


def test_decode_caesar():
    avg = 0
    for i in range(beta):
        file = './testsrc/Crime_and_Punishment.txt'
        avg += get_time(file, 'decode_caesar', 15)
    print('test_decode_caesar execute time: {}'.format(avg / beta))

# vigenere
def test_encode_vigenere():
    avg = 0
    for i in range(beta):
        file = './testsrc/Crime_and_Punishment.txt'
        avg += get_time(file, 'encode_vigenere', "'helloworld'")
    print('test_encode_vigenere execute time: {}'.format(avg / beta))


def test_decode_vigenere():
    avg = 0
    for i in range(beta):
        file = './testsrc/Crime_and_Punishment.txt'
        avg += get_time(file, 'decode_vigenere', "'helloworld'")
    print('test_decode_vigenere execute time: {}'.format(avg / beta))

# vernam
def test_encode_vernam():
    avg = 0
    for i in range(beta):
        file = './testsrc/Crime_and_Punishment.txt'
        avg += get_time(file, 'encode_vernam', "'helloworld'")
    print('test_encode_vernam execute time: {}'.format(avg / beta))


def test_decode_vernam():
    avg = 0
    for i in range(beta):
        file = './testsrc/Crime_and_Punishment.txt'
        avg += get_time(file, 'decode_vernam', "'helloworld'")
    print('test_decode_vernam execute time: {}'.format(avg / beta))
