#!/usr/bin/env python3

def gcd(a,b) :
    if a > b :
        return gcd(a-b,b)
    elif a < b :
        return gcd(a,b-a)
    else :
        return a

print(gcd(12,8))
print(gcd(66528,52920))
