from Crypto.Util.number import inverse

p = 110818190048489041673110922235667224953
q = 245503461123389175221964239541301684621
e = 65537

phi = (p-1)*(q-1)

# modulos
n = p * q
print(phi)
print(inverse(e, phi))