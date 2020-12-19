#!/usr/bin/env python3

# from PIL import Image

# lemur = Image.open("lemur.png", "r")
# flag = Image.open("flag.png", "r")

# lemur_pixel = list(lemur.getdata())
# flag_pixel = list(flag.getdata())

# # print(len(lemur_pixel))
# # print(len(flag_pixel))

# new_pixel = []
# for l in lemur_pixel:
#     for f in flag_pixel:
#         x = l[0] ^ f[0]
#         y = l[1] ^ f[1]
#         z = l[2] ^ f[2]
#         new_pixel.append((x,y,z))

# print(new_pixel)

# lemur = bytearray(open("lemur.png", "rb").read())
# flag = bytearray(open("flag.png", "rb").read())

# size = len(lemur) if len(lemur) < len(flag) else len(flag)
# xord_byte_array = bytearray(size)

# # print(len(lemur))
# # print(len(flag))
# # print(len(xord_byte_array))

# # XOR between the files
# for i in range(size):
# 	xord_byte_array[i] = lemur[i] ^ flag[i]

# # Write the XORd bytes to the output file	
# open("xored_image.png", 'wb').write(xord_byte_array)

from PIL import Image, ImageChops

# Open images
im1 = Image.open("flag.png").convert("1")
im2 = Image.open("lemur.png").convert("1")

result = ImageChops.logical_xor(im1,im2)
result.save("result.png")