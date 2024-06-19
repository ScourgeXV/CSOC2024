#!/usr/bin/env python3

def extended_gcd(a,b,s1,t1,s2,t2) :
    if b == 0 :
        return (s1,t1)
    else :
        q = a//b
        a,b = b,a-(q*b)
        s1,s2 = s2,s1-(q*s2)
        t1,t2 = t2,t1-(q*t2)
        return extended_gcd(a,b,s1,t1,s2,t2)

print(extended_gcd(26513,32321,1,0,0,1))
