#!/usr/bin/env python3

from pwn import xor, unhex

data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

print(xor(unhex(data), 16).decode())