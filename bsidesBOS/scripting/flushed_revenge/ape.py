#!/usr/bin/env python3

from pwn import *

host = "challenge.ctf.games"
port = 30625

c = remote(host, port)
c.recv()
c.interactive()