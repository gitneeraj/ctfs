#!/usr/bin/env python3

from pwn import xor, unhex

data1 = unhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
data = bytearray.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
# key = [hex(ord(c)) for c in "crypto{"]

# print(key, data)
# print(xor(data,b'crypto{')) # this gives use the key some what
hint_plain_text = "crypto{"

key = ''
for i in range(len(hint_plain_text)):
	key += chr(data[i] ^ ord(hint_plain_text[i]))

key = f"{key}y"
print(key)

flag = ''
key_length = len(key)
for i in range(len(data)):
	# i%key_length helps avoiding out of range
	# print(data[i])
	flag += chr(data[i] ^ ord(key[i%key_length]))

print(flag)

# flag = ''
# for n in key:
#     if flag == '':
#         flag = xor(data, n)
#     else:
#         flag = xor(flag, n)
	
#     print(flag)
# key2 = sum(key)
# print(xor(data, key2))
# for k in key:
#     print(xor(data, k))
# xored = xor(data, key)

# print(unhex(data))
# print(xored)

# def encryptDecrypt(inpString): 
  
# 	# Define XOR key 
# 	# Any character value will work 
# 	xorKey = 'crypto{}'
  
# 	# calculate length of input string 
# 	length = len(inpString)
  
# 	# perform XOR operation of key 
# 	# with every caracter in string 
# 	for i in range(length):
	  
# 		inpString = (inpString[:i] + 
# 			 chr(ord(inpString[i]) ^ ord(xorKey)) +
# 					 inpString[i + 1:])
# 		print(inpString[i], end = "")
	  
# 	return inpString

# encryptDecrypt(data)


# from pwn import xor # check the bottom function for usage of this module


# hex_string = bytearray.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
# hex_string2 = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

# known_plain_text = 'crypto{'


# def determine_key(cipher_text : bytearray, plain_text : str):

#     key = ''
#     for i in range(len(plain_text)):
#         key += chr(cipher_text[i] ^ ord(plain_text[i]))
#     return key


# def get_flag(encrypted_msg : bytearray, key):
    
#     flag = ''
#     key_length = len(key)
#     for i in range(len(encrypted_msg)):
#         # i%key_length helps avoiding out of range
#         flag += chr(encrypted_msg[i] ^ ord(key[i%key_length])) 
#     return flag

# key = determine_key(hex_string, known_plain_text) + 'y' # based on the pattern we now now the key value.
# flag = get_flag(hex_string, key)

# print(flag)