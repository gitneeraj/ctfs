#!/usr/bin/env python3

import re

with open('challenge.txt') as h:
    data = h.readlines()[0]
    dashs = re.findall(r"(_|-)", data)
    print("".join(dashs))