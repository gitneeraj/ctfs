#!/usr/bin/env python3

import pickle

data = pickle.load( open( "data", "rb" ) )
print(data)

# for key, value in enumerate(data):
#     print(key, value)
flag = []
characters = [112, 49, 99, 107, 108, 51, 95, 121, 48, 117, 82, 95, 109, 51, 53, 53, 52, 103, 51]

# for v in data:
#     if v != 24 and type(v) == int:
#         flag.append(data[v])
#         print(data[v])

# print(flag)
# print(''.join(flag))

for ch in characters:
    flag.append(chr(ch))

print(''.join(flag))