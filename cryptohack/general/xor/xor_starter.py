#!/usr/bin/env python3

text = "label"

xored = [ ord(c) ^ 13 for c in text]
print('crypto{' + "".join(chr(n) for n in xored) + '}')