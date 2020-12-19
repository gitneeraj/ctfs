#!/usr/bin/env python3
import socketserver
from secrets import flag
import struct

# We implemented a true RNG which hands us cryptographically secure double-precision
# floats measured directly from our quantum flux generator.
import trng


def to_bytes(gen):
    for value in gen:
        yield from struct.pack("d", value)


def xor(a, b):
    for _a, _b in zip(a, b):
        yield _a ^ _b


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        keystream = to_bytes(trng.keystream())
        while True:
            count = int(self.request.recv(4))

            for _ in range(count):
                ct = bytes(xor(flag, keystream))
                self.request.sendall(ct)

        self.request.close()


if __name__ == "__main__":
    HOST, PORT = "okboomer.tasteless.eu", 10501

    with socketserver.TCPServer((HOST, PORT), Handler) as server:
        server.serve_forever()
