import sys
import argparse
import ciphers
import hack

class catcher:
	pass

parser = argparse.ArgumentParser(description = 'Parser')
subparsers = parser.add_subparsers(dest = 'type')

encode_parser = subparsers.add_parser('encode')
encode_parser.add_argument('--cipher', default = None, dest = 'cipher')
encode_parser.add_argument('--key', default = None, dest = 'key')
encode_parser.add_argument('--input-file', default = None, dest = 'In')
encode_parser.add_argument('--output-file', default = None, dest = 'Out')

decode_parser = subparsers.add_parser('decode')
decode_parser.add_argument('--cipher', default = None, dest = 'cipher')
decode_parser.add_argument('--key', default = None, dest = 'key')
decode_parser.add_argument('--input-file', default = None, dest = 'In')
decode_parser.add_argument('--output-file', default = None, dest = 'Out')

train_parser = subparsers.add_parser('train')
train_parser.add_argument('--text-file', default = None, dest = 'text')
train_parser.add_argument('--model-file', default = None, dest = 'model')

hack_parser = subparsers.add_parser('hack')
hack_parser.add_argument('--input-file', default = None, dest = 'In')
hack_parser.add_argument('--output-file', default = None, dest = 'Out')
hack_parser.add_argument('--model-file', default = None, dest = 'model')

parser.parse_args(namespace = catcher)

f = sys.stdin
o = sys.stdout

if (catcher.type == 'encode'):
	if (catcher.In != None):
		f = open(catcher.In, 'r')
	if (catcher.Out != None):
		o = open(catcher.Out, 'w')

	text = f.readlines()
	if (catcher.cipher == 'caesar'):
		o.write(ciphers.encode_caesar(text, int(catcher.key)))
	elif (catcher.cipher == 'vigenere'):
		o.write(ciphers.encode_vigenere(text, str(catcher.key)))

	if (catcher.In != None):
		f.close()
	if (catcher.Out != None):
		o.close()

if (catcher.type == 'decode'):
	if (catcher.In != None):
		f = open(catcher.In, 'r')
	if (catcher.Out != None):
		o = open(catcher.Out, 'w')

	text = f.readlines()
	if (catcher.cipher == 'caesar'):
		o.write(ciphers.decode_caesar(text, int(catcher.key)))
	elif (catcher.cipher == 'vigenere'):
		o.write(ciphers.decode_vigenere(text, str(catcher.key)))

	if (catcher.In != None):
		f.close()
	if (catcher.Out != None):
		o.close()

if (catcher.type == 'train'):
	if (catcher.text != None):
		f = open(catcher.text, 'r')
	if (catcher.model != None):
		o = open(catcher.model, 'w')

	text = f.readlines()
	gista = hack.get_gistagram(text)
	for i in gista:
		o.write(str(i) + '\n')

	if (catcher.text != None):
		f.close()
	if (catcher.model != None):
		o.close()

if (catcher.type == 'hack'):
	if (catcher.In != None):
		f = open(catcher.In, 'r')
	if (catcher.Out != None):
		o = open(catcher.Out, 'w')

	text = f.readlines()
	o.write(hack.hack(text, catcher.model))

	if (catcher.In != None):
		f.close()
	if (catcher.Out != None):
		o.close()
