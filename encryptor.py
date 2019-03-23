import sys
import argparse
from ciphers import *
from hack import *


class catcher:
    pass

parser = argparse.ArgumentParser(description='Parser')
subparsers = parser.add_subparsers(dest='type')

encode_parser = subparsers.add_parser('encode')
encode_parser.add_argument('--cipher', default=None, dest='cipher')
encode_parser.add_argument('--key', default=None, dest='key')
encode_parser.add_argument('--input-file', default=None, dest='In')
encode_parser.add_argument('--output-file', default=None, dest='Out')

decode_parser = subparsers.add_parser('decode')
decode_parser.add_argument('--cipher', default=None, dest='cipher')
decode_parser.add_argument('--key', default=None, dest='key')
decode_parser.add_argument('--input-file', default=None, dest='In')
decode_parser.add_argument('--output-file', default=None, dest='Out')

train_parser = subparsers.add_parser('train')
train_parser.add_argument('--text-file', default=None, dest='text')
train_parser.add_argument('--model-file', default=None, dest='model')
train_parser.add_argument('--cipher', default=None, dest='cipher')

hack_parser = subparsers.add_parser('hack')
hack_parser.add_argument('--input-file', default=None, dest='In')
hack_parser.add_argument('--output-file', default=None, dest='Out')
hack_parser.add_argument('--model-file', default=None, dest='model')
hack_parser.add_argument('--cipher', default=None, dest='cipher')

parser.parse_args(namespace=catcher)

f = sys.stdin
o = sys.stdout

if (catcher.type == 'encode'):
    if (catcher.In is not None):
        f = open(catcher.In, 'r')
    if (catcher.Out is not None):
        o = open(catcher.Out, 'w')

    text = f.read()
    if (catcher.cipher == 'caesar'):
        try:
            int(catcher.key)
        except Exception:
            raise TypeError('key must be integer')
        o.write(encode_caesar(text, int(catcher.key)))
    elif (catcher.cipher == 'vigenere'):
        o.write(encode_vigenere(text, str(catcher.key)))
    elif (catcher.cipher == 'vernam'):
        o.write(encode_vernam(text, str(catcher.key)))
    else:
        raise ValueError('unknown cipher')

    if (catcher.In is not None):
        f.close()
    if (catcher.Out is not None):
        o.close()

if (catcher.type == 'decode'):
    if (catcher.In is not None):
        f = open(catcher.In, 'r')
    if (catcher.Out is not None):
        o = open(catcher.Out, 'w')

    text = f.read()

    if (catcher.cipher == 'caesar'):
        try:
            int(catcher.key)
        except Exception:
            raise TypeError('key must be integer')
        o.write(decode_caesar(text, int(catcher.key)))
    elif (catcher.cipher == 'vigenere'):
        o.write(decode_vigenere(text, str(catcher.key)))
    elif (catcher.cipher == 'vernam'):
        o.write(decode_vernam(text, str(catcher.key)))
    else:
        raise ValueError('unknown cipher')

    if (catcher.In is not None):
        f.close()
    if (catcher.Out is not None):
        o.close()

if (catcher.type == 'train'):
    if (catcher.text is not None):
        f = open(catcher.text, 'r')
    if (catcher.model is not None):
        o = open(catcher.model, 'w')

    text = f.read()

    if (catcher.cipher == 'caesar'):
        gista = get_gistagram(text)
        for i in gista:
            o.write(str(i) + '\n')
    elif (catcher.cipher == 'vigenere'):
        match_index = get_match_index(text)
        o.write(str(match_index) + '\n')
        gista = get_gistagram(text)
        for i in gista:
            o.write(str(i) + '\n')
    else:
        raise ValueError('unknown cipher')

    if (catcher.text is not None):
        f.close()
    if (catcher.model is not None):
        o.close()

if (catcher.type == 'hack'):
    if (catcher.In is not None):
        f = open(catcher.In, 'r')
    if (catcher.Out is not None):
        o = open(catcher.Out, 'w')

    text = f.read()

    if (catcher.cipher == 'caesar'):
        o.write(hack_caesar(text, catcher.model))
    elif (catcher.cipher == 'vigenere'):
        o.write(hack_vigenere(text, catcher.model))
    else:
        raise ValueError('unknow cipher')

    if (catcher.In is not None):
        f.close()
    if (catcher.Out is not None):
        o.close()
