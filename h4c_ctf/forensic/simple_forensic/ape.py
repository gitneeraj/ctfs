#!/usr/bin/env python3

import re

with open("simple/H&C.txt") as h:
    data = [x[:-1] for x in h.readlines()]

for line in data:
    print(re.findall(r"(\s+)", line))