#!/usr/bin/env python3

import string

characters = []
for _, y in zip(range(1, 27), string.ascii_lowercase):
    characters.append(y)

# print(characters)
decimal = [6,2,26,8,16,21,17,18,3,18,1,17,6,8,3,2,1,14,5,18,17,10,21,18,18,25,14,5,5,2,10,20,25,14,13,18,17,10,22,7,21,5,14,22,1,10,14,7,18,5,15,18,6,22,17,7,21,18,10,21,22,7,18,16,21,22,16,24,18,1,6,7,21,18,3,14,6,6,10,2,5,17,22,6,7,10,18,25,25,22,16,24,25,2,6,18,6,16,7,2]

flag = []
for d in decimal:
    flag.append(characters[d-1])

print(''.join(flag))

# somuchdependsuponaredwheelarrowglazedwithrainwaterbesidthewhitechickens the password is twellicklosescto

