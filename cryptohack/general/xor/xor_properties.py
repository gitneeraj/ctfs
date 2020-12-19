#!/usr/bin/env python3

from pwn import xor

# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

k1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
k1_x_k2 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
k2_x_k3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
flag_x_k1_k3_k2 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

k2 = xor(k1, k1_x_k2)
k3 = xor(k2, k2_x_k3)
flag = xor(k1, k3, k2, flag_x_k1_k3_k2)
# print(k1, k1_x_k2, k2_x_k3, flag_x_k1_k3_k2)
# print(k2)
print(flag.decode())