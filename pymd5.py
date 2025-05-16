import struct

# Constants for MD5
A = 0x67452301
B = 0xefcdab89
C = 0x98badcfe
D = 0x10325476

import hashlib

def padding(msg_length_bits):
    msg_length = msg_length_bits // 8
    pad = b'\x80'
    while ((msg_length + len(pad)) % 64) != 56:
        pad += b'\x00'
    pad += struct.pack('<Q', msg_length_bits)
    return pad

class md5:
    def __init__(self, state=None, count=0):
        self._buffer = b""
        self.count = count
        if state:
            self._A, self._B, self._C, self._D = struct.unpack("<4I", state)
        else:
            self._A = A
            self._B = B
            self._C = C
            self._D = D
        self._md5 = hashlib.md5()
        if state:
            self._md5._copy_state = (self._A, self._B, self._C, self._D)
        self._data = b""

    def update(self, data):
        self._data += data
        self._md5.update(data)

    def digest(self):
        return self._md5.digest()

    def hexdigest(self):
        return self._md5.hexdigest()
