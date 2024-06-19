#!/usr/bin/env python3

m = 12
p = 17
q = 23

e = 65537
N = p*q
encrypted_m = pow(m,e,N)
print(encrypted_m)
