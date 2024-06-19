#!/usr/bin/env python3

from pwn import *

k1 = (bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'))
k2 = xor(k1,(bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')))
k3 = xor(k2,(bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')))
k12 = xor(k1,k2)
k = xor(k12,k3)
flag = xor(k,(bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')))
print(flag.decode())
