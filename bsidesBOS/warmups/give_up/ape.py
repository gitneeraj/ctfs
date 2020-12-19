#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes

cipher=3338241147603780238248786938107867350016489922013403739812786768782254742117160331044416747901

print(long_to_bytes(cipher).decode())
