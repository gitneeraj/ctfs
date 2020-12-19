from pwn import * # pip install pwntools
import json
from time import sleep
from Crypto.Util.number import long_to_bytes
import codecs

r = remote('socket.cryptohack.org', 13377)

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

i = 0
_type = None
_encoded = None

while True:
    received = json_recv()
    if i == 100:
        print(f"FLAG: {received['flag']}")
        break

    _type = received["type"]
    _encoded = received["encoded"]

    if _type == "base64":
        decoded = base64.b64decode(_encoded).decode() # wow so encode
    elif _type == "hex":
        decoded = (bytes.fromhex(_encoded)).decode()
    elif _type == "rot13":
        decoded = codecs.decode(_encoded, 'rot_13')
    elif _type == "bigint":
        decoded = (bytes.fromhex(_encoded[2:])).decode()
    elif _type == "utf-8":
        decoded = "".join([chr(b) for b in _encoded])
    elif _type == "flag":
        print(_encoded)
    # sleep(1)


    to_send = {
        "decoded": decoded
    }
    print(f"Level: {i}")
    print(f"Type: {_type}")
    print(f"Encoded: {_encoded}")
    print(f"Decoded: {decoded}")
    print("-"*100)
    json_send(to_send)
    i += 1
