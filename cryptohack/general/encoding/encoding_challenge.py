#!/usr/bin/env python3
from Crypto.Util.number import long_to_bytes

hex_string = "61756275726e735f61766f636174696f6e735f66757274697665"

# print(bytes.fromhex(hex_string).decode())
# print("crypto{" + bytes.fromhex(hex_string).decode() + "}")
# print('{"flag": "crypto{auburns_avocations_furtive}"}')

# {"decoded": "scurvys_internalize_Lockheeds"}

big_int = "0x6675726e6974757265735f6f64655f7375726c696572"
big_int2 = "0x74756d6272656c735f6d657374697a6f735f776f6f6c696572"

print(bytes.fromhex(big_int2[2:]).decode())

# {"decoded":"furnitures_ode_surlier"}
# {"decoded":"tumbrels_mestizos_woolier"}